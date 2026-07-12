"""Transports: an HTTP session helper and a minimal stdlib WebSocket client.

The WebSocket client implements just enough of RFC 6455 (client-side, text and
close/ping frames, no extensions) to talk to a typical chat backend without
pulling in a third-party dependency. If you already have ``websocket-client``
installed you can of course swap it in; this keeps the tool runnable with only
``requests`` (and even that is optional for the WS transport).
"""

from __future__ import annotations

import base64
import hashlib
import os
import socket
import ssl
import struct
from typing import Iterator, List, Optional, Tuple
from urllib.parse import urlparse

try:  # requests is only needed for the HTTP/poll transport
    import requests
except ImportError:  # pragma: no cover - surfaced with a clear message at use time
    requests = None  # type: ignore


def new_http_session(default_headers: Optional[dict] = None):
    """Return a ``requests.Session`` with default headers and a browser-like UA."""
    if requests is None:
        raise RuntimeError(
            "The 'requests' package is required for the HTTP/poll transport.\n"
            "Install it with:  pip install requests"
        )
    sess = requests.Session()
    sess.headers.update(
        {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            ),
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "sl,en;q=0.8",
        }
    )
    if default_headers:
        sess.headers.update(default_headers)
    return sess


# --------------------------------------------------------------------------- #
# Minimal WebSocket client
# --------------------------------------------------------------------------- #

_OP_TEXT = 0x1
_OP_BINARY = 0x2
_OP_CLOSE = 0x8
_OP_PING = 0x9
_OP_PONG = 0xA


class WebSocketClient:
    """A tiny blocking WebSocket client sufficient for chat traffic."""

    def __init__(
        self,
        url: str,
        subprotocols: Optional[List[str]] = None,
        headers: Optional[dict] = None,
        timeout: float = 30.0,
    ) -> None:
        self.url = url
        self.subprotocols = subprotocols or []
        self.extra_headers = headers or {}
        self.timeout = timeout
        self._sock: Optional[socket.socket] = None
        self._buf = b""

    def connect(self) -> None:
        parsed = urlparse(self.url)
        secure = parsed.scheme == "wss"
        host = parsed.hostname or ""
        port = parsed.port or (443 if secure else 80)
        path = parsed.path or "/"
        if parsed.query:
            path += "?" + parsed.query

        raw = socket.create_connection((host, port), timeout=self.timeout)
        if secure:
            ctx = ssl.create_default_context()
            raw = ctx.wrap_socket(raw, server_hostname=host)
        self._sock = raw

        key = base64.b64encode(os.urandom(16)).decode()
        lines = [
            f"GET {path} HTTP/1.1",
            f"Host: {host}:{port}" if parsed.port else f"Host: {host}",
            "Upgrade: websocket",
            "Connection: Upgrade",
            f"Sec-WebSocket-Key: {key}",
            "Sec-WebSocket-Version: 13",
        ]
        if self.subprotocols:
            lines.append("Sec-WebSocket-Protocol: " + ", ".join(self.subprotocols))
        for hk, hv in self.extra_headers.items():
            lines.append(f"{hk}: {hv}")
        handshake = ("\r\n".join(lines) + "\r\n\r\n").encode()
        self._sock.sendall(handshake)

        resp = self._read_until(b"\r\n\r\n")
        status_line = resp.split(b"\r\n", 1)[0].decode(errors="replace")
        if "101" not in status_line:
            raise ConnectionError(f"WebSocket handshake failed: {status_line}")
        expected = base64.b64encode(
            hashlib.sha1((key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11").encode()).digest()
        ).decode()
        if expected.encode() not in resp:
            raise ConnectionError("WebSocket handshake: bad Sec-WebSocket-Accept")

    def send_text(self, text: str) -> None:
        self._send_frame(_OP_TEXT, text.encode("utf-8"))

    def _send_frame(self, opcode: int, payload: bytes) -> None:
        assert self._sock is not None
        fin_op = 0x80 | opcode
        header = bytearray([fin_op])
        length = len(payload)
        mask_bit = 0x80  # clients MUST mask
        if length < 126:
            header.append(mask_bit | length)
        elif length < (1 << 16):
            header.append(mask_bit | 126)
            header += struct.pack(">H", length)
        else:
            header.append(mask_bit | 127)
            header += struct.pack(">Q", length)
        mask = os.urandom(4)
        header += mask
        masked = bytes(b ^ mask[i % 4] for i, b in enumerate(payload))
        self._sock.sendall(bytes(header) + masked)

    def messages(self) -> Iterator[str]:
        """Yield decoded text messages until the socket closes."""
        while True:
            frame = self._read_frame()
            if frame is None:
                return
            opcode, payload = frame
            if opcode == _OP_TEXT:
                yield payload.decode("utf-8", errors="replace")
            elif opcode == _OP_PING:
                self._send_frame(_OP_PONG, payload)
            elif opcode == _OP_CLOSE:
                try:
                    self._send_frame(_OP_CLOSE, b"")
                except OSError:
                    pass
                return

    def _read_frame(self) -> Optional[Tuple[int, bytes]]:
        try:
            first2 = self._read_exact(2)
        except (ConnectionError, OSError):
            return None
        if first2 is None:
            return None
        b0, b1 = first2[0], first2[1]
        opcode = b0 & 0x0F
        masked = b1 & 0x80
        length = b1 & 0x7F
        if length == 126:
            length = struct.unpack(">H", self._read_exact(2))[0]
        elif length == 127:
            length = struct.unpack(">Q", self._read_exact(8))[0]
        mask = self._read_exact(4) if masked else b""
        payload = self._read_exact(length) if length else b""
        if masked and payload:
            payload = bytes(b ^ mask[i % 4] for i, b in enumerate(payload))
        return opcode, payload

    def close(self) -> None:
        if self._sock is not None:
            try:
                self._send_frame(_OP_CLOSE, b"")
            except OSError:
                pass
            try:
                self._sock.close()
            finally:
                self._sock = None

    # -- low level buffered reads ------------------------------------------- #

    def _read_exact(self, n: int) -> bytes:
        while len(self._buf) < n:
            chunk = self._sock.recv(4096)  # type: ignore[union-attr]
            if not chunk:
                raise ConnectionError("socket closed")
            self._buf += chunk
        out, self._buf = self._buf[:n], self._buf[n:]
        return out

    def _read_until(self, marker: bytes) -> bytes:
        while marker not in self._buf:
            chunk = self._sock.recv(4096)  # type: ignore[union-attr]
            if not chunk:
                raise ConnectionError("socket closed during handshake")
            self._buf += chunk
        idx = self._buf.index(marker) + len(marker)
        out, self._buf = self._buf[:idx], self._buf[idx:]
        return out
