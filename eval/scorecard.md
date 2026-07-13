# Maks answer-quality scorecard

Every question asked to the Telekom Slovenije **Maks** chat assistant, its
verbatim answer, the automatic score, and — for each pair — an explanation of
how that score was reached.

## How each answer is scored

The **quality score (0–100)** is a weighted sum of four signals:

| Signal | Weight | What it measures |
|---|---|---|
| **Fact recall** | 55% | Of the key facts published on telekom.si for this question, how many appear in the answer. Each fact is a group of accepted surface forms; the group counts as recalled if **any** form appears after normalisation (lower-cased, `€`→`eur`, decimal comma→dot, whitespace collapsed). |
| **Relevance** | 20% | Share of the question's content words (length ≥ 4, minus stop-words) that also appear in the answer — i.e. did it stay on topic. |
| **Specificity** | 15% | 1 if the answer contains a concrete price / quantity / package name (`€`, `GB`, `Mbit`, `Naj`, `Mobi`, `NEO`, …), else 0. Rewards committing to a real value over vague talk. |
| **Non-deflection** | 10% | 0 if the answer is a *deflection* — a clarify-first reply or human-agent hand-off that never states the fact (a known redirect phrase is present **and** fact recall < 0.34) — else 1. |

`quality = 100 × (0.55·recall + 0.20·relevance + 0.15·specificity + 0.10·non-deflection)`,
then mapped to 1–5 ★ in 20-point bands. This is a deterministic, reproducible
rubric — **no LLM judge** — so the same answer always yields the same score.
It rewards stating the site's facts and penalises vague or deflecting replies;
it cannot judge nuances a human would (e.g. a correct answer worded so
differently that none of the accepted fact forms appear will still score low).

Source of truth: telekom.si product pages and price lists (ceniki), July 2026.

---

## Summary

- Questions scored: **300**
- Mean quality: **77.2/100**

| Topic | Questions | Mean quality |
|---|---|---|
| Prepaid (Mobi) | 75 | 86.8 |
| Postpaid (Naj) | 75 | 78.6 |
| Broadband | 75 | 61.0 |
| IPTV (NEO TV) | 75 | 82.3 |

---


## Prepaid (Mobi)

### `mobi01` · Prepaid (Mobi)

**Q:** Koliko stane paket Mobi A in koliko enot ter podatkov vključuje?

**Maks:**

> ✨ Paket Mobi A trenutno stane 3,73 EUR/mesec za prvih 6 mesecev (akcijska cena ob vklopu v aplikaciji Moj Mobi med 1. 7. in 31. 8. 2026). Vključuje:
> 
> 
> 
> 1000 enot (klici, SMS/MMS v Sloveniji ali državah EU-tarife)
> 1 GB podatkov v Sloveniji (do 1 GB v EU-tarifi)
> Hitrost do 300/100 Mbit/s
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 81.7/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 2/3 = 67%** (weight 55%). Expected facts:
    - ❌ missing: `4,99`
    - ✅ found: `1000` / `1.000`
    - ✅ found: `1 gb`
- **Relevance — 3/3 = 100%** (weight 20%). Echoed: `enot`, `mobi`, `podatkov`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×0.67 + 0.20×1.00 + 0.15×1 + 0.10×1` = **0.817 → 81.7/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi02` · Prepaid (Mobi)

**Q:** Kakšna je redna cena paketa Mobi B?

**Maks:**

> ✨ Redna cena paketa Mobi B je 9,99 EUR na mesec. V času poletne akcije (1. 7.–31. 8. 2026) pa je prvih 6 mesecev cena 6,99 EUR/mesec ob vklopu v aplikaciji Moj Mobi. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `9,99`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `mobi`, `redna`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi03` · Prepaid (Mobi)

**Q:** Koliko GB prenosa v Sloveniji vključuje paket Mobi B?

**Maks:**

> ✨ Paket Mobi B vključuje 100 GB prenosa podatkov v Sloveniji. Če vas zanima še količina za EU ali druge podrobnosti, z veseljem pojasnim. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `100 gb`
- **Relevance — 3/3 = 100%** (weight 20%). Echoed: `mobi`, `prenosa`, `sloveniji`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi04` · Prepaid (Mobi)

**Q:** Kakšna je redna cena paketa Mobi C?

**Maks:**

> ✨ Redna cena paketa Mobi C je 13,99 EUR na mesec. V času poletne akcije (od 1. 7. do 31. 8. 2026) pa je prvih 6 mesecev cena 6,99 EUR/mesec. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `13,99`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `mobi`, `redna`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi05` · Prepaid (Mobi)

**Q:** Po koliko GB se v paketu Mobi C zniža hitrost prenosa?

**Maks:**

> ✨ V paketu Mobi C se hitrost prenosa podatkov zniža po porabi 1 GB prenosa podatkov. Če potrebujete več informacij, mi sporočite! 😊

**Score: 45.0/100  (★★★☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `200 gb`
- **Relevance — 4/4 = 100%** (weight 20%). Echoed: `hitrost`, `mobi`, `prenosa`, `zniža`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×0.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **0.450 → 45.0/100**.
- **Verdict:** Risky: Maks answered confidently with a specific value that does **not** match the site — a candidate factual error.

---

### `mobi06` · Prepaid (Mobi)

**Q:** Kakšna je akcijska cena paketa Mobi A za 6 mesecev?

**Maks:**

> ✨ Akcijska cena paketa Mobi A je 3,73 EUR na mesec za prvih 6 mesecev, če paket vključite v aplikaciji Moj Mobi med 1. 7. in 31. 8. 2026. Po tem obdobju se paket podaljšuje po redni ceni.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 95.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `3,73`
- **Relevance — 3/4 = 75%** (weight 20%). Echoed: `akcijska`, `mesecev`, `mobi`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.75 + 0.15×1 + 0.10×1` = **0.950 → 95.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi07` · Prepaid (Mobi)

**Q:** Kakšna je akcijska cena paketov Mobi B in Mobi C?

**Maks:**

> ✨ Akcijska cena paketa Mobi B je 6,99 EUR/mesec, prav tako je akcijska cena paketa Mobi C 6,99 EUR/mesec. Akcija velja za prvih 6 mesecev ob vklopu v aplikaciji Moj Mobi med 1. 7. in 31. 8. 2026. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `6,99`
- **Relevance — 2/4 = 50%** (weight 20%). Echoed: `akcijska`, `mobi`. **Missing** question keyword(s): `kakšna`, `paketov`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi08` · Prepaid (Mobi)

**Q:** Koliko stane aktivacija kartice SIM ali eSIM Mobi?

**Maks:**

> ✨ Aktivacija eSIM kartice za Mobi uporabnike je mogoča in se zaračuna enako kot menjava klasične SIM kartice, torej 2,95 €. Če potrebujete še kakšno informacijo, kar povejte 😊

