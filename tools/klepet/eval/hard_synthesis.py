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
