# klepet — chat-bot client for www.telekom.si

A small, dependency-light Python client for talking to the **klepet** ("chat")
assistant — **Maks** — on `www.telekom.si` from the command line or from your
own code. A ready-to-run profile ships in `profiles/telekom_si.json`, so it
works out of the box:

```bash
python -m klepet chat profiles/telekom_si.json
```

The client is **profile-driven**: a chat backend is described by a JSON file
(session / send / receive requests) rather than hard-coded. This is deliberate —
see [Why a profile?](#why-a-profile) below.

```
.
├── klepet/            # the chat client package
│   ├── client.py      # KlepetClient: session → send → receive orchestration
│   ├── config.py      # Profile model (loads/validates the JSON)
│   ├── transport.py   # requests session + a stdlib WebSocket client (no extra deps)
│   ├── template.py    # {{var}} substitution + dotted-path extraction
│   ├── harimport.py   # turn a browser HAR capture into a profile
│   ├── demo.py        # offline echo backend + self-test
│   └── __main__.py    # CLI: chat / import-har / demo
├── profiles/
│   ├── telekom_si.json          # ready-to-run profile for Maks
│   └── telekom_si.example.json  # annotated template for other backends
├── eval/              # Maks answer-quality audit (start at eval/REPORT.md)
│   ├── REPORT.md      # full audit report + file manifest
│   ├── evaluate.py    # 300-question harness + rubric
│   ├── hard_synthesis.py  # 30-scenario multi-turn synthesis test
│   └── …              # results, transcripts, LLM-judge verdicts, dashboard
├── tests/test_klepet.py
└── requirements.txt
```

## Why a profile?

The telekom.si klepet widget is powered by the [Boost.ai](https://www.boost.ai)
platform. Its home-page config (`window.TS_VA_CONFIG`) points at the Boost
server `telekom-slovenije`, i.e. `https://telekom-slovenije.boost.ai`, whose
Chat API v2 is public and needs no authentication. That contract is captured in
`profiles/telekom_si.json`, which is why `chat` works with no setup.

Keeping the contract in a **profile** rather than hard-coding it means the same
client can talk to other backends (LivePerson, Genesys, Oracle DA, custom
REST/WebSocket, …) just by dropping in another JSON file — and if telekom.si
ever changes its widget, you can regenerate the profile from a browser capture
in about two minutes (below) instead of editing code. Everything else — session
handling, message sending, synchronous/polled/streamed replies,
de-duplication — is already implemented and tested.

## Install

```bash
pip install -r requirements.txt      # just `requests`; WebSocket is stdlib
```

## Quick start

**Chat with Maks right away** (uses the shipped `profiles/telekom_si.json`):

```bash
python -m klepet chat profiles/telekom_si.json
```

```
Connecting to 'telekom_si' (poll) ...

bot: Hej, sem Maks, svetovalec iz digitalnega sveta✨ ...
Connected. Type a message and press Enter. Ctrl-D or /quit to exit.
> Katere mobilne pakete ponujate?
bot: ✨ Na voljo so naslednji mobilni paketi: ...
> /quit
```

**Verify the plumbing offline** (no network):

```bash
python -m klepet demo
# -> [demo] PASS - client drove the full session/send/poll flow.
```

### Adapting to another backend (or re-capturing telekom.si)

If you want to point the client at a different chat backend — or telekom.si
changes its widget — capture the traffic from a browser and generate a profile:

1. Open the site and start its chat. Open DevTools → **Network** (tick *Preserve
   log*). Send a message or two so the *start*, *send* and *receive* calls fire.
2. Right-click the request list → **Save all as HAR** → e.g. `chat.har`.
3. Generate a profile skeleton and fix any field tagged `REVIEW:` / `REPLACE`
   (usually just the dotted paths):

   ```bash
   python -m klepet import-har chat.har -o profiles/my_backend.json
   ```

`profiles/telekom_si.example.json` is a fully commented template you can copy.

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
| `transport` | `"poll"` (HTTP) or `"websocket"`                                      |
| `session`   | request that opens the conversation; `extract` pulls ids into context |
| `send`      | request that posts a user message; `{{message}}` = the typed text     |
| `reply`     | paths to read replies that come back **in** the send/session response (synchronous backends) |
| `poll`      | request + paths to read replies from a separate polling endpoint     |
| `websocket` | url, opening frames, send template, reply paths (ws transport)       |

A poll-transport profile needs at least one of `reply` or `poll`. telekom.si is
synchronous (Boost answers in the POST response), so `telekom_si.json` uses
`reply` and has no `poll` loop.

Values support `{{var}}` templating; variables come from `vars`, from the
`base_url`, and from anything a previous request's `extract` produced (e.g.
`{{conversation_id}}`). Response fields are read with dotted paths that index
arrays (`data.messages.0.text`) and support a `*` wildcard that maps the rest of
the path over an array (`elements.*.payload.html`). In `reply`/`poll`, set
`strip_html: true` to flatten HTML fragments — and join a list of them — into
plain text.

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
