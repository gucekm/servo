# klepet — chat-bot client for www.telekom.si

A small, dependency-light Python client for talking to the **klepet** ("chat")
assistant on `www.telekom.si` from the command line or from your own code.

The client is **profile-driven**: a chat backend is described by a JSON file
(session / send / receive requests) rather than hard-coded. This is deliberate —
see [Why a profile?](#why-a-profile) below.

```
tools/klepet/
├── klepet/
│   ├── client.py      # KlepetClient: session → send → receive orchestration
│   ├── config.py      # Profile model (loads/validates the JSON)
│   ├── transport.py   # requests session + a stdlib WebSocket client (no extra deps)
│   ├── template.py    # {{var}} substitution + dotted-path extraction
│   ├── harimport.py   # turn a browser HAR capture into a profile
│   ├── demo.py        # offline echo backend + self-test
│   └── __main__.py    # CLI: chat / import-har / demo
├── profiles/
│   └── telekom_si.example.json
├── tests/test_klepet.py
└── requirements.txt
```

## Why a profile?

The exact HTTP/WebSocket contract of the telekom.si klepet widget is **not
public** and is only observable from a browser on the live site. The build
environment this repo runs in is firewalled off from `telekom.si` (and the egress
proxy does not pass WebSocket upgrades), so the real endpoints could not be
captured and baked in here.

Instead of guessing and shipping something that silently breaks, the client
reads the contract from a **profile** you generate from a real session in about
two minutes (below). Everything else — session handling, message sending,
polling/streaming replies, de-duplication — is already implemented and tested.

## Install

```bash
cd tools/klepet
pip install -r requirements.txt      # just `requests`; WebSocket is stdlib
```

## Quick start

**1. Verify the client works (offline, no network):**

```bash
python -m klepet demo
# -> [demo] PASS - client drove the full session/send/poll flow.
```

**2. Capture the real klepet endpoints from your browser:**

1. Open <https://www.telekom.si> and start the **klepet** chat.
2. Open DevTools → **Network** tab (Chrome/Firefox/Edge). Tick *Preserve log*.
3. Send one or two messages so the *start*, *send* and *receive* calls all fire.
4. Right-click the request list → **Save all as HAR** → e.g. `chat.har`.

**3. Generate a profile from the capture:**

```bash
python -m klepet import-har chat.har -o profiles/telekom_si.json
```

This prints the chat-like requests it found and writes a profile skeleton.
Open the file and fix any field tagged `REVIEW:` / `REPLACE` — usually just the
dotted paths (`session_id` location, `messages_path`). Compare with
`profiles/telekom_si.example.json`, which is fully commented.

**4. Chat:**

```bash
python -m klepet chat profiles/telekom_si.json
```

```
Connecting to 'telekom_si' (poll) ...
Connected. Type a message and press Enter. Ctrl-D or /quit to exit.
> Pozdravljeni
bot: Pozdravljeni! Kako vam lahko pomagam?
> ...
```

## Use it from code

```python
from klepet import load_profile, KlepetClient

client = KlepetClient(load_profile("profiles/telekom_si.json"),
                      on_message=lambda who, text: print(f"{who}: {text}"))
client.start()
client.send("Zanima me stanje na računu")
# ... replies arrive via on_message on a background thread ...
client.stop()
```

## Profile format

| Section     | Purpose                                                              |
|-------------|----------------------------------------------------------------------|
| `transport` | `"poll"` (HTTP polling) or `"websocket"`                              |
| `session`   | request that opens the conversation; `extract` pulls ids into context |
| `send`      | request that posts a user message; `{{message}}` = the typed text     |
| `poll`      | request + paths to read the reply array (poll transport)             |
| `websocket` | url, opening frames, send template, reply paths (ws transport)       |

Values support `{{var}}` templating; variables come from `vars`, from the
`base_url`, and from anything a previous request's `extract` produced (e.g.
`{{session_id}}`). Response fields are read with dotted paths that also index
arrays: `data.messages.0.text`.

## Tests

```bash
python tests/test_klepet.py     # stdlib runner, no pytest needed
python -m klepet demo           # end-to-end against a local echo backend
```

## A note on responsible use

This is a single-user client for interacting with a public customer-service
chat, the same way the website's own widget does. Please use it accordingly:
keep to a sane message rate (the default poll interval is conservative), respect
telekom.si's Terms of Service, and don't use it for automated bulk messaging or
anything that would burden their support systems.
