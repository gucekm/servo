# Telekom Slovenije "Maks" chatbot — answer-quality audit

**Full report** · prepared 2026-07-12 · independent automated evaluation
Scope: 300 customer-style questions across **prepaid (Mobi), postpaid (Naj),
fixed broadband, and IPTV (NEO)** — 75 each — asked to the live Maks assistant
and scored against facts published on telekom.si and its price lists (ceniki).

> Independent QA evaluation. Not affiliated with or endorsed by Telekom
> Slovenije. Product names are used only to identify the service under test.
> All figures reflect a single automated run captured 2026-07-12 and may change.

---

## 1. Executive summary

| Metric | Automatic rubric | My (LLM) judgement |
|---|---|---|
| Overall quality | **77.2 / 100** | **79.9 / 100** |
| Fact recall | 77.3 % | — |
| Non-answers (deflections) | 51 / 300 | 51 / 300 |
| Confident factual errors | ~10 flagged | **14 flagged** |

**By topic (quality, automatic / LLM):** prepaid 86.8 / 88.9 · IPTV 82.3 / 84.1 ·
postpaid 78.6 / 81.8 · **broadband 61.0 / 64.7** (weakest).

**Headline findings**

- **Strong on mobile and add-on facts** — prepaid/postpaid prices, data caps, EU
  allowances, activation, refills, device insurance, Ena številka, etc. are
  answered accurately and specifically.
- **Weak and error-prone on fixed broadband/TV** — ~29/75 broadband questions
  were deflected to a human agent or "check in Moj Telekom" instead of answered;
  Maks repeatedly cannot price the fixed NEO packages.
- **14 confident factual errors** where Maks stated a specific value that
  contradicts Telekom's own pages/ceniki — see §4. These are the highest-risk
  failures: a wrong number misleads, whereas a hand-off does not.

**Beyond single facts**, a separate **30-scenario multi-turn synthesis test**
(§5) scored **64/100** — Maks reasons well across turns when the opener is
concrete, but has systematic weak spots: an over-broad "no-math" guardrail that
refuses cost/saving calculations, sycophancy on false numbers, and deflection on
open-ended openers.

---

## 2. How to read this bundle

Start with **`maks_audit.html`** (visual summary), then **`report.md`** and
**`llm_judge.md`** for the findings. **`results.json`** / **`transcript.html`**
hold every question and answer; **`scorecard.md`** explains every score. The
`.py` files are the method and let anyone reproduce the run.

---

## 3. File manifest

For each file: **purpose** · **what it contains** · **why it's included**.

### Report & findings

**`REPORT.md`** (this file)
- *Purpose:* front page of the report.
- *Contains:* executive summary, methodology, this manifest, findings, caveats,
  reproduction steps.
- *Why:* single entry point that ties every other file together.

**`maks_audit.html`** — visual dashboard
- *Purpose:* at-a-glance summary for a non-technical reader.
- *Contains:* overall score gauge, per-topic bars, star distribution, the
  factual-error callout, best/worst examples. Self-contained, theme-aware,
  opens in any browser (no internet needed).
- *Why:* fastest way to grasp the result; suitable to share as-is.

**`report.md`** — aggregate written report
- *Purpose:* the narrative results of the automatic rubric.
- *Contains:* overall + per-topic tables, star distribution, and sampled
  best/worst answers.
- *Why:* the textual companion to the dashboard.

**`llm_judge.md`** — my own (LLM) judgement of all 300 answers
- *Purpose:* a human-style judgement that catches what string-matching cannot.
- *Contains:* my verdict + score per answer (OK / partial / deflection / wrong),
  a comparison against the automatic rubric, and the 14 flagged factual errors.
- *Why:* independent second opinion; the authoritative list of real errors.

**`scorecard.md`** — per-answer scoring rationale
- *Purpose:* full transparency on *how* each score was reached.
- *Contains:* for every question — the answer, the score, which reference facts
  were found/missing, relevance (incl. missing keywords), specificity, deflection,
  and the weighted arithmetic.
- *Why:* lets the recipient audit any individual score.

**`hard_synthesis.md`** — multi-turn synthesis stress test (30 scenarios)
- *Purpose:* test reasoning *across turns* (arithmetic, rules, tradeoffs,
  anaphora, false-premise handling), which the single-fact set doesn't cover.
- *Contains:* the 30 scenario transcripts, my per-scenario verdict, a root-cause
  error analysis, and 4 confirmatory drill probes.
- *Why:* the single-fact scores miss conversational failure modes; this is where
  most real customer questions live.

**`hard_synthesis.py`**, **`make_hard_synthesis.py`**, **`hard_synthesis_runs.json`**
- *Purpose:* run and render the synthesis test.
- *Contains:* the 30 scenario definitions + ground-truth targets, the live
  multi-turn runner, the transcripts, and the report generator (with my verdicts).
- *Why:* makes the multi-turn test reproducible and auditable.

### Evidence (raw data)

**`results.json`** — the transcript
- *Purpose:* the immutable record of the run.
- *Contains:* all 300 questions, Maks's verbatim answers, and every score
  component. Machine-readable.
- *Why:* the primary evidence; everything else is derived from it and it is
  re-scorable deterministically.

**`transcript.html`** — readable transcript
- *Purpose:* browse the conversation without reading JSON.
- *Contains:* every Q&A with score and a topic filter. Self-contained UTF-8 page.
- *Why:* human-friendly view of `results.json`.

### Method & reproducibility

**`questions.py`** / **`questions_extra.py`** — the question bank (100 + 200)
- *Purpose:* define what was asked and the ground truth to check against.
- *Contains:* each question paired with the accepted surface forms of its key
  facts (prices, data caps, speeds, programme counts).
