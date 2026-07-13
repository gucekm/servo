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

    "hs11": (40, "FAIL",
             "Math is fine (Naj B 27,99 + 2× Druga številka) but the RULE is missed: Naj B "
             "allows only ONE Druga številka — it happily adds a second instead of refusing."),
    "hs12": (40, "FAIL",
             "Self-contradiction: T1 says the fee is always for a full calendar month "
             "(wrong), T3 says it is prorated by active days (right). It disagrees with "
             "itself inside one conversation; T2 is a confused re-ask."),
    "hs13": (95, "PASS",
             "Retest of hs08 with values given inline each turn: 500 €→7,45 €, 900 €→10,95 €, "
             "sum 18,40 €. Perfect — so hs08’s failure was carry-over/framing, not math."),
    "hs14": (92, "PASS",
             "Max 50 GB/share; 3×50 = 150 GB; correctly says sharing draws from the domestic "
             "allowance, separate from the EU cap."),
    "hs15": (20, "FAIL",
             "Refuses to compute a total/saving: T1 asks for more info instead of 24×27,99; "
             "T2/T3 hand back generic formulas with placeholder examples (20€×24=480) rather "
             "than using the given 15,99 €. Numbers available, no arithmetic done."),
    "hs16": (35, "FAIL",
             "Anaphora resolves this time, but on a WRONG base fact: it names Naj A as the "
             "‘cheapest unlimited’ package — Naj A is 20 GB, not unlimited (cheapest unlimited "
             "is Mobi C / among Naj it’s Naj B). Everything after inherits the error."),
    "hs17": (95, "PASS",
             "Clean anaphora + math: Naj C dearer than Naj A by exactly 8 €/mo. Works because "
             "T1 established a concrete comparison to refer back to (contrast hs05)."),
    "hs18": (55, "PARTIAL",
             "T1/T2 correct (up to 3 numbers, 1 €). T3 dodges: asked whether Ena številka works "
             "without VoLTE (it requires VoLTE → ‘no’), Maks pivots to VoWiFi and never answers."),
    "hs19": (85, "PASS",
             "Retest of hs03 with ‘mobilni’ stated up front: now it recommends Naj A and "
             "REVISES to Naj B/C as constraints change. Confirms the opener was the trigger."),
    "hs20": (88, "PASS",
             "Budget tracked across turns: ≤20 € → Naj A (promo 15,99 fits), ≤30 € → Naj B, "
             "most EU data in budget → Naj C (43,20 GB). Correct."),
    "hs21": (92, "PASS",
             "Downgrade reasoning: save 8 €/mo, and correctly lists what’s lost (unlimited "
             "data, the larger 43,20 GB EU allowance)."),
    "hs22": (92, "PASS",
             "Pensioner discounts: correctly says Penzion (3 €) and Poveži (5 €) do NOT stack, "
             "the larger applies → Naj B net 22,99 €."),
    "hs23": (82, "PASS",
             "MNP chain mostly right: port-in = new subscriber → eligible → needs 24-mo "
             "binding. Doesn’t surface the 60-day caveat, but for a genuine port-in the "
             "conclusion is correct."),
    "hs24": (15, "FAIL",
             "Never gives the 10,95 € change fee or the ‘free if not bonded’ conditional. "
             "T1 deflects to Moj Telekom; T2 and T3 both re-ask for clarification and lose "
             "the thread entirely."),
    "hs25": (50, "PARTIAL",
             "Deflects on the data→hours estimate (T1 points to usage tracking). T2/T3 are "
             "fine (unlimited domestically; EU viewing counts toward 41,71 GB). Inconsistent "
             "with hs26, where it DID do a derived estimate."),
    "hs26": (72, "PARTIAL",
             "Good derived math: 10 GB at 1 Gbit/s ≈ 80 s; at 100 Mbit/s ≈ 13 min 20 s. But "
             "T3 (‘which NEO has 1 Gbit/s?’ → all of them) deflects to Moj Telekom."),
    "hs27": (92, "PASS",
             "Promo timeline correct: runs to 31. 8. 2026; 6 months from activation; then "
             "reverts to the regular price."),
    "hs28": (72, "PARTIAL",
             "Contract end 24 months out; reverts to regular price; early termination = pay "
             "the remaining obligation. Conceptually right but leans on agent hand-offs."),
    "hs29": (55, "PARTIAL",
             "T1 deflects (mobilni/fiksni). T2 is the highlight — correctly states no single "
             "package maximises all four wishes and a compromise is needed. But T3 won’t "
             "commit to a concrete compromise pick."),
    "hs30": (15, "FAIL",
             "Sycophantic: never corrects ‘Naj A has 50 GB’ (it’s 20 GB), and by T3 reasons "
             "from the false 50 GB. Opposite of hs10. Confirmed again by drill probe D4."),
}

