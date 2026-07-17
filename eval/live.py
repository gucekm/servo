"""Shared live driver for the Maks probe suites.

A thin raw client for the Boost Chat API v2 used by all follow-up test suites
(stability, robustness, hallucination, sycophancy, link audit). Unlike
``klepet``'s profile client — which flattens replies to plain text — this
driver keeps the **full JSON payload** of every reply, so probes can also see
hyperlinks (``<a href>``), Boost "links" elements and action buttons that the
plain-text transcripts drop.

Every conversation is fresh (new START), mirroring how evaluate.py asked the
original 300 questions.
"""

from __future__ import annotations

import re
import sys
import time
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import requests  # noqa: E402

from klepet.client import _strip_html  # noqa: E402  (same normalisation as the main run)

BASE_URL = "https://telekom-slovenije.boost.ai/api/chat/v2"
HEADERS = {
    "Origin": "https://www.telekom.si",
    "Referer": "https://www.telekom.si/",
}

# Boost rejects an over-long POST with 400 {"tag":"request.invalid.message.too.long"}.
# Measured cap is 140 characters; probes must stay at or under it. We check this
# ourselves so a too-long message fails loudly as a length error instead of being
# retried and swallowed as a generic "[ERROR: no reply]".
MAX_MESSAGE_LEN = 140

_HREF_RE = re.compile(r"""href=["']([^"']+)["']""", re.IGNORECASE)
_URL_RE = re.compile(r"https?://[^\s\"'<>\)\]]+")
_PHONE_RE = re.compile(r"\b(?:080|0[1-7]\d|03\d|04\d|05\d|06\d)[\s/.-]?\d{2,4}[\s.-]?\d{2,4}\b")


def _collect_urls(obj: Any, out: List[str]) -> None:
    """Recursively harvest URL-looking strings from a Boost payload."""
    if isinstance(obj, str):
        for m in _URL_RE.findall(obj):
            out.append(m.rstrip(".,;"))
        for m in _HREF_RE.findall(obj):
            if m not in out:
                out.append(m.rstrip(".,;"))
    elif isinstance(obj, dict):
        for v in obj.values():
            _collect_urls(v, out)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            _collect_urls(v, out)


def _reply_from_payload(payload: dict) -> Dict[str, Any]:
    """Reduce one Boost response payload to {text, html, urls, phones, element_types}."""
    resp = payload.get("response") or {}
    elements = resp.get("elements") or []
    htmls, types = [], []
    for el in elements:
        types.append(el.get("type", "?"))
        html = (el.get("payload") or {}).get("html")
        if html:
            htmls.append(html)
    html = "\n".join(htmls)
    text = "\n".join(_strip_html(h) for h in htmls if _strip_html(h))
    urls: List[str] = []
    _collect_urls(elements, urls)
    # de-dup, keep order
    seen: set = set()
    urls = [u for u in urls if not (u in seen or seen.add(u))]
    return {
        "text": text,
        "html": html,
        "urls": urls,
        "phones": sorted(set(_PHONE_RE.findall(text))),
        "element_types": types,
    }


class MessageTooLong(ValueError):
    """A message exceeds the backend's per-POST length cap (MAX_MESSAGE_LEN).

    Deterministic, so callers should report it rather than retry.
    """

    def __init__(self, length: int):
        self.length = length
        super().__init__(
            f"message too long: {length} chars > {MAX_MESSAGE_LEN} limit")


