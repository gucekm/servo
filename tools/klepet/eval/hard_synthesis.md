# Maks — hard multi-turn synthesis probes

Ten scenarios, each a **single conversation** whose turns force Maks to carry context and *combine* facts (arithmetic, conditional rules, tradeoffs, anaphora, false-premise correction) — not retrieve one value. Graded by me (LLM judge) against a ground-truth synthesis target. PASS ≥ 85 · PARTIAL 50–84 · FAIL < 50.

## Summary

- Scenarios: **10**  ·  mean **64/100**
- ✅ PASS **5**  ·  🟡 PARTIAL **2**  ·  ❌ FAIL **3**

| id | Scenario | Type | Verdict | Score |
|---|---|---|:--:|--:|
| `hs01` | Total cost promo→regular (Mobi C) | arithmetic | ✅ PASS | 95 |
| `hs02` | Bundle + Poveži in prihrani discount | composition | 🟡 PARTIAL | 50 |
| `hs03` | Shifting-constraint recommendation | context-update | ❌ FAIL | 20 |
| `hs04` | Mobi C vs Naj B over a year | comparison-math | 🟡 PARTIAL | 55 |
| `hs05` | Anaphora carryover | anaphora | ❌ FAIL | 25 |
| `hs06` | Rule composition / eligibility | rules | ✅ PASS | 95 |
| `hs07` | Two different data limits | constraints | ✅ PASS | 95 |
| `hs08` | Device + package + insurance total | arithmetic | ❌ FAIL | 30 |
| `hs09` | Roaming scenario (EU vs Balkan) | rules | ✅ PASS | 90 |
| `hs10` | False-premise correction | robustness | ✅ PASS | 90 |

**What holds up:** arithmetic when the opener is concrete (hs01), conditional-rule composition (hs06), keeping two different limits apart (hs07), roaming EU-vs-Balkan (hs09), and resisting false premises (hs10).

**Where it breaks:** open-ended recommendations that shift across turns (hs03), anaphora / referring back to ‘that package’ (hs05), and multi-fact arithmetic that needs a value carried from an earlier turn (hs08). A recurring trigger: when the first turn is an open ‘what do you recommend / which package’, Maks deflects (fiksni vs mobilni) and then loses the thread.

**Notable:** hs07 answers the Mobi C 200 GB throttle **correctly**, the same fact it got **wrong** (‘1 GB’) as a standalone question — its answers are not consistent between phrasings/runs. hs03 also **hallucinated** a non-existent package (‘Največ’).

---

## Scenarios

### ✅ `hs01` — Total cost promo→regular (Mobi C)  ·  95/100 (PASS)

*Type: arithmetic. Target: Mobi C promo 6,99 € (6 mo) then 13,99 €. Yr1 = 6×6,99+6×13,99 = 125,88 €; Yr2 = 12×13,99 = 167,88 €; 24-mo avg ≈ 293,76/24 = 12,24 €/mo.*

**T1 — You:** Koliko plačam za Mobi C v prvem letu?
**Maks:** ✨ Paket Mobi C lahko do 31. 8. 2026 vključite po akcijski ceni 6,99 EUR/mesec za prvih 6 mesecev, nato 13,99 EUR/mesec za naslednjih 6 mesecev. Skupaj v enem letu: 6 x 6,99 EUR + 6 x 13,99 EUR = 125,88 EUR.   Potrebujete še kakšno informacijo? Kar povejte 😊

**T2 — You:** In v drugem letu, ko akcija poteče?
**Maks:** ✨ V drugem letu je cena paketa Mobi C 13,99 EUR/mesec, torej za 12 mesecev skupaj 167,88 EUR. Če imate še kakšno vprašanje, sem vam na voljo!

**T3 — You:** Kolikšna je povprečna mesečna cena čez 24 mesecev?
**Maks:** ✨ Povprečna mesečna cena paketa Mobi C v 24 mesecih je:   (125,88 EUR + 167,88 EUR) / 24 = 12,24 EUR na mesec.   Vam lahko svetujem še pri čem?

