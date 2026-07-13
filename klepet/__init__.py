"""klepet - a configurable client for website live-chat / chatbot backends.

The package is intentionally protocol-agnostic. A chat backend is described by
a JSON *profile* (see ``profiles/``) that says how to open a session, how to
send a message, and how to receive replies. This lets the same client talk to
different vendors (LivePerson, Genesys, Oracle DA, custom REST/WebSocket, ...)
without code changes.

A ready-to-run profile for the "klepet" chat on www.telekom.si (the Boost.ai
assistant "Maks") ships in ``profiles/telekom_si.json``. To target a different
backend, capture it from a browser session and generate a new profile (see the
README and ``klepet.harimport``).
"""

from .config import Profile, load_profile
from .client import KlepetClient

__all__ = ["Profile", "load_profile", "KlepetClient"]
__version__ = "0.1.0"
