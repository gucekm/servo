# Maks answers — my (LLM) judgement

I read all 300 question/answer pairs and scored each one myself, as an LLM judge, rather than by the automatic rubric. I judged **correctness first** (does the answer match telekom.si / the ceniki?), then **relevance and helpfulness** (does it actually answer what was asked?).

Labels: ✅ **OK** correct & responsive · 🟡 **PART** on-topic but incomplete/adjacent · 🔁 **DEFLECT** clarify-first or agent hand-off, no answer · ❌ **WRONG** states a value that contradicts the site. I score a **confident wrong answer at or below a deflection**, because a wrong number misleads whereas ‘let me connect you’ at least doesn’t.

## Summary

- Answers judged: **300**
- **My mean score: 79.9/100**  ·  heuristic mean: 77.2/100
- Verdicts: ✅ OK **222** · 🟡 PART **13** · 🔁 DEFLECT **51** · ❌ WRONG **14**

| Topic | Answers | My mean | Heuristic mean | ✅ | 🟡 | 🔁 | ❌ |
|---|---|---|---|---|---|---|---|
| Prepaid (Mobi) | 75 | 88.9 | 86.8 | 62 | 5 | 5 | 3 |
| Postpaid (Naj) | 75 | 81.8 | 78.6 | 57 | 3 | 9 | 6 |
| Broadband | 75 | 64.7 | 61.0 | 42 | 3 | 29 | 1 |
| IPTV (NEO TV) | 75 | 84.1 | 82.3 | 61 | 2 | 8 | 4 |

## Where I agree / disagree with the heuristic

- Within 10 points of the heuristic on **248/300** answers (83%) — the rubric tracks my judgement well on the clear cases.

**❌ Confident factual errors I flagged (14)** — the rubric scores these like weak/partial answers; I score them as failures because they state a wrong value:

