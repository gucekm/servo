#!/usr/bin/env python3
"""Automatically rate the quality of telekom.si "Maks" bot answers.

For each of the 100 questions in ``questions.py`` (prepaid / postpaid /
broadband / IPTV), this asks Maks in a fresh conversation and scores the reply
against facts published on telekom.si using a transparent, reproducible rubric:

    quality = 55% fact-recall      (are the site's key facts in the answer?)
            + 20% relevance        (does it address the question's terms?)
            + 15% specificity      (concrete price / number / package named?)
            + 10% non-deflection   (did it answer vs ask us to rephrase?)

It writes ``results.json`` (per-question detail) and ``report.md`` (aggregate),
and prints a summary. No external LLM judge is used, so results are deterministic
given the same bot answers.

Usage:
    python3 evaluate.py            # ask Maks live, score, report
    python3 evaluate.py --limit 8  # quick smoke run on the first 8 questions
"""

from __future__ import annotations

import argparse
import json
import os
import re
import statistics
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))  # repo root -> import klepet package
sys.path.insert(0, str(HERE))

from klepet import KlepetClient, load_profile  # noqa: E402
from questions import QUESTIONS  # noqa: E402

PROFILE = HERE.parent / "profiles" / "telekom_si.json"

# Phrases that mark a non-answer: Maks punting, handing off to a human agent, or
# telling us to look elsewhere instead of stating the fact. Only counted as a
# deflection when the answer also fails to recall the fact (recall < 0.34).
DEFLECTION = [
    "prosim, napišite", "prosim napišite", "prosim, sporočite", "prosim sporočite",
    "mi lahko poveste", "mi povejte", "lahko natančneje", "natančnejš",
    "potrebujem še", "kateri paket vas zanima", "o katerem", "o kateri",
    "katero poslovalnico", "žal ne razpolagam", "žal nimam", "ne razpolagam s podatk",
    "nimam podatka", "podatka v priloženi bazi", "nimam informacij", "podatkov o statusu",
    "ne najdem", "ne morem pomagati", "se opravičujem, ne", "ali mi lahko",
    "prosim, pojasnite", "prosim pojasnite", "mi lahko zaupate", "lahko poveste, kateri",
    "želite izvedeti", "vas povežem s sodelavcem", "povežem z mojim sodelavcem",
    "vas lahko povežem s sodelavcem", "želite, da vas povežem", "bi želeli nadaljevati",
    "preverite spodaj", "preverite na naši spletni strani", "ali vas zanimajo",
    "prosim, potrdite", "ali se zanimate za", "usmerim na pravo mesto",
    "želite, da preverim", "želite, da vas usmerim",
    # clarify-first / "look it up elsewhere" redirects that still slip a keyword in
    "ali vas zanima", "mi najprej poveste", "mi poveste, ali", "najdete spodaj",
    "predlagam, da preverite", "predlagam vam, da", "priporočam, da preverite",
    "za točne informacije", "za točne cene", "za točen znesek", "za točno informacijo",
    "ni navedena v priloženih", "ni navedeno v priloženih", "ni podatka",
    "v priloženih informacijah", "odvisno od vaših potreb", "odvisno od izbranega",
    "preverite uradno", "preverite prodajno", "na voljo so različn", "različni akcijski",
    "ali imate predplačniško", "ali sprašujete", "odvisna od izbranega",
]

# Small Slovenian stopword set for the relevance metric.
STOP = set("""
in ali je so za na v z s k o pri po od do brez ali kaj kako koliko kje kdaj kdo
ki da ne se si ter tudi lahko vas vam vaš vaša vaše vam me mi ga jih li a e
paket paketa paketu paket? gb eur mesec mesečno cena stane vključuje vključena
""".split())


def normalize(text: str) -> str:
    t = text.lower().replace(" ", " ")
    t = t.replace("€", " eur ")
    t = re.sub(r"(?<=\d),(?=\d)", ".", t)   # 20,99 -> 20.99
    t = re.sub(r"\s+", " ", t)
    return t


def norm_variant(v: str) -> str:
    v = v.lower().replace("€", " eur ")
    v = re.sub(r"(?<=\d),(?=\d)", ".", v)
    v = re.sub(r"\s+", " ", v).strip()
    return v


