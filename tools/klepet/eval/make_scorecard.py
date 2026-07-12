#!/usr/bin/env python3
"""Render results.json into a detailed Markdown scorecard.

For every question it records: the question, Maks's verbatim answer, the score,
and a per-pair explanation of HOW the score was computed and WHY — which facts
were found or missing, the relevance/specificity/deflection signals, and the
weighted arithmetic that produced the final number.

    python3 make_scorecard.py         # results.json -> scorecard.md
"""

from __future__ import annotations

import json
from pathlib import Path

from evaluate import DEFLECTION, content_words, normalize, score_answer, stars
from questions import QUESTIONS

HERE = Path(__file__).resolve().parent
CATS = {"prepaid": "Prepaid (Mobi)", "postpaid": "Postpaid (Naj)",
        "broadband": "Broadband", "iptv": "IPTV (NEO TV)"}
W = {"recall": 0.55, "relevance": 0.20, "specificity": 0.15, "nondeflect": 0.10}

PREAMBLE = f"""# Maks answer-quality scorecard

Every question asked to the Telekom Slovenije **Maks** chat assistant, its
verbatim answer, the automatic score, and — for each pair — an explanation of
how that score was reached.

## How each answer is scored

The **quality score (0–100)** is a weighted sum of four signals:

| Signal | Weight | What it measures |
|---|---|---|
| **Fact recall** | {W['recall']:.0%} | Of the key facts published on telekom.si for this question, how many appear in the answer. Each fact is a group of accepted surface forms; the group counts as recalled if **any** form appears after normalisation (lower-cased, `€`→`eur`, decimal comma→dot, whitespace collapsed). |
| **Relevance** | {W['relevance']:.0%} | Share of the question's content words (length ≥ 4, minus stop-words) that also appear in the answer — i.e. did it stay on topic. |
| **Specificity** | {W['specificity']:.0%} | 1 if the answer contains a concrete price / quantity / package name (`€`, `GB`, `Mbit`, `Naj`, `Mobi`, `NEO`, …), else 0. Rewards committing to a real value over vague talk. |
| **Non-deflection** | {W['nondeflect']:.0%} | 0 if the answer is a *deflection* — a clarify-first reply or human-agent hand-off that never states the fact (a known redirect phrase is present **and** fact recall < 0.34) — else 1. |

`quality = 100 × (0.55·recall + 0.20·relevance + 0.15·specificity + 0.10·non-deflection)`,
then mapped to 1–5 ★ in 20-point bands. This is a deterministic, reproducible
rubric — **no LLM judge** — so the same answer always yields the same score.
It rewards stating the site's facts and penalises vague or deflecting replies;
it cannot judge nuances a human would (e.g. a correct answer worded so
differently that none of the accepted fact forms appear will still score low).

Source of truth: telekom.si product pages and price lists (ceniki), July 2026.

---
"""


def deflection_phrase(answer: str) -> str | None:
    low = answer.lower()
    for p in DEFLECTION:
        if p in low:
            return p
    return None