class MaksConversation:
    """One fresh conversation with Maks over the raw Boost API."""

    def __init__(self, timeout: float = 30.0):
        self.sess = requests.Session()
        self.sess.headers.update(HEADERS)
        self.timeout = timeout
        self.conversation_id: Optional[str] = None
        self.greeting: Optional[Dict[str, Any]] = None

    def start(self) -> Dict[str, Any]:
        r = self.sess.post(
            BASE_URL,
            json={"command": "START", "language": "sl-SI", "filter_values": ["default"]},
            timeout=self.timeout,
        )
        r.raise_for_status()
        payload = r.json()
        self.conversation_id = payload["conversation"]["id"]
        self.greeting = _reply_from_payload(payload)
        return self.greeting

    def say(self, text: str) -> Dict[str, Any]:
        assert self.conversation_id, "call start() first"
        if len(text) > MAX_MESSAGE_LEN:
            raise MessageTooLong(len(text))
        r = self.sess.post(
            BASE_URL,
            json={"command": "POST", "type": "text",
                  "conversation_id": self.conversation_id, "value": text},
            timeout=self.timeout,
        )
        if not r.ok:
            # Surface the backend's own reason (e.g. "Message too long") instead
            # of a bare status code, so callers can see why a probe was rejected.
            detail = r.text[:200]
            try:
                body = r.json()
                if body.get("tag") == "request.invalid.message.too.long":
                    raise MessageTooLong(len(text))
                detail = body.get("error") or detail
            except ValueError:
                pass
            raise requests.HTTPError(
                f"{r.status_code} for POST: {detail}", response=r)
        return _reply_from_payload(r.json())


def ask_fresh(question: str, retries: int = 2, backoff: float = 1.5) -> Dict[str, Any]:
    """Ask one question in a fresh conversation; return the reply record.

    On repeated failure returns a record whose text starts with ``[ERROR:`` so
    callers can score it as a non-answer without crashing the run.
    """
    if len(question) > MAX_MESSAGE_LEN:
        return {"text": f"[ERROR: message too long: {len(question)} > "
                        f"{MAX_MESSAGE_LEN} chars]",
                "html": "", "urls": [], "phones": [], "element_types": []}
    last: Optional[Exception] = None
    for attempt in range(retries + 1):
        try:
            conv = MaksConversation()
            conv.start()
            reply = conv.say(question)
            if reply["text"].strip():
                return reply
        except Exception as exc:  # noqa: BLE001 — keep long runs alive
            last = exc
        time.sleep(backoff * (attempt + 1))
    return {"text": f"[ERROR: no reply{': ' + str(last) if last else ''}]",
            "html": "", "urls": [], "phones": [], "element_types": []}


# Pause between successive turns of one conversation — a human reads the reply
# and types the next message, so ~8s is a natural, polite cadence.
POLITE_TURN_DELAY = 8.0


def converse(turns: List[str], retries: int = 2,
             turn_delay: float = POLITE_TURN_DELAY,
             on_turn: Optional[Callable[[int, str, Dict[str, Any]], None]] = None,
             ) -> List[Dict[str, Any]]:
    """Run one multi-turn conversation; returns a reply record per turn.

    If *on_turn* is given it is called ``on_turn(index, question, reply)`` right
    after each reply arrives, so callers can stream the Q&A as it happens.
    """
    too_long = [t for t in turns if len(t) > MAX_MESSAGE_LEN]
    if too_long:
        # Deterministic — a live call would only earn a 400; report and stop.
        return [{"question": t, "html": "", "urls": [], "phones": [],
                 "element_types": [],
                 "text": (f"[ERROR: message too long: {len(t)} > "
                          f"{MAX_MESSAGE_LEN} chars]"
                          if len(t) > MAX_MESSAGE_LEN else "[ERROR: not sent]")}
                for t in turns]
    for attempt in range(retries + 1):
        try:
            conv = MaksConversation()
            conv.start()
            out = []
            for i, t in enumerate(turns):
                rec = conv.say(t)
                rec["question"] = t
                out.append(rec)
                if on_turn is not None:
                    on_turn(i, t, rec)
                if i < len(turns) - 1:      # no need to wait after the last turn
                    time.sleep(turn_delay)
            return out
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(1.5 * (attempt + 1))
    return [{"question": t, "text": f"[ERROR: no reply: {last}]", "html": "",
             "urls": [], "phones": [], "element_types": []} for t in turns]
