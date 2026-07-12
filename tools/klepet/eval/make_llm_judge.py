#!/usr/bin/env python3
"""Build llm_judge.md from my hand-authored verdicts (llm_judge_data.py).

Combines each LLM-judge verdict with the recorded answer and the deterministic
heuristic score, then writes: methodology, summary stats, a heuristic-vs-judge
comparison, the notable disagreements, and the full 300-row table.

    python3 make_llm_judge.py     # llm_judge_data.py + results.json -> llm_judge.md
"""

from __future__ import annotations

import json
import statistics
from collections import Counter
from pathlib import Path

from llm_judge_data import JUDGE
from questions import QUESTIONS

HERE = Path(__file__).resolve().parent
CATS = {"prepaid": "Prepaid (Mobi)", "postpaid": "Postpaid (Naj)",
        "broadband": "Broadband", "iptv": "IPTV (NEO TV)"}
LABEL_EMOJI = {"OK": "✅", "PART": "🟡", "DEFLECT": "🔁", "WRONG": "❌"}


def short(q: str, n: int = 60) -> str:
    return q if len(q) <= n else q[: n - 1] + "…"


def main() -> int:
    res = {r["id"]: r for r in json.loads((HERE / "results.json").read_text("utf-8"))}
    order = [(qid, cat, q) for qid, cat, q, _ in QUESTIONS if qid in JUDGE and qid in res]

    rows = []
    for qid, cat, q in order:
        ls, label, note = JUDGE[qid]
        hs = res[qid]["quality"]
        rows.append({"id": qid, "cat": cat, "q": q, "llm": ls, "label": label,
                     "note": note, "heur": hs, "delta": round(ls - hs, 1),
                     "answer": res[qid]["answer"]})

    lines = []
    A = lines.append

    A("# Maks answers — my (LLM) judgement\n")
    A("I read all 300 question/answer pairs and scored each one myself, as an "
      "LLM judge, rather than by the automatic rubric. I judged **correctness "
      "first** (does the answer match telekom.si / the ceniki?), then "
      "**relevance and helpfulness** (does it actually answer what was asked?).\n")
    A("Labels: ✅ **OK** correct & responsive · 🟡 **PART** on-topic but "
      "incomplete/adjacent · 🔁 **DEFLECT** clarify-first or agent hand-off, no "
      "answer · ❌ **WRONG** states a value that contradicts the site. I score a "
      "**confident wrong answer at or below a deflection**, because a wrong "
      "number misleads whereas ‘let me connect you’ at least doesn’t.\n")

    # ---- summary ----
    llm = [r["llm"] for r in rows]
    heur = [r["heur"] for r in rows]
    A("## Summary\n")
    A(f"- Answers judged: **{len(rows)}**")
    A(f"- **My mean score: {statistics.mean(llm):.1f}/100**  ·  heuristic mean: "
      f"{statistics.mean(heur):.1f}/100")
    lc = Counter(r["label"] for r in rows)
    A(f"- Verdicts: ✅ OK **{lc['OK']}** · 🟡 PART **{lc['PART']}** · "
      f"🔁 DEFLECT **{lc['DEFLECT']}** · ❌ WRONG **{lc['WRONG']}**\n")

    A("| Topic | Answers | My mean | Heuristic mean | ✅ | 🟡 | 🔁 | ❌ |")
    A("|---|---|---|---|---|---|---|---|")
    for c, lbl in CATS.items():
        rs = [r for r in rows if r["cat"] == c]
        cc = Counter(r["label"] for r in rs)
        A(f"| {lbl} | {len(rs)} | {statistics.mean([r['llm'] for r in rs]):.1f} | "
          f"{statistics.mean([r['heur'] for r in rs]):.1f} | {cc['OK']} | "
          f"{cc['PART']} | {cc['DEFLECT']} | {cc['WRONG']} |")
    A("")

    # ---- agreement ----
    close = sum(1 for r in rows if abs(r["delta"]) <= 10)
    A("## Where I agree / disagree with the heuristic\n")
    A(f"- Within 10 points of the heuristic on **{close}/{len(rows)}** answers "
      f"({100*close/len(rows):.0f}%) — the rubric tracks my judgement well on the "
      f"clear cases.\n")

    wrong = [r for r in rows if r["label"] == "WRONG"]
    A(f"**❌ Confident factual errors I flagged ({len(wrong)})** — the rubric "
      f"scores these like weak/partial answers; I score them as failures because "
      f"they state a wrong value:\n")
    A("| id | Question | Maks | My note |")
    A("|---|---|---|---|")
    for r in sorted(wrong, key=lambda x: x["heur"], reverse=True):
        ans = " ".join(r["answer"].split())
        A(f"| `{r['id']}` | {short(r['q'],48)} | {short(ans,70)} | {r['note']} |")
    A("")

    # biggest disagreements either direction
    up = sorted([r for r in rows if r["delta"] >= 20], key=lambda x: -x["delta"])[:8]
    down = sorted([r for r in rows if r["delta"] <= -20], key=lambda x: x["delta"])[:8]
    if up:
        A("**Where I scored *higher* than the rubric** (it under-credited a "
          "reasonable answer):\n")
        A("| id | Question | My | Heur | Why |")
        A("|---|---|---|---|---|")
        for r in up:
            A(f"| `{r['id']}` | {short(r['q'],46)} | {r['llm']} | {r['heur']:.0f} | {r['note']} |")
        A("")
    if down:
        A("**Where I scored *lower* than the rubric** (it over-credited a "
          "non-answer or wrong reply):\n")
        A("| id | Question | My | Heur | Why |")
        A("|---|---|---|---|---|")
        for r in down:
            A(f"| `{r['id']}` | {short(r['q'],46)} | {r['llm']} | {r['heur']:.0f} | {r['note']} |")
        A("")

    # ---- full table ----
    A("## Full verdicts (all 300)\n")
    for c, lbl in CATS.items():
        A(f"\n### {lbl}\n")
        A("| id | Question | Verdict | My | Heur | Δ | Note |")
        A("|---|---|:--:|--:|--:|--:|---|")
        for r in [x for x in rows if x["cat"] == c]:
            em = LABEL_EMOJI[r["label"]]
            A(f"| `{r['id']}` | {short(r['q'],54)} | {em} {r['label']} | "
              f"{r['llm']} | {r['heur']:.0f} | {r['delta']:+.0f} | {r['note']} |")
    A("")

    (HERE / "llm_judge.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote llm_judge.md ({len(rows)} verdicts) · "
          f"my mean {statistics.mean(llm):.1f} vs heuristic {statistics.mean(heur):.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