**Verdict:** Full arithmetic done correctly and carried across all three turns: 6×6,99 + 6×13,99 = 125,88 € (yr1), 167,88 € (yr2), average 12,24 €/mo. Exactly the target. Genuine multi-step synthesis.

---

### 🟡 `hs02` — Bundle + Poveži in prihrani discount  ·  50/100 (PARTIAL)

*Type: composition. Target: Naj B 27,99 € + Net 39 € = 66,99 €; Poveži in prihrani −5 € (needs fixed on same account) → mobile net 22,99 €; total 61,99 €.*

**T1 — You:** Imam Naj B in doma fiksni paket Net. Koliko skupaj plačam?
**Maks:** ✨ Če imate mobilni paket Naj B in fiksni paket Net, lahko kot novi naročnik za Net plačujete promocijsko ceno 24,99 EUR/mesec za 12 mesecev (velja na omrežjih OŠO, ne velja za RUNE). Redna cena paketa Net je 39 EUR/mesec. Cena paketa Naj B ostane nespremenjena.    Vas zanima še kaj glede kombinacij ali dodatnih ugodnosti?

**T2 — You:** Se pri tem upošteva popust Poveži in prihrani?
**Maks:** ✨ Da, pri kombinaciji mobilnega paketa Naj B in fiksnega paketa Net se upošteva popust Poveži in prihrani. S tem popustom je mesečna naročnina za paket Net lahko še nižja.    Želite podrobnejši izračun ali vas zanima, kako pridobite ta popust?

**T3 — You:** Kolikšna je torej neto mesečna cena mobilnega dela?
**Maks:** ✨ Neto mesečna cena za mobilni paket Naj B z ugodnostjo Poveži in prihrani znaša 19,66 EUR (brez DDV). Če potrebujete še izračun za fiksni del ali skupno ceno, mi sporočite!

**Verdict:** Applies the Poveži in prihrani discount concept and keeps context, but the number is wrong and no clean total is ever given. It quotes 19,66 € ‘brez DDV’ for Naj B — that is Naj C’s ex-VAT discounted figure; Naj B with −5 € is 22,99 € (with VAT). It also silently switches to ex-VAT and never sums mobile + fixed. Right idea, wrong composition.

---

### ❌ `hs03` — Shifting-constraint recommendation  ·  20/100 (FAIL)

*Type: context-update. Target: Should update pick as constraints change: ~Naj A (20 GB) → weigh EU allowance → unlimited pushes to Naj B (41,71 GB EU) or Mobi C. Must reflect the delta.*

**T1 — You:** Porabim 15 GB, ne potujem. Kaj priporočaš?
**Maks:** Da bom lažje našel najboljšo rešitev, mi povejte, ali se zanimate za fiksni 🏠 ali mobilni 📱 internet.

**T2 — You:** Zdaj pa recimo, da mesečno potujem po EU. Se priporočilo spremeni?
**Maks:** ✨ Če pogosto potujete po EU, večina mobilnih paketov že vključuje podatke za EU brez dodatnih stroškov. Za več podatkov lahko dodate zakup. 👉 Več informacij.

**T3 — You:** In če želim še neomejene podatke doma?
**Maks:** ✨ Za neomejene podatke doma priporočamo mobilni paket z neomejenim prenosom podatkov, kot je Največ. Preverite podrobnosti 👉 Mobilni paketi.

**Verdict:** Opens with a deflection (fiksni/mobilni clarify) instead of recommending, never tracks the 15 GB / EU-travel / unlimited constraints as they change, and finally recommends ‘Največ’ — a package that does not exist (hallucination). No synthesis.

---

### 🟡 `hs04` — Mobi C vs Naj B over a year  ·  55/100 (PARTIAL)

*Type: comparison-math. Target: Mobi C ~125,88 €/yr (promo) vs Naj B 12×27,99=335,88 €/yr → Mobi C cheaper. EU data: Naj B 41,71 GB vs Mobi C 20,85 GB → Naj B +20,86 GB.*

