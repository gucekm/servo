"""KlepetClient - drives a chat backend described by a :class:`Profile`."""

from __future__ import annotations

import json
import re
import threading
import time
from typing import Any, Callable, Dict, List, Optional

from .config import Profile, ReplyShape, RequestSpec
from .template import extract, render
from .transport import WebSocketClient, new_http_session

_TAG_RE = re.compile(r"<[^>]+>")
_ENTITIES = {
    "&amp;": "&", "&lt;": "<", "&gt;": ">", "&quot;": '"',
    "&#39;": "'", "&apos;": "'", "&nbsp;": " ",
}


def _strip_html(text: str) -> str:
    """Flatten an HTML fragment into readable plain text."""
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</p\s*>", "\n", text, flags=re.IGNORECASE)
    text = _TAG_RE.sub("", text)
    for entity, char in _ENTITIES.items():
        text = text.replace(entity, char)
    return text.strip()

# Callback invoked for every inbound message: (author, text) -> None
MessageHandler = Callable[[str, str], None]


class KlepetClient:
    """A profile-driven chat client.

    Typical use::

        client = KlepetClient(profile, on_message=print_msg)
        client.start()          # opens session, begins receiving in background
        client.send("Zdravo")   # send a user message
        ...
        client.stop()
    """

    def __init__(self, profile: Profile, on_message: Optional[MessageHandler] = None):
        self.profile = profile
        self.on_message = on_message or (lambda author, text: None)
        self.ctx: Dict[str, Any] = profile.initial_context()
        self._session = new_http_session(profile.headers) if _needs_http(profile) else None
        self._ws: Optional[WebSocketClient] = None
        self._stop = threading.Event()
        self._rx_thread: Optional[threading.Thread] = None
        self._seen_ids: set = set()

    # -- lifecycle ---------------------------------------------------------- #

    def start(self) -> None:
        """Open the conversation and start receiving replies in the background."""
        if self.profile.session is not None:
            payload = self._run_request(self.profile.session, extra={})
            # Synchronous backends greet us in the session response itself.
            if self.profile.reply is not None:
                self._dispatch(payload, self.profile.reply)
        if self.profile.transport == "websocket":
            self._start_websocket()
        elif self.profile.poll is not None:
            self._rx_thread = threading.Thread(target=self._poll_loop, daemon=True)
            self._rx_thread.start()

    def stop(self) -> None:
        self._stop.set()
        if self._ws is not None:
            self._ws.close()
        if self._rx_thread is not None:
            self._rx_thread.join(timeout=3)

    # -- sending ------------------------------------------------------------ #

    def send(self, text: str) -> None:
        """Send one user message."""
        if self.profile.transport == "websocket":
            self._ws_send(text)
        else:
            if self.profile.send is None:
                raise RuntimeError("profile has no 'send' request configured")
            payload = self._run_request(self.profile.send, extra={"message": text})
            # Synchronous backends answer in the send response itself.
            if self.profile.reply is not None:
                self._dispatch(payload, self.profile.reply)

    # -- receiving: polling ------------------------------------------------- #

    def _poll_loop(self) -> None:
        poll = self.profile.poll
        assert poll is not None
        while not self._stop.is_set():
            try:
                data = self._run_request(poll.request, extra={}, return_json=True)
                self._dispatch(data, poll)
            except Exception as exc:  # keep the loop alive on transient errors
                self.on_message("_error", f"poll error: {exc}")
            self._stop.wait(poll.interval_seconds)

    def _dispatch(self, data: Any, shape: ReplyShape) -> None:
        """Surface every new message found in *data* according to *shape*."""
        msgs = extract(data, shape.messages_path, []) or []
        if isinstance(msgs, dict):
            msgs = [msgs]
        for msg in msgs:
            text = self._read_text(msg, shape)
            if not text:
                continue
            author = extract(msg, shape.message_from_path, "bot") or "bot"
            key = json.dumps(msg, sort_keys=True, default=str)
            if key in self._seen_ids:
                continue
            self._seen_ids.add(key)
            if shape.bot_from_values and str(author) not in shape.bot_from_values:
                continue  # only surface configured bot authors
            self.on_message(str(author), text)

    @staticmethod
    def _read_text(msg: Any, shape: ReplyShape) -> str:
        """Extract and normalise a message's text (list fragments + optional HTML)."""
        raw = extract(msg, shape.message_text_path)
        if raw is None:
            return ""
        fragments = raw if isinstance(raw, (list, tuple)) else [raw]
        out: List[str] = []
        for frag in fragments:
            if frag is None:
                continue
            piece = str(frag)
            if shape.strip_html:
                piece = _strip_html(piece)
            if piece:
                out.append(piece)
        return "\n".join(out)

    # -- receiving: websocket ---------------------------------------------- #

    def _start_websocket(self) -> None:
        ws_spec = self.profile.websocket
        assert ws_spec is not None
        url = render(ws_spec.url, self.ctx)
        headers = render(ws_spec.headers, self.ctx)
        self._ws = WebSocketClient(url, ws_spec.subprotocols, headers)
        self._ws.connect()
        for frame in ws_spec.open_frames:
            self._ws.send_text(_as_text(render(frame, self.ctx)))
        self._rx_thread = threading.Thread(target=self._ws_recv_loop, daemon=True)
        self._rx_thread.start()

    def _ws_recv_loop(self) -> None:
        ws_spec = self.profile.websocket
        assert ws_spec is not None and self._ws is not None
        for raw in self._ws.messages():
            if self._stop.is_set():
                break
            try:
                data = json.loads(raw)
            except json.JSONDecodeError:
                self.on_message("bot", raw)
                continue
            text = extract(data, ws_spec.message_text_path)
            if text is not None:
                # A single message object arrived on the socket.
                author = extract(data, ws_spec.message_from_path, "bot") or "bot"
                if not ws_spec.bot_from_values or str(author) in ws_spec.bot_from_values:
                    self.on_message(str(author), str(text))
            else:
                # A batch/envelope: let the shared dispatcher find the array.
                self._dispatch(
                    data,
                    ReplyShape(
                        messages_path="messages",
                        message_text_path=ws_spec.message_text_path,
                        message_from_path=ws_spec.message_from_path,
                        bot_from_values=ws_spec.bot_from_values,
                    ),
                )

    def _ws_send(self, text: str) -> None:
        ws_spec = self.profile.websocket
        assert ws_spec is not None and self._ws is not None
        ctx = dict(self.ctx, message=text)
        frame = render(ws_spec.send_template, ctx) if ws_spec.send_template is not None else text
        self._ws.send_text(_as_text(frame))

    # -- request execution -------------------------------------------------- #

    def _run_request(
        self, spec: RequestSpec, extra: Dict[str, Any], return_json: bool = False
    ) -> Any:
        assert self._session is not None
        ctx = dict(self.ctx, **extra)
        url = render(spec.url, ctx)
        headers = render(spec.headers, ctx)
        params = render(spec.params, ctx)
        json_body = render(spec.json_body, ctx) if spec.json_body is not None else None
        data_body = render(spec.data_body, ctx) if spec.data_body is not None else None

        resp = self._session.request(
            spec.method, url, headers=headers or None, params=params or None,
            json=json_body, data=data_body, timeout=30,
        )
        resp.raise_for_status()
        payload: Any = None
        if resp.content:
            try:
                payload = resp.json()
            except ValueError:
                payload = resp.text
        # Feed extracted values back into the shared context for later requests.
        for var, path in spec.extract.items():
            self.ctx[var] = extract(payload, path)
        return payload if return_json else payload


def _needs_http(profile: Profile) -> bool:
    return profile.transport != "websocket" or profile.session is not None or profile.send is not None


def _as_text(frame: Any) -> str:
    return frame if isinstance(frame, str) else json.dumps(frame, ensure_ascii=False)
