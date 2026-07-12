"""Offline self-test: a local echo chat backend + the client talking to it.

This never touches the network. It proves the profile engine, HTTP transport,
session/send/poll flow and message de-duplication all work together, so the
plumbing can be checked in CI or offline without hitting the real telekom.si
endpoints.
"""

from __future__ import annotations

import json
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from .client import KlepetClient
from .config import Profile

# Shared conversation state for the toy backend.
_STATE = {"messages": [], "counter": 0}
_LOCK = threading.Lock()


class _EchoHandler(BaseHTTPRequestHandler):
    def log_message(self, *args):  # silence default stderr logging
        pass

    def _json(self, obj, code=200):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        payload = json.loads(self.rfile.read(length) or b"{}")
        if self.path == "/api/session":
            self._json({"session": {"id": "sess-123"}})
        elif self.path == "/api/send":
            text = payload.get("text", "")
            with _LOCK:
                _STATE["counter"] += 1
                _STATE["messages"].append(
                    {"id": _STATE["counter"], "from": "bot", "text": f"Echo: {text}"}
                )
            self._json({"ok": True})
        else:
            self._json({"error": "not found"}, 404)

    def do_GET(self):
        if self.path.startswith("/api/poll"):
            with _LOCK:
                msgs = list(_STATE["messages"])
            self._json({"data": {"messages": msgs}})
        else:
            self._json({"error": "not found"}, 404)


def _demo_profile(base_url: str) -> Profile:
    return Profile.from_dict(
        {
            "name": "demo-echo",
            "transport": "poll",
            "base_url": base_url,
            "session": {
                "method": "POST",
                "url": "{{base_url}}/api/session",
                "json": {"channel": "web"},
                "extract": {"session_id": "session.id"},
            },
            "send": {
                "method": "POST",
                "url": "{{base_url}}/api/send",
                "json": {"sessionId": "{{session_id}}", "text": "{{message}}"},
            },
            "poll": {
                "request": {"method": "GET", "url": "{{base_url}}/api/poll?sid={{session_id}}"},
                "messages_path": "data.messages",
                "message_text_path": "text",
                "message_from_path": "from",
                "interval_seconds": 0.2,
            },
        }
    )


def run_demo() -> int:
    _STATE["messages"] = []
    _STATE["counter"] = 0
    server = ThreadingHTTPServer(("127.0.0.1", 0), _EchoHandler)
    host, port = server.server_address
    base_url = f"http://{host}:{port}"
    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()

    received = []
    profile = _demo_profile(base_url)
    client = KlepetClient(profile, on_message=lambda a, txt: received.append((a, txt)))
    try:
        client.start()
        assert client.ctx.get("session_id") == "sess-123", "session id not extracted"
        print(f"[demo] session opened, id={client.ctx['session_id']}")
        client.send("Zdravo, klepet!")
        client.send("Kako si?")
        deadline = time.time() + 5
        while len(received) < 2 and time.time() < deadline:
            time.sleep(0.1)
    finally:
        client.stop()
        server.shutdown()

    print(f"[demo] received {len(received)} message(s):")
    for author, text in received:
        print(f"    {author}: {text}")

    ok = [t for _, t in received]
    if "Echo: Zdravo, klepet!" in ok and "Echo: Kako si?" in ok:
        print("[demo] PASS - client drove the full session/send/poll flow.")
        return 0
    print("[demo] FAIL - expected echo replies not received.")
    return 1