**T1 — You:** Primerjaj Mobi C in Naj B za nekoga, ki veliko potuje po EU.
**Maks:** Za tujino so za predplačnike na voljo različni zakupi. Mi najprej poveste, ali imate predplačniško številko dodano v Moj Telekom?

**T2 — You:** Kateri je cenejši čez eno leto, upoštevaj akcije?
**Maks:** ✨ Paket Naj B je cenejši za nove naročnike:    Naj B: Akcijska cena 10,99 €/mesec (24-mesečna vezava). Po 12 mesecih: 131,88 €. Mobi C: Stroški odvisni od porabe, brez vezave.   Naj B vključuje neomejene klice, sporočila in 41,71 GB podatkov v EU. Mobi C zahteva dodatne zakupi za EU.

**T3 — You:** Kateri ima več GB v EU in za koliko?
**Maks:** ✨ Naj B ima več GB v EU: - Naj B: 41,71 GB v EU. - Mobi C: Zakupi so potrebni, količina odvisna od izbire.     Razlika: Naj B vključuje 41,71 GB več brez dodatnih stroškov.

**Verdict:** Mixed. EU-data comparison is correct (Naj B 41,71 GB vs Mobi C needs a bundle → +41,71 GB). But it opens with a deflection, and the cost claim is shaky: it declares Naj B cheaper using the 10,99 € promo (which needs Poveži + fixed) and never computes Mobi C’s yearly cost, so the comparison isn’t apples-to-apples.

---

### ❌ `hs05` — Anaphora carryover  ·  25/100 (FAIL)

*Type: anaphora. Target: Naj C (43,20 GB EU) → 28,99 € → with −5 € = 23,99 €. Must resolve 'ta paket'=Naj C.*

**T1 — You:** Kateri naročniški paket ima največ GB v EU?
**Maks:** ✨ Trenutno ne morem preveriti, kateri naročniški paket ima največ GB v EU. Ali vas zanima specifična ponudba za mobilne pakete pri Telekomu Slovenije? Lahko preverim podrobnosti za naše pakete!

**T2 — You:** Koliko stane ta paket?
**Maks:** ✨ Ali vas zanima cena mobilnih paketov 📱 ali paketov za internet in TV 🏠? Tako vam lahko pomagam najti pravo ponudbo.

**T3 — You:** In koliko je cenejši z ugodnostjo Poveži in prihrani?
**Maks:** ✨ Ugodnost Poveži in prihrani zniža mesečno naročnino za:    5 EUR pri paketih Naj A, Naj B, Naj C, Naj 5G in Naj Net, 15 EUR pri fiksnem paketu Net, če ste naročnik paketa SUPR.   Potrebujete še kakšno informacijo? Kar povejte 😊

**Verdict:** Anaphora broke. T1 refuses to name the package (should be Naj C, 43,20 GB EU); T2 loses the referent entirely and re-asks mobilni/TV; only T3 gives a generic discount. It never establishes ‘ta paket’, so the chain fails.

---

### ✅ `hs06` — Rule composition / eligibility  ·  95/100 (PASS)

*Type: rules. Target: New subscriber = number not in a subscription in last 60 days → 30 days ago means NOT eligible. Penzion and Poveži in prihrani exclude each other (only the larger, Poveži 5 €, applies).*

**T1 — You:** Sem nov naročnik. Kdaj velja akcijska cena Naj?
**Maks:** ✨ Akcijska cena paketov Naj velja za nove naročnike ob sklenitvi naročniškega razmerja s 24-mesečno vezavo: - 10,99 €/mesec z ugodnostjo Poveži in prihrani (velja za naročnike mobilnih in fiksnih paketov s skupnim računom). - Trajanje ugodnosti:   - 36 mesecev ob sklenitvi v aplikaciji Moj Telekom.   - 24 mesecev ob sklenitvi prek drugih prodajnih kanalov.     Po izteku ugodnosti se zaračuna redna mesečna naročnina. Vas zanima še kaj? 😊