def explain(qid: str, cat: str, question: str, facts, answer: str) -> str:
    s = score_answer(answer, facts)
    recall = s["recall"]
    rel_q = content_words(question)
    rel_a = content_words(answer)
    matched_kw = sorted(rel_q & rel_a)
    relevance = (len(rel_q & rel_a) / len(rel_q)) if rel_q else 0.0
    spec = s["specificity"]
    deflected = s["deflected"]
    quality = 100 * (W["recall"] * recall + W["relevance"] * relevance
                     + W["specificity"] * spec + W["nondeflect"] * (0 if deflected else 1))
    st = stars(quality)

    out = [f"### `{qid}` · {CATS[cat]}\n",
           f"**Q:** {question}\n",
           "**Maks:**\n",
           "> " + answer.replace("\n", "\n> ").strip() + "\n",
           f"**Score: {quality:.1f}/100  ({'★'*st}{'☆'*(5-st)})**\n",
           "**How this score was reached:**\n"]

    # Fact recall detail
    out.append(f"- **Fact recall — {s['hits']}/{s['groups']} = {recall:.0%}** "
               f"(weight {W['recall']:.0%}). Expected facts:")
    for hd in s["hit_detail"]:
        forms = " / ".join(f"`{f}`" for f in hd["group"])
        mark = "✅ found" if hd["hit"] else "❌ missing"
        out.append(f"    - {mark}: {forms}")

    # Relevance detail
    if rel_q:
        shown = ", ".join(f"`{w}`" for w in matched_kw[:8]) or "—"
        out.append(f"- **Relevance — {len(rel_q & rel_a)}/{len(rel_q)} = {relevance:.0%}** "
                   f"(weight {W['relevance']:.0%}). Question keywords echoed in the answer: {shown}"
                   + (" …" if len(matched_kw) > 8 else ""))
    else:
        out.append(f"- **Relevance — n/a** (weight {W['relevance']:.0%}).")

    # Specificity
    out.append(f"- **Specificity — {int(spec)}/1** (weight {W['specificity']:.0%}): "
               + ("the answer contains a concrete price/quantity/package token."
                  if spec else "no concrete price/quantity/package token found."))

    # Deflection
    if deflected:
        ph = deflection_phrase(answer)
        out.append(f"- **Deflection — yes** (weight {W['nondeflect']:.0%} → 0): matched redirect "
                   f"phrase “{ph}” and fact recall < 34%, so this counts as a non-answer.")
    else:
        ph = deflection_phrase(answer)
        note = (f" (a redirect phrase “{ph}” is present, but fact recall ≥ 34%, so it is *not* "
                f"treated as a deflection)") if ph else ""
        out.append(f"- **Deflection — no** (weight {W['nondeflect']:.0%} → 1){note}.")

    # Arithmetic
    out.append(
        f"- **Weighted total:** "
        f"`0.55×{recall:.2f} + 0.20×{relevance:.2f} + 0.15×{spec:.0f} + "
        f"0.10×{0 if deflected else 1}` = **{quality/100:.3f} → {quality:.1f}/100**.")

    # One-line verdict
    if quality >= 80 and recall >= 0.5:
        verdict = "Strong: the answer states the published fact(s) and stays on topic."
    elif deflected:
        verdict = "Weak: Maks deflected/redirected instead of giving the fact."
    elif spec and recall == 0:
        verdict = ("Risky: Maks answered confidently with a specific value that does **not** "
                   "match the site — a candidate factual error.")
    elif recall > 0:
        verdict = "Partial: some but not all expected facts were stated."
    else:
        verdict = "Weak: the expected fact(s) did not appear in the answer."
    out.append(f"- **Verdict:** {verdict}\n")

    return "\n".join(out) + "\n---\n"


def main() -> int:
    results = json.loads((HERE / "results.json").read_text(encoding="utf-8"))
    facts_by_id = {qid: facts for qid, _c, _q, facts in QUESTIONS}
    ans_by_id = {r["id"]: r for r in results}

    # Overall + per-category summary from the recomputation
    parts = [PREAMBLE]
    order = [q for q in QUESTIONS if q[0] in ans_by_id]
    # summary table
    from collections import defaultdict
    agg = defaultdict(list)
    scored = []
    for qid, cat, question, facts in order:
        answer = ans_by_id[qid]["answer"]
        # reuse the same quality the record carries for the summary
        scored.append(ans_by_id[qid]["quality"])
        agg[cat].append(ans_by_id[qid]["quality"])
    parts.append("## Summary\n")
    parts.append(f"- Questions scored: **{len(scored)}**")
    parts.append(f"- Mean quality: **{sum(scored)/len(scored):.1f}/100**\n")
    parts.append("| Topic | Questions | Mean quality |")
    parts.append("|---|---|---|")
    for c, lbl in CATS.items():
        xs = agg[c]
        if xs:
            parts.append(f"| {lbl} | {len(xs)} | {sum(xs)/len(xs):.1f} |")
    parts.append("\n---\n")

    # Per-topic sections with every QA
    for c, lbl in CATS.items():
        parts.append(f"\n## {lbl}\n")
        for qid, cat, question, facts in order:
            if cat != c:
                continue
            parts.append(explain(qid, cat, question, facts, ans_by_id[qid]["answer"]))

    (HERE / "scorecard.md").write_text("\n".join(parts), encoding="utf-8")
    print(f"Wrote scorecard.md ({len(order)} questions)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
