"""Turn a browser-exported HAR of a real klepet session into a profile skeleton.

Because the telekom.si chat endpoints can only be observed from a browser on the
live site, the intended workflow is:

  1. Open www.telekom.si, start the "klepet" chat, open DevTools -> Network.
  2. Send one or two messages so the session/send/receive calls all appear.
  3. Right-click the network list -> "Save all as HAR", save it to a file.
  4. Run:  python -m klepet import-har chat.har -o profiles/telekom_si.json

This module scans the HAR, scores each request by how "chat-like" it looks, and
emits a best-effort profile plus a human-readable report so you can confirm /
adjust the guesses. It never invents endpoints - everything it writes comes from
URLs and bodies actually present in the capture.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse

# Keywords that hint an endpoint is part of a chat/bot flow.
_CHAT_HINTS = re.compile(
    r"chat|klepet|message|messages|conversation|bot|engage|dialog|assistant|"
    r"webchat|livechat|inbound|outbound|session",
    re.IGNORECASE,
)
_SEND_HINTS = re.compile(r"send|message|inbound|post|text|utterance", re.IGNORECASE)
_POLL_HINTS = re.compile(r"poll|receive|messages|events|outbound|history|updates", re.IGNORECASE)
_SESSION_HINTS = re.compile(r"session|start|init|create|conversation|engage|token|auth", re.IGNORECASE)


@dataclass
class Candidate:
    method: str
    url: str
    score: int
    request_body: Any = None
    response_body: Any = None
    is_websocket: bool = False
    ws_messages: List[Tuple[str, str]] = field(default_factory=list)  # (direction, data)

    @property
    def path(self) -> str:
        return urlparse(self.url).path


def load_har(path: str) -> dict:
    with open(path, "r", encoding="utf-8-sig") as fh:
        return json.load(fh)


def _decode_body(obj: Optional[dict]) -> Any:
    if not obj:
        return None
    text = obj.get("text")
    if text is None:
        return None
    mime = (obj.get("mimeType") or "").lower()
    if "json" in mime or text.strip().startswith(("{", "[")):
        try:
            return json.loads(text)
        except ValueError:
            return text
    return text


def analyze(har: dict) -> List[Candidate]:
    """Score every HAR entry; return chat-like candidates, best first."""
    entries = har.get("log", {}).get("entries", [])
    candidates: List[Candidate] = []
    for entry in entries:
        req = entry.get("request", {})
        resp = entry.get("response", {})
        url = req.get("url", "")
        method = req.get("method", "GET").upper()
        ws_msgs = entry.get("_webSocketMessages") or resp.get("_webSocketMessages")

        score = 0
        if _CHAT_HINTS.search(url):
            score += 5
        # JSON traffic is far more likely to be the chat API than assets.
        resp_mime = (resp.get("content", {}).get("mimeType") or "").lower()
        if "json" in resp_mime:
            score += 2
        if method in ("POST", "PUT"):
            score += 1
        if ws_msgs:
            score += 6
        if re.search(r"\.(js|css|png|jpe?g|gif|svg|woff2?|ico)(\?|$)", url, re.IGNORECASE):
            score -= 6  # static asset

        if score <= 0:
            continue

        cand = Candidate(
            method=method,
            url=url,
            score=score,
            request_body=_decode_body(req.get("postData")),
            response_body=_decode_body(resp.get("content")),
            is_websocket=bool(ws_msgs),
        )
        if ws_msgs:
            for m in ws_msgs:
                cand.ws_messages.append((m.get("type", "?"), m.get("data", "")))
        candidates.append(cand)

    candidates.sort(key=lambda c: c.score, reverse=True)
    return candidates


def _classify(candidates: List[Candidate]) -> Dict[str, Optional[Candidate]]:
    """Pick the most likely session / send / poll endpoints from candidates."""
    picks: Dict[str, Optional[Candidate]] = {"session": None, "send": None, "poll": None}
    posts = [c for c in candidates if c.method in ("POST", "PUT")]
    gets = [c for c in candidates if c.method == "GET"]

    for c in posts:
        if picks["session"] is None and _SESSION_HINTS.search(c.url):
            picks["session"] = c
        elif picks["send"] is None and _SEND_HINTS.search(c.url):
            picks["send"] = c
    # Fallbacks: first POST that has a text-ish body is probably "send".
    if picks["send"] is None and posts:
        picks["send"] = next((c for c in posts if c is not picks["session"]), None)
    if picks["session"] is None and posts:
        picks["session"] = posts[0] if posts[0] is not picks["send"] else None

    for c in gets:
        if picks["poll"] is None and _POLL_HINTS.search(c.url):
            picks["poll"] = c
    if picks["poll"] is None and gets:
        picks["poll"] = gets[0]
    return picks


def build_profile(candidates: List[Candidate], name: str = "telekom_si") -> dict:
    """Assemble a best-effort profile dict from classified candidates."""
    ws = next((c for c in candidates if c.is_websocket), None)
    if ws is not None:
        return _build_ws_profile(ws, name)
    return _build_poll_profile(_classify(candidates), name)


def _req_block(c: Optional[Candidate]) -> Optional[dict]:
    if c is None:
        return None
    block: Dict[str, Any] = {"method": c.method, "url": c.url}
    if c.request_body is not None:
        block["json"] = c.request_body
    return block


def _build_poll_profile(picks: Dict[str, Optional[Candidate]], name: str) -> dict:
    prof: Dict[str, Any] = {
        "name": name,
        "transport": "poll",
        "base_url": _base_url(picks),
        "headers": {},
    }
    session = _req_block(picks["session"])
    if session:
        session["extract"] = {"session_id": "REVIEW: dotted.path.to.session.id"}
        prof["session"] = session
    send = _req_block(picks["send"])
    if send:
        # Replace the captured user text with the {{message}} placeholder.
        send["json"] = _placeholder_message(send.get("json"))
        prof["send"] = send
    poll = picks["poll"]
    if poll is not None:
        prof["poll"] = {
            "request": {"method": poll.method, "url": poll.url},
            "messages_path": "REVIEW: dotted.path.to.messages[]",
            "message_text_path": "text",
            "message_from_path": "from",
            "interval_seconds": 2.0,
        }
    return prof


def _build_ws_profile(ws: Candidate, name: str) -> dict:
    sent = [d for direction, d in ws.ws_messages if direction in ("send", "sent", "outgoing")]
    return {
        "name": name,
        "transport": "websocket",
        "base_url": _origin(ws.url),
        "websocket": {
            "url": ws.url,
            "open_frames": sent[:1],
            "send_template": _placeholder_message(_maybe_json(sent[-1])) if sent else "{{message}}",
            "message_text_path": "REVIEW: text",
            "message_from_path": "from",
        },
    }


# Field names that conventionally carry the user's message text.
_MESSAGE_KEYS = ("text", "message", "msg", "body", "content", "utterance", "query", "q", "input")


def _placeholder_message(body: Any) -> Any:
    """Rewrite the body's message field to the ``{{message}}`` template.

    Prefers a field whose name conventionally holds the message text; if none
    matches, falls back to the longest string value in the object.
    """
    if isinstance(body, dict):
        target = next((k for k in _MESSAGE_KEYS if isinstance(body.get(k), str)), None)
        if target is None:
            best_len = -1
            for k, v in body.items():
                if isinstance(v, str) and len(v) > best_len:
                    target, best_len = k, len(v)
        if target is not None:
            body = dict(body)
            body[target] = "{{message}}"
        return body
    if isinstance(body, str):
        return "{{message}}"
    return body


def _maybe_json(text: str) -> Any:
    try:
        return json.loads(text)
    except (ValueError, TypeError):
        return text


def _origin(url: str) -> str:
    p = urlparse(url)
    return f"{p.scheme}://{p.netloc}"


def _base_url(picks: Dict[str, Optional[Candidate]]) -> str:
    for c in picks.values():
        if c is not None:
            return _origin(c.url)
    return ""


def render_report(candidates: List[Candidate], limit: int = 12) -> str:
    """Human-readable summary of what the importer saw, for manual review."""
    lines = [f"Found {len(candidates)} chat-like request(s):", ""]
    for c in candidates[:limit]:
        kind = "WS" if c.is_websocket else c.method
        lines.append(f"  [score {c.score:>2}] {kind:<4} {c.url}")
        if c.is_websocket and c.ws_messages:
            for direction, data in c.ws_messages[:4]:
                snippet = data[:120].replace("\n", " ")
                lines.append(f"        {direction}: {snippet}")
        else:
            if c.request_body is not None:
                lines.append(f"        req:  {_snippet(c.request_body)}")
            if c.response_body is not None:
                lines.append(f"        resp: {_snippet(c.response_body)}")
    if len(candidates) > limit:
        lines.append(f"  ... and {len(candidates) - limit} more")
    return "\n".join(lines)


def _snippet(body: Any, n: int = 160) -> str:
    text = json.dumps(body, ensure_ascii=False) if not isinstance(body, str) else body
    text = text.replace("\n", " ")
    return text[:n] + ("..." if len(text) > n else "")
