#!/usr/bin/env python3
"""Grade the hard-synthesis runs (LLM-judged by Claude) into hard_synthesis.md.

Reads hard_synthesis_runs.json (transcripts + ground-truth targets) and my
per-scenario verdicts below, and renders a readable graded report.

    python3 make_hard_synthesis.py
"""

from __future__ import annotations

import json
import statistics
from pathlib import Path

HERE = Path(__file__).resolve().parent

# My verdicts: id -> (score_0_100, label, assessment). PASS>=85, PARTIAL 50-84, FAIL<50.
JUDGE = {
    "hs01": (95, "PASS",
             "Full arithmetic done correctly and carried across all three turns: "
             "6×6,99 + 6×13,99 = 125,88 € (yr1), 167,88 € (yr2), average 12,24 €/mo. "
             "Exactly the target. Genuine multi-step synthesis."),
    "hs02": (50, "PARTIAL",
             "Applies the Poveži in prihrani discount concept and keeps context, but "
             "the number is wrong and no clean total is ever given. It quotes 19,66 € "
             "‘brez DDV’ for Naj B — that is Naj C’s ex-VAT discounted figure; Naj B with "
             "−5 € is 22,99 € (with VAT). It also silently switches to ex-VAT and never "
             "sums mobile + fixed. Right idea, wrong composition."),
    "hs03": (20, "FAIL",
             "Opens with a deflection (fiksni/mobilni clarify) instead of recommending, "
             "never tracks the 15 GB / EU-travel / unlimited constraints as they change, "
             "and finally recommends ‘Največ’ — a package that does not exist "
             "(hallucination). No synthesis."),
    "hs04": (55, "PARTIAL",
             "Mixed. EU-data comparison is correct (Naj B 41,71 GB vs Mobi C needs a "
             "bundle → +41,71 GB). But it opens with a deflection, and the cost claim is "
             "shaky: it declares Naj B cheaper using the 10,99 € promo (which needs "
             "Poveži + fixed) and never computes Mobi C’s yearly cost, so the comparison "
             "isn’t apples-to-apples."),
    "hs05": (25, "FAIL",
             "Anaphora broke. T1 refuses to name the package (should be Naj C, 43,20 GB "
             "EU); T2 loses the referent entirely and re-asks mobilni/TV; only T3 gives a "
             "generic discount. It never establishes ‘ta paket’, so the chain fails."),
    "hs06": (95, "PASS",
             "All three rules chained correctly: akcijska price conditions → NOT eligible "
             "under the 60-day new-subscriber rule → Penzion and Poveži in prihrani are "
             "mutually exclusive (the larger, Poveži, applies). Strong rule composition."),
    "hs07": (95, "PASS",
             "Correctly keeps two distinct limits apart across turns: SI throttle to "
             "64/64 kbit/s after 200 GB, EU cap 20,85 GB then charged per price list with "
             "speed unchanged. Notably, it gets the Mobi C throttle RIGHT here — the exact "
             "fact it got WRONG (‘1 GB’) as a single-shot question (mobi05). Context helped."),
    "hs08": (30, "FAIL",
             "Context carryover failed. The 700 € phone is stated in T1 but T1 deflects; "
             "T2 dumps the whole insurance-tier table without picking 700 €→9,95 €; T3 "
             "asks for the device value again and never computes the 27,99 + 9,95 = "
             "37,94 €/mo total. The needed facts appear but are never combined."),
    "hs09": (90, "PASS",
             "Distinguishes EU from Balkan across turns: Croatia included (41,71 GB EU) → "
             "Serbia NOT included → recommends the Balkan internet neomejeno bundle and "
             "lists the countries. Only miss: it never states the bundle’s price."),
    "hs10": (90, "PASS",
             "Robust to false premises — corrects ‘Mobi has 24-mo binding’ (it doesn’t) "
             "and ‘Mobi has a monthly subscription’ (it’s prepaid, top-up), then compares "
             "unlimited-data options honestly. No sycophancy."),
}


def main() -> int:
    runs = {r["id"]: r for r in json.loads((HERE / "hard_synthesis_runs.json").read_text("utf-8"))}
    order = [rid for rid in JUDGE if rid in runs]
    scores = [JUDGE[r][0] for r in order]
    labels = [JUDGE[r][1] for r in order]

    L = []
    A = L.append
    A("# Maks — hard multi-turn synthesis probes\n")
    A("Ten scenarios, each a **single conversation** whose turns force Maks to carry "
      "context and *combine* facts (arithmetic, conditional rules, tradeoffs, anaphora, "
      "false-premise correction) — not retrieve one value. Graded by me (LLM judge) against "
      "a ground-truth synthesis target. PASS ≥ 85 · PARTIAL 50–84 · FAIL < 50.\n")

    A("## Summary\n")
    A(f"- Scenarios: **{len(order)}**  ·  mean **{statistics.mean(scores):.0f}/100**")
    A(f"- ✅ PASS **{labels.count('PASS')}**  ·  🟡 PARTIAL **{labels.count('PARTIAL')}**  ·  "
      f"❌ FAIL **{labels.count('FAIL')}**\n")
    A("| id | Scenario | Type | Verdict | Score |")
    A("|---|---|---|:--:|--:|")
    emoji = {"PASS": "✅", "PARTIAL": "🟡", "FAIL": "❌"}
    for rid in order:
        r = runs[rid]
        s, lab, _ = JUDGE[rid]
        A(f"| `{rid}` | {r['name']} | {r['type']} | {emoji[lab]} {lab} | {s} |")
    A("")
    A("**What holds up:** arithmetic when the opener is concrete (hs01), conditional-rule "
      "composition (hs06), keeping two different limits apart (hs07), roaming EU-vs-Balkan "
      "(hs09), and resisting false premises (hs10).\n")
    A("**Where it breaks:** open-ended recommendations that shift across turns (hs03), "
      "anaphora / referring back to ‘that package’ (hs05), and multi-fact arithmetic that "
      "needs a value carried from an earlier turn (hs08). A recurring trigger: when the "
      "first turn is an open ‘what do you recommend / which package’, Maks deflects "
      "(fiksni vs mobilni) and then loses the thread.\n")
    A("**Notable:** hs07 answers the Mobi C 200 GB throttle **correctly**, the same fact "
      "it got **wrong** (‘1 GB’) as a standalone question — its answers are not consistent "
      "between phrasings/runs. hs03 also **hallucinated** a non-existent package (‘Največ’).\n")

    A("---\n\n## Scenarios\n")
    for rid in order:
        r = runs[rid]
        s, lab, note = JUDGE[rid]
        A(f"### {emoji[lab]} `{rid}` — {r['name']}  ·  {s}/100 ({lab})\n")
        A(f"*Type: {r['type']}. Target: {r['target']}*\n")
        for i, t in enumerate(r["turns"], 1):
            A(f"**T{i} — You:** {t['q']}")
            ans = t["a"].replace("\n", " ").strip()
            A(f"**Maks:** {ans}\n")
        A(f"**Verdict:** {note}\n")
        A("---\n")

    (HERE / "hard_synthesis.md").write_text("\n".join(L), encoding="utf-8")
    print(f"Wrote hard_synthesis.md · mean {statistics.mean(scores):.0f}/100 · "
          f"{labels.count('PASS')} pass / {labels.count('PARTIAL')} partial / {labels.count('FAIL')} fail")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
