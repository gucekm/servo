#!/usr/bin/env python3
"""Deflection-quality and link audit for the Maks bot.

The main audit counted 51/300 answers as deflections (non-answers) but scored
them only as *absent* answers. This test asks what a deflection is actually
worth to the customer:

  1. **Re-asks every deflected question** over the raw Boost API so that
     hyperlinks survive (the plain-text transcripts strip ``<a href>``), and
     classifies which escalation channel each answer offers:
     live agent, Moj Telekom app, a web link, a phone number, a shop —
     or nothing but a clarifying counter-question (a dead end).
  2. **Health-checks every URL** Maks emitted (this run + the original
     results.json): HTTP status, redirect target, reachable or broken.

Usage:
    python3 link_audit.py                         # live re-ask + URL checks
    python3 link_audit.py --report link_audit_runs.json   # re-render md only
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

import requests  # noqa: E402

from live import ask_fresh  # noqa: E402

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# Escalation channels a deflection can offer, with detection patterns.
CHANNELS = {
    "agent": ["sodelavc", "povežem", "povezem", "agent", "svetovalc", "klepet s "],
    "moj_telekom": ["moj telekom", "aplikacij"],
    "phone": ["080 8000", "080 70 70", "pokličite", "poklicete", "telefonsko številko 080"],
    "shop": ["poslovaln", "trgovin", "prodajnem mestu", "prodajna mesta"],
    "web": ["spletni strani", "telekom.si", "spletnem mestu", "na spletu", "povezavi"],
}

CLARIFY = ["mi lahko", "prosim, napišite", "prosim napišite", "kateri paket",
           "o katerem", "o kateri", "natančneje", "natančnejš", "ali vas zanima",
           "ali sprašujete", "mi poveste", "pojasnite", "katera", "kakšn"]


def classify(reply: dict) -> dict:
    low = reply["text"].lower()
    offered = [ch for ch, pats in CHANNELS.items() if any(p in low for p in pats)]
    if reply["urls"]:
        if "web" not in offered:
            offered.append("web")
    if reply["phones"] and "phone" not in offered:
        offered.append("phone")
    clarify = any(p in low for p in CLARIFY)
    # actionable = the customer got at least one concrete way forward
    actionable = bool(offered)
    return {"channels": offered, "clarify_only": clarify and not offered,
            "actionable": actionable}


def check_url(url: str) -> dict:
    try:
        r = requests.get(url, headers={"User-Agent": UA}, timeout=20, allow_redirects=True)
        return {"url": url, "status": r.status_code, "final_url": r.url,
                "ok": r.status_code < 400,
                "redirected": r.url.rstrip("/") != url.rstrip("/")}
    except Exception as exc:  # noqa: BLE001
        return {"url": url, "status": None, "final_url": None, "ok": False,
                "error": str(exc)[:200]}


def run_live(delay: float) -> dict:
    results = json.loads((HERE / "results.json").read_text(encoding="utf-8"))
    deflected = [r for r in results if r["deflected"]]
    url_re = re.compile(r"https?://[^\s\)\]\"<>]+")
    baseline_urls = sorted({u.rstrip(".,;") for r in results
                            for u in url_re.findall(r["answer"])})

    out = {"captured": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()),
           "questions": [], "url_checks": []}
    print(f"Re-asking {len(deflected)} deflected questions (raw API, links kept)...\n")
    all_urls = set(baseline_urls)
    for i, r in enumerate(deflected, 1):
        reply = ask_fresh(r["question"])
        cls = classify(reply)
        out["questions"].append({
            "id": r["id"], "category": r["category"], "question": r["question"],
            "answer": reply["text"], "urls": reply["urls"], "phones": reply["phones"],
            **cls,
        })
        all_urls.update(reply["urls"])
        ch = "+".join(cls["channels"]) or ("clarify-only" if cls["clarify_only"] else "NONE")
        print(f"[{i:2}/{len(deflected)}] {r['id']:7} -> {ch}", flush=True)
        time.sleep(delay)

    # Drop non-web schemes (tel:, mailto:) from the HTTP health check.
    web_urls = sorted(u for u in all_urls if u.startswith(("http://", "https://")))
    print(f"\nHealth-checking {len(web_urls)} distinct URLs...")
    for u in web_urls:
        chk = check_url(u)
        out["url_checks"].append(chk)
        print(f"  [{chk.get('status')}] {u}", flush=True)
    return out


def render(data: dict) -> str:
    qs = data["questions"]
    checks = data["url_checks"]
    n_act = sum(1 for q in qs if q["actionable"])
    channel_counts = Counter(ch for q in qs for ch in q["channels"])
    dead = [q for q in qs if not q["actionable"]]
    broken = [c for c in checks if not c["ok"]]

    lines = [
        "# Maks deflection-quality & link audit",
        "",
        f"Captured {data['captured']}. The {len(qs)} questions the main audit scored as "
        "deflections were re-asked over the raw Boost API (so hyperlinks survive), and "
        "every URL Maks emitted was health-checked.",
        "",
        "## What a deflection offers the customer",
        "",
        f"- **{n_act}/{len(qs)} deflections are *actionable*** — they hand the customer at "
        "least one concrete channel (agent, app, link, phone, shop).",
        f"- **{len(dead)}/{len(qs)} are dead ends** — only a clarifying counter-question or "
        "a generic apology, with no way forward.",
        "",
        "| channel offered | count |",
        "|---|---|",
    ]
    label = {"agent": "live agent hand-off", "moj_telekom": "Moj Telekom app",
             "web": "website / link", "phone": "phone number", "shop": "shop visit"}
    for ch, cnt in channel_counts.most_common():
        lines.append(f"| {label.get(ch, ch)} | {cnt} |")
    lines += [
        "",
        "## URL health",
        "",
        f"- {len(checks)} distinct URLs checked; **{len(checks) - len(broken)} OK, "
        f"{len(broken)} broken**.",
        "",
        "| status | URL | note |",
        "|---|---|---|",
    ]
    for c in sorted(checks, key=lambda c: (c["ok"], c["url"])):
        note = c.get("error", "")
        if not note and c.get("redirected"):
            note = f"redirects to {c['final_url']}"
        lines.append(f"| {'OK ' + str(c['status']) if c['ok'] else 'BROKEN ' + str(c.get('status'))} "
                     f"| {c['url']} | {note} |")
    if dead:
        lines += ["", "## Dead-end deflections (no channel offered)", ""]
        for q in dead:
            ans = q["answer"].replace("\n", " ")
            if len(ans) > 220:
                ans = ans[:220] + "…"
            lines.append(f"- **`{q['id']}`** ({q['category']}) — {q['question']}")
            lines.append(f"  - Maks: {ans}")
    lines += ["", "## Per-question detail", "",
              "| id | channels | urls | phones |", "|---|---|---|---|"]
    for q in qs:
        lines.append(f"| `{q['id']}` | {', '.join(q['channels']) or '—'} "
                     f"| {len(q['urls'])} | {', '.join(q['phones']) or '—'} |")
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--delay", type=float, default=0.4)
    ap.add_argument("--report", metavar="RUNS_JSON",
                    help="skip the live run; re-render link_audit.md from saved runs")
    args = ap.parse_args(argv)

    if args.report:
        data = json.loads(Path(args.report).read_text(encoding="utf-8"))
    else:
        data = run_live(args.delay)
        (HERE / "link_audit_runs.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    (HERE / "link_audit.md").write_text(render(data), encoding="utf-8")
    print("Wrote link_audit_runs.json and link_audit.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
