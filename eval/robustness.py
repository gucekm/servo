#!/usr/bin/env python3
"""Paraphrase-robustness test: does the SAME fact survive different phrasings?

The main audit asked each fact once, in careful formal Slovenian. Real
customers don't type like that. This suite takes 20 facts Maks answered
perfectly in the main run (5 per topic) and asks each one in six phrasings:

    formal        the audit's original wording (control)
    colloquial    everyday spoken Slovenian
    nodiacritics  lowercase, no č/š/ž — how people actually type in chat
    typo          misspellings ("kolko", "pakte", ...)
    terse         keyword fragment ("cena Naj B?")
    english       the same question in English

Each variant runs in a fresh conversation and is scored with the audit's fact
groups: HIT (all facts recalled) / MISS / DEFLECT. A robust bot scores the
same fact regardless of wording; every formal-hits-but-informal-misses case
is quality that real users don't receive.

Usage:
    python3 robustness.py                     # live run (120 conversations)
    python3 robustness.py --limit 4           # smoke run, first 4 facts
    python3 robustness.py --report robustness_runs.json   # re-render md only
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

from evaluate import score_answer  # noqa: E402  (same fact matching as the audit)
from live import ask_fresh  # noqa: E402

VARIANTS = ["formal", "colloquial", "nodiacritics", "typo", "terse", "english"]

# (probe id, source question id, fact groups, {variant: phrasing})
# Fact groups use the audit's matching rules (lowercase, €->eur, 20,99->20.99).
PROBES = [
    ("rb01", "mobi02", [["9,99"]], {
        "formal": "Kakšna je redna cena paketa Mobi B?",
        "colloquial": "Koliko pa pride Mobi B?",
        "nodiacritics": "kaksna je redna cena paketa mobi b",
        "typo": "Kolko stane paket Mobi B?",
        "terse": "cena Mobi B?",
        "english": "What is the regular price of the Mobi B prepaid plan?"}),
    ("rb02", "mobi04", [["13,99"]], {
        "formal": "Kakšna je redna cena paketa Mobi C?",
        "colloquial": "Koliko me mesečno stane Mobi C?",
        "nodiacritics": "kaksna je mesecna cena paketa mobi c",
        "typo": "Kolko stane pakte Mobi C?",
        "terse": "Mobi C cena?",
        "english": "How much does the Mobi C plan cost per month?"}),
    ("rb03", "mobi10", [["0,12"]], {
        "formal": "Koliko stanejo klici in SMS po rednem ceniku Mobi brez paketa?",
        "colloquial": "Če nimam nobenega Mobi paketa, koliko plačam za minuto klica?",
        "nodiacritics": "cena klicev in sporocil pri mobi brez paketa",
        "typo": "Kolik stanejo klici pri Mobi brez pakteov?",
        "terse": "Mobi klic cena brez paketa?",
        "english": "How much do calls and SMS cost on Mobi without a bundle?"}),
    ("rb04", "mobi12", [["29,99"]], {
        "formal": "Koliko stane zakup Mobi Net?",
        "colloquial": "Koliko dam za Mobi Net?",
        "nodiacritics": "koliko stane zakup mobi net in koliko casa velja",
        "typo": "Kolko stane Mobi Nett?",
        "terse": "Mobi Net cena?",
        "english": "How much does the Mobi Net data bundle cost?"}),
    ("rb05", "mobi16", [["90 dni", "90 dneh", "90-dnev", "90 days"]], {
        "formal": "Na koliko dni se samodejno podaljša veljavnost računa Mobi?",
        "colloquial": "Za koliko časa se mi Mobi račun sam podaljša?",
        "nodiacritics": "na koliko dni se samodejno podaljsa veljavnost racuna mobi",
        "typo": "Na kolko dni se podaljša veljavnst Mobi računa?",
        "terse": "Mobi veljavnost računa?",
        "english": "By how many days is a Mobi account's validity automatically extended?"}),
    ("rb06", "naj01", [["20,99"]], {
        "formal": "Kakšna je redna mesečna cena paketa Naj A?",
        "colloquial": "Koliko pride Naj A na mesec?",
        "nodiacritics": "kaksna je redna mesecna cena paketa naj a",
        "typo": "Kolko stane pakt Naj A mesečno?",
        "terse": "cena Naj A?",
        "english": "What is the regular monthly price of the Naj A plan?"}),
    ("rb07", "naj03", [["27,99"]], {
        "formal": "Kakšna je redna mesečna cena paketa Naj B?",
        "colloquial": "Koliko pa me udari Naj B po žepu na mesec?",
        "nodiacritics": "kaksna je redna mesecna cena paketa naj b",
        "typo": "Koliko stane paket Naj B na msec?",
        "terse": "Naj B cena?",
        "english": "How much is the Naj B plan per month?"}),
    ("rb08", "naj04", [["200 gb"]], {
        "formal": "Po koliko GB se v paketu Naj B zniža hitrost prenosa podatkov?",
        "colloquial": "Kdaj mi pri Naj B upočasnijo internet?",
        "nodiacritics": "po koliko gb se v paketu naj b zniza hitrost prenosa",
        "typo": "Po kolko GB se pri Naj B zmanjša hitorst?",
        "terse": "Naj B omejitev GB?",
        "english": "After how many GB does Naj B slow down the data speed?"}),
    ("rb09", "naj13", [["5 eur"]], {
        "formal": "Kolikšen je popust pri ugodnosti Poveži in prihrani?",
        "colloquial": "Koliko prišparam s Poveži in prihrani?",
        "nodiacritics": "koliksen je popust pri ugodnosti povezi in prihrani",
        "typo": "Koliko znaša popust Povezi in prihani?",
        "terse": "Poveži in prihrani popust?",
        "english": "How big is the Poveži in prihrani discount?"}),
    ("rb10", "naj14", [["1 eur"]], {
        "formal": "Koliko stane storitev Ena številka?",
        "colloquial": "Koliko me stane, da imam eno številko na dveh SIM karticah?",
        "nodiacritics": "koliko stane storitev ena stevilka",
        "typo": "Kolko stane storitv Ena števlika?",
        "terse": "Ena številka cena?",
        "english": "How much does the Ena številka service cost per month?"}),
    ("rb11", "bb05", [["13,99"]], {
        "formal": "Koliko stane fiksni paket Naj Net na mesec?",
        "colloquial": "Koliko pride Naj Net mesečno?",
        "nodiacritics": "koliko stane paket naj net mesecno",
        "typo": "Kolko stane pakt Naj Net?",
        "terse": "Naj Net cena?",
        "english": "What is the monthly price of the Naj Net fixed internet plan?"}),
    ("rb12", "bb22", [["58 eur", "58,00", "58 €"]], {
        "formal": "Kakšna je redna cena paketa NEO B?",
        "colloquial": "Koliko pa je NEO B na mesec brez akcije?",
        "nodiacritics": "kaksna je redna cena paketa neo b",
        "typo": "Koliko stane pakket NEO B?",
        "terse": "NEO B cena?",
        "english": "What is the regular monthly price of the NEO B package?"}),
    ("rb13", "bb23", [["63 eur", "63,00", "63 €"]], {
        "formal": "Kakšna je redna cena paketa NEO C?",
        "colloquial": "Koliko odštejem za NEO C vsak mesec?",
        "nodiacritics": "kaksna je redna mesecna cena paketa neo c",
        "typo": "Kolko stane NEO C mesečnoo?",
        "terse": "NEO C cena?",
        "english": "How much does the NEO C package cost per month at the regular price?"}),
    ("rb14", "bb17", [["150 mbit", "150"]], {
        "formal": "Do katere hitrosti lahko nadgradim paket Naj Net?",
        "colloquial": "Do kakšne hitrosti lahko pridem z Naj Net, če doplačam?",
        "nodiacritics": "do kaksne hitrosti gre paket naj net z nadgradnjo",
        "typo": "Do ktere hitrosti lahko nadgradim Naj Net?",
        "terse": "Naj Net max hitrost?",
        "english": "Up to what speed can the Naj Net plan be upgraded?"}),
    ("rb15", "bb02", [["5 gbit", "5 gb/s"]], {
        "formal": "Do katere hitrosti lahko nadgradim optični internet NEO?",
        "colloquial": "Kako hiter je lahko največ optični internet pri vas?",
        "nodiacritics": "do katere hitrosti lahko nadgradim opticni internet neo",
        "typo": "Do katre hitrosti gre optika NEO?",
        "terse": "NEO optika max hitrost?",
        "english": "What is the maximum speed I can upgrade NEO fiber internet to?"}),
    ("rb16", "tv01", [["150"]], {
        "formal": "Koliko TV programov vključuje paket NEO A?",
        "colloquial": "Koliko programov sploh dobim v NEO A?",
        "nodiacritics": "koliko tv programov vkljucuje paket neo a",
        "typo": "Kolko TV progrmov ima NEO A?",
        "terse": "NEO A št. programov?",
        "english": "How many TV channels are included in the NEO A package?"}),
    ("rb17", "tv03", [["255"]], {
        "formal": "Koliko TV programov vključuje paket NEO C?",
        "colloquial": "Koliko kanalov ima NEO C?",
        "nodiacritics": "koliko tv programov vkljucuje paket neo c",
        "typo": "Koliko programv ima paket NEO C?",
        "terse": "NEO C programi?",
        "english": "How many TV channels does NEO C include?"}),
    ("rb18", "tv10", [["3,90"]], {
        "formal": "Koliko stane najem vsakega dodatnega TV-komunikatorja?",
        "colloquial": "Koliko doplačam za še en TV box?",
        "nodiacritics": "koliko stane najem dodatnega tv komunikatorja",
        "typo": "Kolko stane dodatni TV-komunikatr?",
        "terse": "dodatni komunikator cena?",
        "english": "How much does renting each additional TV set-top box cost?"}),
    ("rb19", "tv13", [["1,90"]], {
        "formal": "Koliko stane NEO TV Lite na napravo mesečno?",
        "colloquial": "Koliko me pride NEO TV Lite na en televizor?",
        "nodiacritics": "koliko stane neo tv lite na napravo mesecno",
        "typo": "Koliko stne NEO TV Litte?",
        "terse": "NEO TV Lite cena?",
        "english": "How much is NEO TV Lite per device per month?"}),
    ("rb20", "tv08", [["7 dni", "7-dnev", "7 days", "sedem dni"]], {
        "formal": "Koliko dni nazaj lahko gledam vsebine z ogledom nazaj pri NEO?",
        "colloquial": "Za koliko dni nazaj lahko zavrtim oddaje na NEO?",
        "nodiacritics": "koliko dni nazaj lahko gledam vsebine pri neo",
        "typo": "Kolko dni nazja lahko gledam oddaje pri NEO?",
        "terse": "NEO ogled nazaj dni?",
        "english": "How many days back can I watch content with NEO's catch-up TV?"}),
]


def grade(answer: str, facts) -> str:
    if answer.startswith("[ERROR:"):
        return "ERROR"
    s = score_answer(answer, facts)
    if s["deflected"] and s["recall"] < 1.0:
        return "DEFLECT"
    return "HIT" if s["recall"] == 1.0 else "MISS"


def run_live(limit: int, delay: float) -> dict:
    probes = PROBES[:limit] if limit else PROBES
    out = {"captured": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()), "probes": []}
    # Checkpoint file so an interrupted run resumes instead of restarting.
    prog_path = HERE / "robustness_progress.jsonl"
    done: dict = {}
    if prog_path.exists():
        for line in prog_path.read_text(encoding="utf-8").splitlines():
            rec = json.loads(line)
            done[(rec["pid"], rec["variant"])] = rec["rec"]
        print(f"Resuming: {len(done)} conversations already done.")
    total = len(probes) * len(VARIANTS)
    n = 0
    with prog_path.open("a", encoding="utf-8") as prog:
        for pid, qid, facts, variants in probes:
            entry = {"id": pid, "source_qid": qid, "facts": facts, "variants": {}}
            for var in VARIANTS:
                n += 1
                if (pid, var) in done:
                    entry["variants"][var] = done[(pid, var)]
                    continue
                q = variants[var]
                reply = ask_fresh(q)
                v = grade(reply["text"], facts)
                rec = {"question": q, "answer": reply["text"], "grade": v}
                entry["variants"][var] = rec
                prog.write(json.dumps({"pid": pid, "variant": var, "rec": rec},
                                      ensure_ascii=False) + "\n")
                prog.flush()
                print(f"[{n:3}/{total}] {pid} {var:12} -> {v}", flush=True)
                time.sleep(delay)
            out["probes"].append(entry)
    if not limit:
        prog_path.unlink()  # complete — the checkpoint is no longer needed
    return out


def render(data: dict) -> str:
    probes = data["probes"]
    mark = {"HIT": "✓", "MISS": "✗", "DEFLECT": "D", "ERROR": "!"}
    lines = [
        "# Maks paraphrase-robustness test",
        "",
        f"**{len(probes)} facts** Maks answered perfectly in the main audit, each re-asked "
        f"in **{len(VARIANTS)} phrasings** ({len(probes) * len(VARIANTS)} fresh conversations), "
        f"captured {data['captured']}. ✓ = all reference facts recalled · ✗ = fact missing/"
        "wrong · D = deflected.",
        "",
        "| fact | " + " | ".join(VARIANTS) + " | robust |",
        "|---|" + "---|" * (len(VARIANTS) + 1),
    ]
    per_variant = {v: 0 for v in VARIANTS}
    fully_robust = 0
    fragile = []
    for p in probes:
        cells = []
        hits = 0
        for v in VARIANTS:
            g = p["variants"][v]["grade"]
            cells.append(mark.get(g, "?"))
            if g == "HIT":
                per_variant[v] += 1
                hits += 1
        robust = hits == len(VARIANTS)
        fully_robust += robust
        if not robust:
            fragile.append(p)
        lines.append(f"| `{p['id']}` ({p['source_qid']}) | " + " | ".join(cells)
                     + f" | {'yes' if robust else 'NO'} |")
    lines += [
        "",
        "## Hit rate by phrasing style",
        "",
        "| phrasing | facts recalled |",
        "|---|---|",
    ]
    for v in VARIANTS:
        lines.append(f"| {v} | {per_variant[v]}/{len(probes)} |")
    lines += [
        "",
        f"**{fully_robust}/{len(probes)} facts survived every phrasing.** "
        "Facts below flipped on at least one variant — the gap between the audit score "
        "and what a real (informal) user receives.",
        "",
    ]
    for p in fragile:
        lines.append(f"### `{p['id']}` (source `{p['source_qid']}`) — facts: {p['facts']}")
        for v in VARIANTS:
            rec = p["variants"][v]
            if rec["grade"] != "HIT":
                ans = rec["answer"].replace("\n", " ")
                if len(ans) > 200:
                    ans = ans[:200] + "…"
                lines.append(f"- **{v} → {rec['grade']}** — “{rec['question']}”")
                lines.append(f"  - Maks: {ans}")
        lines.append("")
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="only run first N facts")
    ap.add_argument("--delay", type=float, default=0.4)
    ap.add_argument("--report", metavar="RUNS_JSON",
                    help="skip the live run; re-render robustness.md from saved runs")
    args = ap.parse_args(argv)

    if args.report:
        data = json.loads(Path(args.report).read_text(encoding="utf-8"))
    else:
        data = run_live(args.limit, args.delay)
        (HERE / "robustness_runs.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    (HERE / "robustness.md").write_text(render(data), encoding="utf-8")
    print("Wrote robustness_runs.json and robustness.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