- *Why:* the encoded reference set — the basis of every "correct/incorrect".

**`evaluate.py`** — evaluation harness + rubric
- *Purpose:* ask Maks and score the answers.
- *Contains:* the Boost API driver and the deterministic rubric
  (55 % fact-recall + 20 % relevance + 15 % specificity + 10 % non-deflection),
  plus a `--rescore` mode.
- *Why:* defines the scoring precisely and reproduces the numbers.

**`llm_judge_data.py`** — my raw verdicts
- *Purpose:* store my per-answer judgement as data.
- *Contains:* `{id → (score, label, note)}` for all 300, authored by hand.
- *Why:* makes my judgement explicit and auditable; source of `llm_judge.md`.

**`make_transcript.py`**, **`make_scorecard.py`**, **`make_llm_judge.py`**
- *Purpose:* regenerate the three derived documents from the data.
- *Contains:* small, dependency-light renderers.
- *Why:* the reports can be rebuilt from source; nothing is hand-edited.

**`SOURCES.md`** — provenance
- *Purpose:* say exactly where the ground truth came from.
- *Contains:* the product-page URLs and cenik PDF links (captured 2026-07-12),
  example grounding lines behind the flagged errors, and what was *not* verified.
- *Why:* makes the findings checkable against Telekom's own sources.

**`profiles/telekom_si.json`** + **`klepet/`** client package
- *Purpose:* the tool used to reach the bot.
- *Contains:* the Boost-API profile and a dependency-free client
  (`client.py`, `config.py`, `transport.py`, `template.py`, `__main__.py`,
  `demo.py`, `harimport.py`).
- *Why:* documents *how* the answers were obtained and lets the run be repeated.

---

## 4. Confirmed factual errors

Cases where Maks stated a specific value contradicting Telekom's own source
(full list and per-answer notes in `llm_judge.md`):

| id | Question (topic) | Maks said | Source says |
|---|---|---|---|
| `naj10` | priključna taksa (Naj) | 29,00 € | **10,95 €** |
| `naj32` | priključna taksa Ena številka | 10,95 € | **free** |
| `naj33` | SIM 2 monthly | 4,99 € | **11,99 €** |
| `naj46` | Naj B EU allowance | 13 GB | **41,71 GB** |
| `naj57` | Naj B/C throttle speed | 64 kbps | **2/1 Mbit/s** (64 kbps is Mobi C) |
| `mobi05` | Mobi C throttle point | 1 GB | **200 GB** |
| `mobi08`,`mobi41` | Mobi activation | 2,95 € (swap) | **2 €** activation |
| `tv07`,`tv32` | standalone NEO TV | "doesn't exist" | **exists, 41 €/mo** |
| `tv38` | NEO Smartbox issue fee | 3,90 € (rental) | **29 €** issue fee |
| `tv62` | extra IP phone number | 2 € | **1,27 €** |
| `bb26` | NEO A monthly | 20,99 € (Naj A) | **49 €** |

---

## 5. Multi-turn synthesis stress test

30 scenarios, each a **single conversation** whose turns force Maks to *combine*
facts rather than retrieve one — arithmetic, conditional rules, tradeoffs,
anaphora, false-premise correction. Graded by LLM judge (see `hard_synthesis.md`).

**Result: mean 64/100 — 14 PASS · 7 PARTIAL · 9 FAIL.** Built as A/B pairs (same
task, one variable changed) so each failure isolates a cause:

1. **Over-broad "no-math" guardrail** *(highest impact).* Bare calculations are
   refused (`"24 × 27,99"` → "ne morem pomagati pri matematičnih izračunih"),
   yet totals compute fine when the numbers are Maks's own product facts. Blocks
   legitimate cost/saving questions.
2. **Sycophancy on false numbers.** Corrects a false *structural* premise ("Mobi
   has binding") but accepts a false *number* ("Naj A has 50 GB" → 20 GB) and
   reasons on.
3. **Open-opener deflection.** Open "which package / total cost" openers derail
   into mobilni-vs-fiksni clarifying; the *same* task with "mobilni" stated up
   front succeeds. Main driver of the recommendation/broadband failures.
4. **Weak cross-turn state** (a value given earlier is re-requested),
   **rule-limit blindness** (adds a 2nd Druga številka to Naj B though only 1 is
   allowed), **fragile anaphora**, and **phrasing-dependent grounding** (gets the
   Mobi C throttle right here but wrong as a single-shot question).

**Holds up well:** in-domain arithmetic, conditional-rule composition, two-limit
reasoning, budget/downgrade tracking, roaming EU-vs-Balkan, promo timelines.

**Most actionable:** two narrow fixes — relaxing the math guardrail for
cost/saving questions and grounding numeric premises before agreeing — would
clear most of the failures.

---

## 6. Caveats

- **Reference-matching, not live re-verification.** An answer is "correct" iff it
  agrees with a fact extracted from Telekom's pages/ceniki on 2026-07-12.
- **Point-in-time.** Prices/offers change.
- **Automatic layer is reproducible; the LLM-judge layer is a single-pass human
  judgement** and is not deterministic.
- A few reference facts were ambiguous (SIM 2 variant, Da Vinci Kids, roaming
  prices) and were flagged rather than scored as errors.

---

## 7. Reproduce

```bash
cd tools/klepet && pip install -r requirements.txt      # requests, pymupdf optional
cd eval
python3 evaluate.py --rescore results.json              # recompute scores (no network)
python3 make_scorecard.py && python3 make_llm_judge.py  # rebuild the docs
python3 make_hard_synthesis.py                          # rebuild the synthesis report
# fresh live runs (re-ask Maks):  python3 evaluate.py  ·  python3 hard_synthesis.py
```