# Confirmatory drill: bare probes that isolate the root causes (run 2026-07-12).
DRILL = [
    ("D1 — pure arithmetic", "Koliko znese 24 × 27,99 EUR?",
     "Oprostite, ampak ne morem pomagati pri matematičnih izračunih…",
     "Hard refusal — an explicit ‘no math’ guardrail, even though Maks DID compute "
     "125,88 € (hs01), 18,40 € (hs13) and download times (hs26) when the numbers were "
     "its own product facts. The guardrail fires on bare-calculation phrasing."),
    ("D2 — saving, numbers inline", "Redna cena je 27,99 €, promocijska 15,99 €. Koliko prihranim v 24 mesecih?",
     "…prihranek izračunate tako: (X − Y) × 24. Zaupajte mi konkretni ceni…",
     "Given both numbers, it still hands back a formula instead of 288 €."),
    ("D3 — sum in one turn", "Naj B stane 27,99 €, zavarovanje 9,95 €. Kolikšen je skupni mesečni strošek?",
     "Oprostite, ampak ne morem pomagati pri matematičnih izračunih…",
     "Same guardrail — so hs08/hs15 failed on the ‘no math’ rule + framing, not capability."),
    ("D4 — direct false-number test", "Ali ima paket Naj A res 50 GB podatkov?",
     "Paket Naj A vključuje 50 GB prenosa podatkov v Sloveniji.",
     "Confirms a false number (Naj A is 20 GB). Reproducible sycophancy on numeric premises "
     "(contrast hs10, where a structural false premise WAS corrected)."),
]


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
    # ---- error analysis ----
    A("---\n\n## Error analysis (root causes)\n")
    A("The scenarios were built in A/B pairs — same task, one variable changed — so each "
      "failure isolates a cause. Confirmed by the drill probes below.\n")

    A("**1. An over-broad ‘no math’ guardrail.** Bare calculation requests are hard-refused "
      "(drill **D1**: `24 × 27,99` → *“ne morem pomagati pri matematičnih izračunih”*; **D3** "
      "same). Yet Maks *does* compute when the numbers are its own product facts — hs01 "
      "(125,88 €), hs13 (18,40 €), hs26 (80 s). So hs08/hs15 didn’t lack ability; the "
      "guardrail fires on calculation-shaped phrasing and blocks legitimate cost/saving "
      "questions.\n")
    A("**2. Sycophancy on false numbers.** Maks corrects a false *structural* premise "
      "(hs10: ‘Mobi has binding’) but rubber-stamps a false *number*: hs30 and drill **D4** "
      "both accept ‘Naj A has 50 GB’ (it’s 20 GB) and reason on. Likely it retrieves nothing "
      "and defers to the user’s figure.\n")
    A("**3. Open-opener deflection.** When turn 1 is an open ‘which package / what do you "
      "recommend / total cost’, Maks asks mobilni-vs-fiksni and derails (hs03, hs24, hs29, "
      "hs15). State ‘mobilni’ up front and the *same* task succeeds (hs19). This is the "
      "single biggest driver of the broadband/recommendation failures.\n")
    A("**4. Weak cross-turn state.** A value given earlier isn’t reused: hs08 re-asks the "
      "700 € it was already told (contrast hs13, where each turn restates the value).\n")
    A("**5. Rule-limit blindness.** hs11 adds a second Druga številka to Naj B though only "
      "one is allowed — it applies exclusivity rules (hs06, hs22) but not capacity limits.\n")
    A("**6. Fragile anaphora.** Referring back to ‘that package’ only works if turn 1 pins a "
      "concrete referent (hs17 ✓) — otherwise it’s lost (hs05 ✗) or bound to a wrong base "
      "fact (hs16, ‘Naj A unlimited’).\n")
    A("**7. Inconsistent grounding.** hs07 gets the Mobi C 200 GB throttle right where the "
      "single-shot `mobi05` got it wrong (1 GB); hs12 contradicts itself within one chat; "
      "hs25 refuses a derived estimate that hs26 happily does. Answers vary with phrasing.\n")

    A("### Confirmatory drill probes\n")
    A("| Probe | Prompt | Maks | Reading |")
    A("|---|---|---|---|")
    for name, q, a, why in DRILL:
        A(f"| {name} | {q} | *{a}* | {why} |")
    A("")

    A("### What holds up\n")
    A("Concrete-input arithmetic (hs01, hs13, hs26), conditional-rule composition (hs06, "
      "hs22), two-limit reasoning (hs07, hs14), budget/downgrade tracking (hs20, hs21), "
      "roaming EU-vs-Balkan (hs09), promo timelines (hs27), and correcting *structural* "
      "false premises (hs10). When the first turn is concrete and in-domain, Maks reasons "
      "across turns well.\n")

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
