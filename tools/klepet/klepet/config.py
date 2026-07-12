"""Profile model: the data that describes how to talk to a chat backend."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class RequestSpec:
    """A single templated HTTP request plus how to read values back out of it."""

    method: str = "GET"
    url: str = ""
    headers: Dict[str, str] = field(default_factory=dict)
    params: Dict[str, Any] = field(default_factory=dict)
    json_body: Optional[Any] = None
    data_body: Optional[Any] = None
    # response field -> dotted path, merged into the runtime context after the call
    extract: Dict[str, str] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, d: Optional[Dict[str, Any]]) -> Optional["RequestSpec"]:
        if not d:
            return None
        return cls(
            method=d.get("method", "GET").upper(),
            url=d.get("url", ""),
            headers=dict(d.get("headers", {})),
            params=dict(d.get("params", {})),
            json_body=d.get("json"),
            data_body=d.get("data"),
            extract=dict(d.get("extract", {})),
        )


@dataclass
class PollSpec:
    """How to receive messages when the backend uses HTTP long/short polling."""

    request: RequestSpec
    messages_path: str = "messages"          # array of message objects in the response
    message_text_path: str = "text"          # text field within a message object
    message_from_path: str = "from"          # author/role field within a message object
    bot_from_values: List[str] = field(default_factory=list)  # which authors are the bot
    interval_seconds: float = 2.0

    @classmethod
    def from_dict(cls, d: Optional[Dict[str, Any]]) -> Optional["PollSpec"]:
        if not d:
            return None
        req = RequestSpec.from_dict(d.get("request"))
        if req is None:
            raise ValueError("poll.request is required for a polling profile")
        return cls(
            request=req,
            messages_path=d.get("messages_path", "messages"),
            message_text_path=d.get("message_text_path", "text"),
            message_from_path=d.get("message_from_path", "from"),
            bot_from_values=list(d.get("bot_from_values", [])),
            interval_seconds=float(d.get("interval_seconds", 2.0)),
        )


@dataclass
class WebSocketSpec:
    """How to receive/send when the backend uses a WebSocket."""

    url: str
    subprotocols: List[str] = field(default_factory=list)
    headers: Dict[str, str] = field(default_factory=dict)
    open_frames: List[Any] = field(default_factory=list)   # frames sent right after connect
    send_template: Any = None                              # frame template for outgoing messages
    message_text_path: str = "text"
    message_from_path: str = "from"
    bot_from_values: List[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, d: Optional[Dict[str, Any]]) -> Optional["WebSocketSpec"]:
        if not d:
            return None
        if not d.get("url"):
            raise ValueError("websocket.url is required for a websocket profile")
        return cls(
            url=d["url"],
            subprotocols=list(d.get("subprotocols", [])),
            headers=dict(d.get("headers", {})),
            open_frames=list(d.get("open_frames", [])),
            send_template=d.get("send_template"),
            message_text_path=d.get("message_text_path", "text"),
            message_from_path=d.get("message_from_path", "from"),
            bot_from_values=list(d.get("bot_from_values", [])),
        )


@dataclass
class Profile:
    """A full description of one chat backend."""

    name: str = "unnamed"
    transport: str = "poll"                 # "poll" or "websocket"
    base_url: str = ""
    headers: Dict[str, str] = field(default_factory=dict)
    vars: Dict[str, Any] = field(default_factory=dict)
    session: Optional[RequestSpec] = None   # opens the conversation, extracts ids
    send: Optional[RequestSpec] = None      # sends one user message
    poll: Optional[PollSpec] = None
    websocket: Optional[WebSocketSpec] = None

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Profile":
        transport = d.get("transport", "poll").lower()
        prof = cls(
            name=d.get("name", "unnamed"),
            transport=transport,
            base_url=d.get("base_url", ""),
            headers=dict(d.get("headers", {})),
            vars=dict(d.get("vars", {})),
            session=RequestSpec.from_dict(d.get("session")),
            send=RequestSpec.from_dict(d.get("send")),
            poll=PollSpec.from_dict(d.get("poll")),
            websocket=WebSocketSpec.from_dict(d.get("websocket")),
        )
        prof.validate()
        return prof

    def validate(self) -> None:
        if self.transport not in ("poll", "websocket"):
            raise ValueError(f"unknown transport: {self.transport!r}")
        if self.send is None and self.transport != "websocket":
            raise ValueError("a 'send' request is required for the poll transport")
        if self.transport == "poll" and self.poll is None:
            raise ValueError("transport 'poll' requires a 'poll' section")
        if self.transport == "websocket" and self.websocket is None:
            raise ValueError("transport 'websocket' requires a 'websocket' section")

    def initial_context(self) -> Dict[str, Any]:
        """Seed context handed to the templating engine before any request runs."""
        ctx: Dict[str, Any] = {"base_url": self.base_url}
        ctx.update(self.vars)
        return ctx


def load_profile(path: str | Path) -> Profile:
    """Load and validate a profile from a JSON file.

    Lines whose first non-space character is ``//`` are stripped so profiles may
    carry comments (handy for the placeholder telekom template).
    """
    text = Path(path).read_text(encoding="utf-8")
    cleaned = "\n".join(
        line for line in text.splitlines() if not line.lstrip().startswith("//")
    )
    return Profile.from_dict(json.loads(cleaned))