**Score: 45.0/100  (★★★☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `2 eur`
- **Relevance — 4/4 = 100%** (weight 20%). Echoed: `aktivacija`, `esim`, `kartice`, `mobi`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×0.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **0.450 → 45.0/100**.
- **Verdict:** Risky: Maks answered confidently with a specific value that does **not** match the site — a candidate factual error.

---

### `mobi09` · Prepaid (Mobi)

**Q:** Kaj dobim ob aktivaciji Mobi SIM kot promocijski zakup?

**Maks:**

> ✨ Ob aktivaciji Mobi SIM ali eSIM prejmete promocijski zakup: 7 dni neomejenih klicev znotraj omrežja Telekoma Slovenije in 1 GB prenosa podatkov v Sloveniji. Uporaba je možna takoj po aktivaciji kartice. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 96.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 3/3 = 100%** (weight 55%). Expected facts:
    - ✅ found: `7 dni` / `7-dnev`
    - ✅ found: `neomejen`
    - ✅ found: `1 gb`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `aktivaciji`, `mobi`, `promocijski`, `zakup`. **Missing** question keyword(s): `dobim`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.80 + 0.15×1 + 0.10×1` = **0.960 → 96.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi10` · Prepaid (Mobi)

**Q:** Koliko stanejo klici in SMS po rednem ceniku Mobi brez paketa?

**Maks:**

> ✨ Klici in SMS po rednem ceniku Mobi brez paketa stanejo:
> 
> 
> 
> Klici v vsa mobilna in fiksna omrežja v Sloveniji: 0,12 €/minuto
> Sporočilo SMS/MMS: 0,12 €/sporočilo
> 
> 
> Za prenos podatkov: 0,12 €/MB. Cene vključujejo DDV. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `0,12`
- **Relevance — 5/5 = 100%** (weight 20%). Echoed: `ceniku`, `klici`, `mobi`, `rednem`, `stanejo`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi11` · Prepaid (Mobi)

**Q:** Koliko stane prenos podatkov na MB po ceniku Mobi brez paketa?

**Maks:**

> ✨ Prenos podatkov na Mobi brez izbranega paketa stane 0,12 € na MB. Cena velja za uporabo v mobilnem omrežju Telekoma Slovenije. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 95.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `0,12`
- **Relevance — 3/4 = 75%** (weight 20%). Echoed: `mobi`, `podatkov`, `prenos`. **Missing** question keyword(s): `ceniku`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.75 + 0.15×1 + 0.10×1` = **0.950 → 95.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi12` · Prepaid (Mobi)

**Q:** Koliko stane Mobi Net in koliko časa velja?

**Maks:**

> ✨ Paket Mobi Net stane 29,99 EUR in velja 365 dni od vklopa. Vključuje 100 GB prenosa podatkov v Sloveniji s hitrostjo do 300/100 Mbit/s. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 2/2 = 100%** (weight 55%). Expected facts:
    - ✅ found: `29,99`
    - ✅ found: `365` / `eno leto` / `leto`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `mobi`, `velja`. **Missing** question keyword(s): `časa`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi13` · Prepaid (Mobi)

**Q:** Koliko GB vključuje Mobi Net Mesec in po kakšni ceni?

**Maks:**

> ✨ Paket Mobi Net Mesec vključuje 100 GB prenosa podatkov v Sloveniji (od tega do 14,89 GB v državah območja EU-tarife). Cena paketa je 9,99 EUR za en mesec. 
> 
> 
> Za več informacij lahko obiščete 👉 Predplačniški Mobi.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 86.7/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 2/2 = 100%** (weight 55%). Expected facts:
    - ✅ found: `9,99`
    - ✅ found: `100 gb`
- **Relevance — 1/3 = 33%** (weight 20%). Echoed: `mobi`. **Missing** question keyword(s): `ceni`, `kakšni`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.33 + 0.15×1 + 0.10×1` = **0.867 → 86.7/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi14` · Prepaid (Mobi)

**Q:** Kako lahko napolnim račun Mobi?

**Maks:**

> Svoj ali drug račun Mobi lahko enostavno napolnite spodaj 👇
> 💡 Ali že poznate mobilno aplikacijo Moj Mobi? Omogoča vam, da vse v zvezi z računi Mobi urejate na enem mestu. Naložite si jo spodaj 👇

**Score: 56.7/100  (★★★☆☆)**

**How this score was reached:**

- **Fact recall — 1/3 = 33%** (weight 55%). Expected facts:
    - ❌ missing: `vrednostn` / `kartic`
    - ❌ missing: `valú` / `valu`
    - ✅ found: `123` / `moj mobi` / `aplikacij`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `mobi`, `račun`. **Missing** question keyword(s): `napolnim`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×0.33 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.567 → 56.7/100**.
- **Verdict:** Partial: some but not all expected facts were stated.

---

### `mobi15` · Prepaid (Mobi)

**Q:** Na katero številko lahko z ukaznim nizom ali klicem napolnim račun Mobi?

**Maks:**

> ✨ Račun Mobi lahko napolnite z ukaznim nizom na številko *123#. Vnesite *123# in pritisnite tipko za klic. S tem preverite stanje ali izvedete polnitev z vrednostnico. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 92.5/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `123`
- **Relevance — 5/8 = 62%** (weight 20%). Echoed: `mobi`, `nizom`, `račun`, `ukaznim`, `številko`. **Missing** question keyword(s): `katero`, `klicem`, `napolnim`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.62 + 0.15×1 + 0.10×1` = **0.925 → 92.5/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi16` · Prepaid (Mobi)

**Q:** Na koliko dni se samodejno podaljša veljavnost računa Mobi?

**Maks:**

> ✨ Veljavnost vašega računa Mobi se ob uspešnem samodejnem podaljšanju podaljša za 90 dni. Storitev samodejnega podaljšanja je vključena pri vseh uporabnikih Mobi, če je na računu dovolj dobroimetja.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 96.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `90 dni` / `90`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `mobi`, `podaljša`, `računa`, `veljavnost`. **Missing** question keyword(s): `samodejno`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.80 + 0.15×1 + 0.10×1` = **0.960 → 96.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi17` · Prepaid (Mobi)

**Q:** Koliko dobroimetja potrebujem za samodejno podaljšanje veljavnosti Mobi?

**Maks:**

> ✨ Za samodejno podaljšanje veljavnosti računa Mobi potrebujete najmanj 1,99 EUR dobroimetja na računu na dan podaljšanja. S tem se veljavnost samodejno podaljša za novih 90 dni. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 96.7/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `1,99`
- **Relevance — 5/6 = 83%** (weight 20%). Echoed: `dobroimetja`, `mobi`, `podaljšanje`, `samodejno`, `veljavnosti`. **Missing** question keyword(s): `potrebujem`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.83 + 0.15×1 + 0.10×1` = **0.967 → 96.7/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi18` · Prepaid (Mobi)

**Q:** Ali imam pri Mobi na voljo 5G omrežje?

**Maks:**

> ✨ Da, kot uporabnik Mobi lahko uporabljate 5G omrežje prek storitve Hitri internet 4G/5G, če imate:
> 
> 
> 
> napravo, ki podpira 5G,
> USIM kartico,
> signal 5G in vključeno storitev Hitri internet 4G/5G.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `5g`
- **Relevance — 2/4 = 50%** (weight 20%). Echoed: `mobi`, `omrežje`. **Missing** question keyword(s): `imam`, `voljo`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi19` · Prepaid (Mobi)

**Q:** Kje vse lahko kupim kartico Mobi?

**Maks:**

> ✨ Kartico Mobi lahko kupite na naslednjih mestih:
> 
> 
> 
> V aplikaciji Moj Mobi (eSIM)
> Telekomovi centri
> Bencinski servisi Petrol
> Trafike 3DVA
> Pošta Slovenije
> Trgovine Mercator (vrednostne kartice)
> Trgovine Spar (elektronske vrednostne kartice)
> 
> 
> Več informacij najdete 👉 mobi
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 3/3 = 100%** (weight 55%). Expected facts:
    - ✅ found: `petrol`
    - ✅ found: `pošt` / `posta`
    - ✅ found: `telekomov` / `trafik` / `mercator` / `spar` / `prodajn`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `kartico`, `mobi`. **Missing** question keyword(s): `kupim`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi20` · Prepaid (Mobi)

**Q:** Katero aplikacijo uporabljam za upravljanje storitev Mobi?

**Maks:**

> ✨ Za upravljanje storitev Mobi uporabljate aplikacijo Moj Mobi. Omogoča vam spremljanje dobroimetja, polnjenje računa, izbiro paketov, upravljanje več številk in še več. Več informacij najdete tukaj 👉 moj-mobi.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `moj mobi`
- **Relevance — 4/6 = 67%** (weight 20%). Echoed: `aplikacijo`, `mobi`, `storitev`, `upravljanje`. **Missing** question keyword(s): `katero`, `uporabljam`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi21` · Prepaid (Mobi)

**Q:** Ali lahko svojo obstoječo telefonsko številko prenesem na Mobi?

**Maks:**

> Prehod iz naročniškega razmerja v Mobi ali obratno lahko uredi moj sodelavec 😊👍
> Želite, da vas povežem s sodelavcem?

**Score: 18.3/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `prenes` / `ohran` / `obdrž`
- **Relevance — 1/6 = 17%** (weight 20%). Echoed: `mobi`. **Missing** question keyword(s): `obstoječo`, `prenesem`, `svojo`, `telefonsko`, `številko`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “vas povežem s sodelavcem” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.17 + 0.15×1 + 0.10×0` = **0.183 → 18.3/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `mobi22` · Prepaid (Mobi)

**Q:** Koliko enot za klice in sporočila vključuje paket Mobi A?

**Maks:**

> ✨ Paket Mobi A vključuje 1000 enot, ki jih lahko porabite za:
> - klice v vsa slovenska omrežja,
> - sporočila SMS/MMS v Sloveniji ali državah območja EU-tarife.
> 
> 
> Vsaka enota velja za 1 minuto klica ali 1 poslano sporočilo. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `1000` / `1.000`
- **Relevance — 4/4 = 100%** (weight 20%). Echoed: `enot`, `klice`, `mobi`, `sporočila`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi23` · Prepaid (Mobi)

**Q:** Koliko GB v EU-tarifi lahko porabim s paketom Mobi B?

**Maks:**

> ✨ S paketom Mobi B lahko v državah območja EU-tarife porabite do 14,89 GB prenosa podatkov na mesec brez doplačila. Za koriščenje enot v EU-tarifi je potrebna registracija uporabnika. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 95.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `14,89`
- **Relevance — 3/4 = 75%** (weight 20%). Echoed: `mobi`, `paketom`, `tarifi`. **Missing** question keyword(s): `porabim`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.75 + 0.15×1 + 0.10×1` = **0.950 → 95.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi24` · Prepaid (Mobi)

**Q:** Koliko GB za območje EU-tarife vključuje paket Mobi C?

**Maks:**

> ✨ Paket Mobi C vključuje neomejen prenos podatkov v Sloveniji in do 20,85 GB prenosa podatkov v državah območja EU-tarife. Po doseženi tej količini se dodatni prenos podatkov v EU zaračuna skladno s cenikom. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `20,85`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `mobi`, `tarife`. **Missing** question keyword(s): `območje`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi25` · Prepaid (Mobi)

**Q:** Ali se paketi Mobi A, B in C samodejno podaljšujejo?

**Maks:**

> ✨ Da, paketi Mobi A, B in C se po vklopu samodejno podaljšujejo vsak mesec, dokler imate na računu dovolj dobroimetja. Če dobroimetja zmanjka ali paket izključite, se podaljševanje ustavi. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `samodejno` / `podaljš`
- **Relevance — 4/4 = 100%** (weight 20%). Echoed: `mobi`, `paketi`, `podaljšujejo`, `samodejno`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi26` · Prepaid (Mobi)

**Q:** Kakšna je redna cena paketa Mobi A?

**Maks:**

> ✨ Redna cena paketa Mobi A je 4,99 EUR na mesec. V času poletne akcije (1. 7.–31. 8. 2026) pa znaša 3,73 EUR za prvih 6 mesecev ob vklopu v aplikaciji Moj Mobi. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `4,99`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `mobi`, `redna`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi27` · Prepaid (Mobi)

**Q:** Kakšna je redna cena paketa Mobi C?

**Maks:**

> ✨ Redna cena paketa Mobi C je 13,99 EUR na mesec. V času poletne akcije (1. 7.–31. 8. 2026) pa je prvih 6 mesecev cena 6,99 EUR/mesec, če paket vključite v aplikaciji Moj Mobi. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `13,99`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `mobi`, `redna`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi28` · Prepaid (Mobi)

**Q:** Koliko enot za klice in SMS vključuje paket Mobi A?

**Maks:**

> ✨ Paket Mobi A vključuje 1000 enot, ki jih lahko porabite za:
> - klice,
> - poslana SMS ali MMS sporočila v Sloveniji ali državah območja EU-tarife.
> 
> 
> Vsaka enota velja za eno minuto klica ali eno poslano sporočilo. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `1000` / `1.000`
- **Relevance — 3/3 = 100%** (weight 20%). Echoed: `enot`, `klice`, `mobi`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi29` · Prepaid (Mobi)

**Q:** Koliko GB v Sloveniji vključuje paket Mobi B?

**Maks:**

> ✨ Paket Mobi B vključuje 100 GB prenosa podatkov v Sloveniji. V času poletne akcije (1. 7.–31. 8. 2026) ga lahko vključite po znižani ceni 6,99 EUR/mesec za prvih 6 mesecev. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `100 gb`
- **Relevance — 2/2 = 100%** (weight 20%). Echoed: `mobi`, `sloveniji`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi30` · Prepaid (Mobi)

**Q:** Kakšna je hitrost prenosa podatkov pri paketih Mobi?

**Maks:**

> ✨ Hitrost prenosa podatkov pri paketih Mobi A, B, C in Mobi Net je do 300/100 Mbit/s. Ta hitrost velja v mobilnem omrežju Telekoma Slovenije. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 96.7/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `300` / `300/100` / `300 mbit`
- **Relevance — 5/6 = 83%** (weight 20%). Echoed: `hitrost`, `mobi`, `paketih`, `podatkov`, `prenosa`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.83 + 0.15×1 + 0.10×1` = **0.967 → 96.7/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi31` · Prepaid (Mobi)

**Q:** Kakšna je akcijska cena Mobi A za prvih 6 mesecev?

**Maks:**

> ✨ Akcijska cena paketa Mobi A za prvih 6 mesecev je 3,73 EUR na mesec. Akcijo lahko izkoristite, če paket vključite v aplikaciji Moj Mobi med 1. 7. in 31. 8. 2026. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 96.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `3,73`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `akcijska`, `mesecev`, `mobi`, `prvih`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.80 + 0.15×1 + 0.10×1` = **0.960 → 96.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi32` · Prepaid (Mobi)

**Q:** Kakšna je akcijska cena paketov Mobi B in C?

**Maks:**

> ✨ Akcijska cena paketov Mobi B in Mobi C je 6,99 EUR/mesec za prvih 6 mesecev, če paket vključite v aplikaciji Moj Mobi med 1. 7. in 31. 8. 2026. Po tem obdobju se zaračuna redna cena. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 95.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `6,99`
- **Relevance — 3/4 = 75%** (weight 20%). Echoed: `akcijska`, `mobi`, `paketov`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.75 + 0.15×1 + 0.10×1` = **0.950 → 95.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi33` · Prepaid (Mobi)

**Q:** Koliko časa velja akcijska cena paketov Mobi?

**Maks:**

> ✨ Akcijska cena paketov Mobi A, B in C velja za prvih 6 mesecev, če paket vključite v aplikaciji Moj Mobi med 1. 7. in 31. 8. 2026. Po tem obdobju se paket samodejno podaljša po redni ceni. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 96.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `6 mesec` / `šest mesec`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `akcijska`, `mobi`, `paketov`, `velja`. **Missing** question keyword(s): `časa`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.80 + 0.15×1 + 0.10×1` = **0.960 → 96.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi34` · Prepaid (Mobi)

**Q:** Koliko stane klic na minuto po rednem ceniku Mobi brez paketa?

**Maks:**

> ✨ Klic na minuto po rednem ceniku Mobi brez paketa stane 0,12 EUR v vsa mobilna in fiksna omrežja v Sloveniji. Cena velja za vsako začeto minuto. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `0,12`
- **Relevance — 5/5 = 100%** (weight 20%). Echoed: `ceniku`, `klic`, `minuto`, `mobi`, `rednem`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi35` · Prepaid (Mobi)

**Q:** Koliko stane poslano sporočilo SMS/MMS po ceniku Mobi?

**Maks:**

> ✨ Cena poslanega SMS ali MMS sporočila prek Mobi je določena po veljavnem ceniku za SMS oziroma MMS sporočila. Pri paketih z vključenimi količinami se najprej koristijo zakupljene količine. Za natančne cene preverite aktualni cenik na naši spletni strani ali v Moj Telekom aplikaciji.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 35.0/100  (★★☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `0,12`
- **Relevance — 2/4 = 50%** (weight 20%). Echoed: `ceniku`, `mobi`. **Missing** question keyword(s): `poslano`, `sporočilo`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×0.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.350 → 35.0/100**.
- **Verdict:** Risky: Maks answered confidently with a specific value that does **not** match the site — a candidate factual error.

---

### `mobi36` · Prepaid (Mobi)

**Q:** Koliko stane prenos podatkov na MB po ceniku Mobi brez paketa?

**Maks:**

> ✨ Prenos podatkov na Mobi brez izbranega paketa se obračuna po ceni 0,12 € na MB. Cena velja za uporabo v mobilnem omrežju Telekoma Slovenije. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 95.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `0,12`
- **Relevance — 3/4 = 75%** (weight 20%). Echoed: `mobi`, `podatkov`, `prenos`. **Missing** question keyword(s): `ceniku`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.75 + 0.15×1 + 0.10×1` = **0.950 → 95.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi37` · Prepaid (Mobi)

**Q:** Koliko stane paket Mobi Net za eno leto?

**Maks:**

> ✨ Paket Mobi Net za eno leto stane 29,99 EUR. Vključuje 100 GB prenosa podatkov v Sloveniji s hitrostjo do 300/100 Mbit/s in velja 365 dni od vklopa. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `29,99`
- **Relevance — 2/2 = 100%** (weight 20%). Echoed: `leto`, `mobi`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi38` · Prepaid (Mobi)

**Q:** Koliko dni velja paket Mobi Net?

**Maks:**

> ✨ Paket Mobi Net velja 365 dni od dneva vklopa. Po preteku tega obdobja je potrebno paket ponovno vklopiti, če želite nadaljevati z uporabo. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `365` / `eno leto` / `leto`
- **Relevance — 2/2 = 100%** (weight 20%). Echoed: `mobi`, `velja`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi39` · Prepaid (Mobi)

**Q:** Koliko GB vključuje Mobi Net Mesec?

**Maks:**

> ✨ Paket Mobi Net Mesec vključuje 100 GB prenosa podatkov v Sloveniji, od tega lahko do 14,89 GB porabite v državah območja EU-tarife. Hitrost prenosa je do 300/100 Mbit/s. Paket velja en mesec od vklopa.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `100 gb`
- **Relevance — 1/1 = 100%** (weight 20%). Echoed: `mobi`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi40` · Prepaid (Mobi)

**Q:** Kakšna je cena paketa Mobi Net Mesec?

**Maks:**

> ✨ Cena paketa Mobi Net Mesec je 9,99 EUR za en mesec. Paket vključuje 100 GB prenosa podatkov v Sloveniji in do 14,89 GB v državah območja EU-tarife. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `9,99`
- **Relevance — 1/2 = 50%** (weight 20%). Echoed: `mobi`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi41` · Prepaid (Mobi)

**Q:** Koliko stane aktivacija kartice SIM ali eSIM Mobi?

**Maks:**

> ✨ Aktivacija eSIM kartice za Mobi uporabnike (predplačniški račun) se zaračuna enako kot menjava klasične SIM kartice, torej 2,95 €. Če potrebujete pomoč pri naročilu ali aktivaciji, z veseljem pomagam. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 45.0/100  (★★★☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `2 eur` / `2 €`
- **Relevance — 4/4 = 100%** (weight 20%). Echoed: `aktivacija`, `esim`, `kartice`, `mobi`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×0.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **0.450 → 45.0/100**.
- **Verdict:** Risky: Maks answered confidently with a specific value that does **not** match the site — a candidate factual error.

---

### `mobi42` · Prepaid (Mobi)

**Q:** Kaj vključuje promocijski zakup ob aktivaciji Mobi?

**Maks:**

> ✨ Ob aktivaciji SIM ali eSIM Mobi prejmete promocijski zakup: 7 dni neomejenih klicev znotraj omrežja Telekoma Slovenije in 1 GB prenosa podatkov v Sloveniji. Po izteku lahko izberete paket ali plačujete po porabi. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 3/3 = 100%** (weight 55%). Expected facts:
    - ✅ found: `7 dni` / `7-dnev`
    - ✅ found: `neomejen`
    - ✅ found: `1 gb`
- **Relevance — 4/4 = 100%** (weight 20%). Echoed: `aktivaciji`, `mobi`, `promocijski`, `zakup`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi43` · Prepaid (Mobi)

**Q:** Na katero številko lahko z ukaznim nizom napolnim račun Mobi?

**Maks:**

> ✨ Račun Mobi lahko napolnite z ukaznim nizom na katerokoli številko Mobi. V mobitel vtipkajte:
> 12316-mestna številka*telefonska številka#
> in pritisnite tipko za klicanje.
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 94.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `123`
- **Relevance — 5/7 = 71%** (weight 20%). Echoed: `mobi`, `nizom`, `račun`, `ukaznim`, `številko`. **Missing** question keyword(s): `katero`, `napolnim`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.71 + 0.15×1 + 0.10×1` = **0.943 → 94.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi44` · Prepaid (Mobi)

**Q:** S katero storitvijo (moneta) lahko napolnim račun Mobi?

**Maks:**

> ✨ Račun Mobi lahko napolnite s storitvijo VALÚ Moneta. Gre za praktično, hitro in varno možnost, ki omogoča polnitev doma ali v tujini. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `valú` / `valu`
- **Relevance — 4/6 = 67%** (weight 20%). Echoed: `mobi`, `moneta`, `račun`, `storitvijo`. **Missing** question keyword(s): `katero`, `napolnim`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi45` · Prepaid (Mobi)

**Q:** Na koliko dni se samodejno podaljša veljavnost računa Mobi?

**Maks:**

> ✨ Veljavnost vašega Mobi računa se ob uspešnem samodejnem podaljšanju brez polnitve podaljša za 90 dni. Storitev se izvede vsakih 89 dni, če imate dovolj dobroimetja (1,99 EUR). Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 96.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `90` / `90 dni`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `mobi`, `podaljša`, `računa`, `veljavnost`. **Missing** question keyword(s): `samodejno`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.80 + 0.15×1 + 0.10×1` = **0.960 → 96.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi46` · Prepaid (Mobi)

**Q:** Koliko dobroimetja potrebujem za samodejno podaljšanje veljavnosti?

**Maks:**

> ✨ Za samodejno podaljšanje veljavnosti dobroimetja potrebujete zadostno stanje na računu, da pokrijete strošek izbranega paketa ali storitve. Točen znesek je odvisen od vašega paketa. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 26.0/100  (★★☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `1,99`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `dobroimetja`, `podaljšanje`, `samodejno`, `veljavnosti`. **Missing** question keyword(s): `potrebujem`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×0.00 + 0.20×0.80 + 0.15×0 + 0.10×1` = **0.260 → 26.0/100**.
- **Verdict:** Weak: the expected fact(s) did not appear in the answer.

---

### `mobi47` · Prepaid (Mobi)

**Q:** Ali imajo vsi uporabniki Mobi dostop do 5G?

**Maks:**

> ✨ Uporabniki Mobi lahko uporabljajo 5G omrežje, če imajo:
> 
> 
> 
> napravo, ki podpira 5G,
> USIM kartico,
> signal 5G in vključeno storitev Hitri internet 4G/5G.
> 
> 
> Dostop ni samodejen za vse – storitev je treba vključiti. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `5g`
- **Relevance — 4/4 = 100%** (weight 20%). Echoed: `dostop`, `imajo`, `mobi`, `uporabniki`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi48` · Prepaid (Mobi)

**Q:** Na katerih bencinskih servisih lahko kupim kartico Mobi?

**Maks:**

> ✨ Kartico Mobi lahko kupite na vseh bencinskih servisih Petrol po Sloveniji. Na teh mestih so na voljo tudi paketi Mobi in elektronske vrednostne kartice Mobi. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `petrol`
- **Relevance — 4/6 = 67%** (weight 20%). Echoed: `bencinskih`, `kartico`, `mobi`, `servisih`. **Missing** question keyword(s): `katerih`, `kupim`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi49` · Prepaid (Mobi)

**Q:** Ali lahko kartico Mobi kupim na Pošti Slovenije?

**Maks:**

> ✨ Da, kartico Mobi lahko kupite na vseh poslovalnicah Pošte Slovenije po vsej Sloveniji. Prav tako so na voljo tudi paketi Mobi in vrednostne kartice Mobi. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 92.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `pošt` / `posta` / `da`
- **Relevance — 3/5 = 60%** (weight 20%). Echoed: `kartico`, `mobi`, `slovenije`. **Missing** question keyword(s): `kupim`, `pošti`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.60 + 0.15×1 + 0.10×1` = **0.920 → 92.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi50` · Prepaid (Mobi)

**Q:** V katerih trgovinah lahko kupim vrednostnice Mobi (npr. živila)?

**Maks:**

> ✨ Vrednostnice Mobi lahko kupite v naslednjih trgovinah z živili:
> 
> 
> 
> Mercator (vrednostne kartice Mobi)
> Spar (elektronske vrednostne kartice Mobi)
> 
> 
> Na voljo so tudi na Petrolu, Pošti Slovenije in trafikah 3DVA. Želite še seznam vseh prodajnih mest ali podrobnosti o polnitvi računa? Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `mercator` / `spar`
- **Relevance — 3/6 = 50%** (weight 20%). Echoed: `mobi`, `trgovinah`, `vrednostnice`. **Missing** question keyword(s): `katerih`, `kupim`, `živila`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi51` · Prepaid (Mobi)

**Q:** Katero aplikacijo uporabljam za upravljanje Mobi?

**Maks:**

> ✨ Za upravljanje vašega Mobi računa uporabljate aplikacijo Moj Mobi. Omogoča spremljanje dobroimetja, polnjenje računa, izbiro paketov, upravljanje več številk, shranjevanje plačilnih kartic in še več. Več informacij najdete tukaj 👉 moj-mobi.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 92.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `moj mobi`
- **Relevance — 3/5 = 60%** (weight 20%). Echoed: `aplikacijo`, `mobi`, `upravljanje`. **Missing** question keyword(s): `katero`, `uporabljam`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.60 + 0.15×1 + 0.10×1` = **0.920 → 92.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi52` · Prepaid (Mobi)

**Q:** Ali lahko obstoječo telefonsko številko prenesem na Mobi?

**Maks:**

> Prehod iz naročniškega razmerja v Mobi ali obratno lahko uredi moj sodelavec 😊👍
> Želite, da vas povežem s sodelavcem?

**Score: 19.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `prenes` / `ohran` / `obdrž`
- **Relevance — 1/5 = 20%** (weight 20%). Echoed: `mobi`. **Missing** question keyword(s): `obstoječo`, `prenesem`, `telefonsko`, `številko`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “vas povežem s sodelavcem” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.20 + 0.15×1 + 0.10×0` = **0.190 → 19.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `mobi53` · Prepaid (Mobi)

**Q:** Koliko GB v EU-tarifi lahko porabim s paketom Mobi B?

**Maks:**

> ✨ S paketom Mobi B lahko v državah območja EU-tarife brez doplačila porabite do 14,89 GB prenosa podatkov na mesec. V Sloveniji imate na voljo 100 GB. Za uporabo v EU-tarifi je potrebna registracija uporabnika.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 95.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `14,89`
- **Relevance — 3/4 = 75%** (weight 20%). Echoed: `mobi`, `paketom`, `tarifi`. **Missing** question keyword(s): `porabim`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.75 + 0.15×1 + 0.10×1` = **0.950 → 95.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi54` · Prepaid (Mobi)

**Q:** Koliko GB za območje EU-tarife vključuje paket Mobi C?

**Maks:**

> ✨ Paket Mobi C vključuje neomejen prenos podatkov v Sloveniji in do 20,85 GB prenosa podatkov v državah območja EU-tarife na mesec. Po doseženi količini v EU-tarifi se dodatni prenos zaračuna skladno s cenikom. Za uporabo v EU-tarifi je potrebna registracija uporabnika.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `20,85`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `mobi`, `tarife`. **Missing** question keyword(s): `območje`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi55` · Prepaid (Mobi)

**Q:** Po koliko GB se pri paketu Mobi C zniža hitrost?

**Maks:**

> ✨ Pri paketu Mobi C se hitrost prenosa podatkov zniža po porabljenih 200 GB v Sloveniji. Po tem je hitrost omejena na 64/64 kbit/s do naslednjega zakupa. Vam lahko še kaj dodatno pojasnim?

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `200 gb`
- **Relevance — 3/3 = 100%** (weight 20%). Echoed: `hitrost`, `mobi`, `zniža`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi56` · Prepaid (Mobi)

**Q:** Na kakšno hitrost pade prenos po limitu pri paketu Mobi C?

**Maks:**

> ✨ Hitrost prenosa podatkov pri paketu Mobi C po preseženem mesečnem limitu pade na 64 kbps. Če potrebujete več podatkov, lahko vedno dokupite dodatne količine. 
> 
> 
> Vam lahko še kako pomagam? 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `64` / `64/64` / `64 kbit`
- **Relevance — 4/6 = 67%** (weight 20%). Echoed: `hitrost`, `limitu`, `mobi`, `pade`. **Missing** question keyword(s): `kakšno`, `prenos`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi57` · Prepaid (Mobi)

**Q:** Ali se paketi Mobi A, B in C samodejno podaljšujejo?

**Maks:**

> ✨ Da, paketi Mobi A, B in C se po vklopu samodejno podaljšujejo vsak mesec, dokler imate na računu dovolj dobroimetja ali jih ne izklopite sami. Želite izvedeti še kaj glede upravljanja teh paketov? Kar vprašajte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `samodejno` / `podaljš`
- **Relevance — 4/4 = 100%** (weight 20%). Echoed: `mobi`, `paketi`, `podaljšujejo`, `samodejno`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1) (a redirect phrase “želite izvedeti” is present, but fact recall ≥ 34%, so it is *not* treated as a deflection).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi58` · Prepaid (Mobi)

**Q:** Ali lahko Mobi uporabljam brez paketa (plačilo po porabi)?

**Maks:**

> ✨ Da, Mobi lahko uporabljate tudi brez paketa. V tem primeru se klici, sporočila in prenos podatkov obračunavajo po rednem ceniku, poraba pa se odšteva od vašega dobroimetja. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 85.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `po porabi` / `brez paket` / `dobroimetj`
- **Relevance — 1/4 = 25%** (weight 20%). Echoed: `mobi`. **Missing** question keyword(s): `plačilo`, `porabi`, `uporabljam`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.25 + 0.15×1 + 0.10×1` = **0.850 → 85.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi59` · Prepaid (Mobi)

**Q:** Kako se imenuje zakup za neomejene podatke na Hrvaškem (Mobi)?

**Maks:**

> ✨ Zakup za neomejene podatke na Hrvaškem za uporabnike Mobi se imenuje HR-internet Plus (za 7 dni) ali HR-internet neomejeno (mesečni zakup). 
> 
> 
> 
> HR-internet Plus: 5,99 € za 7 dni, neomejen prenos podatkov (po 20 GB hitrost 2/1 Mbit/s).
> HR-internet neomejeno: 9,94 € na mesec, neomejen prenos podatkov (po 30 GB hitrost 2/1 Mbit/s).
> 
> 
> Več informacij 👉 HR-internet.

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `hr-internet` / `hr internet` / `hrvaš`
- **Relevance — 6/6 = 100%** (weight 20%). Echoed: `hrvaškem`, `imenuje`, `mobi`, `neomejene`, `podatke`, `zakup`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi60` · Prepaid (Mobi)

**Q:** Katere države pokrivajo zakupi Balkan pri Mobi?

**Maks:**

> ✨ Zakupi Balkan pri Mobi veljajo v naslednjih državah:
> - Bosna in Hercegovina
> - Srbija
> - Črna gora
> - Severna Makedonija
> - Kosovo
> - Albanija
> 
> 
> 👉 Več informacij

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `bosn` / `srbij` / `kosov` / `makedonij` / `črn` / `albanij`
- **Relevance — 3/6 = 50%** (weight 20%). Echoed: `balkan`, `mobi`, `zakupi`. **Missing** question keyword(s): `države`, `katere`, `pokrivajo`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi61` · Prepaid (Mobi)

**Q:** Ali je za ZDA na voljo zakup podatkov pri Mobi?

**Maks:**

> Za tujino so za predplačnike na voljo različni zakupi.
> Mi najprej poveste, ali imate predplačniško številko dodano v Moj Telekom?

**Score: 20.0/100  (★★☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `zda` / `neomejen`
- **Relevance — 1/4 = 25%** (weight 20%). Echoed: `voljo`. **Missing** question keyword(s): `mobi`, `podatkov`, `zakup`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “mi najprej poveste” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.25 + 0.15×1 + 0.10×0` = **0.200 → 20.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `mobi62` · Prepaid (Mobi)

**Q:** Koliko GB podatkov v Sloveniji vključuje paket Mobi A?

**Maks:**

> ✨ Paket Mobi A vključuje 1 GB prenosa podatkov v Sloveniji na mesec. Vključuje tudi 1000 enot za klice in sporočila v Sloveniji ali državah območja EU-tarife. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `1 gb`
- **Relevance — 3/3 = 100%** (weight 20%). Echoed: `mobi`, `podatkov`, `sloveniji`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi63` · Prepaid (Mobi)

**Q:** Ali so pri paketu Mobi B klici in SMS neomejeni?

**Maks:**

> ✨ Da, pri paketu Mobi B so klici in sporočila (SMS/MMS) v Sloveniji in državah območja EU-tarife neomejeni. Prav tako vključuje 100 GB prenosa podatkov v Sloveniji (od tega do 14,89 GB v državah EU-tarife). 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `neomejen`
- **Relevance — 3/3 = 100%** (weight 20%). Echoed: `klici`, `mobi`, `neomejeni`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi64` · Prepaid (Mobi)

**Q:** Ali lahko dobroimetje prenesem na drug račun Mobi?

**Maks:**

> Dobroimetje z enega na drug račun Mobi enostavno prenesite spodaj 👇
> 💡 Ali že poznate mobilno aplikacijo Moj Mobi? Omogoča vam, da vse v zvezi z računi Mobi urejate na enem mestu. Naložite si jo spodaj 👇

**Score: 96.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `prenos` / `prenes` / `da`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `dobroimetje`, `drug`, `mobi`, `račun`. **Missing** question keyword(s): `prenesem`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.80 + 0.15×1 + 0.10×1` = **0.960 → 96.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi65` · Prepaid (Mobi)

**Q:** Kako se imenuje storitev za brezplačno klicanje ene številke Mobi?

**Maks:**

> ✨ Storitev za brezplačno klicanje ene izbrane številke pri Mobi se imenuje Moja številka Mobi. Omogoča vam, da eno številko uporabnika ali naročnika Telekoma Slovenije kličete brezplačno, če izpolnjujete pogoje uporabe.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `moja številka` / `moja stevilka`
- **Relevance — 6/6 = 100%** (weight 20%). Echoed: `brezplačno`, `imenuje`, `klicanje`, `mobi`, `storitev`, `številke`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi66` · Prepaid (Mobi)

**Q:** Kaj je storitev Žepnina pri Mobi?

**Maks:**

> ✨ Storitev Žepnina omogoča, da mobilni naročnik Telekom Slovenije plačuje storitve Mobi uporabnika prek svojega mesečnega računa. Naročnik določi mesečni limit, Mobi uporabnik pa lahko znotraj tega limita koristi nakupe ali polnitve. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `limit` / `plačuj` / `otrok` / `starš`
- **Relevance — 3/3 = 100%** (weight 20%). Echoed: `mobi`, `storitev`, `žepnina`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi67` · Prepaid (Mobi)

**Q:** Ali lahko eSIM Mobi aktiviram kar v aplikaciji Moj Mobi?

**Maks:**

> ✨ Da, eSIM Mobi lahko enostavno kupite in aktivirate neposredno v aplikaciji Moj Mobi. Postopek je hiter, enostaven in popolnoma digitalen – po nakupu lahko z uporabo pričnete takoj. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 95.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `moj mobi` / `da` / `aplikacij`
- **Relevance — 3/4 = 75%** (weight 20%). Echoed: `aplikaciji`, `esim`, `mobi`. **Missing** question keyword(s): `aktiviram`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.75 + 0.15×1 + 0.10×1` = **0.950 → 95.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi68` · Prepaid (Mobi)

**Q:** Katere pakete (klici/SMS neomejeni) ponuja Mobi poleg A?

**Maks:**

> ✨ Poleg paketa Mobi A sta na voljo še paketa Mobi B in Mobi C, ki vključujeta neomejene klice in sporočila (SMS/MMS) v Sloveniji in državah območja EU-tarife:
> 
> 
> 
> Mobi B: 100 GB podatkov v Sloveniji (do 14,89 GB v EU), 6,99 €/mesec (6 mesecev akcijska cena).
> Mobi C: Neomejen prenos podatkov v Sloveniji (do 20,85 GB v EU), 6,99 €/mesec (6 mesecev akcijska cena).
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 85.7/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `mobi b` / `mobi c`
- **Relevance — 2/7 = 29%** (weight 20%). Echoed: `mobi`, `poleg`. **Missing** question keyword(s): `katere`, `klici`, `neomejeni`, `pakete`, `ponuja`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.29 + 0.15×1 + 0.10×1` = **0.857 → 85.7/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi69` · Prepaid (Mobi)

**Q:** Koliko GB vključuje paket Mobi Net za eno leto?

**Maks:**

> ✨ Paket Mobi Net za eno leto vključuje 100 GB prenosa podatkov v Sloveniji. Veljavnost paketa je 365 dni od vklopa. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `100 gb`
- **Relevance — 2/2 = 100%** (weight 20%). Echoed: `leto`, `mobi`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi70` · Prepaid (Mobi)

**Q:** Ali lahko z Mojim Mobi upravljam več številk Mobi hkrati?

**Maks:**

> V spletni različici Mojega Telekoma lahko z nekaj kliki dodate številko Mobi. Kliknite spodaj 👇
> 💡Če dostopa do Mojega Telekoma še nimate, si ga čim prej zagotovite. Moj Telekom vam omogoča, da vsa svoja razmerja urejate sami 👇

**Score: 84.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `več` / `otrok` / `številk`
- **Relevance — 1/5 = 20%** (weight 20%). Echoed: `mobi`. **Missing** question keyword(s): `hkrati`, `mojim`, `upravljam`, `številk`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.20 + 0.15×1 + 0.10×1` = **0.840 → 84.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi71` · Prepaid (Mobi)

**Q:** Kje lahko poleg spleta osebno kupim SIM Mobi?

**Maks:**

> ✨ SIM-kartico Mobi lahko osebno kupite na naslednjih mestih:
> 
> 
> 
> Telekomovi centri
> Petrol bencinski servisi
> Trafike 3DVA
> Pošta Slovenije
> Trgovine Mercator (vrednostne kartice)
> Trgovine SPAR (elektronske vrednostne kartice)
> 
> 
> Želite še podrobnosti o posameznih lokacijah? Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 88.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `telekomov` / `prodajn` / `petrol` / `pošt`
- **Relevance — 2/5 = 40%** (weight 20%). Echoed: `mobi`, `osebno`. **Missing** question keyword(s): `kupim`, `poleg`, `spleta`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.40 + 0.15×1 + 0.10×1` = **0.880 → 88.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi72` · Prepaid (Mobi)

**Q:** Ali se neporabljene količine Mobi prenašajo v naslednji mesec?

**Maks:**

> ✨ Ne, neizkoriščene enote iz paketov Mobi se ne prenašajo v naslednje mesečno obdobje in zapadejo po izteku veljavnosti paketa. Porabo lahko kadarkoli preverite s sporočilom PORABA na 1917 ali v Mojem Telekomu. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 88.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `ne` / `ne prenaš`
- **Relevance — 2/5 = 40%** (weight 20%). Echoed: `mobi`, `prenašajo`. **Missing** question keyword(s): `količine`, `naslednji`, `neporabljene`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.40 + 0.15×1 + 0.10×1` = **0.880 → 88.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi73` · Prepaid (Mobi)

**Q:** Kakšna je hitrost prenosa (upload) pri paketih Mobi?

**Maks:**

> ✨ Paketi Mobi so predplačniški mobilni paketi, ne fiksni internet. Hitrost prenosa podatkov (upload) je odvisna od omrežja (3G, 4G, 5G) in zakupljene količine podatkov. Natančne hitrosti niso določene kot pri fiksnih paketih, običajno pa se gibljejo v okviru zmožnosti posameznega omrežja. Vas zanima še kaj glede fiksnega interneta ali drugih storitev?

**Score: 41.7/100  (★★★☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `100` / `100 mbit`
- **Relevance — 5/6 = 83%** (weight 20%). Echoed: `hitrost`, `mobi`, `paketih`, `prenosa`, `upload`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×0.00 + 0.20×0.83 + 0.15×1 + 0.10×1` = **0.417 → 41.7/100**.
- **Verdict:** Risky: Maks answered confidently with a specific value that does **not** match the site — a candidate factual error.

---

### `mobi74` · Prepaid (Mobi)

**Q:** Kakšna je redna cena paketa Mobi B?

**Maks:**

> ✨ Redna cena paketa Mobi B je 9,99 EUR na mesec. V času poletne akcije (1. 7.–31. 8. 2026) pa je prvih 6 mesecev cena 6,99 EUR/mesec. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `9,99`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `mobi`, `redna`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `mobi75` · Prepaid (Mobi)

**Q:** Ali je za koriščenje enot v EU potrebna registracija (Mobi)?

**Maks:**

> Uporabniki predplačniških storitev, ki želite enote v paketih Mobi koristiti v državah območja EU-tarife, se morate registrirati v aplikaciji Moj Mobi 👇
> Registracija bo urejena najkasneje v roku petih delovnih dni, o čemer boste obveščeni z SMS-om.

**Score: 88.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `registracij`
- **Relevance — 2/5 = 40%** (weight 20%). Echoed: `mobi`, `registracija`. **Missing** question keyword(s): `enot`, `koriščenje`, `potrebna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.40 + 0.15×1 + 0.10×1` = **0.880 → 88.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---


## Postpaid (Naj)

### `naj01` · Postpaid (Naj)

**Q:** Koliko stane paket Naj A na mesec in koliko podatkov vključuje?

**Maks:**

> ✨ Paket Naj A stane 20,99 € na mesec (redna cena). Vključuje 20 GB prenosa podatkov, od tega do 20 GB v državah EU-tarife. 
> 
> 
> Če ste novi naročnik, je na voljo promocijska cena:
> - 10,99 € na mesec za 36 mesecev (sklenitev prek Moj Telekom) ali 24 mesecev (drugi kanali), ob vezavi za 24 mesecev in ugodnosti Poveži in prihrani. Po promociji velja redna cena. 
> 
> 
> Vas zanima še kaj? 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 2/2 = 100%** (weight 55%). Expected facts:
    - ✅ found: `20,99`
    - ✅ found: `20 gb`
- **Relevance — 1/1 = 100%** (weight 20%). Echoed: `podatkov`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj02` · Postpaid (Naj)

**Q:** Koliko prenosa podatkov je vključenega v paketu Naj A?

**Maks:**

> ✨ Paket Naj A vključuje 20 GB prenosa podatkov, od tega lahko v državah območja EU-tarife brezplačno porabite do 20 GB. 😊 Potrebujete še kakšno informacijo?

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `20 gb`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `podatkov`, `prenosa`. **Missing** question keyword(s): `vključenega`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj03` · Postpaid (Naj)

**Q:** Kakšna je redna mesečna cena paketa Naj B?

**Maks:**

> ✨ Redna mesečna cena paketa Naj B znaša 27,99 €.

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `27,99`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `mesečna`, `redna`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj04` · Postpaid (Naj)

**Q:** Po koliko GB se v paketu Naj B zniža hitrost prenosa podatkov?

**Maks:**

> ✨ V paketu Naj B se hitrost prenosa podatkov zniža po porabljenih 200 GB. Hitrost se zmanjša na 2/1 Mbit/s do konca obračunskega obdobja.

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `200 gb`
- **Relevance — 4/4 = 100%** (weight 20%). Echoed: `hitrost`, `podatkov`, `prenosa`, `zniža`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj05` · Postpaid (Naj)

**Q:** Kakšna je redna cena paketa Naj C na mesec?

**Maks:**

> ✨ Redna cena paketa Naj C znaša 28,99 € na mesec. Po izteku morebitnih akcijskih ugodnosti se začne zaračunavati ta cena.

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `28,99`
- **Relevance — 1/2 = 50%** (weight 20%). Echoed: `redna`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj06` · Postpaid (Naj)

**Q:** Po koliko porabljenih GB se v paketu Naj C zniža hitrost?

**Maks:**

> ✨ Pri paketu Naj C se hitrost prenosa podatkov zniža po porabljenih 500 GB. Hitrost se zniža na 2/1 Mbit/s, z običajno hitrostjo pa se nadaljuje v naslednjem obračunskem obdobju.

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `500 gb`
- **Relevance — 3/3 = 100%** (weight 20%). Echoed: `hitrost`, `porabljenih`, `zniža`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj07` · Postpaid (Naj)

**Q:** Koliko stane paket Naj naprava in kaj vključuje?

**Maks:**

> ✨ Paket Naj Naprava stane 4,99 € na mesec. Vključuje:
> - Prenos podatkov: 1 GB (tudi v EU-tarifi).
> - Sporočila: 500 SMS/MMS v Sloveniji ali EU-tarifi.
> - Klici: Do 10 € mesečnega limita, nato brezplačno.
> - Hitrost interneta: Do 300/100 Mbit/s.  
> 
> 
> Po porabi vključenih količin se dodatne storitve zaračunajo po ceniku.  
> 
> 
> Vam lahko še kaj razložim? 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 3/3 = 100%** (weight 55%). Expected facts:
    - ✅ found: `4,99`
    - ✅ found: `1 gb`
    - ✅ found: `500`
- **Relevance — 1/1 = 100%** (weight 20%). Echoed: `naprava`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj08` · Postpaid (Naj)

**Q:** Kakšna je najvišja hitrost prenosa do uporabnika pri paketih Naj?

**Maks:**

> ✨ Najvišja hitrost prenosa do uporabnika pri paketih Naj je odvisna od izbranega paketa in tehnologije. Bi želeli preveriti hitrost vašega paketa?

**Score: 31.7/100  (★★☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `1 gbit` / `gbit`
- **Relevance — 5/6 = 83%** (weight 20%). Echoed: `hitrost`, `najvišja`, `paketih`, `prenosa`, `uporabnika`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “odvisna od izbranega” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.83 + 0.15×1 + 0.10×0` = **0.317 → 31.7/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `naj09` · Postpaid (Naj)

**Q:** Ali paketi Naj vključujejo neomejene klice in SMS v Sloveniji?

**Maks:**

> ✨ Paketi Naj vključujejo neomejene klice in SMS v Sloveniji. Če potrebujete podrobnejše informacije o posameznem paketu ali dodatnih storitvah, mi prosim sporočite. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `neomejen`
- **Relevance — 5/5 = 100%** (weight 20%). Echoed: `klice`, `neomejene`, `paketi`, `sloveniji`, `vključujejo`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1) (a redirect phrase “prosim sporočite” is present, but fact recall ≥ 34%, so it is *not* treated as a deflection).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj10` · Postpaid (Naj)

**Q:** Koliko znaša priključna taksa ob sklenitvi paketa Naj?

**Maks:**

> ✨ Priključna taksa ob sklenitvi paketa Naj znaša 29,00 EUR. 
> 
> 
> Ali potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 45.0/100  (★★★☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `10,95`
- **Relevance — 4/4 = 100%** (weight 20%). Echoed: `priključna`, `sklenitvi`, `taksa`, `znaša`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×0.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **0.450 → 45.0/100**.
- **Verdict:** Risky: Maks answered confidently with a specific value that does **not** match the site — a candidate factual error.

---

### `naj11` · Postpaid (Naj)

**Q:** Koliko stane sprememba naročniškega paketa?

**Maks:**

> Da bom lažje našel najboljšo rešitev, mi povejte, ali želite spremeniti mobilni paket 📱 ali paket s televizijo in internetom 🏠

**Score: 15.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `10,95`
- **Relevance — 0/2 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `naročniškega`, `sprememba`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “mi povejte” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.00 + 0.15×1 + 0.10×0` = **0.150 → 15.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `naj12` · Postpaid (Naj)

**Q:** Kje lahko spremenim svoj naročniški paket Naj?

**Maks:**

> Da bom lažje našel najboljšo rešitev, mi povejte, ali želite spremeniti mobilni paket 📱 ali paket s televizijo in internetom 🏠

**Score: 15.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/2 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `moj telekom` / `mojem telekomu`
    - ❌ missing: `041 700 700` / `prodajn`
- **Relevance — 0/3 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `naročniški`, `spremenim`, `svoj`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “mi povejte” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.00 + 0.15×1 + 0.10×0` = **0.150 → 15.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `naj13` · Postpaid (Naj)

**Q:** Kolikšen je popust pri ugodnosti Poveži in prihrani?

**Maks:**

> ✨ Popust Poveži in prihrani znaša 5 EUR na mesec pri mobilnih paketih Naj A, Naj B, Naj C, Naj 5G ter pri paketu Naj Net. Pri fiksnem paketu Net v kombinaciji s paketom SUPR je popust 15 EUR na mesec. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 92.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `5 eur`
- **Relevance — 3/5 = 60%** (weight 20%). Echoed: `popust`, `poveži`, `prihrani`. **Missing** question keyword(s): `kolikšen`, `ugodnosti`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “5 eur”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.60 + 0.15×1 + 0.10×1` = **0.920 → 92.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj14` · Postpaid (Naj)

**Q:** Koliko stane storitev Ena številka?

**Maks:**

> ✨ Storitev Ena številka stane 1 EUR na mesec. Ta znesek se zaračuna le nosilni številki, dodatne številke imajo storitev brezplačno. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `1 eur`
- **Relevance — 2/2 = 100%** (weight 20%). Echoed: `storitev`, `številka`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “1 eur”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj15` · Postpaid (Naj)

**Q:** Koliko dodatnih naročniških razmerij Druga številka omogoča paket Naj C?

**Maks:**

> ✨ Paket Naj C omogoča do 4 dodatna naročniška razmerja Druga številka. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `4` / `štiri`
- **Relevance — 3/6 = 50%** (weight 20%). Echoed: `druga`, `omogoča`, `številka`. **Missing** question keyword(s): `dodatnih`, `naročniških`, `razmerij`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj16` · Postpaid (Naj)

**Q:** Po koliko GB lahko z Delim GB delim gigabajte najbližjim?

**Maks:**

> ✨ Z Delim GB lahko svojim najbližjim večkrat mesečno delite 5, 10, 20 ali 50 GB. Delitev lahko opravite v Moj Telekom ali prek SMS sporočila. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `50 gb` / `20 gb` / `10 gb` / `5 gb`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `delim`, `najbližjim`. **Missing** question keyword(s): `gigabajte`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj17` · Postpaid (Naj)

**Q:** Na katero številko pošljem SMS za deljenje GB (Delim GB)?

**Maks:**

> ✨ SMS za deljenje GB pošljete na številko 1918. V sporočilo napišite: DELIM XXGB MOBILNA STEVILKA PREJEMNIKA (npr. DELIM 5GB 041700700). Storitev je na voljo naročnikom.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 92.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `1918`
- **Relevance — 3/5 = 60%** (weight 20%). Echoed: `delim`, `deljenje`, `številko`. **Missing** question keyword(s): `katero`, `pošljem`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.60 + 0.15×1 + 0.10×1` = **0.920 → 92.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj18` · Postpaid (Naj)

**Q:** Ali imam pri paketih Naj na voljo omrežje 5G?

**Maks:**

> ✨ Da, omrežje 5G je na voljo pri paketih Naj. Pokritost z 5G omrežjem dosega 99 % prebivalstva. Za podrobnosti o pokritosti lahko preverite na spodnji povezavi:
> https://www.telekom.si/mobilno/pokritost-mobilnega-omrezja
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 95.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `5g`
- **Relevance — 3/4 = 75%** (weight 20%). Echoed: `omrežje`, `paketih`, `voljo`. **Missing** question keyword(s): `imam`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.75 + 0.15×1 + 0.10×1` = **0.950 → 95.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj19` · Postpaid (Naj)

**Q:** Koliko GB lahko v paketu Naj B brezplačno porabim v EU?

**Maks:**

> ✨ V paketu Naj B lahko v državah območja EU-tarife brezplačno porabite 41,71 GB podatkov. Po tej količini se dodatni prenos podatkov zaračuna po ceniku.

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `41,71`
- **Relevance — 1/2 = 50%** (weight 20%). Echoed: `brezplačno`. **Missing** question keyword(s): `porabim`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj20` · Postpaid (Naj)

**Q:** Koliko GB za območje EU-tarife vključuje paket Naj C?

**Maks:**

> ✨ Paket Naj C vključuje 43,20 GB prenosa podatkov v državah območja EU-tarife. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `43,20` / `43,2`
- **Relevance — 1/2 = 50%** (weight 20%). Echoed: `tarife`. **Missing** question keyword(s): `območje`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj21` · Postpaid (Naj)

**Q:** Ali za nove naročnike paketa Naj velja 30-dnevna garancija zadovoljstva?

**Maks:**

> ✨ Da, za nove naročnike paketa Naj velja 30-dnevna garancija zadovoljstva. Če z uporabo storitve niste zadovoljni, lahko v tem obdobju odstopite od pogodbe. Več informacij najdete tukaj 👉 Garancija zadovoljstva. Potrebujete še kakšno informacijo? 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 2/2 = 100%** (weight 55%). Expected facts:
    - ✅ found: `30`
    - ✅ found: `garancij`
- **Relevance — 6/6 = 100%** (weight 20%). Echoed: `dnevna`, `garancija`, `naročnike`, `nove`, `velja`, `zadovoljstva`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj22` · Postpaid (Naj)

**Q:** Kdo velja za novega naročnika pri akcijski ponudbi paketov Naj?

**Maks:**

> ✨ Novi naročnik pri akcijski ponudbi paketov Naj je oseba, ki:
> - sklene novo naročniško razmerje (nov vklop),
> - preide s številke Mobi v naročniško razmerje, ali
> - preide od drugega operaterja (MNP).  
> 
> 
> Pomembno: Telefonska številka v zadnjih 60 dneh ne sme biti v naročniškem razmerju pri Telekomu Slovenije.

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `60 dni` / `zadnjih 60`
- **Relevance — 3/6 = 50%** (weight 20%). Echoed: `akcijski`, `paketov`, `ponudbi`. **Missing** question keyword(s): `naročnika`, `novega`, `velja`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj23` · Postpaid (Naj)

**Q:** Katera telefonska številka je za informacije o paketih Naj?

**Maks:**

> Svoje trenutne pakete preverite spodaj, v sklopu Moja razmerja 👇
> Če vas zanima, kaj vključujejo in kateri paketi so še na voljo, pa kliknite spodaj 👇

**Score: 0.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `041 700 700`
- **Relevance — 0/5 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `informacije`, `katera`, `paketih`, `telefonska`, `številka`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “preverite spodaj” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.00 + 0.15×0 + 0.10×0` = **0.000 → 0.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `naj24` · Postpaid (Naj)

**Q:** Kakšna je akcijska cena paketov Naj za nove naročnike?

**Maks:**

> ✨ Akcijska cena paketov Naj za nove naročnike je naslednja:
> 
> 
> 
> Naj A: 15,99 €/mesec (10,99 €/mesec z ugodnostjo Poveži in prihrani)
> Naj B: 15,99 €/mesec (10,99 €/mesec z ugodnostjo Poveži in prihrani)
> Naj C: 15,99 €/mesec (10,99 €/mesec z ugodnostjo Poveži in prihrani)
> 
> 
> Trajanje ugodnosti:
> - 36 mesecev ob sklenitvi v aplikaciji Moj Telekom.
> - 24 mesecev ob sklenitvi prek drugih kanalov.
> 
> 
> Po izteku ugodnosti velja redna cena. Vas zanima še kaj? 😊

**Score: 96.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `15,99` / `10,99`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `akcijska`, `naročnike`, `nove`, `paketov`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.80 + 0.15×1 + 0.10×1` = **0.960 → 96.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj25` · Postpaid (Naj)

**Q:** V kateri aplikaciji sklenem paket Naj po enotni ceni 10,99 EUR?

**Maks:**

> ✨ Paket Naj lahko sklenete v naši aplikaciji Moj Telekom. Preverite možnosti in sklenite paket hitro in enostavno. 😊 
> 
> 
> Ali potrebujete pomoč pri uporabi aplikacije Moj Telekom?

**Score: 84.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `moj telekom`
- **Relevance — 1/5 = 20%** (weight 20%). Echoed: `aplikaciji`. **Missing** question keyword(s): `ceni`, `enotni`, `kateri`, `sklenem`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.20 + 0.15×1 + 0.10×1` = **0.840 → 84.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj26` · Postpaid (Naj)

**Q:** Kakšna je hitrost oddajanja (upload) pri paketih Naj A, B in C?

**Maks:**

> ✨ Hitrost oddajanja pri paketih Naj A, Naj B in Naj C je do 200 Mbit/s. Če imate še kakšno vprašanje, kar povejte! 😊

**Score: 92.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `200 mbit`
- **Relevance — 3/5 = 60%** (weight 20%). Echoed: `hitrost`, `oddajanja`, `paketih`. **Missing** question keyword(s): `kakšna`, `upload`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.60 + 0.15×1 + 0.10×1` = **0.920 → 92.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj27` · Postpaid (Naj)

**Q:** Kakšna je hitrost prenosa do uporabnika pri paketu Naj naprava?

**Maks:**

> ✨ Hitrost prenosa podatkov pri paketu Naj naprava je do 300 Mbit/s do uporabnika in do 100 Mbit/s od uporabnika. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 96.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `300 mbit` / `300`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `hitrost`, `naprava`, `prenosa`, `uporabnika`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.80 + 0.15×1 + 0.10×1` = **0.960 → 96.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj28` · Postpaid (Naj)

**Q:** Kakšen zneskovni limit za klice velja pri paketu Naj naprava?

**Maks:**

> ✨ Pri paketu Naj Naprava velja zneskovni limit za klice v vsa slovenska omrežja in odhodne klice znotraj držav območja EU-tarife v višini 10 EUR mesečno. 
> 
> 
> 
> Do tega limita se klici obračunavajo po ceniku paketa.
> Po dosegu limita so klici brezplačni. 
> 
> 
> Vam lahko še kako pomagam? 😊

**Score: 96.7/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `10 eur` / `10 €` / `do 10`
- **Relevance — 5/6 = 83%** (weight 20%). Echoed: `klice`, `limit`, `naprava`, `velja`, `zneskovni`. **Missing** question keyword(s): `kakšen`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.83 + 0.15×1 + 0.10×1` = **0.967 → 96.7/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj29` · Postpaid (Naj)

**Q:** Koliko sporočil SMS vključuje paket Naj naprava?

**Maks:**

> ✨ Paket Naj Naprava vključuje 500 sporočil SMS/MMS v Sloveniji ali državah območja EU-tarife. 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `500`
- **Relevance — 2/2 = 100%** (weight 20%). Echoed: `naprava`, `sporočil`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj30` · Postpaid (Naj)

**Q:** Koliko stane dodatna storitev Ena številka na mesec?

**Maks:**

> ✨ Cena dodatne storitve Ena številka znaša 1 EUR na mesec in se zaračunava le nosilni številki. Dodatne številke imajo storitev na voljo brezplačno. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `1 eur` / `1,00` / `1 €`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `storitev`, `številka`. **Missing** question keyword(s): `dodatna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “1 eur”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj31` · Postpaid (Naj)

**Q:** Koliko telefonskih številk lahko združim s storitvijo Ena številka?

**Maks:**

> ✨ S storitvijo Ena številka lahko združite do tri telefonske številke: eno nosilno in dve dodatni. Vse naprave zvonijo ob klicu na izbrano številko, klic pa prevzamete na kateri koli povezani napravi. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 73.0/100  (★★★★☆)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `3` / `tri`
- **Relevance — 2/5 = 40%** (weight 20%). Echoed: `storitvijo`, `številka`. **Missing** question keyword(s): `telefonskih`, `združim`, `številk`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.40 + 0.15×0 + 0.10×1` = **0.730 → 73.0/100**.
- **Verdict:** Partial: some but not all expected facts were stated.

---

### `naj32` · Postpaid (Naj)

**Q:** Kolikšna je priključna taksa za storitev Ena številka?

**Maks:**

> ✨ Priključna taksa za storitev Ena številka znaša 10,95 EUR z DDV. Če potrebujete še dodatne informacije, mi prosim sporočite 😊

**Score: 31.0/100  (★★☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `brezplač`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `priključna`, `storitev`, `taksa`, `številka`. **Missing** question keyword(s): `kolikšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “10.95 eur”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “prosim sporočite” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.80 + 0.15×1 + 0.10×0` = **0.310 → 31.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `naj33` · Postpaid (Naj)

**Q:** Koliko stane mesečna naročnina storitve SIM 2 (Brezskrbni)?

**Maks:**

> ✨ Mesečna naročnina za storitev SIM 2 Brezskrbni znaša 4,99 €. Če potrebujete dodatne informacije, sem tukaj za vas! 😊

**Score: 40.0/100  (★★★☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `11,99` / `14,99`
- **Relevance — 3/4 = 75%** (weight 20%). Echoed: `brezskrbni`, `mesečna`, `naročnina`. **Missing** question keyword(s): `storitve`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “4.99 eur”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×0.00 + 0.20×0.75 + 0.15×1 + 0.10×1` = **0.400 → 40.0/100**.
- **Verdict:** Risky: Maks answered confidently with a specific value that does **not** match the site — a candidate factual error.

---

### `naj34` · Postpaid (Naj)

**Q:** Kolikšna je priključna taksa za storitev SIM 2?

**Maks:**

> ✨ Priključna taksa za storitev SIM 2 znaša 10,95 EUR z DDV. Če preklopite obstoječi mobilni paket na enega izmed podprtih paketov, se sprememba paketa ne zaračuna. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 95.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `10,95`
- **Relevance — 3/4 = 75%** (weight 20%). Echoed: `priključna`, `storitev`, `taksa`. **Missing** question keyword(s): `kolikšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “10.95 eur”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.75 + 0.15×1 + 0.10×1` = **0.950 → 95.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj35` · Postpaid (Naj)

**Q:** Koliko prenosa podatkov vključuje storitev SIM 2?

**Maks:**

> ✨ Storitev SIM 2 uporablja zakupljene količine prenosa podatkov vašega osnovnega mobilnega paketa (npr. Naj A, Naj B, Naj C). Sama SIM 2 ne vključuje dodatnih količin, temveč deli podatke s primarno številko. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 45.0/100  (★★★☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `100 mb`
- **Relevance — 3/3 = 100%** (weight 20%). Echoed: `podatkov`, `prenosa`, `storitev`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×0.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **0.450 → 45.0/100**.
- **Verdict:** Risky: Maks answered confidently with a specific value that does **not** match the site — a candidate factual error.

---

### `naj36` · Postpaid (Naj)

**Q:** Koliko stane storitev Varen splet na mesec?

**Maks:**

> ✨ Storitev Varen splet je na voljo že od 0,99 € na mesec. Za zaščito celotnega omrežja je cena 1,49 € na mesec, za zaščito mobilne naprave ali Mobi pa 0,99 € na mesec. Prva dva meseca je za naročnike brezplačna (ne velja za Mobi). Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `0,99`
- **Relevance — 3/3 = 100%** (weight 20%). Echoed: `splet`, `storitev`, `varen`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “0.99 eur”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj37` · Postpaid (Naj)

**Q:** Koliko stane zavarovanje naprave, vredne med 401 in 600 EUR (paket Premium)?

**Maks:**

> ✨ Mesečna premija za zavarovanje naprave v vrednosti med 401 in 600 EUR v paketu Premium znaša 7,45 EUR. Soudeležba zavarovanca ob škodnem primeru je 60 EUR.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 95.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `7,45`
- **Relevance — 3/4 = 75%** (weight 20%). Echoed: `naprave`, `premium`, `zavarovanje`. **Missing** question keyword(s): `vredne`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “600 eur”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.75 + 0.15×1 + 0.10×1` = **0.950 → 95.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj38` · Postpaid (Naj)

**Q:** Koliko stane zavarovanje najdražjih naprav (1001–3000 EUR, Premium)?

**Maks:**

> ✨ Mesečna premija za Premium paket zavarovanja naprav z redno ceno med 1001 in 3000 EUR znaša 14,95 EUR. Soudeležba zavarovanca pri škodnem primeru je 110 EUR. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `14,95`
- **Relevance — 4/6 = 67%** (weight 20%). Echoed: `1001`, `3000`, `naprav`, `premium`. **Missing** question keyword(s): `najdražjih`, `zavarovanje`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “3000 eur”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj39` · Postpaid (Naj)

**Q:** Koliko stane zavarovanje pametne ure na mesec?

**Maks:**

> ✨ Zavarovanje pametne ure pri nas stane 2 € na mesec. Vključuje kritje za nenamerne poškodbe, tatvino, vlom, rop in podaljšano jamstvo. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `2 eur` / `2,00` / `2 €`
- **Relevance — 2/2 = 100%** (weight 20%). Echoed: `pametne`, `zavarovanje`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “2 eur”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj40` · Postpaid (Naj)

**Q:** Koliko stane zavarovanje tablice ali prenosnika do 400 EUR?

**Maks:**

> ✨ Zavarovanje tablice ali prenosnika do 400 EUR stane 2 EUR na mesec. Soudeležba zavarovanca ob škodnem primeru znaša 40 EUR. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `2 eur` / `2,00` / `2 €`
- **Relevance — 3/3 = 100%** (weight 20%). Echoed: `prenosnika`, `tablice`, `zavarovanje`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “400 eur”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj41` · Postpaid (Naj)

**Q:** Kolikšen popust prinaša ugodnost Poveži in prihrani?

**Maks:**

> ✨ Ugodnost Poveži in prihrani prinaša:
> 
> 
> 
> 5 EUR popusta na mesečno naročnino pri paketih Naj A, Naj B, Naj C, Naj 5G in Naj Net.
> 15 EUR popusta na fiksni paket Net, če ste naročnik paketa SUPR.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `5 eur`
- **Relevance — 4/6 = 67%** (weight 20%). Echoed: `poveži`, `prihrani`, `prinaša`, `ugodnost`. **Missing** question keyword(s): `kolikšen`, `popust`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “5 eur”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj42` · Postpaid (Naj)

**Q:** Po koliko GB lahko naenkrat največ delim z Delim GB?

**Maks:**

> ✨ Največja količina, ki jo lahko naenkrat delite z Delim GB, je 50 GB. Na voljo so količine 5, 10, 20 ali 50 GB. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `50 gb`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `delim`, `naenkrat`. **Missing** question keyword(s): `največ`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj43` · Postpaid (Naj)

**Q:** Na katero številko pošljem SMS DELIM za deljenje gigabajtov?

**Maks:**

> ✨ SMS za deljenje gigabajtov pošljete na številko 1918. V sporočilo napišite: DELIM XGB ŠTEVILKA PREJEMNIKA (npr. DELIM 5GB 041700700). Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `1918`
- **Relevance — 4/6 = 67%** (weight 20%). Echoed: `delim`, `deljenje`, `gigabajtov`, `številko`. **Missing** question keyword(s): `katero`, `pošljem`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “5gb”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj44` · Postpaid (Naj)

**Q:** Koliko dodatnih razmerij Druga številka omogoča paket Naj B?

**Maks:**

> ✨ Paket Naj B omogoča eno dodatno razmerje Druga številka. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 92.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `1` / `eno` / `ena`
- **Relevance — 3/5 = 60%** (weight 20%). Echoed: `druga`, `omogoča`, `številka`. **Missing** question keyword(s): `dodatnih`, `razmerij`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.60 + 0.15×1 + 0.10×1` = **0.920 → 92.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj45` · Postpaid (Naj)

**Q:** Koliko dodatnih razmerij Druga številka omogoča paket Naj C?

**Maks:**

> ✨ Paket Naj C omogoča do 4 dodatna razmerja Druga številka. Vsaka Druga številka ima svojo SIM-kartico in mobilno številko ter koristi količine osnovnega naročniškega razmerja. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 92.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `4` / `štiri`
- **Relevance — 3/5 = 60%** (weight 20%). Echoed: `druga`, `omogoča`, `številka`. **Missing** question keyword(s): `dodatnih`, `razmerij`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.60 + 0.15×1 + 0.10×1` = **0.920 → 92.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj46` · Postpaid (Naj)

**Q:** Koliko GB v EU-tarifi lahko brezplačno porabim s paketom Naj B?

**Maks:**

> ✨ S paketom Naj B lahko v državah EU brez dodatnih stroškov porabite 13 GB podatkov. Če presežete to količino, se dodatna poraba zaračuna po veljavnem ceniku.
> 
> 
> Vas zanima še kaj glede vašega paketa? 😊

**Score: 30.0/100  (★★☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `41,71`
- **Relevance — 1/4 = 25%** (weight 20%). Echoed: `paketom`. **Missing** question keyword(s): `brezplačno`, `porabim`, `tarifi`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×0.00 + 0.20×0.25 + 0.15×1 + 0.10×1` = **0.300 → 30.0/100**.
- **Verdict:** Risky: Maks answered confidently with a specific value that does **not** match the site — a candidate factual error.

---

### `naj47` · Postpaid (Naj)

**Q:** Koliko GB za območje EU-tarife vključuje paket Naj C?

**Maks:**

> ✨ Paket Naj C vključuje 43,20 GB prenosa podatkov v državah območja EU-tarife. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `43,20` / `43,2`
- **Relevance — 1/2 = 50%** (weight 20%). Echoed: `tarife`. **Missing** question keyword(s): `območje`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj48` · Postpaid (Naj)

**Q:** Kolikšen dodatek se zaračuna za SMS iz Slovenije v tuja omrežja?

**Maks:**

> Cene klicev iz fiksne telefonije lahko preverite spodaj 👇
> Obračun mobilnih klicev in SMS-ov je odvisen od območja, kjer se nahajate. Mi poveste, kje nameravate opraviti klic ali poslati sporočilo?

**Score: 15.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `0,11`
- **Relevance — 0/6 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `dodatek`, `kolikšen`, `omrežja`, `slovenije`, `tuja`, `zaračuna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “preverite spodaj” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.00 + 0.15×1 + 0.10×0` = **0.150 → 15.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `naj49` · Postpaid (Naj)

**Q:** Kakšna je akcijska cena paketov Naj za nove naročnike?

**Maks:**

> ✨ Akcijska cena paketov Naj za nove naročnike je naslednja:
> - Naj A: 15,99 €/mesec (10,99 € z ugodnostjo Poveži in prihrani).
> - Naj B: 15,99 €/mesec (10,99 € z ugodnostjo Poveži in prihrani).
> - Naj C: 15,99 €/mesec (10,99 € z ugodnostjo Poveži in prihrani).  
> 
> 
> Trajanje ugodnosti:
> - 36 mesecev ob sklenitvi v aplikaciji Moj Telekom.
> - 24 mesecev ob sklenitvi prek drugih kanalov.  
> 
> 
> Po izteku velja redna cena. 😊

**Score: 96.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `15,99` / `10,99`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `akcijska`, `naročnike`, `nove`, `paketov`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.80 + 0.15×1 + 0.10×1` = **0.960 → 96.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj50` · Postpaid (Naj)

**Q:** Katera je telefonska številka za informacije o paketih Naj?

**Maks:**

> Svoje trenutne pakete preverite spodaj, v sklopu Moja razmerja 👇
> Če vas zanima, kaj vključujejo in kateri paketi so še na voljo, pa kliknite spodaj 👇

**Score: 0.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `041 700 700`
- **Relevance — 0/5 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `informacije`, `katera`, `paketih`, `telefonska`, `številka`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “preverite spodaj” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.00 + 0.15×0 + 0.10×0` = **0.000 → 0.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `naj51` · Postpaid (Naj)

**Q:** Na kateri e-naslov lahko pišem za informacije o ponudbi?

**Maks:**

> Elektronski naslov Telekoma Slovenije je info@telekom.si.

**Score: 69.0/100  (★★★★☆)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `info@telekom.si`
- **Relevance — 1/5 = 20%** (weight 20%). Echoed: `naslov`. **Missing** question keyword(s): `informacije`, `kateri`, `pišem`, `ponudbi`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.20 + 0.15×0 + 0.10×1` = **0.690 → 69.0/100**.
- **Verdict:** Partial: some but not all expected facts were stated.

---

### `naj52` · Postpaid (Naj)

**Q:** Koliko časa velja enotna akcijska cena Naj v aplikaciji Moj Telekom?

**Maks:**

> ✨ Akcijska cena paketa Naj v aplikaciji Moj Telekom velja do preklica ali do konca promocijskega obdobja, ki je določeno v pogojih akcije. Za točne informacije preverite podrobnosti v aplikaciji Moj Telekom ali na naši spletni strani. 
> 
> 
> Vam lahko še kako pomagam? 😊

**Score: 28.3/100  (★★☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `3 leta` / `tri leta`
- **Relevance — 4/6 = 67%** (weight 20%). Echoed: `akcijska`, `aplikaciji`, `telekom`, `velja`. **Missing** question keyword(s): `enotna`, `časa`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “za točne informacije” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.67 + 0.15×1 + 0.10×0` = **0.283 → 28.3/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `naj53` · Postpaid (Naj)

**Q:** Ali lahko paket Naj sklenem z eSIM?

**Maks:**

> ✨ Da, paket Naj lahko sklenete tudi z eSIM, če vaša naprava podpira eSIM. Ob sklenitvi naročniškega razmerja izberite eSIM in prejeli boste QR-kodo za aktivacijo. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `esim`
- **Relevance — 1/2 = 50%** (weight 20%). Echoed: `esim`. **Missing** question keyword(s): `sklenem`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj54` · Postpaid (Naj)

**Q:** Kako se imenuje zakup za neomejene podatke na Hrvaškem?

**Maks:**

> ✨ Za neomejene podatke na Hrvaškem sta na voljo naslednja zakupa:
> 
> 
> 
> HR-internet neomejeno:
> 
> 
> 
> Cena: 9,94 €/mesec
> Prenos podatkov: neomejeno (po 30 GB hitrost do 2/1 Mbit/s)
> Veljavnost: do preklica
> Aktivacija: SMS s ključno besedo HR INTERNET na 1918 (naročniki) ali 1917 (Mobi)
> 
> HR-internet Plus:
> 
> 
> 
> Cena: 5,99 €
> Prenos podatkov: neomejeno (po 20 GB hitrost do 2/1 Mbit/s)
> Veljavnost: 7 dni
> Aktivacija: SMS s ključno besedo HR PLUS na 1918 (naročniki) ali 1917 (Mobi)
> 
> 
> 
> Več informacij 👉 HR-internet.

**Score: 92.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `hr-internet` / `hr internet` / `hrvaš`
- **Relevance — 3/5 = 60%** (weight 20%). Echoed: `hrvaškem`, `neomejene`, `podatke`. **Missing** question keyword(s): `imenuje`, `zakup`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.60 + 0.15×1 + 0.10×1` = **0.920 → 92.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj55` · Postpaid (Naj)

**Q:** Katere države pokriva zakup Balkan?

**Maks:**

> ✨ Zakup Balkan velja v naslednjih državah:
> - Bosna in Hercegovina
> - Srbija
> - Črna gora
> - Severna Makedonija
> - Kosovo
> - Albanija
> 
> 
> Vas zanima več o posameznih zakupih? 😊

**Score: 73.0/100  (★★★★☆)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `bosn` / `srbij` / `kosov` / `makedonij` / `črn` / `albanij`
- **Relevance — 2/5 = 40%** (weight 20%). Echoed: `balkan`, `zakup`. **Missing** question keyword(s): `države`, `katere`, `pokriva`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.40 + 0.15×0 + 0.10×1` = **0.730 → 73.0/100**.
- **Verdict:** Partial: some but not all expected facts were stated.

---

### `naj56` · Postpaid (Naj)

**Q:** Ali je na voljo zakup neomejenih podatkov za ZDA?

**Maks:**

> ✨ Da, za ZDA so na voljo naslednji zakupi:
> 
> 
> 
> ZDA, ZK in Švica - internet neomejeno:
> 
> 
> 
> Cena: 15,99 €/mesec
> Prenos podatkov: neomejeno (po 10 GB hitrost do 2/1 Mbit/s)
> Aktivacija: SMS s ključno besedo ZDA NEOMEJENO na 1918 (naročniki) ali 1917 (Mobi).
> 
> ZDA, ZK in Švica - internet:
> 
> 
> 
> Cena: 12,00 €
> Prenos podatkov: 10 GB
> Veljavnost: 7 dni
> Aktivacija: SMS s ključno besedo ZDA INTERNET na 1918 (naročniki) ali 1917 (Mobi).
> 
> ZDA, ZK in Švica - 7:
> 
> 
> 
> Cena: 9,90 €
> Prenos podatkov: 1 GB + 500 enot (klici/SMS)
> Veljavnost: 7 dni
> Aktivacija: SMS s ključno besedo ZDA 7 na 1918 (naročniki).
> 
> 
> 
> Več informacij 👉 Zakupi za ZDA, ZK in Švico.

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `zda` / `neomejen`
- **Relevance — 2/4 = 50%** (weight 20%). Echoed: `podatkov`, `voljo`. **Missing** question keyword(s): `neomejenih`, `zakup`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj57` · Postpaid (Naj)

**Q:** Na kakšno hitrost pade prenos po limitu pri paketih Naj B in Naj C?

**Maks:**

> ✨ Pri paketih Naj B in Naj C se hitrost prenosa podatkov po preseženem mesečnem vključku zmanjša na 64 kbps za prenos v Sloveniji. Če potrebujete več informacij ali dodatne opcije za povečanje hitrosti, mi sporočite! 😊

**Score: 35.0/100  (★★☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `2/1` / `2 mbit` / `2 mbit/s`
- **Relevance — 3/6 = 50%** (weight 20%). Echoed: `hitrost`, `paketih`, `prenos`. **Missing** question keyword(s): `kakšno`, `limitu`, `pade`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×0.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.350 → 35.0/100**.
- **Verdict:** Risky: Maks answered confidently with a specific value that does **not** match the site — a candidate factual error.

---

### `naj58` · Postpaid (Naj)

**Q:** Ali paketi Naj vključujejo neomejene klice v vsa slovenska omrežja?

**Maks:**

> ✨ Paketi Naj vključujejo neomejene klice v vsa slovenska omrežja. Če potrebujete dodatne informacije o paketih ali dodatnih storitvah, sem vam na voljo. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `neomejen`
- **Relevance — 6/6 = 100%** (weight 20%). Echoed: `klice`, `neomejene`, `omrežja`, `paketi`, `slovenska`, `vključujejo`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj59` · Postpaid (Naj)

**Q:** Ali imam pri paketih Naj neomejene SMS in MMS v Sloveniji?

**Maks:**

> ✨ Da, pri naših paketih Naj so neomejeni SMS in MMS v Sloveniji vključeni v mesečno naročnino. Pošiljate jih lahko brez dodatnih stroškov znotraj Slovenije. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `neomejen`
- **Relevance — 2/4 = 50%** (weight 20%). Echoed: `paketih`, `sloveniji`. **Missing** question keyword(s): `imam`, `neomejene`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj60` · Postpaid (Naj)

**Q:** Kolikšna je priključna taksa ob sklenitvi paketa Naj?

**Maks:**

> Ali vas zanima priključna taksa za mobilni paket📱ali paket s televizijo in internetom 🏠?

**Score: 25.0/100  (★★☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `10,95`
- **Relevance — 2/4 = 50%** (weight 20%). Echoed: `priključna`, `taksa`. **Missing** question keyword(s): `kolikšna`, `sklenitvi`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “ali vas zanima” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.50 + 0.15×1 + 0.10×0` = **0.250 → 25.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `naj61` · Postpaid (Naj)

**Q:** Ali je za nove naročnike Naj na voljo garancija zadovoljstva?

**Maks:**

> ✨ Da, za nove naročnike paketov Naj je na voljo garancija zadovoljstva. V 30 dneh od vklopa lahko odstopite od pogodbe brez poplačila pogodbene obveznosti (razen za subvencionirane naprave). Več informacij in obrazec najdete tukaj 👉 Garancija zadovoljstva. 
> 
> 
> Potrebujete še kakšno informacijo? 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `30` / `garancij`
- **Relevance — 5/5 = 100%** (weight 20%). Echoed: `garancija`, `naročnike`, `nove`, `voljo`, `zadovoljstva`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj62` · Postpaid (Naj)

**Q:** Koliko podatkov (GB) vključuje paket Naj A?

**Maks:**

> ✨ Paket Naj A vključuje 20 GB prenosa podatkov, od tega lahko v državah območja EU-tarife brezplačno porabite do 20 GB.

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `20 gb`
- **Relevance — 1/1 = 100%** (weight 20%). Echoed: `podatkov`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj63` · Postpaid (Naj)

**Q:** Ali je prenos podatkov pri paketu Naj B neomejen?

**Maks:**

> ✨ Da, prenos podatkov pri paketu Naj B je neomejen. Po doseženih 200 GB v obračunskem obdobju se hitrost zniža na 2/1 Mbit/s.

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `neomejen`
- **Relevance — 3/3 = 100%** (weight 20%). Echoed: `neomejen`, `podatkov`, `prenos`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj64` · Postpaid (Naj)

**Q:** V katerih državah velja EU-tarifa (naštej nekaj)?

**Maks:**

> ✨ EU-tarifa velja v naslednjih državah: Avstrija, Belgija, Hrvaška, Italija, Nemčija, Španija, Švedska, Norveška, Islandija, Ukrajina in še več. Celoten seznam najdete tukaj. 
> 
> 
> Potrebujete še kakšno informacijo? 😊

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `avstrij` / `hrvaš` / `nemčij` / `italij` / `francij`
- **Relevance — 3/6 = 50%** (weight 20%). Echoed: `državah`, `tarifa`, `velja`. **Missing** question keyword(s): `katerih`, `naštej`, `nekaj`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj65` · Postpaid (Naj)

**Q:** Kje lahko spremenim naročniški paket Naj?

**Maks:**

> Da bom lažje našel najboljšo rešitev, mi povejte, ali želite spremeniti mobilni paket 📱 ali paket s televizijo in internetom 🏠

**Score: 15.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/2 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `moj telekom` / `mojem telekomu`
    - ❌ missing: `041 700 700` / `prodajn`
- **Relevance — 0/2 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `naročniški`, `spremenim`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “mi povejte” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.00 + 0.15×1 + 0.10×0` = **0.150 → 15.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `naj66` · Postpaid (Naj)

**Q:** Ali paketi Naj delujejo v omrežju 5G?

**Maks:**

> ✨ Paketi Naj delujejo v omrežju 5G, ki pokriva 99 % prebivalstva. Za podrobnosti o pokritosti si lahko ogledate našo uradno stran:
> 
> 
> https://www.telekom.si/mobilno/pokritost-mobilnega-omrezja
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `5g`
- **Relevance — 3/3 = 100%** (weight 20%). Echoed: `delujejo`, `omrežju`, `paketi`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj67` · Postpaid (Naj)

**Q:** Kakšna je hitrost oddajanja (upload) pri paketu Naj naprava?

**Maks:**

> ✨ Pri paketu Naj naprava je hitrost oddajanja (upload) do 100 Mbit/s. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 96.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `100 mbit` / `100`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `hitrost`, `naprava`, `oddajanja`, `upload`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.80 + 0.15×1 + 0.10×1` = **0.960 → 96.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj68` · Postpaid (Naj)

**Q:** Koliko GB podatkov vključuje paket Naj naprava?

**Maks:**

> ✨ Paket Naj Naprava vključuje 1 GB prenosa podatkov, ki ga lahko porabite v Sloveniji ali državah območja EU-tarife. 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `1 gb`
- **Relevance — 2/2 = 100%** (weight 20%). Echoed: `naprava`, `podatkov`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj69` · Postpaid (Naj)

**Q:** Za koga velja popust Penzion?

**Maks:**

> ✨ Popust Penzion velja za upokojence oziroma osebe, starejše od 60 let. Popusti za študente, upokojence oz. starejše od 60 let (ugodnost Penzion), invalide, člane AMZS, nogometaše in obrtnike se ne seštevajo – uveljavljate lahko le en popust.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 80.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `upokojen` / `starej` / `penzion`
- **Relevance — 3/4 = 75%** (weight 20%). Echoed: `penzion`, `popust`, `velja`. **Missing** question keyword(s): `koga`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.75 + 0.15×0 + 0.10×1` = **0.800 → 80.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj70` · Postpaid (Naj)

**Q:** Ali lahko z Delim GB delim gigabajte tudi uporabnikom Mobi?

**Maks:**

> ✨ Da, z Delim GB lahko naročniki izbranih mobilnih paketov Telekoma Slovenije delite gigabajte tudi uporabnikom Mobi. Prejemnik mora biti uporabnik Mobi ali naročnik mobilnih storitev pri Telekomu Slovenije. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `mobi` / `predplač` / `da`
- **Relevance — 4/4 = 100%** (weight 20%). Echoed: `delim`, `gigabajte`, `mobi`, `uporabnikom`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj71` · Postpaid (Naj)

**Q:** Kakšna je najvišja hitrost prenosa do uporabnika pri paketih Naj?

**Maks:**

> ✨ Najvišja hitrost prenosa do uporabnika pri paketih Naj je odvisna od tehnologije:
> 
> 
> 
> VDSL: do 80 Mbit/s
> FTTH (optika): do 1 Gbit/s ali 2 Gbit/s (z doplačilom)
> 
> 
> Za nadgradnje hitrosti preverite 👉 več tukaj.

**Score: 96.7/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `1 gbit` / `gbit`
- **Relevance — 5/6 = 83%** (weight 20%). Echoed: `hitrost`, `najvišja`, `paketih`, `prenosa`, `uporabnika`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.83 + 0.15×1 + 0.10×1` = **0.967 → 96.7/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj72` · Postpaid (Naj)

**Q:** Ali storitev Ena številka zahteva vključen VoLTE?

**Maks:**

> ✨ Storitev VoLTE omogoča klicanje in pošiljanje sporočil prek omrežja 4G/5G. Če želite izvedeti, ali je VoLTE že vključen za vašo številko ali kako ga vključiti, mi prosim sporočite, ali želite navodila za vklop? Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 77.0/100  (★★★★☆)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `volte`
- **Relevance — 3/5 = 60%** (weight 20%). Echoed: `storitev`, `vključen`, `volte`. **Missing** question keyword(s): `zahteva`, `številka`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — no** (weight 10% → 1) (a redirect phrase “prosim sporočite” is present, but fact recall ≥ 34%, so it is *not* treated as a deflection).
- **Weighted total:** `0.55×1.00 + 0.20×0.60 + 0.15×0 + 0.10×1` = **0.770 → 77.0/100**.
- **Verdict:** Partial: some but not all expected facts were stated.

---

### `naj73` · Postpaid (Naj)

**Q:** Koliko stane zavarovanje naprave med 801 in 1000 EUR (Premium)?

**Maks:**

> ✨ Mesečna premija za zavarovanje naprave v vrednosti med 801 in 1000 EUR v paketu Premium znaša 10,95 EUR. Če potrebujete ceno za višji znesek, prosim navedite točen znesek naprave. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `10,95`
- **Relevance — 4/4 = 100%** (weight 20%). Echoed: `1000`, `naprave`, `premium`, `zavarovanje`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “1000 eur”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `naj74` · Postpaid (Naj)

**Q:** Kolikšna je cena minute klica iz Slovenije v EU po ceniku (Naj naprava)?

**Maks:**

> Klici iz domačega omrežja v tujino niso vključeni v vaš paket. Cenik za tujino in seznam držav po območjih najdete spodaj 👇
> Predlagam vam, da izberete ustrezen zakup in tako ugodneje kličete v tujino. Povejte mi, ali želite zakup za mobilno 📱 ali fiksno 🏠 številko.

**Score: 15.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `0,23` / `0,2318` / `0,19`
- **Relevance — 0/6 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `ceniku`, `klica`, `kolikšna`, `minute`, `naprava`, `slovenije`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “najdete spodaj” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.00 + 0.15×1 + 0.10×0` = **0.150 → 15.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `naj75` · Postpaid (Naj)

**Q:** Kolikšna je redna mesečna cena paketa Naj C?

**Maks:**

> ✨ Redna mesečna cena paketa Naj C znaša 28,99 €. Če potrebujete dodatne informacije, sem tukaj za vas! 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `28,99`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `mesečna`, `redna`. **Missing** question keyword(s): `kolikšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---


## Broadband

### `bb01` · Broadband

**Q:** Kakšna je najvišja hitrost optičnega interneta pri paketih NEO?

**Maks:**

> ✨ Najlepša hvala za vprašanje! Pri paketih NEO gre za internet in TV storitve. 
> 
> 
> Ali vas zanima več o teh paketih? Če želite, lahko preverim podrobnosti za vas 🏠.

**Score: 18.3/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `1 gbit` / `gbit`
- **Relevance — 1/6 = 17%** (weight 20%). Echoed: `paketih`. **Missing** question keyword(s): `hitrost`, `interneta`, `kakšna`, `najvišja`, `optičnega`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “ali vas zanima” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.17 + 0.15×1 + 0.10×0` = **0.183 → 18.3/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb02` · Broadband

**Q:** Do katere hitrosti lahko nadgradim optični internet NEO?

**Maks:**

> ✨ Optični internet v paketu NEO lahko nadgradite do hitrosti 5 Gbit/s. Na voljo so naslednje možnosti nadgradnje:
> 
> 
> 
> do 1 Gbit/s / 300 Mbit/s (doplačilo 10 €/mesec)
> do 2 Gbit/s / 100 Mbit/s (doplačilo 15 €/mesec)
> do 5 Gbit/s / 1 Gbit/s (doplačilo 99 €/mesec)
> do 5 Gbit/s / 5 Gbit/s (na NEO A, doplačilo 499 €/mesec)
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 92.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `5 gbit`
- **Relevance — 3/5 = 60%** (weight 20%). Echoed: `hitrosti`, `internet`, `optični`. **Missing** question keyword(s): `katere`, `nadgradim`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.60 + 0.15×1 + 0.10×1` = **0.920 → 92.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb03` · Broadband

**Q:** Koliko stane paket Net (samo internet) na mesec?

**Maks:**

> Da bom lažje našel najboljšo rešitev, mi povejte, ali se zanimate za fiksni 🏠 ali mobilni 📱 internet.

**Score: 25.0/100  (★★☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `39 eur` / `39,00` / `39 €`
- **Relevance — 1/2 = 50%** (weight 20%). Echoed: `internet`. **Missing** question keyword(s): `samo`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “mi povejte” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.50 + 0.15×1 + 0.10×0` = **0.250 → 25.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb04` · Broadband

**Q:** Kakšna je hitrost internetnega paketa Net na optiki?

**Maks:**

> Hitrost interneta, ki je vključena v vašem paketu, lahko preverite spodaj 👇
> 💡 Če dostopa do Mojega Telekoma še nimate, si ga čim prej zagotovite. Moj Telekom vam omogoča, da vsa svoja razmerja urejate sami 👇

**Score: 5.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `1 gbit` / `gbit`
- **Relevance — 1/4 = 25%** (weight 20%). Echoed: `hitrost`. **Missing** question keyword(s): `internetnega`, `kakšna`, `optiki`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “preverite spodaj” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.25 + 0.15×0 + 0.10×0` = **0.050 → 5.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb05` · Broadband

**Q:** Koliko stane fiksni paket Naj Net na mesec?

**Maks:**

> ✨ Paket Naj Net je mobilni internet in ni fiksni paket. Cena je 13,99 EUR/mesec, vključuje neomejen prenos podatkov v omrežju Telekoma Slovenije (hitrost do 2/1 Mbit/s). Možna je nadgradnja hitrosti. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `13,99`
- **Relevance — 1/1 = 100%** (weight 20%). Echoed: `fiksni`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb06` · Broadband

**Q:** Kakšna je akcijska cena fiksnih paketov NEO ob 24-mesečni vezavi?

**Maks:**

> ✨ Na voljo so različni akcijski paketi NEO ob 24-mesečni vezavi, odvisno od vaših potreb (internet, TV, telefonija). 
> 
> 
> Za točne cene in podrobnosti priporočam, da preverite našo aktualno ponudbo na 👉 NEO paketi. Če želite, vas lahko povežem tudi z mojim sodelavcem za dodatne informacije. Bi to želeli? 😊

**Score: 21.7/100  (★★☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `32,99`
- **Relevance — 2/6 = 33%** (weight 20%). Echoed: `mesečni`, `vezavi`. **Missing** question keyword(s): `akcijska`, `fiksnih`, `kakšna`, `paketov`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “priporočam, da preverite” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.33 + 0.15×1 + 0.10×0` = **0.217 → 21.7/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb07` · Broadband

**Q:** Kaj lahko naredim, če na mojem naslovu še ni optike?

**Maks:**

> Pokritost optičnega omrežja na želeni lokaciji preverite spodaj 👇
> Za dodatne informacije o optičnem omrežju ali oddajo naročila vas lahko povežem s sodelavcem 🤝💬
> Želite, da vas povežem s sodelavcem?

**Score: 0.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `neo 5g` / `5g`
- **Relevance — 0/4 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `mojem`, `naredim`, `naslovu`, `optike`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “vas povežem s sodelavcem” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.00 + 0.15×0 + 0.10×0` = **0.000 → 0.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb08` · Broadband

**Q:** Kako preverim, ali je na mojem naslovu na voljo optika?

**Maks:**

> Pokritost optičnega omrežja na želeni lokaciji preverite spodaj 👇
> Za dodatne informacije o optičnem omrežju ali oddajo naročila vas lahko povežem s sodelavcem 🤝💬
> Želite, da vas povežem s sodelavcem?

**Score: 65.0/100  (★★★★☆)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `naslov` / `lokacij`
- **Relevance — 0/5 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `mojem`, `naslovu`, `optika`, `preverim`, `voljo`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — no** (weight 10% → 1) (a redirect phrase “vas povežem s sodelavcem” is present, but fact recall ≥ 34%, so it is *not* treated as a deflection).
- **Weighted total:** `0.55×1.00 + 0.20×0.00 + 0.15×0 + 0.10×1` = **0.650 → 65.0/100**.
- **Verdict:** Partial: some but not all expected facts were stated.

---

### `bb09` · Broadband

**Q:** Ali je priklop optike lahko brezplačen?

**Maks:**

> Podatkov o statusu gradnje nimam, ampak brez skrbi, lahko vas povežem s sodelavcem 🏗️🚧
> Želite, da vas povežem s sodelavcem?

**Score: 0.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `brezplač`
- **Relevance — 0/3 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `brezplačen`, `optike`, `priklop`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “podatkov o statusu” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.00 + 0.15×0 + 0.10×0` = **0.000 → 0.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb10` · Broadband

**Q:** Za koliko gospodinjstev bo optika priključena brezplačno?

**Maks:**

> Podatkov o statusu gradnje nimam, ampak brez skrbi, lahko vas povežem s sodelavcem 🏗️🚧
> Želite, da vas povežem s sodelavcem?

**Score: 0.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `250.000` / `250000` / `250 000`
- **Relevance — 0/4 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `brezplačno`, `gospodinjstev`, `optika`, `priključena`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “podatkov o statusu” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.00 + 0.15×0 + 0.10×0` = **0.000 → 0.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb11` · Broadband

**Q:** Katere tehnologije za dostop do interneta ponuja Telekom?

**Maks:**

> ✨ Telekom Slovenije ponuja več tehnologij za dostop do interneta:
> 
> 
> 
> Optično omrežje (FTTH): omogoča hitrosti do 10 Gbit/s.
> Mobilno omrežje (4G/5G): za internet tam, kjer ni druge možnosti.
> Bakrena omrežja (xDSL): na območjih, kjer optika še ni na voljo.
> 
> 
> Vas zanima več o kateri izmed teh tehnologij? Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 2/2 = 100%** (weight 55%). Expected facts:
    - ✅ found: `optik` / `ftth`
    - ✅ found: `vdsl` / `adsl` / `lte` / `5g`
- **Relevance — 4/6 = 67%** (weight 20%). Echoed: `dostop`, `interneta`, `ponuja`, `telekom`. **Missing** question keyword(s): `katere`, `tehnologije`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “10 gb”).
- **Deflection — no** (weight 10% → 1) (a redirect phrase “o kateri” is present, but fact recall ≥ 34%, so it is *not* treated as a deflection).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb12` · Broadband

**Q:** Kakšna je hitrost do uporabnika pri paketu NEO A na optiki?

**Maks:**

> Hitrost interneta, ki je vključena v vašem paketu, lahko preverite spodaj 👇
> 💡 Če dostopa do Mojega Telekoma še nimate, si ga čim prej zagotovite. Moj Telekom vam omogoča, da vsa svoja razmerja urejate sami 👇

**Score: 5.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `1 gbit` / `gbit`
- **Relevance — 1/4 = 25%** (weight 20%). Echoed: `hitrost`. **Missing** question keyword(s): `kakšna`, `optiki`, `uporabnika`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “preverite spodaj” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.25 + 0.15×0 + 0.10×0` = **0.050 → 5.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb13` · Broadband

**Q:** Kakšna je hitrost od uporabnika (oddajanje) pri paketu NEO C?

**Maks:**

> ✨ Pri paketu NEO C je hitrost oddajanja (upload) do 300 Mbit/s na optiki (FTTH), do 100/100 ali 500/500 Mbit/s na določenih optičnih povezavah, do 20 Mbit/s na VDSL, do 20 Mbit/s na LTE in do 30 Mbit/s na 5G. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 85.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `300 mbit` / `300`
- **Relevance — 1/4 = 25%** (weight 20%). Echoed: `hitrost`. **Missing** question keyword(s): `kakšna`, `oddajanje`, `uporabnika`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.25 + 0.15×1 + 0.10×1` = **0.850 → 85.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb14` · Broadband

**Q:** Kaj je NEO 5G in za koga je primeren?

**Maks:**

> ✨ NEO 5G je rešitev za internet in televizijo prek mobilnega omrežja, namenjena tistim, ki nimajo možnosti optičnega priklopa. Omogoča hitrosti do 1 Gbit/s in takojšen priklop brez posegov v dom. Primeren je za dom, vikend ali odročnejše lokacije. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 2/2 = 100%** (weight 55%). Expected facts:
    - ✅ found: `mobiln` / `5g`
    - ✅ found: `optik` / `brez optike` / `vikend` / `odročn`
- **Relevance — 1/2 = 50%** (weight 20%). Echoed: `primeren`. **Missing** question keyword(s): `koga`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb15` · Broadband

**Q:** Ali priklop NEO 5G zahteva vrtanje ali posege v dom?

**Maks:**

> ✨ Ali prav razumem, da vas zanima, ali je za priklop NEO 5G potrebna montaža, ki vključuje vrtanje ali druge posege v vaš dom? Prosim, potrdite ali dodatno pojasnite, da vam lahko pomagam. 😊

**Score: 30.0/100  (★★☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `brez` / `ni potreb` / `ne zahteva`
- **Relevance — 3/4 = 75%** (weight 20%). Echoed: `posege`, `priklop`, `vrtanje`. **Missing** question keyword(s): `zahteva`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “prosim, potrdite” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.75 + 0.15×1 + 0.10×0` = **0.300 → 30.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb16` · Broadband

**Q:** Kakšna je hitrost paketa Naj Net in ali je prenos neomejen?

**Maks:**

> ✨ Ali vas zanimajo Internet in TV storitve 🏠 ali mobilne storitve 📱? Tako vam lahko natančneje pomagam!

**Score: 15.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/2 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `2 mbit`
    - ❌ missing: `neomejen`
- **Relevance — 0/4 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `hitrost`, `kakšna`, `neomejen`, `prenos`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “lahko natančneje” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.00 + 0.15×1 + 0.10×0` = **0.150 → 15.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb17` · Broadband

**Q:** Do katere hitrosti lahko nadgradim paket Naj Net?

**Maks:**

> ✨ Paket Naj Net omogoča osnovno hitrost do 2 Mbit/s (prejemanje) in do 1 Mbit/s (pošiljanje). Nadgradite ga lahko do hitrosti 150 Mbit/s (prejemanje) in 50 Mbit/s (pošiljanje) z dodatnimi zakupnimi opcijami. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 86.7/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `150 mbit` / `150`
- **Relevance — 1/3 = 33%** (weight 20%). Echoed: `hitrosti`. **Missing** question keyword(s): `katere`, `nadgradim`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.33 + 0.15×1 + 0.10×1` = **0.867 → 86.7/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb18` · Broadband

**Q:** Kaj je Turbo WiFi?

**Maks:**

> ✨ Turbo WiFi je napredno brezžično omrežje, ki zagotavlja zanesljiv in varen WiFi-signal v vseh kotičkih vašega doma. Omogoča povezavo več dostopnih točk v eno skupno omrežje z istim imenom in geslom, kar izboljša pokritost in stabilnost. Namestitev je enostavna, upravljate pa ga lahko prek aplikacije FRITZ!App. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 85.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 2/2 = 100%** (weight 55%). Expected facts:
    - ✅ found: `wifi` / `wi-fi`
    - ✅ found: `signal` / `dom`
- **Relevance — 2/2 = 100%** (weight 20%). Echoed: `turbo`, `wifi`. **Missing:** none — every question keyword appeared.
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×0 + 0.10×1` = **0.850 → 85.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb19` · Broadband

**Q:** Na katero številko pokličem za priklop internetne opreme?

**Maks:**

> ✨ Pri Telekomu Slovenije ne usmerjamo več na klicne številke za podporo. Če potrebujete pomoč pri priklopu internetne opreme, vam lahko ponudim dve možnosti: 
> 
> 
> 
> Samopomoč: Obiščite aplikacijo Moj Telekom, kjer najdete navodila in podporo.
> Pomoč svetovalca: Vas povežem z mojim sodelavcem, ki vam bo pomagal.
> 
> 
> Kako naj nadaljujem? 😊

**Score: 21.7/100  (★★☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `041 700 700`
- **Relevance — 2/6 = 33%** (weight 20%). Echoed: `internetne`, `opreme`. **Missing** question keyword(s): `katero`, `pokličem`, `priklop`, `številko`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “povežem z mojim sodelavcem” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.33 + 0.15×1 + 0.10×0` = **0.217 → 21.7/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb20` · Broadband

**Q:** Ali lahko dobim internet prek mobilnega omrežja, če ni optike?

**Maks:**

> ✨ Seveda, pri nas lahko dobite internet prek mobilnega omrežja z našim paketom Naj Net. Paket omogoča neomejen prenos podatkov po Sloveniji, tudi tam, kjer ni optike. Več informacij najdete tukaj 👉 naj-net. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 96.7/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `neo 5g` / `5g` / `mobiln`
- **Relevance — 5/6 = 83%** (weight 20%). Echoed: `internet`, `mobilnega`, `omrežja`, `optike`, `prek`. **Missing** question keyword(s): `dobim`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.83 + 0.15×1 + 0.10×1` = **0.967 → 96.7/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb21` · Broadband

**Q:** Kakšna je redna mesečna cena paketa NEO A?

**Maks:**

> ✨ Redna mesečna naročnina za paket NEO A ni navedena v priloženih informacijah. Če želite točen znesek, predlagam, da preverite uradno prodajno ponudbo ali vprašate mojega sodelavca za podrobnosti. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 28.3/100  (★★☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `49 eur` / `49,00` / `49 €`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `mesečna`, `redna`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “predlagam, da preverite” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.67 + 0.15×1 + 0.10×0` = **0.283 → 28.3/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb22` · Broadband

**Q:** Kakšna je redna cena paketa NEO B?

**Maks:**

> ✨ Redna cena paketa NEO B je 58 EUR na mesec. Za nove naročnike z izbranimi mobilnimi paketi velja akcijska cena 32,99 EUR do 24 mesecev. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `58 eur` / `58,00` / `58 €`
- **Relevance — 1/2 = 50%** (weight 20%). Echoed: `redna`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb23` · Broadband

**Q:** Kakšna je redna cena paketa NEO C?

**Maks:**

> ✨ Redna cena paketa NEO C je 63 EUR na mesec. Za nove naročnike z izbranimi mobilnimi paketi velja akcijska cena 32,99 EUR do 24 mesecev (ob vezavi). Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `63 eur` / `63,00` / `63 €`
- **Relevance — 1/2 = 50%** (weight 20%). Echoed: `redna`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb24` · Broadband

**Q:** Koliko časa velja akcijska cena NEO za naročnike brez mobilnega paketa?

**Maks:**

> ✨ Akcijska cena za pakete NEO za naročnike brez mobilnega paketa velja prvih 6 mesecev ob vezavi za 24 mesecev. Po tem obdobju se začne zaračunavati redna mesečna naročnina.

**Score: 96.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `6 mesec` / `šest mesec`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `akcijska`, `mobilnega`, `naročnike`, `velja`. **Missing** question keyword(s): `časa`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.80 + 0.15×1 + 0.10×1` = **0.960 → 96.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb25` · Broadband

**Q:** Koliko časa velja akcijska cena NEO za nove naročnike z mobilnim paketom?

**Maks:**

> ✨ Akcijska cena za nove naročnike paketov NEO z mobilnim paketom velja 24 mesecev ob vezavi za 24 mesecev.

**Score: 97.1/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `24 mesec`
- **Relevance — 6/7 = 86%** (weight 20%). Echoed: `akcijska`, `mobilnim`, `naročnike`, `nove`, `paketom`, `velja`. **Missing** question keyword(s): `časa`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.86 + 0.15×1 + 0.10×1` = **0.971 → 97.1/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb26` · Broadband

**Q:** Kakšna je redna mesečna cena paketa NEO A?

**Maks:**

> ✨ Redna mesečna naročnina za paket Naj A znaša 20,99 EUR. Če ste imeli v mislih drug paket (npr. NEO TV), prosim, pojasnite, saj podatka za NEO A v priloženi bazi ni. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 28.3/100  (★★☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `49 eur` / `49,00` / `49 €`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `mesečna`, `redna`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “prosim, pojasnite” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.67 + 0.15×1 + 0.10×0` = **0.283 → 28.3/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb27` · Broadband

**Q:** Kakšna je redna cena paketa NEO B?

**Maks:**

> ✨ Redna cena paketa NEO B je 58 EUR na mesec. Za nove naročnike z izbranimi mobilnimi paketi velja akcijska cena 32,99 EUR/mesec do 24 mesecev. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `58 eur` / `58,00` / `58 €`
- **Relevance — 1/2 = 50%** (weight 20%). Echoed: `redna`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb28` · Broadband

**Q:** Kakšna je redna cena paketa NEO C?

**Maks:**

> ✨ Redna mesečna naročnina paketa NEO C znaša 63 EUR. Če vas zanima tudi akcijska cena ali druge podrobnosti, z veseljem pojasnim. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `63 eur` / `63,00` / `63 €`
- **Relevance — 1/2 = 50%** (weight 20%). Echoed: `redna`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb29` · Broadband

**Q:** Koliko stane paket Net (samo internet) na mesec?

**Maks:**

> Da bom lažje našel najboljšo rešitev, mi povejte, ali se zanimate za fiksni 🏠 ali mobilni 📱 internet.

**Score: 25.0/100  (★★☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `39 eur` / `39,00` / `39 €`
- **Relevance — 1/2 = 50%** (weight 20%). Echoed: `internet`. **Missing** question keyword(s): `samo`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “mi povejte” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.50 + 0.15×1 + 0.10×0` = **0.250 → 25.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb30` · Broadband

**Q:** Kakšna je akcijska cena fiksnih paketov NEO ob 24-mesečni vezavi?

**Maks:**

> ✨ Trenutne akcijske cene fiksnih paketov NEO ob 24-mesečni vezavi so odvisne od izbranega paketa in promocije. Za točne informacije o cenah in ugodnostih vam priporočam, da obiščete našo spletno stran NEO paketi ali pa mi sporočite, kateri paket vas zanima, da vam lahko bolj natančno pomagam.
> 
> 
> Potrebujete še kakšno informacijo? 😊

**Score: 28.3/100  (★★☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `32,99`
- **Relevance — 4/6 = 67%** (weight 20%). Echoed: `fiksnih`, `mesečni`, `paketov`, `vezavi`. **Missing** question keyword(s): `akcijska`, `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “kateri paket vas zanima” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.67 + 0.15×1 + 0.10×0` = **0.283 → 28.3/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb31` · Broadband

**Q:** Kakšna je najvišja hitrost do uporabnika na optiki pri paketih NEO?

**Maks:**

> ✨ Najvišja hitrost do uporabnika na optiki (FTTH) pri vseh paketih NEO (NEO A, NEO B, NEO C) je do 1 Gbit/s. Možna je tudi nadgradnja do 5 Gbit/s. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 96.7/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `1 gbit` / `gbit`
- **Relevance — 5/6 = 83%** (weight 20%). Echoed: `hitrost`, `najvišja`, `optiki`, `paketih`, `uporabnika`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.83 + 0.15×1 + 0.10×1` = **0.967 → 96.7/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb32` · Broadband

**Q:** Do katere hitrosti lahko nadgradim optični internet NEO?

**Maks:**

> ✨ Optični internet v paketu NEO lahko nadgradite do hitrosti 5 Gbit/s. Na voljo so naslednje možnosti nadgradnje:
> 
> 
> 
> do 1 Gbit/s / 300 Mbit/s (10 €/mesec)
> do 2 Gbit/s / 100 Mbit/s (15 €/mesec)
> do 5 Gbit/s (cena je odvisna od paketa)
> 
> 
> Več informacij najdete tukaj 👉 internet.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 92.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `5 gbit`
- **Relevance — 3/5 = 60%** (weight 20%). Echoed: `hitrosti`, `internet`, `optični`. **Missing** question keyword(s): `katere`, `nadgradim`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.60 + 0.15×1 + 0.10×1` = **0.920 → 92.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb33` · Broadband

**Q:** Kakšna je hitrost oddajanja (upload) pri paketu NEO C na optiki?

**Maks:**

> ✨ Pri paketu NEO C na optiki (FTTH) je hitrost oddajanja (upload) do 300 Mbit/s. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 96.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `300 mbit` / `300`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `hitrost`, `oddajanja`, `optiki`, `upload`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.80 + 0.15×1 + 0.10×1` = **0.960 → 96.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb34` · Broadband

**Q:** Kakšna je hitrost oddajanja pri paketu NEO A na optiki (FTTH)?

**Maks:**

> ✨ Pri paketu NEO A na optiki (FTTH) je hitrost oddajanja do 40 Mbit/s. Hitrost lahko tudi nadgradite za doplačilo. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 96.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `40 mbit` / `40`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `ftth`, `hitrost`, `oddajanja`, `optiki`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.80 + 0.15×1 + 0.10×1` = **0.960 → 96.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb35` · Broadband

**Q:** Kakšna je hitrost oddajanja pri paketu NEO B na optiki?

**Maks:**

> ✨ Pri paketu NEO B na optiki (FTTH) je hitrost oddajanja do 100 Mbit/s. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 95.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `100 mbit` / `100`
- **Relevance — 3/4 = 75%** (weight 20%). Echoed: `hitrost`, `oddajanja`, `optiki`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.75 + 0.15×1 + 0.10×1` = **0.950 → 95.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb36` · Broadband

**Q:** Koliko stane fiksni paket Naj Net na mesec?

**Maks:**

> ✨ Za informacije o fiksnih paketih, kot je Naj Net, bom preveril podrobnosti. 🏠 Ali želite izvedeti več o fiksnih internetnih in TV storitvah?

**Score: 15.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `13,99`
- **Relevance — 0/1 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `fiksni`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “želite izvedeti” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.00 + 0.15×1 + 0.10×0` = **0.150 → 15.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb37` · Broadband

**Q:** Kakšna je osnovna hitrost paketa Naj Net?

**Maks:**

> ✨ Osnovna hitrost paketa Naj Net je do 2 Mbit/s v smeri k uporabniku in do 1 Mbit/s iz smeri uporabnika. Hitrost lahko po želji nadgradite. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `2 mbit`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `hitrost`, `osnovna`. **Missing** question keyword(s): `kakšna`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb38` · Broadband

**Q:** Do katere hitrosti lahko nadgradim paket Naj Net?

**Maks:**

> ✨ Paket Naj Net omogoča osnovno hitrost do 2 Mbit/s (prejemanje) in 1 Mbit/s (pošiljanje). Hitrost lahko nadgradite do največ 150 Mbit/s (prejemanje) in 50 Mbit/s (pošiljanje) z dodatnimi zakupnimi opcijami. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 80.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `150 mbit` / `150`
- **Relevance — 0/3 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `hitrosti`, `katere`, `nadgradim`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.00 + 0.15×1 + 0.10×1` = **0.800 → 80.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb39` · Broadband

**Q:** Ali je prenos podatkov pri Naj Net v Sloveniji neomejen?

**Maks:**

> ✨ Da, pri paketu Naj Net je prenos podatkov v Sloveniji neomejen. Hitrost prenosa je do 2 Mbit/s do uporabnika in do 1 Mbit/s od uporabnika. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `neomejen`
- **Relevance — 4/4 = 100%** (weight 20%). Echoed: `neomejen`, `podatkov`, `prenos`, `sloveniji`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb40` · Broadband

**Q:** Kaj je rešitev, če na mojem naslovu še ni optike?

**Maks:**

> Pokritost optičnega omrežja na želeni lokaciji preverite spodaj 👇
> Za dodatne informacije o optičnem omrežju ali oddajo naročila vas lahko povežem s sodelavcem 🤝💬
> Želite, da vas povežem s sodelavcem?

**Score: 0.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `neo 5g` / `5g`
- **Relevance — 0/4 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `mojem`, `naslovu`, `optike`, `rešitev`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “vas povežem s sodelavcem” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.00 + 0.15×0 + 0.10×0` = **0.000 → 0.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb41` · Broadband

**Q:** Ali priklop NEO 5G zahteva vrtanje ali posege v dom?

**Maks:**

> ✨ Ali sprašujete, ali je za priklop NEO Smartboxa s 5G potrebna montaža, ki vključuje vrtanje ali posege v vaš dom? Če lahko pojasnite malo bolj natančno, vam bom z veseljem pomagal! 😊

**Score: 30.0/100  (★★☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `brez` / `ne zahteva` / `ni potreb`
- **Relevance — 3/4 = 75%** (weight 20%). Echoed: `posege`, `priklop`, `vrtanje`. **Missing** question keyword(s): `zahteva`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “ali sprašujete” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.75 + 0.15×1 + 0.10×0` = **0.300 → 30.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb42` · Broadband

**Q:** Kako preverim dostopnost optike na svojem naslovu?

**Maks:**

> Pokritost optičnega omrežja na želeni lokaciji preverite spodaj 👇
> Za dodatne informacije o optičnem omrežju ali oddajo naročila vas lahko povežem s sodelavcem 🤝💬
> Želite, da vas povežem s sodelavcem?

**Score: 65.0/100  (★★★★☆)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `naslov` / `lokacij` / `prever`
- **Relevance — 0/5 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `dostopnost`, `naslovu`, `optike`, `preverim`, `svojem`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — no** (weight 10% → 1) (a redirect phrase “vas povežem s sodelavcem” is present, but fact recall ≥ 34%, so it is *not* treated as a deflection).
- **Weighted total:** `0.55×1.00 + 0.20×0.00 + 0.15×0 + 0.10×1` = **0.650 → 65.0/100**.
- **Verdict:** Partial: some but not all expected facts were stated.

---

### `bb43` · Broadband

**Q:** Za koliko gospodinjstev bo optika priključena brezplačno?

**Maks:**

> Podatkov o statusu gradnje nimam, ampak brez skrbi, lahko vas povežem s sodelavcem 🏗️🚧
> Želite, da vas povežem s sodelavcem?

**Score: 0.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `250.000` / `250000` / `250 000`
- **Relevance — 0/4 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `brezplačno`, `gospodinjstev`, `optika`, `priključena`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “podatkov o statusu” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.00 + 0.15×0 + 0.10×0` = **0.000 → 0.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb44` · Broadband

**Q:** Katere tehnologije za dostop do interneta ponuja Telekom?

**Maks:**

> ✨ Telekom Slovenije ponuja več tehnologij za dostop do interneta:
> 
> 
> 
> Optično omrežje (FTTH): omogoča hitrosti do 10 Gbit/s, pokriva več kot polovico slovenskih gospodinjstev.
> Mobilni internet (4G, 5G): široka pokritost, tudi za fiksne storitve prek mobilnih tehnologij.
> Bakrena omrežja (ADSL, VDSL): na območjih, kjer optika še ni na voljo.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 2/2 = 100%** (weight 55%). Expected facts:
    - ✅ found: `optik` / `ftth`
    - ✅ found: `vdsl` / `adsl` / `lte` / `5g`
- **Relevance — 4/6 = 67%** (weight 20%). Echoed: `dostop`, `interneta`, `ponuja`, `telekom`. **Missing** question keyword(s): `katere`, `tehnologije`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “10 gb”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb45` · Broadband

**Q:** Kaj je storitev Turbo WiFi?

**Maks:**

> ✨ Turbo WiFi je napredno brezžično omrežje, ki zagotavlja zanesljiv in varen WiFi-signal v vseh kotičkih vašega doma. Omogoča povezavo več dostopnih točk v eno omrežje (eno ime in geslo), kar prinaša vrhunsko pokritost, visoke hitrosti (do 1,3 Gbit/s) in enostavno upravljanje. Storitev vključuje tudi možnosti za varnost otrok in ločen WiFi za goste.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 2/2 = 100%** (weight 55%). Expected facts:
    - ✅ found: `wifi` / `wi-fi`
    - ✅ found: `signal` / `dom`
- **Relevance — 3/3 = 100%** (weight 20%). Echoed: `storitev`, `turbo`, `wifi`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “1.3 gb”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb46` · Broadband

**Q:** Ali Telekom ponuja internet prek satelita?

**Maks:**

> ✨ Da, pri Telekomu Slovenije ponujamo internet prek satelita, predvsem za območja, kjer klasična rešitev ali mobilni signal nista mogoča. Na voljo so različni paketi s hitrostjo do 25/6 Mbit/s in možnostjo nadgradnje hitrosti. Več informacij najdete tukaj 👉 internet prek satelita.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 92.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `satelit`
- **Relevance — 3/5 = 60%** (weight 20%). Echoed: `internet`, `prek`, `satelita`. **Missing** question keyword(s): `ponuja`, `telekom`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1) (a redirect phrase “na voljo so različn” is present, but fact recall ≥ 34%, so it is *not* treated as a deflection).
- **Weighted total:** `0.55×1.00 + 0.20×0.60 + 0.15×1 + 0.10×1` = **0.920 → 92.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb47` · Broadband

**Q:** Kaj omogoča brezžični sistem PLC?

**Maks:**

> ✨ Brezžični sistem PLC omogoča prenos internetnega signala prek obstoječega električnega omrežja v vašem domu. Prednosti so:
> 
> 
> 
> Odlična WiFi pokritost tudi v večjih stanovanjih ali hišah
> Preprosta uporaba brez dodatnih kablov ali gradbenih posegov
> Modularna nadgradnja za vse velikosti stanovanj
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 85.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `plc` / `električn` / `vtičnic` / `omrežj`
- **Relevance — 3/3 = 100%** (weight 20%). Echoed: `brezžični`, `omogoča`, `sistem`. **Missing:** none — every question keyword appeared.
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×0 + 0.10×1` = **0.850 → 85.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb48` · Broadband

**Q:** Katera varnostna rešitev (Kaspersky) je na voljo za internet?

**Maks:**

> ✨ Za internetno zaščito so na voljo naslednje rešitve Kaspersky:
> 
> 
> 
> Kaspersky Internet Security Multi-Device: zaščita do treh naprav (PC, Mac, Android).
> Kaspersky Total Security Multi-Device: napredna zaščita za zahtevnejše uporabnike.
> Kaspersky Small Office Security: za domače pisarne in mala podjetja.
> 
> 
> Vsaka rešitev vključuje antivirusno zaščito, varno brskanje in dodatne funkcije. Potrebujete še dodatne informacije? Kar povejte 😊

**Score: 78.3/100  (★★★★☆)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `kaspersky`
- **Relevance — 4/6 = 67%** (weight 20%). Echoed: `internet`, `kaspersky`, `rešitev`, `voljo`. **Missing** question keyword(s): `katera`, `varnostna`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×0 + 0.10×1` = **0.783 → 78.3/100**.
- **Verdict:** Partial: some but not all expected facts were stated.

---

### `bb49` · Broadband

**Q:** Kaj je storitev Strela alarm?

**Maks:**

> ✨ Storitev Strela alarm je brezplačno SMS-obveščanje o nevarnosti strel v realnem času. Namenjena je uporabnikom naših fiksnih in mobilnih storitev. Obvestila prejmete za eno ali več lokacij fiksnega priključka, kar vam omogoča pravočasno izklop naprav in zaščito pred poškodbami zaradi strele. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `neviht` / `strel` / `obvest` / `alarm`
- **Relevance — 3/3 = 100%** (weight 20%). Echoed: `alarm`, `storitev`, `strela`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb50` · Broadband

**Q:** Na katero številko pokličem za priklop internetne opreme?

**Maks:**

> ✨ Za priklop internetne opreme vam ni treba klicati. Če potrebujete pomoč pri priklopu ali nastavitvi, lahko to uredimo na več načinov:
> 
> 
> 
> Preverite navodila za priklop opreme na naši spletni strani ali v Moj Telekom aplikaciji.
> Če potrebujete dodatno pomoč, vas lahko povežem z mojim sodelavcem, ki vam bo z veseljem pomagal.
> 
> 
> Ali želite, da vas povežem? 😊

**Score: 10.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `041 700 700`
- **Relevance — 3/6 = 50%** (weight 20%). Echoed: `internetne`, `opreme`, `priklop`. **Missing** question keyword(s): `katero`, `pokličem`, `številko`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “povežem z mojim sodelavcem” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.50 + 0.15×0 + 0.10×0` = **0.100 → 10.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb51` · Broadband

**Q:** Ali lahko internet dobim prek mobilnega omrežja, če ni optike?

**Maks:**

> Pokritost optičnega omrežja na želeni lokaciji preverite spodaj 👇
> Za dodatne informacije o optičnem omrežju ali oddajo naročila vas lahko povežem s sodelavcem 🤝💬
> Želite, da vas povežem s sodelavcem?

**Score: 3.3/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `neo 5g` / `5g` / `mobiln`
- **Relevance — 1/6 = 17%** (weight 20%). Echoed: `omrežja`. **Missing** question keyword(s): `dobim`, `internet`, `mobilnega`, `optike`, `prek`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “vas povežem s sodelavcem” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.17 + 0.15×0 + 0.10×0` = **0.033 → 3.3/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb52` · Broadband

**Q:** Kakšna je hitrost do uporabnika pri paketu Net na optiki?

**Maks:**

> Hitrost interneta, ki je vključena v vašem paketu, lahko preverite spodaj 👇
> 💡 Če dostopa do Mojega Telekoma še nimate, si ga čim prej zagotovite. Moj Telekom vam omogoča, da vsa svoja razmerja urejate sami 👇

**Score: 5.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `1 gbit` / `gbit`
- **Relevance — 1/4 = 25%** (weight 20%). Echoed: `hitrost`. **Missing** question keyword(s): `kakšna`, `optiki`, `uporabnika`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “preverite spodaj” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.25 + 0.15×0 + 0.10×0` = **0.050 → 5.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb53` · Broadband

**Q:** Koliko časa velja akcijska cena NEO za naročnike brez mobilnega paketa?

**Maks:**

> ✨ Akcijska cena paketa NEO za naročnike brez mobilnega paketa velja prvih 6 mesecev ob vezavi za 24 mesecev. Po tem obdobju se začne zaračunavati redna mesečna naročnina.

**Score: 96.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `6 mesec` / `šest mesec`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `akcijska`, `mobilnega`, `naročnike`, `velja`. **Missing** question keyword(s): `časa`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.80 + 0.15×1 + 0.10×1` = **0.960 → 96.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb54` · Broadband

**Q:** Koliko časa velja akcijska cena NEO za nove naročnike z mobilnim paketom?

**Maks:**

> ✨ Akcijska cena paketov NEO za nove naročnike z mobilnim paketom velja 24 mesecev ob vezavi za 24 mesecev. Po tem obdobju se začne zaračunavati redna mesečna naročnina.

**Score: 97.1/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `24 mesec`
- **Relevance — 6/7 = 86%** (weight 20%). Echoed: `akcijska`, `mobilnim`, `naročnike`, `nove`, `paketom`, `velja`. **Missing** question keyword(s): `časa`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.86 + 0.15×1 + 0.10×1` = **0.971 → 97.1/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb55` · Broadband

**Q:** Ali je priklop optike lahko brezplačen?

**Maks:**

> Podatkov o statusu gradnje nimam, ampak brez skrbi, lahko vas povežem s sodelavcem 🏗️🚧
> Želite, da vas povežem s sodelavcem?

**Score: 0.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `brezplač`
- **Relevance — 0/3 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `brezplačen`, `optike`, `priklop`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “podatkov o statusu” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.00 + 0.15×0 + 0.10×0` = **0.000 → 0.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb56` · Broadband

**Q:** Kolikšen popust na naročnino NEO A prinaša akcija (16 EUR)?

**Maks:**

> ✨ Ali morda sprašujete o trenutnih promocijah za paket NEO A in kakšen popust je na voljo? Če potrebujete točne informacije, mi prosim sporočite več podrobnosti, da vam lahko natančneje pomagam. 😊

**Score: 19.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `16` / `16,01`
- **Relevance — 1/5 = 20%** (weight 20%). Echoed: `popust`. **Missing** question keyword(s): `akcija`, `kolikšen`, `naročnino`, `prinaša`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “prosim sporočite” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.20 + 0.15×1 + 0.10×0` = **0.190 → 19.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb57` · Broadband

**Q:** Kolikšen popust prinaša akcija pri paketu NEO C?

**Maks:**

> ✨ Akcija pri paketu NEO C prinaša 30,01 € popusta na mesečno naročnino za obdobje 24 mesecev ob vezavi. Redna cena je 63 €, akcijska pa 32,99 €/mesec.

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `30` / `30,01`
- **Relevance — 2/4 = 50%** (weight 20%). Echoed: `akcija`, `prinaša`. **Missing** question keyword(s): `kolikšen`, `popust`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb58` · Broadband

**Q:** Ali za pakete NEO velja garancija zadovoljstva?

**Maks:**

> ✨ Da, za pakete NEO velja garancija zadovoljstva. Novi naročniki lahko v 30 dneh od vklopa paketa zahtevate vračilo denarja, če niste zadovoljni s storitvijo. Pogoj je prijavljena tehnična napaka v tem obdobju. Želite, da kaj dodatno razložim? Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `30` / `garancij`
- **Relevance — 4/4 = 100%** (weight 20%). Echoed: `garancija`, `pakete`, `velja`, `zadovoljstva`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb59` · Broadband

**Q:** Kaj potrebujem za priklop NEO 5G doma?

**Maks:**

> ✨ Za priklop NEO 5G doma potrebujete:
> 
> 
> 
> Pokritost z mobilnim omrežjem Telekoma Slovenije.
> NEO 5G modem, ki ga preprosto priklopite v električno vtičnico.
> TV-komunikator (če želite TV-izkušnjo).
> 
> 
> Namestitev je hitra, brez dodatnih posegov v dom. Želite še podrobnosti glede postopka ali opreme? Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `modem` / `oprem`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `doma`, `priklop`. **Missing** question keyword(s): `potrebujem`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb60` · Broadband

**Q:** Ali lahko z NEO 5G pokrijem tudi vikend ali odročno lokacijo?

**Maks:**

> ✨ Storitev Hitri internet 4G/5G za Mobi omogoča hiter prenos podatkov tudi na zunajmestnih območjih, če je na voljo signal 5G in uporabljate ustrezno napravo ter USIM kartico. Pokritost je odvisna od lokacije in omrežja.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 80.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `vikend` / `odročn` / `da`
- **Relevance — 0/4 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `lokacijo`, `odročno`, `pokrijem`, `vikend`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.00 + 0.15×1 + 0.10×1` = **0.800 → 80.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb61` · Broadband

**Q:** Kakšna je hitrost oddajanja pri paketu Net na optiki?

**Maks:**

> Hitrost interneta, ki je vključena v vašem paketu, lahko preverite spodaj 👇
> 💡 Če dostopa do Mojega Telekoma še nimate, si ga čim prej zagotovite. Moj Telekom vam omogoča, da vsa svoja razmerja urejate sami 👇

**Score: 5.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `100 mbit` / `100`
- **Relevance — 1/4 = 25%** (weight 20%). Echoed: `hitrost`. **Missing** question keyword(s): `kakšna`, `oddajanja`, `optiki`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “preverite spodaj” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.25 + 0.15×0 + 0.10×0` = **0.050 → 5.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb62` · Broadband

**Q:** Katera je najhitrejša internetna povezava (optika) po mnenju uporabnikov?

**Maks:**

> ✨ Najhitrejša optična povezava pri Telekomu Slovenije je do 2 Gbit/s / 100 Mbit/s. Na voljo je za doplačilo 15 €/mesec, odvisno od tehničnih zmogljivosti linije.

**Score: 85.7/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `1 gbit` / `gbit` / `najhitrej`
- **Relevance — 2/7 = 29%** (weight 20%). Echoed: `najhitrejša`, `povezava`. **Missing** question keyword(s): `internetna`, `katera`, `mnenju`, `optika`, `uporabnikov`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.29 + 0.15×1 + 0.10×1` = **0.857 → 85.7/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb63` · Broadband

**Q:** Ali je hitrost pri paketih NEO nadgradljiva?

**Maks:**

> ✨ Da, pri paketih NEO A, B, C in Net lahko nadgradite hitrost interneta. Na voljo so različne nadgradnje, odvisno od tehnologije (VDSL ali FTTH). Želite podrobnosti o možnostih in cenah nadgradenj? Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `nadgrad` / `5 gbit` / `da`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `hitrost`, `paketih`. **Missing** question keyword(s): `nadgradljiva`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1) (a redirect phrase “na voljo so različn” is present, but fact recall ≥ 34%, so it is *not* treated as a deflection).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb64` · Broadband

**Q:** Kje naročim opremo za priklop, če ni optike?

**Maks:**

> ✨ Oprema za priklop fiksnih storitev (če ni optike) je odvisna od vaše interne napeljave. Če potrebujete pomoč pri naročilu opreme, vas lahko povežem z mojim sodelavcem, ki bo uredil naročilo. Želite, da vas povežem? Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 10.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `prodajn` / `041 700 700` / `pošt`
- **Relevance — 2/4 = 50%** (weight 20%). Echoed: `optike`, `priklop`. **Missing** question keyword(s): `naročim`, `opremo`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “povežem z mojim sodelavcem” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.50 + 0.15×0 + 0.10×0` = **0.100 → 10.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb65` · Broadband

**Q:** Kakšna je cena minute klica iz Slovenije v EU po ceniku NEO?

**Maks:**

> Klici iz domačega omrežja v tujino niso vključeni v vaš paket. Cenik za tujino in seznam držav po območjih najdete spodaj 👇
> Predlagam vam, da izberete ustrezen zakup in tako ugodneje kličete v tujino. Povejte mi, ali želite zakup za mobilno 📱 ali fiksno 🏠 številko.

**Score: 15.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `0,23` / `0,2318` / `0,19`
- **Relevance — 0/5 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `ceniku`, `kakšna`, `klica`, `minute`, `slovenije`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “najdete spodaj” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.00 + 0.15×1 + 0.10×0` = **0.150 → 15.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb66` · Broadband

**Q:** Ali paketi NEO vključujejo tudi televizijo?

**Maks:**

> ✨ Da, vsi paketi NEO (NEO A, NEO B, NEO C) vključujejo televizijo. Razlikujejo se po številu programov in programski shemi:
> 
> 
> 
> NEO A: Osnovna shema, 150+ programov
> NEO B: Standardna shema, 210+ programov
> NEO C: Mega HD shema, 255+ programov
> 
> 
> Vsi omogočajo ogled nazaj do 7 dni. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `televiz` / `tv` / `program`
- **Relevance — 3/3 = 100%** (weight 20%). Echoed: `paketi`, `televizijo`, `vključujejo`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb67` · Broadband

**Q:** Ali paket Net (samo internet) vključuje televizijo?

**Maks:**

> Da bom lažje našel najboljšo rešitev, mi povejte, ali se zanimate za fiksni 🏠 ali mobilni 📱 internet.

**Score: 86.7/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `ne` / `brez tv` / `samo internet`
- **Relevance — 1/3 = 33%** (weight 20%). Echoed: `internet`. **Missing** question keyword(s): `samo`, `televizijo`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1) (a redirect phrase “mi povejte” is present, but fact recall ≥ 34%, so it is *not* treated as a deflection).
- **Weighted total:** `0.55×1.00 + 0.20×0.33 + 0.15×1 + 0.10×1` = **0.867 → 86.7/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb68` · Broadband

**Q:** Kakšna je najvišja hitrost mobilnega interneta pri paketu Naj Net?

**Maks:**

> ✨ Pri paketu Naj Net je hitrost mobilnega interneta do 2 Mbit/s do uporabnika in do 1 Mbit/s od uporabnika. Možna je nadgradnja hitrosti z dodatnimi opcijami. Več informacij najdete tukaj 👉 naj-net.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 92.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `150` / `150/50` / `150 mbit` / `2 mbit`
- **Relevance — 3/5 = 60%** (weight 20%). Echoed: `hitrost`, `interneta`, `mobilnega`. **Missing** question keyword(s): `kakšna`, `najvišja`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.60 + 0.15×1 + 0.10×1` = **0.920 → 92.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb69` · Broadband

**Q:** Ali lahko fiksni internet dobim tudi na omrežju OŠO (alternativni)?

**Maks:**

> Želite, da vas povežem s sodelavcem?

**Score: 0.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `ošo` / `oso` / `alternativ`
- **Relevance — 0/5 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `alternativni`, `dobim`, `fiksni`, `internet`, `omrežju`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “vas povežem s sodelavcem” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.00 + 0.15×0 + 0.10×0` = **0.000 → 0.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb70` · Broadband

**Q:** Kolikšen popust na naročnino prinaša akcija pri paketu NEO B?

**Maks:**

> ✨ Akcija pri paketu NEO B prinaša popust 25,01 € na mesečno naročnino. Redna cena je 58 €, akcijska cena pa znaša 32,99 € ob vezavi za 24 mesecev.

**Score: 96.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `25` / `25,01`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `akcija`, `naročnino`, `popust`, `prinaša`. **Missing** question keyword(s): `kolikšen`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.80 + 0.15×1 + 0.10×1` = **0.960 → 96.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb71` · Broadband

**Q:** Ali za pakete NEO velja 24-mesečna vezava za akcijsko ceno?

**Maks:**

> ✨ Da, za pakete NEO pri akcijski ceni običajno velja 24-mesečna vezava. Če potrebujete več informacij o pogojih ali želite preveriti specifične podrobnosti, mi sporočite! 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `24 mesec` / `24-mesec` / `24-mesečn` / `24 mesečn`
- **Relevance — 4/6 = 67%** (weight 20%). Echoed: `mesečna`, `pakete`, `velja`, `vezava`. **Missing** question keyword(s): `akcijsko`, `ceno`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb72` · Broadband

**Q:** Kaj se zgodi s ceno NEO po izteku akcijskega obdobja?

**Maks:**

> ✨ Po izteku akcijskega obdobja se cena storitve NEO vrne na redno ceno, določeno v veljavnem ceniku. Če želite preveriti točen znesek ali imate dodatna vprašanja, mi sporočite, da vas povežem z mojim sodelavcem za podrobnejše informacije. 😊

**Score: 96.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `redn` / `redna cena` / `redna naročnina`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `akcijskega`, `ceno`, `izteku`, `obdobja`. **Missing** question keyword(s): `zgodi`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1) (a redirect phrase “povežem z mojim sodelavcem” is present, but fact recall ≥ 34%, so it is *not* treated as a deflection).
- **Weighted total:** `0.55×1.00 + 0.20×0.80 + 0.15×1 + 0.10×1` = **0.960 → 96.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb73` · Broadband

**Q:** Ali lahko hitrost interneta pri NEO nadgradim do 2 Gbit/s?

**Maks:**

> ✨ Da, pri paketih NEO (A, B, C) lahko nadgradite hitrost interneta do 2 Gbit/s/100 Mbit/s na optični povezavi (FTTH) za doplačilo 15 € na mesec. 
> 
> 
> Vas zanima še kaj glede nadgradenj ali paketov? Kar vprašajte 😊

**Score: 95.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `2 gbit` / `5 gbit` / `nadgrad`
- **Relevance — 3/4 = 75%** (weight 20%). Echoed: `gbit`, `hitrost`, `interneta`. **Missing** question keyword(s): `nadgradim`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.75 + 0.15×1 + 0.10×1` = **0.950 → 95.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `bb74` · Broadband

**Q:** Katera telefonska številka je za pomoč pri internetu?

**Maks:**

> ✨ Za pomoč pri internetu vam lahko pomagam tukaj. Če potrebujete dodatno pomoč, vas lahko povežem z mojim sodelavcem. Bi želeli to? 😊

**Score: 8.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `041 700 700`
- **Relevance — 2/5 = 40%** (weight 20%). Echoed: `internetu`, `pomoč`. **Missing** question keyword(s): `katera`, `telefonska`, `številka`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “povežem z mojim sodelavcem” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.40 + 0.15×0 + 0.10×0` = **0.080 → 8.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `bb75` · Broadband

**Q:** Ali je za NEO 5G priklop takojšen?

**Maks:**

> ✨ Da, za NEO 5G je priklop takojšen. Modem preprosto priključite in že lahko uporabljate internet ter televizijo, brez dodatnih posegov v stanovanju. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `takoj` / `hiter` / `enostav`
- **Relevance — 2/2 = 100%** (weight 20%). Echoed: `priklop`, `takojšen`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---


## IPTV (NEO TV)

### `tv01` · IPTV (NEO TV)

**Q:** Koliko TV programov vključuje paket NEO A?

**Maks:**

> ✨ Paket NEO A vključuje programsko shemo Osnovna, ki vsebuje več kot 150 TV programov. Celoten seznam programov si lahko ogledate tukaj 👉 TV-programi v paketu NEO A.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `150`
- **Relevance — 1/1 = 100%** (weight 20%). Echoed: `programov`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv02` · IPTV (NEO TV)

**Q:** Koliko programov ima paket NEO B?

**Maks:**

> ✨ Paket NEO B vključuje programsko shemo Standard, ki vsebuje več kot 210 TV programov. Celoten seznam programov si lahko ogledate tukaj 👉 tv-programi-v-paketu-neo-b.pdf.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `210`
- **Relevance — 1/1 = 100%** (weight 20%). Echoed: `programov`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv03` · IPTV (NEO TV)

**Q:** Koliko TV programov vključuje paket NEO C?

**Maks:**

> ✨ Paket NEO C vključuje televizijo s programsko shemo Mega HD, ki vsebuje več kot 255 TV programov. Celoten seznam programov si lahko ogledate tukaj 👉 TV-programi v paketu NEO C.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `255`
- **Relevance — 1/1 = 100%** (weight 20%). Echoed: `programov`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv04` · IPTV (NEO TV)

**Q:** Katero programsko shemo vključuje paket NEO C?

**Maks:**

> ✨ Paket NEO C vključuje programsko shemo Mega HD. Mega shema vsebuje več kot 255 TV programov. Celoten seznam programov si lahko ogledate tukaj 👉 TV-programi v paketu NEO C.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `mega hd` / `mega`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `programsko`, `shemo`. **Missing** question keyword(s): `katero`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv05` · IPTV (NEO TV)

**Q:** Katero programsko shemo ima paket NEO A?

**Maks:**

> ✨ Paket NEO A vključuje programsko shemo Osnovna. Osnovna shema vsebuje več kot 150 TV programov. Celoten seznam programov si lahko ogledate tukaj 👉 TV-programi v paketu NEO A.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `osnovna`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `programsko`, `shemo`. **Missing** question keyword(s): `katero`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv06` · IPTV (NEO TV)

**Q:** Kakšno programsko shemo vključuje paket NEO B?

**Maks:**

> ✨ Paket NEO B vključuje programsko shemo Standard, ki vsebuje več kot 210 TV programov. Celoten seznam programov v tej shemi si lahko ogledate tukaj 👉 tv-programi-v-paketu-neo-b.pdf.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `standard`
- **Relevance — 3/3 = 100%** (weight 20%). Echoed: `kakšno`, `programsko`, `shemo`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv07` · IPTV (NEO TV)

**Q:** Koliko stane samostojni TV paket NEO TV brez interneta?

**Maks:**

> ✨ NEO TV Lite ni na voljo kot samostojni TV paket brez interneta. Za uporabo potrebujete naročniško razmerje, ki vključuje internet in televizijo z NEO Smartboxom. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 45.0/100  (★★★☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `41 eur` / `41,00` / `41 €`
- **Relevance — 2/2 = 100%** (weight 20%). Echoed: `interneta`, `samostojni`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×0.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **0.450 → 45.0/100**.
- **Verdict:** Risky: Maks answered confidently with a specific value that does **not** match the site — a candidate factual error.

---

### `tv08` · IPTV (NEO TV)

**Q:** Koliko dni nazaj lahko gledam vsebine z ogledom nazaj pri NEO?

**Maks:**

> ✨ Ogled nazaj pri NEO omogoča ogled izbranih TV vsebin do 7 dni nazaj. Storitev je vključena v vse TV pakete. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 85.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `7 dni` / `7-dnev` / `7`
- **Relevance — 1/4 = 25%** (weight 20%). Echoed: `nazaj`. **Missing** question keyword(s): `gledam`, `ogledom`, `vsebine`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.25 + 0.15×1 + 0.10×1` = **0.850 → 85.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv09` · IPTV (NEO TV)

**Q:** Ali lahko pri NEO snemam oddaje?

**Maks:**

> ✨ Da, pri naši storitvi NEO lahko snemate oddaje na vseh platformah: NEO Smartbox, spletno mesto NEO.io in aplikacijo NEO. Posneti je možno samo celotno TV-vsebino na programih, kjer je snemanje omogočeno. Podrobna navodila z slikami najdete tukaj 👉 snemalnik.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `snema` / `posne`
- **Relevance — 1/2 = 50%** (weight 20%). Echoed: `oddaje`. **Missing** question keyword(s): `snemam`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv10` · IPTV (NEO TV)

**Q:** Koliko stane najem vsakega dodatnega TV-komunikatorja?

**Maks:**

> ✨ Najem vsakega dodatnega NEO Smartboxa znaša 3,90 € na mesec za posamezno napravo. Na eno naročnino lahko najamete do 8 NEO Smartboxov. Dodatni Smartbox lahko naročite prek Moj Telekom. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 95.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `3,90`
- **Relevance — 3/4 = 75%** (weight 20%). Echoed: `dodatnega`, `najem`, `vsakega`. **Missing** question keyword(s): `komunikatorja`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.75 + 0.15×1 + 0.10×1` = **0.950 → 95.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv11` · IPTV (NEO TV)

**Q:** Ali je najem prvega TV-komunikatorja brezplačen?

**Maks:**

> ✨ Najem prvega NEO Smartbox TV-komunikatorja je vključen v mesečno naročnino paketa NEO, zato za prvega komunikatorja ni dodatnega stroška najema. Vsak dodatni NEO Smartbox pa se zaračuna 3,90 € na mesec na napravo. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 95.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `brezplač` / `vključen v naročnino` / `vključen v mesečno` / `vključen v ceno`
- **Relevance — 3/4 = 75%** (weight 20%). Echoed: `komunikatorja`, `najem`, `prvega`. **Missing** question keyword(s): `brezplačen`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.75 + 0.15×1 + 0.10×1` = **0.950 → 95.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv12` · IPTV (NEO TV)

**Q:** Kaj je NEO TV Lite?

**Maks:**

> ✨ NEO TV Lite je aplikacija, ki omogoča ogled TV-programov, vsebin na zahtevo, snemanje in ogled za nazaj do 7 dni na pametnih televizorjih (Android TV, Google TV, LG WebOS, Samsung Tizen, Hisense Vidaa, Philips Saphi/Titan OS). Potrebujete naročniško razmerje z internetom, televizijo in NEO Smartboxom.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 2/2 = 100%** (weight 55%). Expected facts:
    - ✅ found: `aplikacij`
    - ✅ found: `pametn` / `televizor`
- **Relevance — 1/1 = 100%** (weight 20%). Echoed: `lite`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv13` · IPTV (NEO TV)

**Q:** Koliko stane NEO TV Lite na napravo mesečno?

**Maks:**

> ✨ NEO TV Lite stane 1,90 EUR na mesec za posamezno napravo. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `1,90`
- **Relevance — 2/2 = 100%** (weight 20%). Echoed: `lite`, `napravo`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv14` · IPTV (NEO TV)

**Q:** Na koliko pametnih televizorjih lahko uporabljam NEO TV Lite?

**Maks:**

> ✨ NEO TV Lite lahko uporabljate na največ petih pametnih televizorjih hkrati. Potrebujete aktivacijo in veljavno naročnino za vsak televizor posebej. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 95.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `5` / `pet`
- **Relevance — 3/4 = 75%** (weight 20%). Echoed: `lite`, `pametnih`, `televizorjih`. **Missing** question keyword(s): `uporabljam`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.75 + 0.15×1 + 0.10×1` = **0.950 → 95.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv15` · IPTV (NEO TV)

**Q:** Na katerih pametnih televizorjih deluje NEO TV Lite?

**Maks:**

> ✨ NEO TV Lite deluje na pametnih televizorjih z naslednjimi operacijskimi sistemi:
> 
> 
> 
> Android TV (7.0 Nougat ali novejši)
> Google TV
> LG webOS (6.0 ali novejši)
> Samsung Tizen (letnik 2018 in novejši)
> Hisense Vidaa (serija U4 in novejši)
> Philips Saphi OS (modelno leto 2021, 2022)
> Philips Titan OS (modelno leto 2023 in novejši)
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 96.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 3/3 = 100%** (weight 55%). Expected facts:
    - ✅ found: `samsung` / `tizen`
    - ✅ found: `lg` / `webos`
    - ✅ found: `android` / `hisense` / `philips`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `deluje`, `lite`, `pametnih`, `televizorjih`. **Missing** question keyword(s): `katerih`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.80 + 0.15×1 + 0.10×1` = **0.960 → 96.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv16` · IPTV (NEO TV)

**Q:** Kateri pogoj (napravo) potrebujem za uporabo NEO TV Lite?

**Maks:**

> ✨ Za uporabo NEO TV Lite potrebujete:
> 
> 
> 
> Naročniško razmerje z internetom in televizijo ter NEO Smartboxom
> Pametni televizor z Android TV (7.0+), Google TV, LG WebOS (6.0+), Samsung Tizen (2018+), Hisense Vidaa (U4+), Philips Saphi OS (2021/2022) ali Titan OS (2023+)
> Aplikacijo NEO TV Lite nameščeno na televizorju
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 86.7/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `smartbox`
- **Relevance — 2/6 = 33%** (weight 20%). Echoed: `lite`, `uporabo`. **Missing** question keyword(s): `kateri`, `napravo`, `pogoj`, `potrebujem`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.33 + 0.15×1 + 0.10×1` = **0.867 → 86.7/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv17` · IPTV (NEO TV)

**Q:** Ali lahko NEO vsebine gledam na računalniku?

**Maks:**

> ✨ Da, NEO vsebine lahko gledate na računalniku preko spletnega mesta neo.io. Prijavite se z istimi podatki kot za Moj Telekom. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `neo.io` / `računalnik` / `splet`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `računalniku`, `vsebine`. **Missing** question keyword(s): `gledam`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv18` · IPTV (NEO TV)

**Q:** Katere vsebine niso na voljo v paketu NEO TV brez interneta?

**Maks:**

> ✨ Paket NEO TV brez interneta omogoča dostop do televizijskih vsebin prek aplikacije NEO, vendar ima določene omejitve glede funkcionalnosti in vsebin. Na voljo so:
> 
> 
> 
> Osnovni TV-programi, ki so vključeni v paket.
> Dostop do aplikacije NEO za ogled vsebin.
> 
> 
> Vendar pa ne vključuje naslednjega:
> - Internetne funkcionalnosti, kot so napredne aplikacije, ki zahtevajo internetno povezavo.
> - Dodatni programski paketi, ki niso del osnovnega paketa.
> 
> 
> Če potrebujete več informacij, mi sporočite! 😊

**Score: 37.0/100  (★★☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `voyo` / `youtube` / `pickbox` / `max` / `igre`
- **Relevance — 3/5 = 60%** (weight 20%). Echoed: `interneta`, `niso`, `voljo`. **Missing** question keyword(s): `katere`, `vsebine`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×0.00 + 0.20×0.60 + 0.15×1 + 0.10×1` = **0.370 → 37.0/100**.
- **Verdict:** Risky: Maks answered confidently with a specific value that does **not** match the site — a candidate factual error.

---

### `tv19` · IPTV (NEO TV)

**Q:** Ali NEO ponuja varno vsebino za otroke (Otroški park)?

**Maks:**

> ✨ Da, naša storitev NEO ponuja možnost varne vsebine za otroke prek funkcije Otroški park. Ta omogoča omejen dostop do vsebin, ki so primerne za otroke, in starševski nadzor. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `otroš` / `otrok`
- **Relevance — 4/6 = 67%** (weight 20%). Echoed: `otroke`, `otroški`, `park`, `ponuja`. **Missing** question keyword(s): `varno`, `vsebino`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv20` · IPTV (NEO TV)

**Q:** Katere programske opcije lahko dodam k paketu NEO?

**Maks:**

> ✨ K paketu NEO lahko dodate številne programske opcije, kot so:
> 
> 
> 
> HBO Premium
> CineStar Premiere
> FilmBox
> PlayKids Learning
> Pink
> Balkan
> Eksplozivni
> Eksplozivni+
> Dajmedol+
> Minimax+
> Šport
> Kultura
> Kitchen TV
> Pickbox NOW
> RUS 5+
> 
> 
> Celoten seznam in pogoje najdete tukaj 👉 tv-vsebine.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `hbo` / `šport` / `sport` / `pink` / `balkan` / `filmbox`
- **Relevance — 2/4 = 50%** (weight 20%). Echoed: `opcije`, `programske`. **Missing** question keyword(s): `dodam`, `katere`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv21` · IPTV (NEO TV)

**Q:** Ali lahko NEO gledam na več napravah hkrati?

**Maks:**

> ✨ Da, NEO lahko gledate na več napravah hkrati. Uporabljate lahko do 8 NEO Smartboxov na eni naročnini, poleg tega pa še aplikacijo NEO na mobilnih napravah in računalniku. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `naprav`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `hkrati`, `napravah`. **Missing** question keyword(s): `gledam`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv22` · IPTV (NEO TV)

**Q:** Kaj je NEO SmartBox?

**Maks:**

> ✨ NEO SmartBox je napredni TV-komunikator, ki omogoča ogled televizije, uporabo aplikacij, glasovno upravljanje, snemanje vsebin, ogled nazaj do 7 dni in še več. Z njim lahko ustvarite profile za družinske člane, uporabljate Otroški park ter razširite WiFi omrežje v vašem domu.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `komunikator` / `predvaj` / `naprav` / `tv`
- **Relevance — 1/1 = 100%** (weight 20%). Echoed: `smartbox`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv23` · IPTV (NEO TV)

**Q:** Ali je za pakete NEO na voljo garancija zadovoljstva?

**Maks:**

> ✨ Da, za pakete NEO je na voljo garancija zadovoljstva. Novi naročniki lahko v 30 dneh od vklopa odstopijo od pogodbe, če niso zadovoljni. Več informacij in obrazec najdete tukaj 👉 Garancija zadovoljstva. Potrebujete še kakšno informacijo? 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 2/2 = 100%** (weight 55%). Expected facts:
    - ✅ found: `30`
    - ✅ found: `garancij`
- **Relevance — 4/4 = 100%** (weight 20%). Echoed: `garancija`, `pakete`, `voljo`, `zadovoljstva`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv24` · IPTV (NEO TV)

**Q:** Kakšna je akcijska cena paketa NEO TV ob 24-mesečni vezavi?

**Maks:**

> ✨ Akcijske cene paketov NEO TV so odvisne od trenutnih promocij in pogojev. Če želite izvedeti več o programskih opcijah, mi prosim sporočite, ali imate televizijske storitve pri nas. 😊

**Score: 15.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `32,99`
- **Relevance — 0/4 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `akcijska`, `kakšna`, `mesečni`, `vezavi`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “prosim sporočite” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.00 + 0.15×1 + 0.10×0` = **0.150 → 15.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `tv25` · IPTV (NEO TV)

**Q:** Do kdaj je NEO TV Lite brezplačen ob nakupu izbranega televizorja?

**Maks:**

> ✨ Ponudba NEO TV Lite brezplačno ob nakupu izbranega televizorja je časovno omejena. Za točne informacije o trajanju akcije priporočam, da preverite pogoje ponudbe na naši spletni strani ali se obrnete na mojega sodelavca za podrobnosti. Bi želeli, da vas povežem? 😊

**Score: 31.0/100  (★★☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `31.12.2026` / `31. 12. 2026` / `konca leta 2026` / `2026`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `izbranega`, `lite`, `nakupu`, `televizorja`. **Missing** question keyword(s): `brezplačen`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “priporočam, da preverite” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.80 + 0.15×1 + 0.10×0` = **0.310 → 31.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `tv26` · IPTV (NEO TV)

**Q:** Koliko TV programov vključuje paket NEO A?

**Maks:**

> ✨ Paket NEO A vključuje programsko shemo Osnovna, ki vsebuje več kot 150 TV programov. Celoten seznam programov si lahko ogledate tukaj 👉 TV-programi v paketu NEO A.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `150`
- **Relevance — 1/1 = 100%** (weight 20%). Echoed: `programov`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv27` · IPTV (NEO TV)

**Q:** Koliko programov ima paket NEO B?

**Maks:**

> ✨ Paket NEO B vključuje programsko shemo Standard, ki vsebuje več kot 210 TV programov. Celoten seznam programov si lahko ogledate tukaj 👉 tv-programi-v-paketu-neo-b.pdf.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `210`
- **Relevance — 1/1 = 100%** (weight 20%). Echoed: `programov`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv28` · IPTV (NEO TV)

**Q:** Koliko TV programov vključuje paket NEO C?

**Maks:**

> ✨ Paket NEO C vključuje televizijo s programsko shemo Mega HD, ki vsebuje več kot 255 TV programov. Celoten seznam programov si lahko ogledate tukaj 👉 TV-programi v paketu NEO C.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `255`
- **Relevance — 1/1 = 100%** (weight 20%). Echoed: `programov`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv29` · IPTV (NEO TV)

**Q:** Katero programsko shemo vključuje paket NEO A?

**Maks:**

> ✨ Paket NEO A vključuje programsko shemo Osnovna. Osnovna shema vsebuje več kot 150 TV programov. Za celoten seznam programov si lahko ogledate tukaj 👉 TV-programi v paketu NEO A.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `osnovna`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `programsko`, `shemo`. **Missing** question keyword(s): `katero`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv30` · IPTV (NEO TV)

**Q:** Katero programsko shemo ima paket NEO B?

**Maks:**

> ✨ Paket NEO B vključuje programsko shemo Standard. Standardna shema vsebuje več kot 210 TV programov. Celoten seznam programov si lahko ogledate tukaj 👉 tv-programi-v-paketu-neo-b.pdf.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `standard`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `programsko`, `shemo`. **Missing** question keyword(s): `katero`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv31` · IPTV (NEO TV)

**Q:** Katero programsko shemo vključuje paket NEO C?

**Maks:**

> ✨ Paket NEO C vključuje programsko shemo Mega HD. Mega shema vključuje več kot 255 TV programov. Celoten seznam programov si lahko ogledate tukaj 👉 TV-programi v paketu NEO C.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `mega hd` / `mega`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `programsko`, `shemo`. **Missing** question keyword(s): `katero`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv32` · IPTV (NEO TV)

**Q:** Koliko stane samostojni TV paket NEO TV (brez interneta)?

**Maks:**

> ✨ NEO TV Lite ni na voljo kot samostojni TV paket brez interneta. Za uporabo potrebujete naročniško razmerje, ki vključuje internet in televizijo z NEO Smartboxom. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 45.0/100  (★★★☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `41 eur` / `41,00` / `41 €`
- **Relevance — 2/2 = 100%** (weight 20%). Echoed: `interneta`, `samostojni`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×0.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **0.450 → 45.0/100**.
- **Verdict:** Risky: Maks answered confidently with a specific value that does **not** match the site — a candidate factual error.

---

### `tv33` · IPTV (NEO TV)

**Q:** Koliko programov ima samostojni paket NEO TV?

**Maks:**

> ✨ Samostojni paket NEO TV vključuje osnovni nabor TV-programov, vendar točno število programov ni navedeno v razpoložljivi bazi znanja. Želite, da vas povežem z mojim sodelavcem za podrobnejše informacije? Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 35.0/100  (★★☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `210`
- **Relevance — 2/2 = 100%** (weight 20%). Echoed: `programov`, `samostojni`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “povežem z mojim sodelavcem” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×1.00 + 0.15×1 + 0.10×0` = **0.350 → 35.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `tv34` · IPTV (NEO TV)

**Q:** Koliko dni nazaj lahko gledam vsebine z ogledom nazaj?

**Maks:**

> ✨ Z ogledom nazaj lahko gledate izbrane TV-vsebine do 7 dni nazaj. Storitev je vključena v vse naše TV pakete. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 95.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `7 dni` / `7-dnev` / `7`
- **Relevance — 3/4 = 75%** (weight 20%). Echoed: `nazaj`, `ogledom`, `vsebine`. **Missing** question keyword(s): `gledam`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “7 dni”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.75 + 0.15×1 + 0.10×1` = **0.950 → 95.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv35` · IPTV (NEO TV)

**Q:** Ali lahko pri NEO snemam oddaje?

**Maks:**

> ✨ Da, pri NEO lahko snemate oddaje na vseh platformah: NEO Smartbox, spletno mesto NEO.io in aplikacijo NEO Pametno življenje. Posneti je mogoče le celotno oddajo, ki ima ikono krogca. Podrobna navodila s slikami najdete tukaj 👉 snemalnik.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `snema` / `posne`
- **Relevance — 1/2 = 50%** (weight 20%). Echoed: `oddaje`. **Missing** question keyword(s): `snemam`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv36` · IPTV (NEO TV)

**Q:** Koliko stane najem vsakega dodatnega TV-komunikatorja (NEO Smartbox)?

**Maks:**

> ✨ Najem vsakega dodatnega TV-komunikatorja NEO Smartbox stane 3,90 € na mesec za posamezno napravo. Na eno naročnino lahko najamete do 8 NEO Smartboxov. Dodatni Smartbox lahko naročite v Moj Telekomu. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `3,90`
- **Relevance — 5/5 = 100%** (weight 20%). Echoed: `dodatnega`, `komunikatorja`, `najem`, `smartbox`, `vsakega`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv37` · IPTV (NEO TV)

**Q:** Ali je najem prvega TV-komunikatorja brezplačen?

**Maks:**

> ✨ Najem prvega NEO Smartbox TV-komunikatorja je vključen v naročnino paketa z IP-televizijo, zato za prvega komunikatorja ne plačate dodatne najemnine. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 95.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `brezplač` / `vključen`
- **Relevance — 3/4 = 75%** (weight 20%). Echoed: `komunikatorja`, `najem`, `prvega`. **Missing** question keyword(s): `brezplačen`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.75 + 0.15×1 + 0.10×1` = **0.950 → 95.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv38` · IPTV (NEO TV)

**Q:** Koliko znaša strošek izdaje TV-komunikatorja NEO Smartbox?

**Maks:**

> ✨ Strošek najema dodatnega TV-komunikatorja NEO Smartbox znaša 3,90 € na mesec za vsak dodatni Smartbox. Na eno naročnino lahko najamete do 8 NEO Smartboxov. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 41.0/100  (★★★☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `29 eur` / `29,00` / `29 €`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `komunikatorja`, `smartbox`, `strošek`, `znaša`. **Missing** question keyword(s): `izdaje`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×0.00 + 0.20×0.80 + 0.15×1 + 0.10×1` = **0.410 → 41.0/100**.
- **Verdict:** Risky: Maks answered confidently with a specific value that does **not** match the site — a candidate factual error.

---

### `tv39` · IPTV (NEO TV)

**Q:** Kaj je NEO TV Lite?

**Maks:**

> ✨ NEO TV Lite je aplikacija, ki vam omogoča ogled TV-programov, vsebin na zahtevo, snemanje in ogled nazaj do 7 dni neposredno na pametnem televizorju (Android TV, Google TV, LG WebOS, Samsung Tizen, Hisense Vidaa, Philips Saphi OS ali Titan OS). Potrebujete naročniško razmerje z internetom, televizijo in NEO Smartboxom. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 2/2 = 100%** (weight 55%). Expected facts:
    - ✅ found: `aplikacij`
    - ✅ found: `pametn` / `televizor`
- **Relevance — 1/1 = 100%** (weight 20%). Echoed: `lite`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv40` · IPTV (NEO TV)

**Q:** Koliko stane NEO TV Lite na napravo mesečno?

**Maks:**

> ✨ NEO TV Lite stane 1,90 EUR na mesec za posamezno napravo. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `1,90`
- **Relevance — 2/2 = 100%** (weight 20%). Echoed: `lite`, `napravo`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv41` · IPTV (NEO TV)

**Q:** Na koliko pametnih televizorjih lahko uporabljam NEO TV Lite?

**Maks:**

> ✨ NEO TV Lite lahko uporabljate na največ petih pametnih televizorjih hkrati. Potrebujete ustrezno naročniško razmerje in aktivirano aplikacijo na vsaki napravi. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 95.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `5` / `pet`
- **Relevance — 3/4 = 75%** (weight 20%). Echoed: `lite`, `pametnih`, `televizorjih`. **Missing** question keyword(s): `uporabljam`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.75 + 0.15×1 + 0.10×1` = **0.950 → 95.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv42` · IPTV (NEO TV)

**Q:** Na katerih pametnih televizorjih deluje NEO TV Lite?

**Maks:**

> ✨ NEO TV Lite deluje na pametnih televizorjih z naslednjimi operacijskimi sistemi:
> 
> 
> 
> Android TV (7.0 Nougat ali novejši)
> Google TV
> LG webOS (6.0 ali novejši)
> Samsung Tizen (2018 ali novejši)
> Hisense Vidaa (serija U4 in novejši)
> Philips Saphi OS (2021, 2022) in Titan OS (2023 ali novejši)
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 96.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 3/3 = 100%** (weight 55%). Expected facts:
    - ✅ found: `samsung` / `tizen`
    - ✅ found: `lg` / `webos`
    - ✅ found: `android` / `hisense` / `philips`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `deluje`, `lite`, `pametnih`, `televizorjih`. **Missing** question keyword(s): `katerih`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.80 + 0.15×1 + 0.10×1` = **0.960 → 96.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv43` · IPTV (NEO TV)

**Q:** Kateri pogoj (napravo) potrebujem za uporabo NEO TV Lite?

**Maks:**

> ✨ Za uporabo NEO TV Lite potrebujete:
> 
> 
> 
> Naročniško razmerje z internetom in televizijo (IPTV) ter NEO Smartboxom.
> Pametni televizor z Android TV (7.0+), Google TV, LG WebOS (6.0+), Samsung Tizen (2018+), Hisense Vidaa (U4+), Philips Saphi OS (2021/2022) ali Titan OS (2023+).
> Aplikacijo NEO TV Lite iz trgovine aplikacij na vašem televizorju.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 86.7/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `smartbox`
- **Relevance — 2/6 = 33%** (weight 20%). Echoed: `lite`, `uporabo`. **Missing** question keyword(s): `kateri`, `napravo`, `pogoj`, `potrebujem`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.33 + 0.15×1 + 0.10×1` = **0.867 → 86.7/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv44` · IPTV (NEO TV)

**Q:** Do kdaj je NEO TV Lite brezplačen ob nakupu izbranega televizorja?

**Maks:**

> ✨ Ponudba NEO TV Lite brezplačno ob nakupu izbranega televizorja je običajno časovno omejena. Za točne informacije o trajanju te akcije priporočam, da preverite pogoje ponudbe na naši spletni strani ali pa mi sporočite več podrobnosti, da vam lahko bolje pomagam. 😊 
> 
> 
> Vas zanima še kaj?

**Score: 31.0/100  (★★☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `31.12.2026` / `31. 12. 2026` / `konca leta 2026` / `2026`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `izbranega`, `lite`, `nakupu`, `televizorja`. **Missing** question keyword(s): `brezplačen`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “priporočam, da preverite” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.80 + 0.15×1 + 0.10×0` = **0.310 → 31.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `tv45` · IPTV (NEO TV)

**Q:** Kje na spletu (računalnik) lahko gledam NEO vsebine?

**Maks:**

> ✨ NEO vsebine lahko na računalniku spremljate preko spletnega mesta neo.io. Prijavite se z istimi podatki kot za Moj Telekom. Po prijavi izberete razmerje in privzeti NEO Smartbox, nato pa dostopate do vseh vsebin. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 85.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `neo.io` / `računalnik`
- **Relevance — 1/4 = 25%** (weight 20%). Echoed: `vsebine`. **Missing** question keyword(s): `gledam`, `računalnik`, `spletu`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.25 + 0.15×1 + 0.10×1` = **0.850 → 85.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv46` · IPTV (NEO TV)

**Q:** Koliko stane programski dodatek NEO igre na mesec?

**Maks:**

> ✨ Programski dodatek NEO Igre stane 8 EUR na mesec. Prvi mesec je igranje brezplačno, nato se začne redno zaračunavanje. Če izberete vezavo za 24 mesecev ob fiksnem paketu s televizijo, je cena 4 EUR na mesec. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `7,99` / `8 eur` / `8,00`
- **Relevance — 3/3 = 100%** (weight 20%). Echoed: `dodatek`, `igre`, `programski`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv47` · IPTV (NEO TV)

**Q:** Kako se od 1. 8. 2025 imenuje TV-opcija, prej znana kot Max?

**Maks:**

> ✨ Trenutno v naši bazi ni podatka o preimenovanju TV-opcije, prej znane kot Max, od 1. 8. Prosimo, povejte, ali želite, da vas povežem s sodelavcem za dodatne informacije?

**Score: 4.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `hbo max` / `hbo`
- **Relevance — 1/5 = 20%** (weight 20%). Echoed: `prej`. **Missing** question keyword(s): `2025`, `imenuje`, `opcija`, `znana`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “vas povežem s sodelavcem” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.20 + 0.15×0 + 0.10×0` = **0.040 → 4.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `tv48` · IPTV (NEO TV)

**Q:** Ali je programska opcija Da Vinci Kids brezplačna?

**Maks:**

> Cena programske opcije Da Vinci je 3,99 EUR/mesec.
> Več o programski opciji Da Vinci si oglejte spodaj 👇

**Score: 84.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `brezplač` / `da vinci`
- **Relevance — 1/5 = 20%** (weight 20%). Echoed: `vinci`. **Missing** question keyword(s): `brezplačna`, `kids`, `opcija`, `programska`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “3.99 eur”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.20 + 0.15×1 + 0.10×1` = **0.840 → 84.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv49` · IPTV (NEO TV)

**Q:** Katere športne programske opcije lahko dodam k NEO?

**Maks:**

> ✨ Na voljo je športna programska opcija Šport, ki vključuje 10 športnih programov (vse Arena Sport in Šport TV) z ogledom nazaj do 7 dni. Cena je 4,90 EUR/mesec (akcijska do 30. 6. 2026). Po tem obdobju velja redna cena.
> 
> 
> Več informacij najdete tukaj 👉 tv-vsebine
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 80.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `šport` / `sport` / `arena` / `sport tv`
- **Relevance — 0/5 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `dodam`, `katere`, `opcije`, `programske`, `športne`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “7 dni”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.00 + 0.15×1 + 0.10×1` = **0.800 → 80.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv50` · IPTV (NEO TV)

**Q:** Katere filmske/serijske opcije lahko dodam k NEO (naštej eno)?

**Maks:**

> ✨ Na voljo je opcija HBO Max, ki vam omogoča dostop do široke izbire priljubljenih filmov in serij. 
> 
> 
> Vam lahko še kaj pomagam? 😊

**Score: 65.0/100  (★★★★☆)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `hbo` / `pickbox` / `filmbox` / `cinestar` / `pink` / `balkan`
- **Relevance — 0/6 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `dodam`, `filmske`, `katere`, `naštej`, `opcije`, `serijske`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.00 + 0.15×0 + 0.10×1` = **0.650 → 65.0/100**.
- **Verdict:** Partial: some but not all expected facts were stated.

---

### `tv51` · IPTV (NEO TV)

**Q:** Katere vsebine niso na voljo v paketu NEO TV brez interneta?

**Maks:**

> ✨ Paket NEO TV brez interneta vključuje dostop do televizijskih programov, vendar ne omogoča vseh funkcionalnosti, ki so na voljo v kombinaciji z internetom. Na primer:
> 
> 
> 
> Brez dostopa do aplikacij: Aplikacije, ki zahtevajo internetno povezavo (npr. YouTube, Netflix), niso na voljo.
> Omejena interaktivnost: Funkcije, kot so glasovno upravljanje, ogled nazaj in videoteke, so lahko omejene ali nedostopne.
> 
> 
> Za podrobnosti o vsebini paketa priporočam, da preverite našo ponudbo ali vprašate mojega sodelavca. Želite, da vas povežem? 😊

**Score: 92.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `voyo` / `youtube` / `pickbox` / `max` / `igre`
- **Relevance — 3/5 = 60%** (weight 20%). Echoed: `interneta`, `niso`, `voljo`. **Missing** question keyword(s): `katere`, `vsebine`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1) (a redirect phrase “želite, da vas povežem” is present, but fact recall ≥ 34%, so it is *not* treated as a deflection).
- **Weighted total:** `0.55×1.00 + 0.20×0.60 + 0.15×1 + 0.10×1` = **0.920 → 92.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv52` · IPTV (NEO TV)

**Q:** Ali NEO ponuja varno vsebino za otroke (Otroški park)?

**Maks:**

> ✨ Da, naša storitev NEO ponuja možnost varne vsebine za otroke, imenovano Otroški park. Ta omogoča otrokom dostop le do vsebin, ki so primerne njihovi starosti, in omogoča starševski nadzor. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `otroš` / `otrok`
- **Relevance — 4/6 = 67%** (weight 20%). Echoed: `otroke`, `otroški`, `park`, `ponuja`. **Missing** question keyword(s): `varno`, `vsebino`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv53` · IPTV (NEO TV)

**Q:** Kaj je NEO SmartBox?

**Maks:**

> ✨ NEO Smartbox je napredni TV komunikator, ki omogoča ogled televizije, uporabo aplikacij, glasovno upravljanje, snemanje vsebin in dostop do interneta. Z njim lahko ustvarite profile za družinske člane, uporabljate otroški park in celo razširite WiFi omrežje v vašem domu. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `komunikator` / `predvaj` / `naprav` / `tv`
- **Relevance — 1/1 = 100%** (weight 20%). Echoed: `smartbox`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv54` · IPTV (NEO TV)

**Q:** S katerima protokoloma lahko brezžično predvajam vsebine na TV?

**Maks:**

> ✨ Za brezžično predvajanje vsebin na TV z aplikacijo NEO lahko uporabite protokola Chromecast in Airplay. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 84.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `chromecast` / `airplay`
- **Relevance — 1/5 = 20%** (weight 20%). Echoed: `brezžično`. **Missing** question keyword(s): `katerima`, `predvajam`, `protokoloma`, `vsebine`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.20 + 0.15×1 + 0.10×1` = **0.840 → 84.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv55` · IPTV (NEO TV)

**Q:** Kaj omogoča virtualni daljinec pri NEO?

**Maks:**

> ✨ Virtualni daljinec pri NEO omogoča upravljanje NEO Smartboxa preko mobilne naprave ali tablice, kot bi uporabljali fizični daljinec. Z njim lahko:
> 
> 
> 
> upravljate TV vsebine,
> preklapljate programe,
> prilagajate glasnost,
> uporabljate glasovne ukaze.
> 
> 
> Za uporabo potrebujete ustrezno aplikacijo in povezavo z NEO Smartboxom. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `glasovn` / `mobitel` / `upravlja`
- **Relevance — 3/3 = 100%** (weight 20%). Echoed: `daljinec`, `omogoča`, `virtualni`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv56` · IPTV (NEO TV)

**Q:** Ali je za pakete NEO na voljo garancija zadovoljstva?

**Maks:**

> ✨ Da, za pakete NEO je na voljo garancija zadovoljstva. Novi naročniki lahko v 30 dneh od vklopa odstopite od pogodbe brez poplačila pogodbene obveznosti. Več informacij 👉 Garancija zadovoljstva. Potrebujete še kakšno informacijo? 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `30` / `garancij`
- **Relevance — 4/4 = 100%** (weight 20%). Echoed: `garancija`, `pakete`, `voljo`, `zadovoljstva`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv57` · IPTV (NEO TV)

**Q:** Kakšna je akcijska cena paketa NEO TV ob 24-mesečni vezavi?

**Maks:**

> ✨ Akcijske cene paketov NEO TV so odvisne od trenutnih promocij in pogojev vezave. Za točno ponudbo vas prosim, da preverite na naši spletni strani ali pa mi sporočite, če želite, da vas povežem z mojim sodelavcem za podrobnejše informacije. Bi želeli nadaljevati? 😊

**Score: 15.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `32,99`
- **Relevance — 0/4 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `akcijska`, `kakšna`, `mesečni`, `vezavi`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “povežem z mojim sodelavcem” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.00 + 0.15×1 + 0.10×0` = **0.150 → 15.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `tv58` · IPTV (NEO TV)

**Q:** Ali lahko NEO gledam na več napravah?

**Maks:**

> ✨ Da, NEO lahko gledate na več napravah: na televizorju, računalniku (neo.io), mobilni napravi in s pomočjo aplikacije NEO TV Lite na pametnih televizorjih. Potrebujete aktivno naročnino z vsaj enim NEO Smartboxom. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `naprav`
- **Relevance — 1/2 = 50%** (weight 20%). Echoed: `napravah`. **Missing** question keyword(s): `gledam`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv59` · IPTV (NEO TV)

**Q:** Kolikšen popust na naročnino prinaša akcija pri paketu NEO TV?

**Maks:**

> ✨ Akcije za obstoječe naročnike vključujejo dve kategoriji:
> 
> 
> 
> 🛍️ Izdelki (mobilni in fiksni uporabniki)
> 📺 Programske opcije (samo za fiksne naročnike s TV storitvami)
> 
> 
> Ali vas zanima katera od teh možnosti? 😊

**Score: 15.0/100  (★☆☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `8` / `8,01`
- **Relevance — 0/5 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `akcija`, `kolikšen`, `naročnino`, `popust`, `prinaša`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “mobi”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “ali vas zanima” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.00 + 0.15×1 + 0.10×0` = **0.150 → 15.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `tv60` · IPTV (NEO TV)

**Q:** Ali paket NEO TV omogoča ogled programskih opcij, ki potrebujejo internet?

**Maks:**

> ✨ Paket NEO TV ne omogoča ogleda programskih opcij in aplikacij, ki za delovanje potrebujejo internet (npr. VOYO, YouTube, NEO Igre, Max, Pickbox NOW). Na voljo je le televizija s programsko shemo Standard in ogledom nazaj do 7 dni.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 96.7/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `ne` / `brez internet` / `ni mogoč`
- **Relevance — 5/6 = 83%** (weight 20%). Echoed: `internet`, `omogoča`, `opcij`, `potrebujejo`, `programskih`. **Missing** question keyword(s): `ogled`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.83 + 0.15×1 + 0.10×1` = **0.967 → 96.7/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv61` · IPTV (NEO TV)

**Q:** Koliko stane najem TV-komunikatorja BOX S na mesec?

**Maks:**

> ✨ Najem dodatnega NEO Smartboxa (TV komunikatorja) znaša 3,90 € na mesec za posamezno napravo. Na eno naročnino lahko najamete do 8 NEO Smartboxov. Dodatni Smartbox lahko naročite v Moj Telekom. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `3,90`
- **Relevance — 2/2 = 100%** (weight 20%). Echoed: `komunikatorja`, `najem`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “naj”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv62` · IPTV (NEO TV)

**Q:** Koliko stane dodatna telefonska številka pri fiksnem paketu (IP-telefonija)?

**Maks:**

> ✨ Dodatna IP-telefonska številka pri fiksnem paketu NEO stane 2 EUR na mesec na številko. Vsaka številka vključuje neomejene klice v vsa slovenska omrežja. Na paket lahko dodate največ dve številki.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 41.0/100  (★★★☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `1,27`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `dodatna`, `fiksnem`, `telefonska`, `številka`. **Missing** question keyword(s): `telefonija`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×0.00 + 0.20×0.80 + 0.15×1 + 0.10×1` = **0.410 → 41.0/100**.
- **Verdict:** Risky: Maks answered confidently with a specific value that does **not** match the site — a candidate factual error.

---

### `tv63` · IPTV (NEO TV)

**Q:** Katero shemo (koliko programov) ima najvišji paket NEO C?

**Maks:**

> ✨ Paket NEO C vključuje programsko shemo Mega HD, ki vsebuje več kot 255 TV programov. Celoten seznam programov si lahko ogledate tukaj 👉 TV-programi v paketu NEO C.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `mega` / `255`
- **Relevance — 2/4 = 50%** (weight 20%). Echoed: `programov`, `shemo`. **Missing** question keyword(s): `katero`, `najvišji`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv64` · IPTV (NEO TV)

**Q:** Ali lahko NEO TV Lite uporabljam na televizorju LG?

**Maks:**

> ✨ Da, NEO TV Lite lahko uporabljate na televizorju LG z operacijskim sistemom webOS TV, različica 6.0 ali novejša. Pred namestitvijo preverite, ali je aplikacija na voljo v trgovini z aplikacijami vašega televizorja. Potrebujete še naročniško razmerje z internetom, televizijo in NEO Smartboxom. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 93.3/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `lg` / `webos` / `da`
- **Relevance — 2/3 = 67%** (weight 20%). Echoed: `lite`, `televizorju`. **Missing** question keyword(s): `uporabljam`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×1 + 0.10×1` = **0.933 → 93.3/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv65` · IPTV (NEO TV)

**Q:** Ali lahko NEO TV Lite uporabljam na televizorju Samsung?

**Maks:**

> ✨ Da, NEO TV Lite lahko uporabljate na televizorju Samsung z operacijskim sistemom Tizen (letnik 2018 in novejši). Preverite v trgovini z aplikacijami na vašem televizorju, ali je aplikacija na voljo. Potrebujete še naročniško razmerje z internetom in televizijo ter NEO Smartbox.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 95.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `samsung` / `tizen` / `da`
- **Relevance — 3/4 = 75%** (weight 20%). Echoed: `lite`, `samsung`, `televizorju`. **Missing** question keyword(s): `uporabljam`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.75 + 0.15×1 + 0.10×1` = **0.950 → 95.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv66` · IPTV (NEO TV)

**Q:** Ali NEO TV Lite omogoča snemanje in ogled nazaj?

**Maks:**

> ✨ Da, NEO TV Lite omogoča snemanje vsebin in ogled nazaj do 7 dni na največ 5 različnih pametnih televizorjih. Potrebujete aktivno naročnino na internet in IP-televizijo ter vsaj en NEO Smartbox. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `snema` / `ogled nazaj` / `7 dni`
- **Relevance — 5/5 = 100%** (weight 20%). Echoed: `lite`, `nazaj`, `ogled`, `omogoča`, `snemanje`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv67` · IPTV (NEO TV)

**Q:** Ali je NEO TV Lite na voljo pri paketu Net (brez televizije)?

**Maks:**

> ✨ NEO TV Lite ni na voljo pri paketih brez televizije (npr. Net). Za uporabo potrebujete paket, ki vključuje internet in televizijo z NEO Smartboxom. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `ne` / `ni na voljo` / `brez televiz`
- **Relevance — 3/3 = 100%** (weight 20%). Echoed: `lite`, `televizije`, `voljo`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv68` · IPTV (NEO TV)

**Q:** Ali je NEO najboljša TV-izkušnja po mnenju uporabnikov?

**Maks:**

> ✨ NEO ponuja vrhunsko TV-izkušnjo z enotnim videzom in delovanjem na vseh napravah, glasovnim upravljanjem v slovenščini ter številnimi naprednimi funkcijami. Uporabniki cenijo enostavno uporabo, dostopnost in bogato ponudbo vsebin. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 80.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `najbolj` / `uporabnik` / `izkušnj`
- **Relevance — 0/4 = 0%** (weight 20%). Echoed: —. **Missing** question keyword(s): `izkušnja`, `mnenju`, `najboljša`, `uporabnikov`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.00 + 0.15×1 + 0.10×1` = **0.800 → 80.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv69` · IPTV (NEO TV)

**Q:** Ali lahko NEO 5G uporabljam za televizijo, kjer ni optike?

**Maks:**

> ✨ Da, NEO 5G lahko uporabljate za televizijo tudi tam, kjer optika ni na voljo. Deluje prek našega mobilnega omrežja in omogoča hitro ter stabilno internetno in TV-izkušnjo brez posegov v dom. 
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 90.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `neo 5g` / `5g` / `brez optike`
- **Relevance — 2/4 = 50%** (weight 20%). Echoed: `kjer`, `televizijo`. **Missing** question keyword(s): `optike`, `uporabljam`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.50 + 0.15×1 + 0.10×1` = **0.900 → 90.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv70` · IPTV (NEO TV)

**Q:** Koliko programov (vsaj) ponuja programska shema Standard?

**Maks:**

> ✨Programska shema Standard vključuje več kot 210 TV programov. Celoten seznam si lahko ogledate tukaj 👉 TV-programi v shemi Standard.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 78.3/100  (★★★★☆)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `210`
- **Relevance — 4/6 = 67%** (weight 20%). Echoed: `programov`, `programska`, `shema`, `standard`. **Missing** question keyword(s): `ponuja`, `vsaj`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.67 + 0.15×0 + 0.10×1` = **0.783 → 78.3/100**.
- **Verdict:** Partial: some but not all expected facts were stated.

---

### `tv71` · IPTV (NEO TV)

**Q:** Ali NEO ponuja videoteke (vsebine na zahtevo)?

**Maks:**

> ✨ Na NEO Smartboxu so na voljo številne videoteke, kot so DKino, HBO OD, Pickbox, Minimax+, VOYO, Da Vinci, Pickbox NOW in Dajmedol+. Dostopate lahko prek menija ali glasovnega ukaza. Več informacij najdete tukaj 👉 Videoteke na NEO.
> 
> 
> Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 85.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `videotek` / `na zahtevo` / `vod`
- **Relevance — 1/4 = 25%** (weight 20%). Echoed: `videoteke`. **Missing** question keyword(s): `ponuja`, `vsebine`, `zahtevo`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.25 + 0.15×1 + 0.10×1` = **0.850 → 85.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv72` · IPTV (NEO TV)

**Q:** Ali lahko med gledanjem TV z mini predvajalnikom brskam po spletu?

**Maks:**

> ✨ Da, z Mini TV-vmesnikom lahko hkrati gledate televizijo in brskate po spletu, če je vaš internetni paket dovolj zmogljiv. Vse je odvisno od hitrosti vaše internetne povezave in števila naprav, ki so hkrati povezane.
> 
> 
> Če potrebujete dodatne informacije o vašem paketu ali hitrosti interneta, mi sporočite! 😊

**Score: 73.0/100  (★★★★☆)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `mini` / `brska` / `hkrati`
- **Relevance — 2/5 = 40%** (weight 20%). Echoed: `mini`, `spletu`. **Missing** question keyword(s): `brskam`, `gledanjem`, `predvajalnikom`
- **Specificity — 0/1** (weight 15%): **missing** a concrete value — the answer states none of a price (`€`/`EUR`), a data amount (`GB`/`MB`/`TB`), a speed (`Mbit`/`Gbit`/`kbit`), a duration (`dni`), a channel count (`program`), a percentage, or a package name (`Naj`/`Mobi`/`NEO`/`SUPR`).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.40 + 0.15×0 + 0.10×1` = **0.730 → 73.0/100**.
- **Verdict:** Partial: some but not all expected facts were stated.

---

### `tv73` · IPTV (NEO TV)

**Q:** Kakšen je strošek izdaje za NEO Smartbox (enkratno)?

**Maks:**

> ✨ Enkratni strošek izdaje za NEO Smartbox ni naveden v razpoložljivih podatkih. Če želite natančno informacijo o enkratni izdaji, vam priporočam, da povprašate mojega sodelavca. Želite, da vas povežem? Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 27.0/100  (★★☆☆☆)**

**How this score was reached:**

- **Fact recall — 0/1 = 0%** (weight 55%). Expected facts:
    - ❌ missing: `29 eur` / `29,00` / `29 €`
- **Relevance — 3/5 = 60%** (weight 20%). Echoed: `izdaje`, `smartbox`, `strošek`. **Missing** question keyword(s): `enkratno`, `kakšen`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — yes** (weight 10% → 0): matched redirect phrase “želite, da vas povežem” and fact recall < 34%, so this counts as a non-answer.
- **Weighted total:** `0.55×0.00 + 0.20×0.60 + 0.15×1 + 0.10×0` = **0.270 → 27.0/100**.
- **Verdict:** Weak: Maks deflected/redirected instead of giving the fact.

---

### `tv74` · IPTV (NEO TV)

**Q:** Ali paket NEO A vključuje programsko shemo Osnovna?

**Maks:**

> ✨ Da, paket NEO A vključuje programsko shemo Osnovna. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 100.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `osnovna`
- **Relevance — 3/3 = 100%** (weight 20%). Echoed: `osnovna`, `programsko`, `shemo`. **Missing:** none — every question keyword appeared.
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×1.00 + 0.15×1 + 0.10×1` = **1.000 → 100.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---

### `tv75` · IPTV (NEO TV)

**Q:** Koliko različnih pametnih TV podpira NEO TV Lite hkrati?

**Maks:**

> ✨ NEO TV Lite lahko namestite in aktivirate na največ petih različnih pametnih televizorjih hkrati. Potrebujete še kakšno informacijo? Kar povejte 😊

**Score: 96.0/100  (★★★★★)**

**How this score was reached:**

- **Fact recall — 1/1 = 100%** (weight 55%). Expected facts:
    - ✅ found: `5` / `pet`
- **Relevance — 4/5 = 80%** (weight 20%). Echoed: `hkrati`, `lite`, `pametnih`, `različnih`. **Missing** question keyword(s): `podpira`
- **Specificity — 1/1** (weight 15%): a concrete token is present (matched on “neo”).
- **Deflection — no** (weight 10% → 1).
- **Weighted total:** `0.55×1.00 + 0.20×0.80 + 0.15×1 + 0.10×1` = **0.960 → 96.0/100**.
- **Verdict:** Strong: the answer states the published fact(s) and stays on topic.

---
