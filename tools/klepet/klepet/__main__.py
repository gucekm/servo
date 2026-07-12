"""Command line interface for the klepet chat client.

Subcommands:

    chat        Open an interactive chat session against a profile.
    import-har  Build a profile skeleton from a browser HAR capture.
    demo        Run a local, offline echo server to exercise the client.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .client import KlepetClient
from .config import load_profile


def _print_message(author: str, text: str) -> None:
    if author == "_error":
        print(f"\n[!] {text}", file=sys.stderr)
    else:
        print(f"\n{author}: {text}\n> ", end="", flush=True)


def cmd_chat(args: argparse.Namespace) -> int:
    profile = load_profile(args.profile)
    print(f"Connecting to '{profile.name}' ({profile.transport}) ...")
    client = KlepetClient(profile, on_message=_print_message)
    try:
        client.start()
    except Exception as exc:
        print(f"Failed to start session: {exc}", file=sys.stderr)
        return 1
    print("Connected. Type a message and press Enter. Ctrl-D or /quit to exit.")
    try:
        while True:
            try:
                line = input("> ")
            except EOFError:
                break
            line = line.strip()
            if line in ("/quit", "/exit"):
                break
            if not line:
                continue
            try:
                client.send(line)
            except Exception as exc:
                print(f"[!] send failed: {exc}", file=sys.stderr)
    except KeyboardInterrupt:
        pass
    finally:
        client.stop()
    print("\nBye.")
    return 0


def cmd_import_har(args: argparse.Namespace) -> int:
    from . import harimport

    har = harimport.load_har(args.har)
    candidates = harimport.analyze(har)
    if not candidates:
        print("No chat-like requests found in the HAR.", file=sys.stderr)
        print("Make sure you captured the network traffic *while* chatting.", file=sys.stderr)
        return 1

    print(harimport.render_report(candidates))
    profile = harimport.build_profile(candidates, name=args.name)
    text = json.dumps(profile, indent=2, ensure_ascii=False)
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"\nWrote profile skeleton to {args.output}")
        print("Review the fields marked 'REVIEW:' before running `chat`.")
    else:
        print("\n--- generated profile (use -o to save) ---")
        print(text)
    return 0


def cmd_demo(args: argparse.Namespace) -> int:
    """Offline self-test: a local echo backend proves the client end-to-end."""
    from .demo import run_demo

    return run_demo()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="klepet", description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_chat = sub.add_parser("chat", help="interactive chat against a profile")
    p_chat.add_argument("profile", help="path to a profile JSON file")
    p_chat.set_defaults(func=cmd_chat)

    p_har = sub.add_parser("import-har", help="build a profile from a browser HAR")
    p_har.add_argument("har", help="path to a .har file")
    p_har.add_argument("-o", "--output", help="write the generated profile here")
    p_har.add_argument("-n", "--name", default="telekom_si", help="profile name")
    p_har.set_defaults(func=cmd_import_har)

    p_demo = sub.add_parser("demo", help="run the offline echo self-test")
    p_demo.set_defaults(func=cmd_demo)

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