**T2 — You:** Pred 30 dnevi sem imel Naj pri vas. Sem še upravičen?
**Maks:** ✨ Žal niste upravičeni do akcijske cene, saj je telefonska številka, ki je bila v naročniškem razmerju pri Telekomu Slovenije v zadnjih 60 dneh, izključena iz ugodnosti za nove naročnike.     Ali potrebujete dodatne informacije? 😊

**T3 — You:** Ali lahko hkrati uveljavim Penzion in Poveži in prihrani?
**Maks:** ✨ Ne, popusta Penzion in Poveži in prihrani se med seboj izključujeta. Na računu se upošteva tisti popust, ki prinaša večjo ugodnost — običajno Poveži in prihrani.    Vam lahko še kaj pojasnim? 😊

**Verdict:** All three rules chained correctly: akcijska price conditions → NOT eligible under the 60-day new-subscriber rule → Penzion and Poveži in prihrani are mutually exclusive (the larger, Poveži, applies). Strong rule composition.

---

### ✅ `hs07` — Two different data limits  ·  95/100 (PASS)

*Type: constraints. Target: SI: after 200 GB throttle to 64/64 kbit/s. EU cap = 20,85 GB, then charged per price list. Two distinct limits — must not conflate them.*

**T1 — You:** Imam Mobi C. Kaj se zgodi, ko presežem 200 GB doma?
**Maks:** ✨ Ko pri paketu Mobi C v Sloveniji presežete 200 GB prenosa podatkov, se hitrost zniža na 64/64 kbit/s do naslednjega zakupa. Ob novem zakupu se povrne običajna hitrost.    Potrebujete še kakšno informacijo? Kar povejte 😊

**T2 — You:** In koliko od tega lahko porabim v EU?
**Maks:** ✨ Pri paketu Mobi C lahko v državah območja EU-tarife brezplačno porabite do 20,85 GB prenosa podatkov na mesec. Po tej količini se dodatni prenos podatkov zaračuna skladno s cenikom.   Vam lahko svetujem še pri čem?

**T3 — You:** Če v EU porabim 25 GB, kaj se zgodi po 20,85 GB?
**Maks:** ✨ Ko v EU z Mobi C porabite 20,85 GB, se vsak dodatni MB zaračuna po ceniku za prenos podatkov nad vključeno količino. Hitrost ostane nespremenjena, le dodatna poraba je plačljiva.   Želite, da kaj dodatno razložim?

**Verdict:** Correctly keeps two distinct limits apart across turns: SI throttle to 64/64 kbit/s after 200 GB, EU cap 20,85 GB then charged per price list with speed unchanged. Notably, it gets the Mobi C throttle RIGHT here — the exact fact it got WRONG (‘1 GB’) as a single-shot question (mobi05). Context helped.

---

### ❌ `hs08` — Device + package + insurance total  ·  30/100 (FAIL)

*Type: arithmetic. Target: Naj B 27,99 €/mo + Premium insurance tier 601–800 € = 9,95 €/mo → 37,94 €/mo (phone paid/subsidised separately).*

**T1 — You:** Kupim telefon za 700 € in vzamem Naj B. Kolikšna je mesečna cena?
**Maks:** Vas zanimajo dodatni zakupi doma ali v tujini?

**T2 — You:** Dodam še zavarovanje za ta telefon (Premium). Koliko to doda?
**Maks:** ✨ Cena mesečne premije za paket Premium je odvisna od redne cene naprave:    do 100 €: 1,95 € 101–200 €: 3,45 € 201–400 €: 5,95 € 401–600 €: 7,45 € 601–800 €: 9,95 € 801–1000 €: 10,95 € 1001–3000 €: 14,95 €   Za natančen znesek potrebujem še vrednost vašega telefona. Potrebujete še kakšno informacijo? Kar povejte 😊

