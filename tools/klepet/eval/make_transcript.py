#!/usr/bin/env python3
"""Render results.json into a readable, self-contained HTML transcript.

Produces transcript.html: all questions + Maks's verbatim answers with the
per-question quality score, colour-coded by band, filterable by topic. The
output is a complete UTF-8 document (explicit charset) so it renders correctly
when opened directly in a browser.

    python3 make_transcript.py            # reads results.json -> transcript.html
"""

from __future__ import annotations

import html
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
CATS = {
    "prepaid": "Prepaid · Mobi", "postpaid": "Postpaid · Naj",
    "broadband": "Broadband", "iptv": "IPTV · NEO",
}


def band(q: float) -> str:
    return "good" if q >= 80 else ("warn" if q >= 55 else "crit")


CSS = """
*{box-sizing:border-box}
:root{--bg:#faf7f9;--surface:#fff;--surface2:#f4eef3;--ink:#1e1720;--muted:#736a75;
  --line:#e7dee6;--accent:#c60068;--good:#0e7c5a;--warn:#9a6a12;--crit:#c1362f;
  --good-bg:#e3f3ec;--warn-bg:#f6edd8;--crit-bg:#f7e3e1}
@media (prefers-color-scheme:dark){:root{--bg:#16121a;--surface:#1e1922;--surface2:#262029;
  --ink:#f2e9ef;--muted:#a79dab;--line:#322b36;--accent:#ff4fa3;--good:#43c295;--warn:#e0a63c;
  --crit:#f2726b;--good-bg:#12271f;--warn-bg:#2a2314;--crit-bg:#2c1919}}
body{margin:0;background:var(--bg);color:var(--ink);line-height:1.5;
  font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.wrap{max-width:860px;margin:0 auto;padding:clamp(18px,4vw,44px)}
.eyebrow{font-family:ui-monospace,Menlo,monospace;font-size:.72rem;letter-spacing:.16em;
  text-transform:uppercase;color:var(--accent);margin:0 0 8px}
h1{font-size:clamp(1.6rem,4vw,2.3rem);margin:0;font-weight:800;letter-spacing:-.02em}
.lede{color:var(--muted);margin:12px 0 22px;max-width:62ch}
.filters{display:flex;flex-wrap:wrap;gap:8px;position:sticky;top:0;padding:12px 0;
  background:var(--bg);z-index:5;border-bottom:1px solid var(--line);margin-bottom:20px}
.f{font:inherit;font-size:.82rem;font-weight:600;padding:6px 12px;border-radius:99px;
  border:1px solid var(--line);background:var(--surface);color:var(--ink);cursor:pointer}
.f.active{background:var(--accent);color:#fff;border-color:var(--accent)}
.qa{background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--muted);
  border-radius:12px;padding:16px 18px;margin-bottom:14px}
.qa.good{border-left-color:var(--good)} .qa.warn{border-left-color:var(--warn)}
.qa.crit{border-left-color:var(--crit)}
.qa header{display:flex;align-items:center;gap:10px;margin-bottom:8px}
.qid{font-family:ui-monospace,Menlo,monospace;font-size:.72rem;color:var(--muted)}
.cat{font-size:.72rem;color:var(--muted)}
.score{margin-left:auto;font-weight:800;font-variant-numeric:tabular-nums}
.stars{color:var(--accent);font-weight:400;margin-left:6px;font-size:.85rem}
.q{font-weight:700;margin:0 0 8px}
.a{margin:0;color:var(--ink)}
.meta{margin-top:10px;font-size:.75rem;color:var(--muted);font-family:ui-monospace,Menlo,monospace;
  display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.chip{font-size:.68rem;font-weight:700;padding:2px 8px;border-radius:99px}
.chip.crit{color:var(--crit);background:var(--crit-bg)}
footer{margin-top:30px;padding-top:16px;border-top:1px solid var(--line);color:var(--muted);font-size:.76rem}
"""

JS = """
const btns=document.querySelectorAll('.f'),cards=document.querySelectorAll('.qa');
btns.forEach(b=>b.addEventListener('click',()=>{
  btns.forEach(x=>x.classList.remove('active'));b.classList.add('active');
  const f=b.dataset.f;
  cards.forEach(c=>c.style.display=(f==='all'||c.dataset.cat===f)?'':'none');
}));
"""


def build(results: list) -> str:
    rows = []
    for r in results:
        ans = html.escape(r["answer"]).replace("\n", "<br>")
        flags = []
        if r["deflected"]:
            flags.append('<span class="chip crit">deflection</span>')
        if r["specificity"] == 1.0 and not r["deflected"] and r["recall"] == 0.0:
            flags.append('<span class="chip crit">fact-check failed</span>')
        rows.append(f'''<article class="qa {band(r['quality'])}" data-cat="{r['category']}">
  <header>
    <span class="qid">{r['id']}</span>
    <span class="cat">{CATS[r['category']]}</span>
    <span class="score">{r['quality']:.0f}<span class="stars">{'★'*r['stars']}</span></span>
  </header>
  <p class="q">{html.escape(r['question'])}</p>
  <p class="a">{ans}</p>
  <div class="meta">recall {r['recall']*100:.0f}% · {r['hits']}/{r['groups']} facts {' '.join(flags)}</div>
</article>''')

    cc = Counter(r["category"] for r in results)
    btns = f'<button class="f active" data-f="all">All ({len(results)})</button>'
    for c, lbl in CATS.items():
        btns += f'<button class="f" data-f="{c}">{lbl.split(" · ")[0]} ({cc[c]})</button>'

    return f'''<!doctype html>
<html lang="sl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Maks — Conversation transcript ({len(results)} Q&amp;A)</title>
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
  <p class="eyebrow">Telekom Slovenije · Maks · automated evaluation</p>
  <h1>Conversation transcript</h1>
  <p class="lede">All {len(results)} questions asked to the Maks chat assistant and its verbatim
  replies, with the automatic quality score for each. Left border: green = strong, amber = mixed,
  red = weak.</p>
  <div class="filters">{btns}</div>
  {"".join(rows)}
  <footer>Independent, automated evaluation · not affiliated with Telekom Slovenije ·
  answers reflect a single run and may change over time.</footer>
</div>
<script>{JS}</script>
</body>
</html>'''


def main() -> int:
    results = json.loads((HERE / "results.json").read_text(encoding="utf-8"))
    (HERE / "transcript.html").write_text(build(results), encoding="utf-8")
    print(f"Wrote transcript.html ({len(results)} entries)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
