"""Tiny ``{{var}}`` templating and dotted-path extraction helpers.

These two primitives are the glue between a profile (which is just data) and the
live values discovered at runtime (session ids, cursors, the user's message).

* :func:`render` walks any JSON-like structure and substitutes ``{{name}}``
  placeholders from a context dict. If a string is *exactly* one placeholder,
  the substituted value keeps its original type (so a template of ``"{{n}}"``
  can resolve to an int, list, etc.), otherwise normal string interpolation is
  used.
* :func:`extract` reads a value out of a decoded JSON response using a dotted
  path such as ``"data.session.id"`` or ``"messages.0.text"``.
"""

from __future__ import annotations

import re
from typing import Any, Mapping

_PLACEHOLDER = re.compile(r"\{\{\s*([a-zA-Z0-9_.]+)\s*\}\}")
_EXACT = re.compile(r"^\{\{\s*([a-zA-Z0-9_.]+)\s*\}\}$")


def render(obj: Any, ctx: Mapping[str, Any]) -> Any:
    """Recursively substitute ``{{var}}`` placeholders in *obj* from *ctx*."""
    if isinstance(obj, str):
        exact = _EXACT.match(obj)
        if exact:
            # Whole-string placeholder: preserve the referenced value's type.
            return _lookup(ctx, exact.group(1))
        return _PLACEHOLDER.sub(lambda m: str(_lookup(ctx, m.group(1), "")), obj)
    if isinstance(obj, Mapping):
        return {render(k, ctx): render(v, ctx) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [render(v, ctx) for v in obj]
    return obj


def extract(data: Any, path: str, default: Any = None) -> Any:
    """Read *path* (dotted, with numeric indices) out of decoded JSON *data*."""
    if not path:
        return data
    cur = data
    for part in path.split("."):
        if cur is None:
            return default
        if isinstance(cur, Mapping):
            cur = cur.get(part, default)
        elif isinstance(cur, (list, tuple)):
            try:
                cur = cur[int(part)]
            except (ValueError, IndexError):
                return default
        else:
            return default
    return cur


def _lookup(ctx: Mapping[str, Any], name: str, default: Any = None) -> Any:
    """Context lookup that also understands dotted paths into nested values."""
    if name in ctx:
        return ctx[name]
    return extract(ctx, name, default)