**T3 — You:** Skupni mesečni strošek?
**Maks:** ✨ Za izračun skupnega mesečnega stroška potrebujem še podatek o vrednosti vašega telefona in ali imate že kakšna druga zavarovanja pri nas. Mi lahko to sporočite?

**Verdict:** Context carryover failed. The 700 € phone is stated in T1 but T1 deflects; T2 dumps the whole insurance-tier table without picking 700 €→9,95 €; T3 asks for the device value again and never computes the 27,99 + 9,95 = 37,94 €/mo total. The needed facts appear but are never combined.

---

### ✅ `hs09` — Roaming scenario (EU vs Balkan)  ·  90/100 (PASS)

*Type: rules. Target: Croatia = EU-tariff (included, 41,71 GB). Serbia = Balkan (NOT EU) → needs a Balkan bundle. Must distinguish EU from Balkan.*

**T1 — You:** Z Naj B grem za teden na Hrvaško. Je poraba vključena?
**Maks:** ✨ Da, paket Naj B vključuje neomejeno količino prenosa podatkov v Sloveniji. Na Hrvaškem pa lahko brezplačno porabite do 41,71 GB podatkov v okviru EU-tarife. Po preseženi količini se dodatna poraba zaračuna skladno s cenikom. 😊   Ste še glede česa radovedni? Kar povejte!

**T2 — You:** Nato nadaljujem v Srbijo. Kaj takrat?
**Maks:** ✨ V Srbiji paket Naj B ne vključuje brezplačne porabe. Priporočamo, da pred odhodom aktivirate zakup Balkan internet neomejeno za brezskrbno uporabo.    Bi želeli več informacij o tem? 😊

**T3 — You:** Kateri zakup potrebujem in koliko stane?
**Maks:** ✨ Za Srbijo priporočamo zakup Balkan internet neomejeno, ki omogoča neomejeno uporabo podatkov v Bosni in Hercegovini, Srbiji, Črni Gori, Severni Makedoniji, Albaniji in na Kosovu. Cena zakupa je odvisna od trajanja in pogojev.    Bi želeli pomoč pri aktivaciji? 😊

**Verdict:** Distinguishes EU from Balkan across turns: Croatia included (41,71 GB EU) → Serbia NOT included → recommends the Balkan internet neomejeno bundle and lists the countries. Only miss: it never states the bundle’s price.

---

### ✅ `hs10` — False-premise correction  ·  90/100 (PASS)

*Type: robustness. Target: Must CORRECT the premise: Mobi has no binding and no monthly subscription (prepaid). Then compare unlimited-data options honestly.*

**T1 — You:** Mobi ima 24-mesečno vezavo, kajne?
**Maks:** ✨ Ne, predplačniški paket Mobi pri Telekomu Slovenije ne vključuje vezave ali pogodbenega obdobja. Uporabite ga lahko brez dolgoročnih obveznosti 😊    Ste še glede česa radovedni? Kar povejte!

**T2 — You:** Torej pri Mobi plačujem mesečno naročnino?
**Maks:** ✨ Ne, pri Mobi ne plačujete mesečne naročnine. Gre za predplačniški paket, kjer svoj račun polnite po potrebi. Porabite lahko le toliko, kolikor napolnite. 😊    Vam lahko še kaj razložim?

**T3 — You:** Kateri je cenejši za neomejene podatke — Mobi ali Naj?
**Maks:** ✨ Paket Mobi C nudi neomejen prenos podatkov v Sloveniji za 6,99 EUR/mesec (prvih 6 mesecev ob aktivaciji v času akcije, sicer 13,99 EUR/mesec). Paket Naj je naročniški in ima drugačne pogoje ter cene.   Želite podrobno primerjavo ali več informacij o paketu Naj?

**Verdict:** Robust to false premises — corrects ‘Mobi has 24-mo binding’ (it doesn’t) and ‘Mobi has a monthly subscription’ (it’s prepaid, top-up), then compares unlimited-data options honestly. No sycophancy.

---