def content_words(text: str) -> set:
    words = re.findall(r"[a-zČčŠšŽžĐđĆć0-9]{4,}", text.lower())
    return {w for w in words if w not in STOP}


# A concrete price / quantity / package token — the specificity signal.
SPECIFICITY_RE = re.compile(
    r"\d+[.,]?\d*\s*(?:eur|€|gb|tb|mbit|gbit|mb|kbit|dni|program|%)|naj|mobi|neo|supr")


def score_answer(answer: str, facts) -> dict:
    norm = normalize(answer)
    raw_low = answer.lower()

    # 1) fact recall
    hits = 0
    hit_detail = []
    for group in facts:
        got = any(norm_variant(v) in norm for v in group)
        hits += 1 if got else 0
        hit_detail.append({"group": group, "hit": got})
    recall = hits / len(facts) if facts else 0.0

    # 2) relevance: share of the question's content words echoed in the answer
    #    (filled in by caller which has the question); placeholder here.

    # 3) specificity: does it contain a concrete price / quantity / package token
    specificity = 1.0 if SPECIFICITY_RE.search(norm) else 0.0

    # 4) deflection
    deflected = any(p in raw_low for p in DEFLECTION) and recall < 0.34

    return {
        "recall": recall,
        "hits": hits,
        "groups": len(facts),
        "hit_detail": hit_detail,
        "specificity": specificity,
        "deflected": deflected,
        "answer_chars": len(answer),
    }


def ask_maks(client_profile, question: str, retries: int = 2) -> str:
    """Ask one question in a fresh conversation; return the concatenated reply."""
    last_exc = None
    for attempt in range(retries + 1):
        collected: list[str] = []
        client = KlepetClient(client_profile,
                              on_message=lambda who, txt: collected.append((who, txt)))
        try:
            client.start()          # greeting lands in `collected`
            greeting_len = len(collected)
            client.send(question)   # reply appended synchronously
            reply = "\n".join(t for _, t in collected[greeting_len:])
            client.stop()
            if reply.strip():
                return reply.strip()
        except Exception as exc:  # noqa: BLE001
            last_exc = exc
            client.stop()
        time.sleep(1.5 * (attempt + 1))
    return f"[ERROR: no reply{': ' + str(last_exc) if last_exc else ''}]"


