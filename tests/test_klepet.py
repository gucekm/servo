"""Unit tests for the profile engine and HAR importer (no network required).

Run from the repo root:

    python -m pytest tests            # if pytest is installed
    python tests/test_klepet.py       # plain-stdlib fallback runner
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from klepet import harimport
from klepet.client import KlepetClient
from klepet.config import Profile
from klepet.template import extract, render


def test_render_exact_preserves_type():
    ctx = {"n": 42, "arr": [1, 2, 3]}
    assert render("{{n}}", ctx) == 42
    assert render("{{arr}}", ctx) == [1, 2, 3]
    assert render("id={{n}}", ctx) == "id=42"


def test_render_nested_structures():
    ctx = {"sid": "abc", "message": "hi"}
    body = {"conversationId": "{{sid}}", "text": "{{message}}", "meta": ["{{sid}}"]}
    assert render(body, ctx) == {
        "conversationId": "abc",
        "text": "hi",
        "meta": ["abc"],
    }


def test_extract_dotted_and_indexed():
    data = {"a": {"b": [{"c": 7}]}}
    assert extract(data, "a.b.0.c") == 7
    assert extract(data, "a.b.9.c", default="x") == "x"
    assert extract(data, "missing", default=None) is None


def test_profile_validation_requires_send_for_poll():
    try:
        Profile.from_dict({"transport": "poll", "poll": {"request": {"url": "u"}}})
    except ValueError as exc:
        assert "send" in str(exc)
    else:
        raise AssertionError("expected ValueError for missing send")


def test_harimport_classifies_poll_flow():
    har = {
        "log": {
            "entries": [
                {
                    "request": {"method": "GET", "url": "https://x/app.js"},
                    "response": {"content": {"mimeType": "application/javascript"}},
                },
                {
                    "request": {
                        "method": "POST",
                        "url": "https://chat.telekom.si/api/conversation/start",
                        "postData": {"mimeType": "application/json", "text": "{}"},
                    },
                    "response": {"content": {"mimeType": "application/json", "text": "{\"id\":\"1\"}"}},
                },
                {
                    "request": {
                        "method": "POST",
                        "url": "https://chat.telekom.si/api/message/send",
                        "postData": {"mimeType": "application/json", "text": "{\"text\":\"hi\"}"},
                    },
                    "response": {"content": {"mimeType": "application/json", "text": "{}"}},
                },
                {
                    "request": {"method": "GET", "url": "https://chat.telekom.si/api/message/poll"},
                    "response": {"content": {"mimeType": "application/json", "text": "{\"messages\":[]}"}},
                },
            ]
        }
    }
    candidates = harimport.analyze(har)
    # The static asset must be filtered out; the three API calls kept.
    urls = [c.url for c in candidates]
    assert not any("app.js" in u for u in urls)
    assert len(candidates) == 3

    profile = harimport.build_profile(candidates, name="telekom_si")
    assert profile["transport"] == "poll"
    assert "start" in profile["session"]["url"]
    assert profile["send"]["json"]["text"] == "{{message}}"
    assert "poll" in profile["poll"]["request"]["url"]


def test_extract_wildcard_collects_fragments():
    data = {"response": {"elements": [
        {"payload": {"html": "<p>Hej</p>"}},
        {"payload": {"html": "<p>Svet</p>"}},
        {"type": "links", "payload": {"links": []}},  # no html -> dropped
    ]}}
    assert extract(data, "response.elements.*.payload.html") == [
        "<p>Hej</p>", "<p>Svet</p>", None,
    ]
    # A wildcard over a non-list yields the default.
    assert extract({"x": 1}, "x.*.y", default="d") == "d"


def test_reply_only_profile_is_valid_without_poll():
    # A synchronous backend receives via `reply`, so a `poll` section is optional.
    prof = Profile.from_dict({
        "transport": "poll",
        "send": {"method": "POST", "url": "u"},
        "reply": {"messages_path": "response"},
    })
    assert prof.poll is None and prof.reply is not None


def test_reply_dispatch_flattens_boost_style_response():
    prof = Profile.from_dict({
        "name": "boost", "transport": "poll", "base_url": "https://x",
        "session": {"method": "POST", "url": "{{base_url}}/s"},
        "send": {"method": "POST", "url": "{{base_url}}/m",
                 "json": {"value": "{{message}}"}},
        "reply": {
            "messages_path": "response",
            "message_text_path": "elements.*.payload.html",
            "message_from_path": "source",
            "bot_from_values": ["bot"],
            "strip_html": True,
        },
    })
    got = []
    client = KlepetClient(prof, on_message=lambda a, t: got.append((a, t)))
    payload = {"response": {"source": "bot", "id": "1", "elements": [
        {"type": "html", "payload": {"html": "<p>Pozdravljeni!</p>"}},
        {"type": "html", "payload": {"html": "<p>Kako <b>pomagam</b>?</p>"}},
    ]}}
    client._dispatch(payload, prof.reply)
    assert got == [("bot", "Pozdravljeni!\nKako pomagam?")]
    # Re-dispatching the same response is de-duplicated.
    client._dispatch(payload, prof.reply)
    assert len(got) == 1


def test_harimport_websocket():
    har = {
        "log": {
            "entries": [
                {
                    "request": {"method": "GET", "url": "wss://chat.telekom.si/socket"},
                    "response": {"content": {}},
                    "_webSocketMessages": [
                        {"type": "send", "data": "{\"type\":\"msg\",\"text\":\"hi\"}"},
                        {"type": "receive", "data": "{\"text\":\"pozdravljeni\"}"},
                    ],
                }
            ]
        }
    }
    candidates = harimport.analyze(har)
    profile = harimport.build_profile(candidates, name="telekom_si")
    assert profile["transport"] == "websocket"
    assert profile["websocket"]["url"] == "wss://chat.telekom.si/socket"
    assert profile["websocket"]["send_template"]["text"] == "{{message}}"


def _run_all():
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failures = 0
    for fn in fns:
        try:
            fn()
            print(f"PASS {fn.__name__}")
        except Exception as exc:  # noqa: BLE001
            failures += 1
            print(f"FAIL {fn.__name__}: {exc}")
    print(f"\n{len(fns) - failures}/{len(fns)} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(_run_all())
