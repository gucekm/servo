#!/usr/bin/env python3
"""Hard multi-turn synthesis probes for the Maks bot.

Unlike the 300 single-fact questions, each scenario here is ONE conversation
whose turns force Maks to carry context and *combine* facts — arithmetic,
conditional rules, tradeoffs, anaphora, false-premise correction. Exact-match
grading doesn't apply, so this harness only records the transcripts (with a
ground-truth `target` for each scenario); grading is done by an LLM judge
afterwards (see hard_synthesis.md).

    python3 hard_synthesis.py      # runs live -> hard_synthesis_runs.json
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from klepet import KlepetClient, load_profile  # noqa: E402

PROFILE = HERE.parent / "profiles" / "telekom_si.json"

# Each scenario: id, name, reasoning type, turns (each <=140 chars), and the
# ground-truth synthesis a correct assistant should produce (for judging).
SCENARIOS = [
    {"id": "hs01", "name": "Total cost promo→regular (Mobi C)", "type": "arithmetic",
     "turns": ["Koliko plačam za Mobi C v prvem letu?",
               "In v drugem letu, ko akcija poteče?",
               "Kolikšna je povprečna mesečna cena čez 24 mesecev?"],
     "target": "Mobi C promo 6,99 € (6 mo) then 13,99 €. Yr1 = 6×6,99+6×13,99 = 125,88 €; "
               "Yr2 = 12×13,99 = 167,88 €; 24-mo avg ≈ 293,76/24 = 12,24 €/mo."},

    {"id": "hs02", "name": "Bundle + Poveži in prihrani discount", "type": "composition",
     "turns": ["Imam Naj B in doma fiksni paket Net. Koliko skupaj plačam?",
               "Se pri tem upošteva popust Poveži in prihrani?",
               "Kolikšna je torej neto mesečna cena mobilnega dela?"],
     "target": "Naj B 27,99 € + Net 39 € = 66,99 €; Poveži in prihrani −5 € (needs fixed on "
               "same account) → mobile net 22,99 €; total 61,99 €."},

    {"id": "hs03", "name": "Shifting-constraint recommendation", "type": "context-update",
     "turns": ["Porabim 15 GB, ne potujem. Kaj priporočaš?",
               "Zdaj pa recimo, da mesečno potujem po EU. Se priporočilo spremeni?",
               "In če želim še neomejene podatke doma?"],
     "target": "Should update pick as constraints change: ~Naj A (20 GB) → weigh EU allowance "
               "→ unlimited pushes to Naj B (41,71 GB EU) or Mobi C. Must reflect the delta."},

    {"id": "hs04", "name": "Mobi C vs Naj B over a year", "type": "comparison-math",
     "turns": ["Primerjaj Mobi C in Naj B za nekoga, ki veliko potuje po EU.",
               "Kateri je cenejši čez eno leto, upoštevaj akcije?",
               "Kateri ima več GB v EU in za koliko?"],
     "target": "Mobi C ~125,88 €/yr (promo) vs Naj B 12×27,99=335,88 €/yr → Mobi C cheaper. "
               "EU data: Naj B 41,71 GB vs Mobi C 20,85 GB → Naj B +20,86 GB."},

    {"id": "hs05", "name": "Anaphora carryover", "type": "anaphora",
     "turns": ["Kateri naročniški paket ima največ GB v EU?",
               "Koliko stane ta paket?",
               "In koliko je cenejši z ugodnostjo Poveži in prihrani?"],
     "target": "Naj C (43,20 GB EU) → 28,99 € → with −5 € = 23,99 €. Must resolve 'ta paket'=Naj C."},

    {"id": "hs06", "name": "Rule composition / eligibility", "type": "rules",
     "turns": ["Sem nov naročnik. Kdaj velja akcijska cena Naj?",
               "Pred 30 dnevi sem imel Naj pri vas. Sem še upravičen?",
               "Ali lahko hkrati uveljavim Penzion in Poveži in prihrani?"],
     "target": "New subscriber = number not in a subscription in last 60 days → 30 days ago "
               "means NOT eligible. Penzion and Poveži in prihrani exclude each other (only the "
               "larger, Poveži 5 €, applies)."},

    {"id": "hs07", "name": "Two different data limits", "type": "constraints",
     "turns": ["Imam Mobi C. Kaj se zgodi, ko presežem 200 GB doma?",
               "In koliko od tega lahko porabim v EU?",
               "Če v EU porabim 25 GB, kaj se zgodi po 20,85 GB?"],
     "target": "SI: after 200 GB throttle to 64/64 kbit/s. EU cap = 20,85 GB, then charged per "
               "price list. Two distinct limits — must not conflate them."},

    {"id": "hs08", "name": "Device + package + insurance total", "type": "arithmetic",
     "turns": ["Kupim telefon za 700 € in vzamem Naj B. Kolikšna je mesečna cena?",
               "Dodam še zavarovanje za ta telefon (Premium). Koliko to doda?",
               "Skupni mesečni strošek?"],
     "target": "Naj B 27,99 €/mo + Premium insurance tier 601–800 € = 9,95 €/mo → 37,94 €/mo "
               "(phone paid/subsidised separately)."},

    {"id": "hs09", "name": "Roaming scenario (EU vs Balkan)", "type": "rules",
     "turns": ["Z Naj B grem za teden na Hrvaško. Je poraba vključena?",
               "Nato nadaljujem v Srbijo. Kaj takrat?",
               "Kateri zakup potrebujem in koliko stane?"],
     "target": "Croatia = EU-tariff (included, 41,71 GB). Serbia = Balkan (NOT EU) → needs a "
               "Balkan bundle. Must distinguish EU from Balkan."},

    {"id": "hs10", "name": "False-premise correction", "type": "robustness",
     "turns": ["Mobi ima 24-mesečno vezavo, kajne?",
               "Torej pri Mobi plačujem mesečno naročnino?",
               "Kateri je cenejši za neomejene podatke — Mobi ali Naj?"],
     "target": "Must CORRECT the premise: Mobi has no binding and no monthly subscription "
               "(prepaid). Then compare unlimited-data options honestly."},

    # ---- expansion: retest failure modes + new reasoning types (hs11–hs30) ----
    {"id": "hs11", "name": "Family: Naj B + Druga številka limit", "type": "rules+math",
     "turns": ["Vzamem Naj B in dodam eno Druga številka. Koliko približno na mesec?",
               "In če dodam še eno Druga številka?",
               "Kolikšen je skupni mesečni strošek?"],
     "target": "Naj B allows only 1 Druga številka — a 2nd is NOT possible on Naj B (Naj C/5G "
               "allow 4). Should refuse the 2nd, not just add cost."},

    {"id": "hs12", "name": "Mid-month proration", "type": "arithmetic",
     "turns": ["Sklenem Naj A sredi meseca, 15. dne. Koliko plačam prvi mesec?",
               "In naslednji mesec polno?",
               "Kako se obračuna prvi delni mesec?"],
     "target": "First month is prorated (sorazmerni del by active days); next month full 20,99 €."},

    {"id": "hs13", "name": "Insurance arithmetic, values inline", "type": "arithmetic",
     "turns": ["Zavarujem telefon vreden 500 € (Premium). Kolikšna premija?",
               "In če telefon stane 900 €?",
               "Za oba telefona skupaj na mesec?"],
     "target": "500 €→7,45 €; 900 €→10,95 €; sum 18,40 €/mo. Retest of hs08 with values given inline."},

    {"id": "hs14", "name": "Delim GB budget", "type": "constraints",
     "turns": ["Imam Naj C. Po koliko GB lahko največ delim naenkrat?",
               "Če trikrat delim po 50 GB, koliko GB skupaj razdelim?",
               "Ali deljenje vpliva na mojo EU-tarifo?"],
     "target": "Max 50 GB per share; 3×50 = 150 GB; sharing draws from the SI allowance, "
               "separate from the EU-tariff cap."},

    {"id": "hs15", "name": "24-mo total + promo saving", "type": "arithmetic",
     "turns": ["Naj B z 24-mesečno vezavo — kolikšna je skupna naročnina po redni ceni?",
               "In s promocijsko ceno 15,99 € vseh 24 mesecev?",
               "Koliko prihranim s promocijo?"],
     "target": "Regular 24×27,99 = 671,76 €; promo 24×15,99 = 383,76 €; saving 288,00 €."},

    {"id": "hs16", "name": "Anaphora: cheapest unlimited", "type": "anaphora",
     "turns": ["Kateri paket ima neomejene podatke najceneje?",
               "Koliko GB v EU ima ta paket?",
               "Ima ta paket vezavo?"],
     "target": "Cheapest unlimited = Mobi C (13,99 €, promo 6,99 €). ‘Ta paket’ → Mobi C: "
               "20,85 GB EU, no binding. Retest of hs05 anaphora."},

    {"id": "hs17", "name": "Anaphora: the pricier one", "type": "anaphora",
     "turns": ["Primerjaj paketa Naj A in Naj C.",
               "Kateri je dražji?",
               "Za koliko evrov na mesec je dražji?"],
     "target": "Naj C (28,99 €) dearer than Naj A (20,99 €) by 8,00 €/mo. Must resolve ‘dražji’."},

    {"id": "hs18", "name": "Anaphora: it (Ena številka)", "type": "anaphora",
     "turns": ["Kaj je storitev Ena številka?",
               "Koliko stane?",
               "Ali jo lahko uporabljam brez VoLTE?"],
     "target": "Ena številka 1 €/mo; requires VoLTE (so ‘no’). Pronoun ‘jo’ must stay bound."},

    {"id": "hs19", "name": "Shift-constraint, mobilni stated", "type": "context-update",
     "turns": ["Priporoči mobilni paket za 25 GB brez potovanj.",
               "Zdaj potujem po EU 10 GB mesečno. Se spremeni?",
               "In želim neomejene podatke doma."],
     "target": "Should recommend and then REVISE as constraints change. Retest of hs03 but "
               "with ‘mobilni’ stated up front (does that avoid the opener deflection?)."},

    {"id": "hs20", "name": "Budget-bounded pick", "type": "optimization",
     "turns": ["Kateri mobilni naročniški paket je najboljši do 20 € na mesec?",
               "In če proračun dvignem na 30 €?",
               "Kateri ima največ EU-podatkov znotraj tega proračuna?"],
     "target": "≤20 € → Naj A (20,99 is just over; promo 15,99 fits). ≤30 € → Naj B/C. Most EU "
               "data within 30 € = Naj C (43,20 GB)."},

    {"id": "hs21", "name": "Downgrade tradeoff", "type": "context-update",
     "turns": ["Imam Naj C, a premalo uporabljam. Naj preklopim na Naj A?",
               "Koliko prihranim mesečno?",
               "Kaj pomembnega izgubim?"],
     "target": "Save 28,99−20,99 = 8 €/mo; lose unlimited data (Naj A caps at 20 GB) and the "
               "larger 43,20 GB EU allowance."},

    {"id": "hs22", "name": "Discount stacking (pensioner)", "type": "rules",
     "turns": ["Sem upokojenec z Naj B in fiksnim Net. Kateri popusti veljajo?",
               "Se Penzion in Poveži in prihrani seštevata?",
               "Kolikšna je končna cena mobilnega dela?"],
     "target": "Penzion and Poveži do NOT stack — only the larger applies (Poveži −5 €). "
               "Naj B net 22,99 €."},

    {"id": "hs23", "name": "MNP eligibility chain", "type": "rules",
     "turns": ["Prenesem številko od drugega operaterja (MNP). Sem nov naročnik?",
               "Velja zame akcijska cena Naj?",
               "Ali potrebujem 24-mesečno vezavo za to ceno?"],
     "target": "MNP port-in = new subscriber (number not at TS in last 60 days) → eligible; "
               "promo needs 24-month binding."},

    {"id": "hs24", "name": "Migration fee logic", "type": "rules",
     "turns": ["Koliko stane sprememba iz Naj A v Naj C?",
               "Je brezplačno, če nisem vezan?",
               "Kje to uredim?"],
     "target": "Package change 10,95 € charged only to bonded relationships; change via Moj "
               "Telekom / 041 700 700 / a store."},

    {"id": "hs25", "name": "Data→usage conversion", "type": "derived",
     "turns": ["Koliko ur videa v HD lahko približno gledam z 20 GB?",
               "In z neomejenim paketom Naj B?",
               "Se gledanje šteje v EU-zakup?"],
     "target": "~0,7–1 GB/h HD → ~20–28 h from 20 GB (honest estimate ok; hallucinated "
               "precision not). Naj B unlimited domestically; EU counts against 41,71 GB."},

    {"id": "hs26", "name": "Speed→download time", "type": "derived",
     "turns": ["Pri optiki 1 Gbit/s, kako hitro prenesem 10 GB datoteko?",
               "In pri 100 Mbit/s?",
               "Kateri paket NEO ima 1 Gbit/s?"],
     "target": "10 GB=80 Gb → ~80 s at 1 Gbit/s; ~800 s (~13 min) at 100 Mbit/s. All NEO A/B/C "
               "reach 1 Gbit/s down on FTTH."},

    {"id": "hs27", "name": "Promo timeline", "type": "temporal",
     "turns": ["Kdaj se konča akcija za pakete Mobi?",
               "Če vključim danes, do kdaj imam akcijsko ceno?",
               "Kaj se zgodi po tem obdobju?"],
     "target": "Mobi promo runs to 31. 8. 2026; on activation the price holds 6 months, then "
               "reverts to the regular price."},

    {"id": "hs28", "name": "Contract-end reasoning", "type": "temporal",
     "turns": ["Sklenem 24-mesečno vezavo danes. Kdaj se konča?",
               "Kaj se zgodi s ceno po izteku vezave?",
               "Ali lahko prekinem prej in kaj to stane?"],
     "target": "Ends 24 months from today; after that the regular price applies; early "
               "termination triggers the remaining contractual obligation."},

    {"id": "hs29", "name": "Contradictory constraints", "type": "robustness",
     "turns": ["Želim neomejene podatke, brez vezave, najceneje in največ EU-podatkov. Kateri paket?",
               "Ali obstaja en paket, ki izpolni vse hkrati?",
               "Kaj priporočaš kot najboljši kompromis?"],
     "target": "No single package maximises all: no-binding → Mobi C (20,85 GB EU); most EU "
               "data → Naj C (43,20 GB, but 24-mo binding). Must articulate the tradeoff, not "
               "pretend one wins."},

    {"id": "hs30", "name": "False premise + arithmetic", "type": "robustness",
     "turns": ["Naj A ima 50 GB podatkov, kajne?",
               "Koliko je to na dan v enem mesecu?",
               "Zadošča za dnevno uporabo zemljevidov in glasbe?"],
     "target": "Correct the premise: Naj A is 20 GB, not 50. Then 20 GB/30 ≈ 0,67 GB/day; "
               "reason about adequacy from the corrected figure."},
]


def run_scenario(profile, sc, delay=0.4):
    msgs = []
    client = KlepetClient(profile, on_message=lambda who, t: msgs.append(t))
    client.start()
    base = len(msgs)
    turns = []
    for q in sc["turns"]:
        assert len(q) <= 140, f"{sc['id']} turn too long ({len(q)}): {q}"
        try:
            client.send(q)
            a = "\n".join(msgs[base:]).strip()
        except Exception as exc:  # noqa: BLE001
            a = f"[ERROR: {exc}]"
        base = len(msgs)
        turns.append({"q": q, "a": a})
        time.sleep(delay)
    client.stop()
    return {"id": sc["id"], "name": sc["name"], "type": sc["type"],
            "target": sc["target"], "turns": turns}


def main() -> int:
    profile = load_profile(PROFILE)
    runs = []
    for i, sc in enumerate(SCENARIOS, 1):
        print(f"[{i}/{len(SCENARIOS)}] {sc['id']} {sc['name']} …")
        r = run_scenario(profile, sc)
        runs.append(r)
        for t in r["turns"]:
            print(f"    > {t['q']}")
            print(f"      {t['a'][:160].replace(chr(10),' ')}")
    (HERE / "hard_synthesis_runs.json").write_text(
        json.dumps(runs, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\nWrote hard_synthesis_runs.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