def stars(q: float) -> int:
    # 0-100 quality -> 1..5 stars
    return max(1, min(5, int(q // 20) + 1))


def build_record(qid, cat, q, facts, answer) -> dict:
    """Score one (question, answer) pair into a result record."""
    s = score_answer(answer, facts)
    rel_q = content_words(q)
    rel_a = content_words(answer)
    relevance = (len(rel_q & rel_a) / len(rel_q)) if rel_q else 0.0
    quality = 100 * (0.55 * s["recall"] + 0.20 * relevance
                     + 0.15 * s["specificity"] + 0.10 * (0 if s["deflected"] else 1))
    return {
        "id": qid, "category": cat, "question": q, "answer": answer,
        "recall": round(s["recall"], 3), "relevance": round(relevance, 3),
        "specificity": s["specificity"], "deflected": s["deflected"],
        "hits": s["hits"], "groups": s["groups"],
        "quality": round(quality, 1), "stars": stars(quality),
        "answer_chars": s["answer_chars"],
    }


def rescore(path: str) -> int:
    """Recompute scores from a saved results.json (no network) — reproducible."""
    facts_by_id = {qid: facts for qid, _c, _q, facts in QUESTIONS}
    saved = json.loads(Path(path).read_text(encoding="utf-8"))
    results = [build_record(r["id"], r["category"], r["question"],
                            facts_by_id[r["id"]], r["answer"]) for r in saved]
    write_outputs(results)
    print_summary(results)
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="only run first N questions")
    ap.add_argument("--delay", type=float, default=15.0,
                    help="pause between questions (s); default is a polite human cadence")
    ap.add_argument("--rescore", metavar="RESULTS_JSON",
                    help="recompute scores from a saved results.json (no network)")
    args = ap.parse_args(argv)

    if args.rescore:
        return rescore(args.rescore)

    profile = load_profile(PROFILE)
    items = QUESTIONS[: args.limit] if args.limit else QUESTIONS

    results = []
    print(f"Asking Maks {len(items)} questions...\n")
    for i, (qid, cat, q, facts) in enumerate(items, 1):
        answer = ask_maks(profile, q)
        rec = build_record(qid, cat, q, facts, answer)
        results.append(rec)
        flag = "DEFLECT" if rec["deflected"] else f"{rec['hits']}/{rec['groups']}"
        print(f"[{i:3}/{len(items)}] {cat:9} {qid:7} q={rec['quality']:5.1f} "
              f"{'★'*rec['stars']:<5} {flag}")
        time.sleep(args.delay)

    write_outputs(results)
    print_summary(results)
    return 0


def _avg(xs):
    return round(statistics.mean(xs), 1) if xs else 0.0


def write_outputs(results) -> None:
    (HERE / "results.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")

    cats = ["prepaid", "postpaid", "broadband", "iptv"]
    lines = ["# Maks answer-quality evaluation\n",
             f"Questions: **{len(results)}** · Source of truth: telekom.si product pages (Jul 2026)\n",
             "Rubric: 55% fact-recall + 20% relevance + 15% specificity + 10% non-deflection.\n"]

    overall_q = _avg([r["quality"] for r in results])
    overall_r = _avg([100 * r["recall"] for r in results])
    defl = sum(1 for r in results if r["deflected"])
    lines.append(f"\n## Overall\n")
    lines.append(f"- **Quality score: {overall_q}/100** (avg {overall_q/20:.2f}★)")
    lines.append(f"- Fact recall: {overall_r}%")
    lines.append(f"- Deflections (non-answers): {defl}/{len(results)} "
                 f"({100*defl/len(results):.0f}%)")

    lines.append("\n## By category\n")
    lines.append("| Category | Quality /100 | Fact recall % | Deflections |")
    lines.append("|---|---|---|---|")
    for c in cats:
        rs = [r for r in results if r["category"] == c]
        if not rs:
            continue
        lines.append(f"| {c} | {_avg([r['quality'] for r in rs])} | "
                     f"{_avg([100*r['recall'] for r in rs])} | "
                     f"{sum(1 for r in rs if r['deflected'])}/{len(rs)} |")

    lines.append("\n## Star distribution\n")
    lines.append("| ★ | count |")
    lines.append("|---|---|")
    for st in range(5, 0, -1):
        lines.append(f"| {'★'*st} | {sum(1 for r in results if r['stars']==st)} |")

    def sample(rs, title):
        lines.append(f"\n## {title}\n")
        for r in rs:
            ans = r["answer"].replace("\n", " ")
            if len(ans) > 220:
                ans = ans[:220] + "…"
            lines.append(f"- **[{r['quality']}] {r['category']}/{r['id']}** — {r['question']}")
            lines.append(f"  - Maks: {ans}")

    # Potential misinformation: confident, specific, non-deflection answers that
    # still miss every published fact -> likely a wrong or fabricated answer.
    suspect = [r for r in results
               if r["specificity"] == 1.0 and not r["deflected"] and r["recall"] == 0.0]
    if suspect:
        sample(suspect, "Potential factual errors (answered confidently, fact-check failed)")

    ranked = sorted(results, key=lambda r: r["quality"])
    sample(ranked[-5:][::-1], "Best answers")
    sample(ranked[:8], "Worst answers")

    (HERE / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def print_summary(results) -> None:
    print("\n" + "=" * 60)
    print(f"OVERALL quality: {_avg([r['quality'] for r in results])}/100  "
          f"| fact recall {_avg([100*r['recall'] for r in results])}%  "
          f"| deflections {sum(1 for r in results if r['deflected'])}/{len(results)}")
    for c in ["prepaid", "postpaid", "broadband", "iptv"]:
        rs = [r for r in results if r["category"] == c]
        if rs:
            print(f"  {c:10} quality {_avg([r['quality'] for r in rs]):5}/100  "
                  f"recall {_avg([100*r['recall'] for r in rs]):5}%")
    print("Wrote results.json and report.md")


if __name__ == "__main__":
    raise SystemExit(main())