| id | Question | Maks | My note |
|---|---|---|---|
| `naj10` | Koliko znaša priključna taksa ob sklenitvi pake… | ✨ Priključna taksa ob sklenitvi paketa Naj znaša 29,00 EUR. Ali potre… | priključna taksa 29,00 € — site says 10,95 € |
| `mobi05` | Po koliko GB se v paketu Mobi C zniža hitrost p… | ✨ V paketu Mobi C se hitrost prenosa podatkov zniža po porabi 1 GB pr… | throttle after 1 GB — site says 200 GB (contradicts mobi55 in the same run) |
| `mobi08` | Koliko stane aktivacija kartice SIM ali eSIM Mo… | ✨ Aktivacija eSIM kartice za Mobi uporabnike je mogoča in se zaračuna… | 2,95 € is the SIM↔eSIM swap, not the 2 € activation asked about |
| `tv07` | Koliko stane samostojni TV paket NEO TV brez in… | ✨ NEO TV Lite ni na voljo kot samostojni TV paket brez interneta. Za … | claims standalone NEO TV doesn’t exist; it does, at 41 €/mo |
| `mobi41` | Koliko stane aktivacija kartice SIM ali eSIM Mo… | ✨ Aktivacija eSIM kartice za Mobi uporabnike (predplačniški račun) se… | 2,95 € swap quoted instead of the 2 € activation |
| `tv32` | Koliko stane samostojni TV paket NEO TV (brez i… | ✨ NEO TV Lite ni na voljo kot samostojni TV paket brez interneta. Za … | same NEO TV standalone error as tv07 |
| `tv38` | Koliko znaša strošek izdaje TV-komunikatorja NE… | ✨ Strošek najema dodatnega TV-komunikatorja NEO Smartbox znaša 3,90 €… | answers rental 3,90 € instead of the 29 € issue fee asked for |
| `tv62` | Koliko stane dodatna telefonska številka pri fi… | ✨ Dodatna IP-telefonska številka pri fiksnem paketu NEO stane 2 EUR n… | extra IP number 2 € — cenik says 1,27 € |
| `naj33` | Koliko stane mesečna naročnina storitve SIM 2 (… | ✨ Mesečna naročnina za storitev SIM 2 Brezskrbni znaša 4,99 €. Če pot… | SIM 2 quoted 4,99 € — cenik 11,99 €/14,99 € |
| `naj57` | Na kakšno hitrost pade prenos po limitu pri pak… | ✨ Pri paketih Naj B in Naj C se hitrost prenosa podatkov po presežene… | 64 kbps is Mobi C’s spec — Naj B/C throttle to 2/1 Mbit/s |
| `naj32` | Kolikšna je priključna taksa za storitev Ena št… | ✨ Priključna taksa za storitev Ena številka znaša 10,95 EUR z DDV. Če… | Ena številka taksa 10,95 € — cenik says it is FREE |
| `naj46` | Koliko GB v EU-tarifi lahko brezplačno porabim … | ✨ S paketom Naj B lahko v državah EU brez dodatnih stroškov porabite … | Naj B EU allowance 13 GB — site says 41,71 GB |
| `naj52` | Koliko časa velja enotna akcijska cena Naj v ap… | ✨ Akcijska cena paketa Naj v aplikaciji Moj Telekom velja do preklica… | ‘until cancelled’ — the unified promo price is fixed for 3 years |
| `bb26` | Kakšna je redna mesečna cena paketa NEO A? | ✨ Redna mesečna naročnina za paket Naj A znaša 20,99 EUR. Če ste imel… | quotes Naj A’s 20,99 € for NEO A, then admits no NEO A data |

**Where I scored *higher* than the rubric** (it under-credited a reasonable answer):

| id | Question | My | Heur | Why |
|---|---|---|---|---|
| `naj55` | Katere države pokriva zakup Balkan? | 100 | 73 |  |
| `naj51` | Na kateri e-naslov lahko pišem za informacije… | 95 | 69 | email correct (heuristic under-scored on relevance) |
| `bb64` | Kje naročim opremo za priklop, če ni optike? | 35 | 10 | hand-off |
| `naj31` | Koliko telefonskih številk lahko združim s st… | 95 | 73 |  |
| `naj35` | Koliko prenosa podatkov vključuje storitev SI… | 65 | 45 | ‘SIM 2 shares the main package’s data’ — plausibly correct; my 100 MB reference may be the wrong SIM 2 variant |
| `bb38` | Do katere hitrosti lahko nadgradim paket Naj … | 100 | 80 |  |
| `tv50` | Katere filmske/serijske opcije lahko dodam k … | 85 | 65 | HBO Max — one valid example |

**Where I scored *lower* than the rubric** (it over-credited a non-answer or wrong reply):

| id | Question | My | Heur | Why |
|---|---|---|---|---|
| `bb67` | Ali paket Net (samo internet) vključuje telev… | 30 | 87 | clarify; the answer is simply ‘no TV’ |
| `mobi64` | Ali lahko dobroimetje prenesem na drug račun … | 55 | 96 | confirms yes but pushes to UI |
| `tv48` | Ali je programska opcija Da Vinci Kids brezpl… | 45 | 84 | answers about the paid ‘Da Vinci’ (3,99 €), not the free ‘Da Vinci Kids’ asked about |
| `naj10` | Koliko znaša priključna taksa ob sklenitvi pa… | 15 | 45 | priključna taksa 29,00 € — site says 10,95 € |
| `mobi05` | Po koliko GB se v paketu Mobi C zniža hitrost… | 15 | 45 | throttle after 1 GB — site says 200 GB (contradicts mobi55 in the same run) |
| `mobi70` | Ali lahko z Mojim Mobi upravljam več številk … | 55 | 84 | answers via ‘add in Moj Telekom’ but a bit deflecting |
| `bb62` | Katera je najhitrejša internetna povezava (op… | 60 | 86 | says max 2 Gbit/s — the real optical maximum is 5 Gbit/s |
| `tv07` | Koliko stane samostojni TV paket NEO TV brez … | 20 | 45 | claims standalone NEO TV doesn’t exist; it does, at 41 €/mo |

## Full verdicts (all 300)


### Prepaid (Mobi)

| id | Question | Verdict | My | Heur | Δ | Note |
|---|---|:--:|--:|--:|--:|---|
| `mobi01` | Koliko stane paket Mobi A in koliko enot ter podatkov… | 🟡 PART | 82 | 82 | +0 | gave only the promo 3,73 €, not the regular 4,99 € — incomplete but not wrong |
| `mobi02` | Kakšna je redna cena paketa Mobi B? | ✅ OK | 100 | 93 | +7 |  |
| `mobi03` | Koliko GB prenosa v Sloveniji vključuje paket Mobi B? | ✅ OK | 100 | 100 | +0 |  |
| `mobi04` | Kakšna je redna cena paketa Mobi C? | ✅ OK | 100 | 93 | +7 |  |
| `mobi05` | Po koliko GB se v paketu Mobi C zniža hitrost prenosa? | ❌ WRONG | 15 | 45 | -30 | throttle after 1 GB — site says 200 GB (contradicts mobi55 in the same run) |
| `mobi06` | Kakšna je akcijska cena paketa Mobi A za 6 mesecev? | ✅ OK | 100 | 95 | +5 |  |
| `mobi07` | Kakšna je akcijska cena paketov Mobi B in Mobi C? | ✅ OK | 100 | 90 | +10 |  |
| `mobi08` | Koliko stane aktivacija kartice SIM ali eSIM Mobi? | ❌ WRONG | 35 | 45 | -10 | 2,95 € is the SIM↔eSIM swap, not the 2 € activation asked about |
| `mobi09` | Kaj dobim ob aktivaciji Mobi SIM kot promocijski zaku… | ✅ OK | 100 | 96 | +4 |  |
| `mobi10` | Koliko stanejo klici in SMS po rednem ceniku Mobi bre… | ✅ OK | 100 | 100 | +0 |  |
| `mobi11` | Koliko stane prenos podatkov na MB po ceniku Mobi bre… | ✅ OK | 100 | 95 | +5 |  |
| `mobi12` | Koliko stane Mobi Net in koliko časa velja? | ✅ OK | 100 | 93 | +7 |  |
| `mobi13` | Koliko GB vključuje Mobi Net Mesec in po kakšni ceni? | ✅ OK | 100 | 87 | +13 |  |
| `mobi14` | Kako lahko napolnim račun Mobi? | 🟡 PART | 50 | 57 | -7 | ‘top up below’ + names Moj Mobi; partly helpful, no method detail |
| `mobi15` | Na katero številko lahko z ukaznim nizom ali klicem n… | ✅ OK | 95 | 92 | +2 | *123* correct |
| `mobi16` | Na koliko dni se samodejno podaljša veljavnost računa… | ✅ OK | 100 | 96 | +4 |  |
| `mobi17` | Koliko dobroimetja potrebujem za samodejno podaljšanj… | ✅ OK | 100 | 97 | +3 |  |
| `mobi18` | Ali imam pri Mobi na voljo 5G omrežje? | ✅ OK | 90 | 90 | +0 | 5G yes, with conditions |
| `mobi19` | Kje vse lahko kupim kartico Mobi? | ✅ OK | 100 | 93 | +7 |  |
| `mobi20` | Katero aplikacijo uporabljam za upravljanje storitev … | ✅ OK | 100 | 93 | +7 |  |
| `mobi21` | Ali lahko svojo obstoječo telefonsko številko prenese… | 🔁 DEFLECT | 30 | 18 | +12 | hand-off; portability is possible but never clearly confirmed |
| `mobi22` | Koliko enot za klice in sporočila vključuje paket Mob… | ✅ OK | 100 | 100 | +0 |  |
| `mobi23` | Koliko GB v EU-tarifi lahko porabim s paketom Mobi B? | ✅ OK | 100 | 95 | +5 |  |
| `mobi24` | Koliko GB za območje EU-tarife vključuje paket Mobi C? | ✅ OK | 100 | 93 | +7 |  |
| `mobi25` | Ali se paketi Mobi A, B in C samodejno podaljšujejo? | ✅ OK | 100 | 100 | +0 |  |
| `mobi26` | Kakšna je redna cena paketa Mobi A? | ✅ OK | 100 | 93 | +7 |  |
| `mobi27` | Kakšna je redna cena paketa Mobi C? | ✅ OK | 100 | 93 | +7 |  |
| `mobi28` | Koliko enot za klice in SMS vključuje paket Mobi A? | ✅ OK | 100 | 100 | +0 |  |
| `mobi29` | Koliko GB v Sloveniji vključuje paket Mobi B? | ✅ OK | 100 | 100 | +0 |  |
| `mobi30` | Kakšna je hitrost prenosa podatkov pri paketih Mobi? | ✅ OK | 100 | 97 | +3 |  |
| `mobi31` | Kakšna je akcijska cena Mobi A za prvih 6 mesecev? | ✅ OK | 100 | 96 | +4 |  |
| `mobi32` | Kakšna je akcijska cena paketov Mobi B in C? | ✅ OK | 100 | 95 | +5 |  |
| `mobi33` | Koliko časa velja akcijska cena paketov Mobi? | ✅ OK | 100 | 96 | +4 |  |
| `mobi34` | Koliko stane klic na minuto po rednem ceniku Mobi bre… | ✅ OK | 100 | 100 | +0 |  |
| `mobi35` | Koliko stane poslano sporočilo SMS/MMS po ceniku Mobi? | 🔁 DEFLECT | 35 | 35 | +0 | ‘per the price list’ — never states the 0,12 € price |
| `mobi36` | Koliko stane prenos podatkov na MB po ceniku Mobi bre… | ✅ OK | 100 | 95 | +5 |  |
| `mobi37` | Koliko stane paket Mobi Net za eno leto? | ✅ OK | 100 | 100 | +0 |  |
| `mobi38` | Koliko dni velja paket Mobi Net? | ✅ OK | 100 | 100 | +0 |  |
| `mobi39` | Koliko GB vključuje Mobi Net Mesec? | ✅ OK | 100 | 100 | +0 |  |
| `mobi40` | Kakšna je cena paketa Mobi Net Mesec? | ✅ OK | 100 | 90 | +10 |  |
| `mobi41` | Koliko stane aktivacija kartice SIM ali eSIM Mobi? | ❌ WRONG | 35 | 45 | -10 | 2,95 € swap quoted instead of the 2 € activation |
| `mobi42` | Kaj vključuje promocijski zakup ob aktivaciji Mobi? | ✅ OK | 100 | 100 | +0 |  |
| `mobi43` | Na katero številko lahko z ukaznim nizom napolnim rač… | ✅ OK | 90 | 94 | -4 | 123 + command-string format |
| `mobi44` | S katero storitvijo (moneta) lahko napolnim račun Mob… | ✅ OK | 100 | 93 | +7 |  |
| `mobi45` | Na koliko dni se samodejno podaljša veljavnost računa… | ✅ OK | 100 | 96 | +4 | also volunteered the 1,99 € threshold |
| `mobi46` | Koliko dobroimetja potrebujem za samodejno podaljšanj… | 🔁 DEFLECT | 28 | 26 | +2 | ‘depends on package’ — never states 1,99 € |
| `mobi47` | Ali imajo vsi uporabniki Mobi dostop do 5G? | ✅ OK | 90 | 100 | -10 |  |
| `mobi48` | Na katerih bencinskih servisih lahko kupim kartico Mo… | ✅ OK | 100 | 93 | +7 |  |
| `mobi49` | Ali lahko kartico Mobi kupim na Pošti Slovenije? | ✅ OK | 100 | 92 | +8 |  |
| `mobi50` | V katerih trgovinah lahko kupim vrednostnice Mobi (np… | ✅ OK | 100 | 90 | +10 |  |
| `mobi51` | Katero aplikacijo uporabljam za upravljanje Mobi? | ✅ OK | 100 | 92 | +8 |  |
| `mobi52` | Ali lahko obstoječo telefonsko številko prenesem na M… | 🔁 DEFLECT | 20 | 19 | +1 | hand-off |
| `mobi53` | Koliko GB v EU-tarifi lahko porabim s paketom Mobi B? | ✅ OK | 100 | 95 | +5 |  |
| `mobi54` | Koliko GB za območje EU-tarife vključuje paket Mobi C? | ✅ OK | 100 | 93 | +7 |  |
| `mobi55` | Po koliko GB se pri paketu Mobi C zniža hitrost? | ✅ OK | 100 | 100 | +0 | correct 200 GB — directly contradicts mobi05 |
| `mobi56` | Na kakšno hitrost pade prenos po limitu pri paketu Mo… | ✅ OK | 95 | 93 | +2 | 64 kbit/s correct for Mobi C |
| `mobi57` | Ali se paketi Mobi A, B in C samodejno podaljšujejo? | ✅ OK | 100 | 100 | +0 |  |
| `mobi58` | Ali lahko Mobi uporabljam brez paketa (plačilo po por… | ✅ OK | 100 | 85 | +15 |  |
| `mobi59` | Kako se imenuje zakup za neomejene podatke na Hrvaške… | ✅ OK | 90 | 100 | -10 | HR-internet Plus; prices unverified but plausible |
| `mobi60` | Katere države pokrivajo zakupi Balkan pri Mobi? | ✅ OK | 100 | 90 | +10 |  |
| `mobi61` | Ali je za ZDA na voljo zakup podatkov pri Mobi? | 🔁 DEFLECT | 20 | 20 | +0 | clarify-first; never confirms the ZDA bundle exists |
| `mobi62` | Koliko GB podatkov v Sloveniji vključuje paket Mobi A? | ✅ OK | 100 | 100 | +0 |  |
| `mobi63` | Ali so pri paketu Mobi B klici in SMS neomejeni? | ✅ OK | 100 | 100 | +0 |  |
| `mobi64` | Ali lahko dobroimetje prenesem na drug račun Mobi? | 🟡 PART | 55 | 96 | -41 | confirms yes but pushes to UI |
| `mobi65` | Kako se imenuje storitev za brezplačno klicanje ene š… | ✅ OK | 100 | 100 | +0 |  |
| `mobi66` | Kaj je storitev Žepnina pri Mobi? | ✅ OK | 100 | 100 | +0 |  |
| `mobi67` | Ali lahko eSIM Mobi aktiviram kar v aplikaciji Moj Mo… | ✅ OK | 100 | 95 | +5 |  |
| `mobi68` | Katere pakete (klici/SMS neomejeni) ponuja Mobi poleg… | ✅ OK | 100 | 86 | +14 |  |
| `mobi69` | Koliko GB vključuje paket Mobi Net za eno leto? | ✅ OK | 100 | 100 | +0 |  |
| `mobi70` | Ali lahko z Mojim Mobi upravljam več številk Mobi hkr… | 🟡 PART | 55 | 84 | -29 | answers via ‘add in Moj Telekom’ but a bit deflecting |
| `mobi71` | Kje lahko poleg spleta osebno kupim SIM Mobi? | ✅ OK | 100 | 88 | +12 |  |
| `mobi72` | Ali se neporabljene količine Mobi prenašajo v nasledn… | ✅ OK | 100 | 88 | +12 |  |
| `mobi73` | Kakšna je hitrost prenosa (upload) pri paketih Mobi? | 🟡 PART | 60 | 42 | +18 | ‘upload depends on the network’ — reasonable, but no committed figure |
| `mobi74` | Kakšna je redna cena paketa Mobi B? | ✅ OK | 100 | 93 | +7 |  |
| `mobi75` | Ali je za koriščenje enot v EU potrebna registracija … | ✅ OK | 95 | 88 | +7 |  |

### Postpaid (Naj)

| id | Question | Verdict | My | Heur | Δ | Note |
|---|---|:--:|--:|--:|--:|---|
| `naj01` | Koliko stane paket Naj A na mesec in koliko podatkov … | ✅ OK | 100 | 100 | +0 |  |
| `naj02` | Koliko prenosa podatkov je vključenega v paketu Naj A? | ✅ OK | 100 | 93 | +7 |  |
| `naj03` | Kakšna je redna mesečna cena paketa Naj B? | ✅ OK | 100 | 93 | +7 |  |
| `naj04` | Po koliko GB se v paketu Naj B zniža hitrost prenosa … | ✅ OK | 100 | 100 | +0 | also gave the correct 2/1 Mbit/s throttle speed |
| `naj05` | Kakšna je redna cena paketa Naj C na mesec? | ✅ OK | 100 | 90 | +10 |  |
| `naj06` | Po koliko porabljenih GB se v paketu Naj C zniža hitr… | ✅ OK | 100 | 100 | +0 |  |
| `naj07` | Koliko stane paket Naj naprava in kaj vključuje? | ✅ OK | 100 | 100 | +0 | complete: price, 1 GB, 500 SMS, 10 € limit, speed |
| `naj08` | Kakšna je najvišja hitrost prenosa do uporabnika pri … | 🔁 DEFLECT | 30 | 32 | -2 | ‘depends on package’ — never states up to 1 Gbit/s |
| `naj09` | Ali paketi Naj vključujejo neomejene klice in SMS v S… | ✅ OK | 95 | 100 | -5 |  |
| `naj10` | Koliko znaša priključna taksa ob sklenitvi paketa Naj? | ❌ WRONG | 15 | 45 | -30 | priključna taksa 29,00 € — site says 10,95 € |
| `naj11` | Koliko stane sprememba naročniškega paketa? | 🔁 DEFLECT | 20 | 15 | +5 | clarify-first, no fee given |
| `naj12` | Kje lahko spremenim svoj naročniški paket Naj? | 🔁 DEFLECT | 20 | 15 | +5 | clarify-first; never names Moj Telekom / 041 |
| `naj13` | Kolikšen je popust pri ugodnosti Poveži in prihrani? | ✅ OK | 100 | 92 | +8 |  |
| `naj14` | Koliko stane storitev Ena številka? | ✅ OK | 100 | 100 | +0 |  |
| `naj15` | Koliko dodatnih naročniških razmerij Druga številka o… | ✅ OK | 100 | 90 | +10 |  |
| `naj16` | Po koliko GB lahko z Delim GB delim gigabajte najbliž… | ✅ OK | 100 | 93 | +7 |  |
| `naj17` | Na katero številko pošljem SMS za deljenje GB (Delim … | ✅ OK | 100 | 92 | +8 |  |
| `naj18` | Ali imam pri paketih Naj na voljo omrežje 5G? | ✅ OK | 95 | 95 | +0 | ‘99 % pokritost’ unverified but plausible |
| `naj19` | Koliko GB lahko v paketu Naj B brezplačno porabim v E… | ✅ OK | 100 | 90 | +10 |  |
| `naj20` | Koliko GB za območje EU-tarife vključuje paket Naj C? | ✅ OK | 100 | 90 | +10 |  |
| `naj21` | Ali za nove naročnike paketa Naj velja 30-dnevna gara… | ✅ OK | 100 | 100 | +0 |  |
| `naj22` | Kdo velja za novega naročnika pri akcijski ponudbi pa… | ✅ OK | 100 | 90 | +10 | 60-day rule correct |
| `naj23` | Katera telefonska številka je za informacije o paketi… | 🔁 DEFLECT | 15 | 0 | +15 | points to UI; never gives 041 700 700 |
| `naj24` | Kakšna je akcijska cena paketov Naj za nove naročnike? | ✅ OK | 100 | 96 | +4 |  |
| `naj25` | V kateri aplikaciji sklenem paket Naj po enotni ceni … | ✅ OK | 95 | 84 | +11 |  |
| `naj26` | Kakšna je hitrost oddajanja (upload) pri paketih Naj … | ✅ OK | 100 | 92 | +8 |  |
| `naj27` | Kakšna je hitrost prenosa do uporabnika pri paketu Na… | ✅ OK | 100 | 96 | +4 |  |
| `naj28` | Kakšen zneskovni limit za klice velja pri paketu Naj … | ✅ OK | 100 | 97 | +3 |  |
| `naj29` | Koliko sporočil SMS vključuje paket Naj naprava? | ✅ OK | 100 | 100 | +0 |  |
| `naj30` | Koliko stane dodatna storitev Ena številka na mesec? | ✅ OK | 100 | 93 | +7 |  |
| `naj31` | Koliko telefonskih številk lahko združim s storitvijo… | ✅ OK | 95 | 73 | +22 |  |
| `naj32` | Kolikšna je priključna taksa za storitev Ena številka? | ❌ WRONG | 20 | 31 | -11 | Ena številka taksa 10,95 € — cenik says it is FREE |
| `naj33` | Koliko stane mesečna naročnina storitve SIM 2 (Brezsk… | ❌ WRONG | 20 | 40 | -20 | SIM 2 quoted 4,99 € — cenik 11,99 €/14,99 € |
| `naj34` | Kolikšna je priključna taksa za storitev SIM 2? | ✅ OK | 95 | 95 | +0 | SIM 2 taksa 10,95 € correct |
| `naj35` | Koliko prenosa podatkov vključuje storitev SIM 2? | 🟡 PART | 65 | 45 | +20 | ‘SIM 2 shares the main package’s data’ — plausibly correct; my 100 MB reference may be the wrong SIM 2 variant |
| `naj36` | Koliko stane storitev Varen splet na mesec? | ✅ OK | 100 | 100 | +0 |  |
| `naj37` | Koliko stane zavarovanje naprave, vredne med 401 in 6… | ✅ OK | 100 | 95 | +5 | 7,45 € + 60 € excess, matches cenik |
| `naj38` | Koliko stane zavarovanje najdražjih naprav (1001–3000… | ✅ OK | 100 | 93 | +7 |  |
| `naj39` | Koliko stane zavarovanje pametne ure na mesec? | ✅ OK | 100 | 100 | +0 |  |
| `naj40` | Koliko stane zavarovanje tablice ali prenosnika do 40… | ✅ OK | 100 | 100 | +0 |  |
| `naj41` | Kolikšen popust prinaša ugodnost Poveži in prihrani? | ✅ OK | 100 | 93 | +7 |  |
| `naj42` | Po koliko GB lahko naenkrat največ delim z Delim GB? | ✅ OK | 100 | 93 | +7 |  |
| `naj43` | Na katero številko pošljem SMS DELIM za deljenje giga… | ✅ OK | 100 | 93 | +7 |  |
| `naj44` | Koliko dodatnih razmerij Druga številka omogoča paket… | ✅ OK | 100 | 92 | +8 |  |
| `naj45` | Koliko dodatnih razmerij Druga številka omogoča paket… | ✅ OK | 100 | 92 | +8 |  |
| `naj46` | Koliko GB v EU-tarifi lahko brezplačno porabim s pake… | ❌ WRONG | 15 | 30 | -15 | Naj B EU allowance 13 GB — site says 41,71 GB |
| `naj47` | Koliko GB za območje EU-tarife vključuje paket Naj C? | ✅ OK | 100 | 90 | +10 |  |
| `naj48` | Kolikšen dodatek se zaračuna za SMS iz Slovenije v tu… | 🔁 DEFLECT | 20 | 15 | +5 | never gives the 0,11 € surcharge |
| `naj49` | Kakšna je akcijska cena paketov Naj za nove naročnike? | ✅ OK | 100 | 96 | +4 |  |
| `naj50` | Katera je telefonska številka za informacije o paketi… | 🔁 DEFLECT | 15 | 0 | +15 | points to UI; never gives 041 700 700 |
| `naj51` | Na kateri e-naslov lahko pišem za informacije o ponud… | ✅ OK | 95 | 69 | +26 | email correct (heuristic under-scored on relevance) |
| `naj52` | Koliko časa velja enotna akcijska cena Naj v aplikaci… | ❌ WRONG | 35 | 28 | +7 | ‘until cancelled’ — the unified promo price is fixed for 3 years |
| `naj53` | Ali lahko paket Naj sklenem z eSIM? | ✅ OK | 95 | 90 | +5 |  |
| `naj54` | Kako se imenuje zakup za neomejene podatke na Hrvaške… | ✅ OK | 90 | 92 | -2 | HR-internet correct; quoted prices unverified but plausible |
| `naj55` | Katere države pokriva zakup Balkan? | ✅ OK | 100 | 73 | +27 |  |
| `naj56` | Ali je na voljo zakup neomejenih podatkov za ZDA? | ✅ OK | 90 | 90 | +0 | ZDA bundle correct; prices unverified |
| `naj57` | Na kakšno hitrost pade prenos po limitu pri paketih N… | ❌ WRONG | 15 | 35 | -20 | 64 kbps is Mobi C’s spec — Naj B/C throttle to 2/1 Mbit/s |
| `naj58` | Ali paketi Naj vključujejo neomejene klice v vsa slov… | ✅ OK | 100 | 100 | +0 |  |
| `naj59` | Ali imam pri paketih Naj neomejene SMS in MMS v Slove… | ✅ OK | 100 | 90 | +10 |  |
| `naj60` | Kolikšna je priključna taksa ob sklenitvi paketa Naj? | 🔁 DEFLECT | 20 | 25 | -5 | clarify-first |
| `naj61` | Ali je za nove naročnike Naj na voljo garancija zadov… | ✅ OK | 100 | 100 | +0 |  |
| `naj62` | Koliko podatkov (GB) vključuje paket Naj A? | ✅ OK | 100 | 100 | +0 |  |
| `naj63` | Ali je prenos podatkov pri paketu Naj B neomejen? | ✅ OK | 100 | 100 | +0 |  |
| `naj64` | V katerih državah velja EU-tarifa (naštej nekaj)? | ✅ OK | 95 | 90 | +5 |  |
| `naj65` | Kje lahko spremenim naročniški paket Naj? | 🔁 DEFLECT | 18 | 15 | +3 | clarify-first; never names Moj Telekom / 041 |
| `naj66` | Ali paketi Naj delujejo v omrežju 5G? | ✅ OK | 95 | 100 | -5 |  |
| `naj67` | Kakšna je hitrost oddajanja (upload) pri paketu Naj n… | ✅ OK | 100 | 96 | +4 |  |
| `naj68` | Koliko GB podatkov vključuje paket Naj naprava? | ✅ OK | 100 | 100 | +0 |  |
| `naj69` | Za koga velja popust Penzion? | ✅ OK | 95 | 80 | +15 |  |
| `naj70` | Ali lahko z Delim GB delim gigabajte tudi uporabnikom… | ✅ OK | 100 | 100 | +0 |  |
| `naj71` | Kakšna je najvišja hitrost prenosa do uporabnika pri … | 🟡 PART | 80 | 97 | -17 | answer drifts into fixed-network tech but does state 1 Gbit/s |
| `naj72` | Ali storitev Ena številka zahteva vključen VoLTE? | 🟡 PART | 60 | 77 | -17 | explains VoLTE and asks back instead of a clear ‘yes, it is required’ |
| `naj73` | Koliko stane zavarovanje naprave med 801 in 1000 EUR … | ✅ OK | 100 | 100 | +0 |  |
| `naj74` | Kolikšna je cena minute klica iz Slovenije v EU po ce… | 🔁 DEFLECT | 20 | 15 | +5 | no per-minute price given |
| `naj75` | Kolikšna je redna mesečna cena paketa Naj C? | ✅ OK | 100 | 93 | +7 |  |

### Broadband

| id | Question | Verdict | My | Heur | Δ | Note |
|---|---|:--:|--:|--:|--:|---|
| `bb01` | Kakšna je najvišja hitrost optičnega interneta pri pa… | 🔁 DEFLECT | 18 | 18 | -0 | never states 1 Gbit/s |
| `bb02` | Do katere hitrosti lahko nadgradim optični internet N… | ✅ OK | 95 | 92 | +3 | 5 Gbit/s correct; the 99 €/mo upgrade figure is unverified |
| `bb03` | Koliko stane paket Net (samo internet) na mesec? | 🔁 DEFLECT | 20 | 25 | -5 | clarify fixed vs mobile |
| `bb04` | Kakšna je hitrost internetnega paketa Net na optiki? | 🔁 DEFLECT | 15 | 5 | +10 | ‘check in Moj Telekom’ |
| `bb05` | Koliko stane fiksni paket Naj Net na mesec? | ✅ OK | 90 | 100 | -10 | 13,99 € and correctly flags Naj Net is mobile not fixed |
| `bb06` | Kakšna je akcijska cena fiksnih paketov NEO ob 24-mes… | 🔁 DEFLECT | 25 | 22 | +3 | never states 32,99 € |
| `bb07` | Kaj lahko naredim, če na mojem naslovu še ni optike? | 🔁 DEFLECT | 18 | 0 | +18 | coverage check is relevant but never names NEO 5G |
| `bb08` | Kako preverim, ali je na mojem naslovu na voljo optik… | 🟡 PART | 70 | 65 | +5 | pointing to the address checker is the genuinely correct action |
| `bb09` | Ali je priklop optike lahko brezplačen? | 🔁 DEFLECT | 12 | 0 | +12 | ‘no data’ hand-off; answer is yes, free for ~250k homes |
| `bb10` | Za koliko gospodinjstev bo optika priključena brezpla… | 🔁 DEFLECT | 12 | 0 | +12 | no 250,000 figure |
| `bb11` | Katere tehnologije za dostop do interneta ponuja Tele… | ✅ OK | 90 | 93 | -3 | technologies listed; 10 Gbit/s optical max plausible |
| `bb12` | Kakšna je hitrost do uporabnika pri paketu NEO A na o… | 🔁 DEFLECT | 15 | 5 | +10 | ‘check in Moj Telekom’ |
| `bb13` | Kakšna je hitrost od uporabnika (oddajanje) pri paket… | ✅ OK | 95 | 85 | +10 |  |
| `bb14` | Kaj je NEO 5G in za koga je primeren? | ✅ OK | 100 | 90 | +10 |  |
| `bb15` | Ali priklop NEO 5G zahteva vrtanje ali posege v dom? | 🔁 DEFLECT | 30 | 30 | +0 | re-asks a yes/no it could have answered |
| `bb16` | Kakšna je hitrost paketa Naj Net in ali je prenos neo… | 🔁 DEFLECT | 15 | 15 | +0 | clarify-first |
| `bb17` | Do katere hitrosti lahko nadgradim paket Naj Net? | ✅ OK | 100 | 87 | +13 |  |
| `bb18` | Kaj je Turbo WiFi? | ✅ OK | 100 | 85 | +15 |  |
| `bb19` | Na katero številko pokličem za priklop internetne opr… | 🔁 DEFLECT | 35 | 22 | +13 | refuses to give a number; 041 700 700 is in fact published |
| `bb20` | Ali lahko dobim internet prek mobilnega omrežja, če n… | ✅ OK | 88 | 97 | -9 | Naj Net over mobile is a valid answer (site would also cite NEO 5G) |
| `bb21` | Kakšna je redna mesečna cena paketa NEO A? | 🔁 DEFLECT | 20 | 28 | -8 | ‘not in my data’ |
| `bb22` | Kakšna je redna cena paketa NEO B? | ✅ OK | 100 | 90 | +10 |  |
| `bb23` | Kakšna je redna cena paketa NEO C? | ✅ OK | 100 | 90 | +10 |  |
| `bb24` | Koliko časa velja akcijska cena NEO za naročnike brez… | ✅ OK | 100 | 96 | +4 |  |
| `bb25` | Koliko časa velja akcijska cena NEO za nove naročnike… | ✅ OK | 100 | 97 | +3 |  |
| `bb26` | Kakšna je redna mesečna cena paketa NEO A? | ❌ WRONG | 18 | 28 | -10 | quotes Naj A’s 20,99 € for NEO A, then admits no NEO A data |
| `bb27` | Kakšna je redna cena paketa NEO B? | ✅ OK | 100 | 90 | +10 |  |
| `bb28` | Kakšna je redna cena paketa NEO C? | ✅ OK | 100 | 90 | +10 |  |
| `bb29` | Koliko stane paket Net (samo internet) na mesec? | 🔁 DEFLECT | 20 | 25 | -5 | clarify fixed vs mobile |
| `bb30` | Kakšna je akcijska cena fiksnih paketov NEO ob 24-mes… | 🔁 DEFLECT | 25 | 28 | -3 | never states 32,99 € |
| `bb31` | Kakšna je najvišja hitrost do uporabnika na optiki pr… | ✅ OK | 100 | 97 | +3 |  |
| `bb32` | Do katere hitrosti lahko nadgradim optični internet N… | ✅ OK | 95 | 92 | +3 |  |
| `bb33` | Kakšna je hitrost oddajanja (upload) pri paketu NEO C… | ✅ OK | 100 | 96 | +4 |  |
| `bb34` | Kakšna je hitrost oddajanja pri paketu NEO A na optik… | ✅ OK | 100 | 96 | +4 |  |
| `bb35` | Kakšna je hitrost oddajanja pri paketu NEO B na optik… | ✅ OK | 100 | 95 | +5 |  |
| `bb36` | Koliko stane fiksni paket Naj Net na mesec? | 🔁 DEFLECT | 20 | 15 | +5 | never states 13,99 € |
| `bb37` | Kakšna je osnovna hitrost paketa Naj Net? | ✅ OK | 100 | 93 | +7 |  |
| `bb38` | Do katere hitrosti lahko nadgradim paket Naj Net? | ✅ OK | 100 | 80 | +20 |  |
| `bb39` | Ali je prenos podatkov pri Naj Net v Sloveniji neomej… | ✅ OK | 100 | 100 | +0 |  |
| `bb40` | Kaj je rešitev, če na mojem naslovu še ni optike? | 🔁 DEFLECT | 15 | 0 | +15 | never names NEO 5G |
| `bb41` | Ali priklop NEO 5G zahteva vrtanje ali posege v dom? | 🔁 DEFLECT | 30 | 30 | +0 | re-asks a yes/no |
| `bb42` | Kako preverim dostopnost optike na svojem naslovu? | 🟡 PART | 70 | 65 | +5 | address-checker pointer is the correct action |
| `bb43` | Za koliko gospodinjstev bo optika priključena brezpla… | 🔁 DEFLECT | 12 | 0 | +12 | no 250,000 figure |
| `bb44` | Katere tehnologije za dostop do interneta ponuja Tele… | ✅ OK | 90 | 93 | -3 |  |
| `bb45` | Kaj je storitev Turbo WiFi? | ✅ OK | 100 | 100 | +0 |  |
| `bb46` | Ali Telekom ponuja internet prek satelita? | ✅ OK | 90 | 92 | -2 | satellite; 25/6 Mbit/s plausible |
| `bb47` | Kaj omogoča brezžični sistem PLC? | ✅ OK | 90 | 85 | +5 |  |
| `bb48` | Katera varnostna rešitev (Kaspersky) je na voljo za i… | ✅ OK | 88 | 78 | +10 | Kaspersky products listed |
| `bb49` | Kaj je storitev Strela alarm? | ✅ OK | 100 | 100 | +0 |  |
| `bb50` | Na katero številko pokličem za priklop internetne opr… | 🔁 DEFLECT | 20 | 10 | +10 | refuses 041 700 700 |
| `bb51` | Ali lahko internet dobim prek mobilnega omrežja, če n… | 🔁 DEFLECT | 12 | 3 | +9 | answer is yes (NEO 5G / Naj Net) but never given |
| `bb52` | Kakšna je hitrost do uporabnika pri paketu Net na opt… | 🔁 DEFLECT | 15 | 5 | +10 | ‘check in Moj Telekom’ |
| `bb53` | Koliko časa velja akcijska cena NEO za naročnike brez… | ✅ OK | 100 | 96 | +4 |  |
| `bb54` | Koliko časa velja akcijska cena NEO za nove naročnike… | ✅ OK | 100 | 97 | +3 |  |
| `bb55` | Ali je priklop optike lahko brezplačen? | 🔁 DEFLECT | 12 | 0 | +12 | ‘no data’ hand-off |
| `bb56` | Kolikšen popust na naročnino NEO A prinaša akcija (16… | 🔁 DEFLECT | 25 | 19 | +6 | re-asks instead of giving the 16 € discount |
| `bb57` | Kolikšen popust prinaša akcija pri paketu NEO C? | ✅ OK | 100 | 90 | +10 | 30,01 € correct |
| `bb58` | Ali za pakete NEO velja garancija zadovoljstva? | ✅ OK | 100 | 100 | +0 |  |
| `bb59` | Kaj potrebujem za priklop NEO 5G doma? | ✅ OK | 100 | 93 | +7 |  |
| `bb60` | Ali lahko z NEO 5G pokrijem tudi vikend ali odročno l… | ✅ OK | 85 | 80 | +5 | yes via 4G/5G |
| `bb61` | Kakšna je hitrost oddajanja pri paketu Net na optiki? | 🔁 DEFLECT | 15 | 5 | +10 | ‘check in Moj Telekom’ |
| `bb62` | Katera je najhitrejša internetna povezava (optika) po… | 🟡 PART | 60 | 86 | -26 | says max 2 Gbit/s — the real optical maximum is 5 Gbit/s |
| `bb63` | Ali je hitrost pri paketih NEO nadgradljiva? | ✅ OK | 95 | 93 | +2 |  |
| `bb64` | Kje naročim opremo za priklop, če ni optike? | 🔁 DEFLECT | 35 | 10 | +25 | hand-off |
| `bb65` | Kakšna je cena minute klica iz Slovenije v EU po ceni… | 🔁 DEFLECT | 20 | 15 | +5 | no price |
| `bb66` | Ali paketi NEO vključujejo tudi televizijo? | ✅ OK | 100 | 100 | +0 |  |
| `bb67` | Ali paket Net (samo internet) vključuje televizijo? | 🔁 DEFLECT | 30 | 87 | -57 | clarify; the answer is simply ‘no TV’ |
| `bb68` | Kakšna je najvišja hitrost mobilnega interneta pri pa… | ✅ OK | 90 | 92 | -2 | 2 Mbit/s correct for the fixed Naj Net (question was ambiguous) |
| `bb69` | Ali lahko fiksni internet dobim tudi na omrežju OŠO (… | 🔁 DEFLECT | 10 | 0 | +10 | pure hand-off; answer is yes (OŠO) |
| `bb70` | Kolikšen popust na naročnino prinaša akcija pri paket… | ✅ OK | 100 | 96 | +4 | 25,01 € correct |
| `bb71` | Ali za pakete NEO velja 24-mesečna vezava za akcijsko… | ✅ OK | 95 | 93 | +2 |  |
| `bb72` | Kaj se zgodi s ceno NEO po izteku akcijskega obdobja? | ✅ OK | 90 | 96 | -6 |  |
| `bb73` | Ali lahko hitrost interneta pri NEO nadgradim do 2 Gb… | ✅ OK | 95 | 95 | +0 | 2 Gbit/s at 15 €/mo |
| `bb74` | Katera telefonska številka je za pomoč pri internetu? | 🔁 DEFLECT | 20 | 8 | +12 | refuses 041 700 700 |
| `bb75` | Ali je za NEO 5G priklop takojšen? | ✅ OK | 100 | 100 | +0 |  |

### IPTV (NEO TV)

| id | Question | Verdict | My | Heur | Δ | Note |
|---|---|:--:|--:|--:|--:|---|
| `tv01` | Koliko TV programov vključuje paket NEO A? | ✅ OK | 100 | 100 | +0 |  |
| `tv02` | Koliko programov ima paket NEO B? | ✅ OK | 100 | 100 | +0 |  |
| `tv03` | Koliko TV programov vključuje paket NEO C? | ✅ OK | 100 | 100 | +0 |  |
| `tv04` | Katero programsko shemo vključuje paket NEO C? | ✅ OK | 100 | 93 | +7 |  |
| `tv05` | Katero programsko shemo ima paket NEO A? | ✅ OK | 100 | 93 | +7 |  |
| `tv06` | Kakšno programsko shemo vključuje paket NEO B? | ✅ OK | 100 | 100 | +0 |  |
| `tv07` | Koliko stane samostojni TV paket NEO TV brez internet… | ❌ WRONG | 20 | 45 | -25 | claims standalone NEO TV doesn’t exist; it does, at 41 €/mo |
| `tv08` | Koliko dni nazaj lahko gledam vsebine z ogledom nazaj… | ✅ OK | 100 | 85 | +15 |  |
| `tv09` | Ali lahko pri NEO snemam oddaje? | ✅ OK | 95 | 90 | +5 |  |
| `tv10` | Koliko stane najem vsakega dodatnega TV-komunikatorja? | ✅ OK | 100 | 95 | +5 |  |
| `tv11` | Ali je najem prvega TV-komunikatorja brezplačen? | ✅ OK | 100 | 95 | +5 |  |
| `tv12` | Kaj je NEO TV Lite? | ✅ OK | 100 | 100 | +0 |  |
| `tv13` | Koliko stane NEO TV Lite na napravo mesečno? | ✅ OK | 100 | 100 | +0 |  |
| `tv14` | Na koliko pametnih televizorjih lahko uporabljam NEO … | ✅ OK | 95 | 95 | +0 |  |
| `tv15` | Na katerih pametnih televizorjih deluje NEO TV Lite? | ✅ OK | 100 | 96 | +4 |  |
| `tv16` | Kateri pogoj (napravo) potrebujem za uporabo NEO TV L… | ✅ OK | 95 | 87 | +8 |  |
| `tv17` | Ali lahko NEO vsebine gledam na računalniku? | ✅ OK | 100 | 93 | +7 |  |
| `tv18` | Katere vsebine niso na voljo v paketu NEO TV brez int… | 🟡 PART | 55 | 37 | +18 | generic; doesn’t name the excluded apps (VOYO/YouTube/NEO igre…) |
| `tv19` | Ali NEO ponuja varno vsebino za otroke (Otroški park)? | ✅ OK | 95 | 93 | +2 |  |
| `tv20` | Katere programske opcije lahko dodam k paketu NEO? | ✅ OK | 100 | 90 | +10 |  |
| `tv21` | Ali lahko NEO gledam na več napravah hkrati? | ✅ OK | 95 | 93 | +2 |  |
| `tv22` | Kaj je NEO SmartBox? | ✅ OK | 100 | 100 | +0 |  |
| `tv23` | Ali je za pakete NEO na voljo garancija zadovoljstva? | ✅ OK | 100 | 100 | +0 |  |
| `tv24` | Kakšna je akcijska cena paketa NEO TV ob 24-mesečni v… | 🔁 DEFLECT | 20 | 15 | +5 | never states 32,99 € |
| `tv25` | Do kdaj je NEO TV Lite brezplačen ob nakupu izbranega… | 🔁 DEFLECT | 25 | 31 | -6 | ‘time-limited’, no date |
| `tv26` | Koliko TV programov vključuje paket NEO A? | ✅ OK | 100 | 100 | +0 |  |
| `tv27` | Koliko programov ima paket NEO B? | ✅ OK | 100 | 100 | +0 |  |
| `tv28` | Koliko TV programov vključuje paket NEO C? | ✅ OK | 100 | 100 | +0 |  |
| `tv29` | Katero programsko shemo vključuje paket NEO A? | ✅ OK | 100 | 93 | +7 |  |
| `tv30` | Katero programsko shemo ima paket NEO B? | ✅ OK | 100 | 93 | +7 |  |
| `tv31` | Katero programsko shemo vključuje paket NEO C? | ✅ OK | 100 | 93 | +7 |  |
| `tv32` | Koliko stane samostojni TV paket NEO TV (brez interne… | ❌ WRONG | 20 | 45 | -25 | same NEO TV standalone error as tv07 |
| `tv33` | Koliko programov ima samostojni paket NEO TV? | 🔁 DEFLECT | 25 | 35 | -10 | ‘not in knowledge base’; answer is 210 |
| `tv34` | Koliko dni nazaj lahko gledam vsebine z ogledom nazaj? | ✅ OK | 100 | 95 | +5 |  |
| `tv35` | Ali lahko pri NEO snemam oddaje? | ✅ OK | 95 | 90 | +5 |  |
| `tv36` | Koliko stane najem vsakega dodatnega TV-komunikatorja… | ✅ OK | 100 | 100 | +0 |  |
| `tv37` | Ali je najem prvega TV-komunikatorja brezplačen? | ✅ OK | 100 | 95 | +5 |  |
| `tv38` | Koliko znaša strošek izdaje TV-komunikatorja NEO Smar… | ❌ WRONG | 30 | 41 | -11 | answers rental 3,90 € instead of the 29 € issue fee asked for |
| `tv39` | Kaj je NEO TV Lite? | ✅ OK | 100 | 100 | +0 |  |
| `tv40` | Koliko stane NEO TV Lite na napravo mesečno? | ✅ OK | 100 | 100 | +0 |  |
| `tv41` | Na koliko pametnih televizorjih lahko uporabljam NEO … | ✅ OK | 95 | 95 | +0 |  |
| `tv42` | Na katerih pametnih televizorjih deluje NEO TV Lite? | ✅ OK | 100 | 96 | +4 |  |
| `tv43` | Kateri pogoj (napravo) potrebujem za uporabo NEO TV L… | ✅ OK | 95 | 87 | +8 |  |
| `tv44` | Do kdaj je NEO TV Lite brezplačen ob nakupu izbranega… | 🔁 DEFLECT | 25 | 31 | -6 | no date given |
| `tv45` | Kje na spletu (računalnik) lahko gledam NEO vsebine? | ✅ OK | 95 | 85 | +10 |  |
| `tv46` | Koliko stane programski dodatek NEO igre na mesec? | ✅ OK | 95 | 100 | -5 | ‘8 €’ ≈ cenik 7,99 €; also gives 4 € bonded price |
| `tv47` | Kako se od 1. 8. 2025 imenuje TV-opcija, prej znana k… | 🔁 DEFLECT | 15 | 4 | +11 | ‘no data’; answer is HBO Max |
| `tv48` | Ali je programska opcija Da Vinci Kids brezplačna? | 🟡 PART | 45 | 84 | -39 | answers about the paid ‘Da Vinci’ (3,99 €), not the free ‘Da Vinci Kids’ asked about |
| `tv49` | Katere športne programske opcije lahko dodam k NEO? | ✅ OK | 90 | 80 | +10 | Šport option, 4,90 € |
| `tv50` | Katere filmske/serijske opcije lahko dodam k NEO (naš… | ✅ OK | 85 | 65 | +20 | HBO Max — one valid example |
| `tv51` | Katere vsebine niso na voljo v paketu NEO TV brez int… | ✅ OK | 90 | 92 | -2 | names YouTube/Netflix; close enough to the excluded set |
| `tv52` | Ali NEO ponuja varno vsebino za otroke (Otroški park)? | ✅ OK | 95 | 93 | +2 |  |
| `tv53` | Kaj je NEO SmartBox? | ✅ OK | 100 | 100 | +0 |  |
| `tv54` | S katerima protokoloma lahko brezžično predvajam vseb… | ✅ OK | 100 | 84 | +16 |  |
| `tv55` | Kaj omogoča virtualni daljinec pri NEO? | ✅ OK | 100 | 100 | +0 |  |
| `tv56` | Ali je za pakete NEO na voljo garancija zadovoljstva? | ✅ OK | 100 | 100 | +0 |  |
| `tv57` | Kakšna je akcijska cena paketa NEO TV ob 24-mesečni v… | 🔁 DEFLECT | 15 | 15 | +0 | never states 32,99 € |
| `tv58` | Ali lahko NEO gledam na več napravah? | ✅ OK | 95 | 90 | +5 |  |
| `tv59` | Kolikšen popust na naročnino prinaša akcija pri paket… | 🔁 DEFLECT | 15 | 15 | +0 | never gives the 8 € discount |
| `tv60` | Ali paket NEO TV omogoča ogled programskih opcij, ki … | ✅ OK | 100 | 97 | +3 | correctly names VOYO/YouTube/NEO igre/Max/Pickbox |
| `tv61` | Koliko stane najem TV-komunikatorja BOX S na mesec? | ✅ OK | 95 | 100 | -5 | BOX S rental is indeed 3,90 € |
| `tv62` | Koliko stane dodatna telefonska številka pri fiksnem … | ❌ WRONG | 25 | 41 | -16 | extra IP number 2 € — cenik says 1,27 € |
| `tv63` | Katero shemo (koliko programov) ima najvišji paket NE… | ✅ OK | 100 | 90 | +10 |  |
| `tv64` | Ali lahko NEO TV Lite uporabljam na televizorju LG? | ✅ OK | 95 | 93 | +2 |  |
| `tv65` | Ali lahko NEO TV Lite uporabljam na televizorju Samsu… | ✅ OK | 95 | 95 | +0 |  |
| `tv66` | Ali NEO TV Lite omogoča snemanje in ogled nazaj? | ✅ OK | 100 | 100 | +0 |  |
| `tv67` | Ali je NEO TV Lite na voljo pri paketu Net (brez tele… | ✅ OK | 100 | 100 | +0 |  |
| `tv68` | Ali je NEO najboljša TV-izkušnja po mnenju uporabniko… | ✅ OK | 85 | 80 | +5 | subjective but supported |
| `tv69` | Ali lahko NEO 5G uporabljam za televizijo, kjer ni op… | ✅ OK | 95 | 90 | +5 |  |
| `tv70` | Koliko programov (vsaj) ponuja programska shema Stand… | ✅ OK | 95 | 78 | +17 |  |
| `tv71` | Ali NEO ponuja videoteke (vsebine na zahtevo)? | ✅ OK | 95 | 85 | +10 |  |
| `tv72` | Ali lahko med gledanjem TV z mini predvajalnikom brsk… | ✅ OK | 90 | 73 | +17 |  |
| `tv73` | Kakšen je strošek izdaje za NEO Smartbox (enkratno)? | 🔁 DEFLECT | 25 | 27 | -2 | ‘not in data’; answer is 29 € |
| `tv74` | Ali paket NEO A vključuje programsko shemo Osnovna? | ✅ OK | 100 | 100 | +0 |  |
| `tv75` | Koliko različnih pametnih TV podpira NEO TV Lite hkra… | ✅ OK | 100 | 96 | +4 |  |
