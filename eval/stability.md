# Maks answer-stability test

Panel of **20 questions**, each asked in **5 fresh conversations** (100 conversations total), captured 2026-07-13 13:24 UTC. Scored with the same rubric as the main audit (`evaluate.py`).

Verdicts: **FULL** = every reference fact recalled · **PARTIAL** = some · **ZERO** = none (specific but wrong, or off-topic) · **DEFLECT** = non-answer hand-off · **ERROR** = transport failure.

| id | baseline (audit) | run verdicts | distinct answers | stable? |
|---|---|---|---|---|
| `naj10` | ZERO | ZERO ZERO ZERO ZERO ZERO | 4/5 | yes |
| `naj32` | DEFLECT | ZERO ZERO ZERO ZERO ZERO | 4/5 | yes (differs from audit) |
| `naj33` | ZERO | FULL FULL FULL FULL FULL | 5/5 | yes (differs from audit) |
| `naj46` | ZERO | ZERO DEFLECT DEFLECT ZERO DEFLECT | 5/5 | NO |
| `naj57` | ZERO | ZERO ZERO ZERO ZERO ZERO | 5/5 | yes |
| `mobi05` | ZERO | FULL FULL FULL FULL FULL | 5/5 | yes (differs from audit) |
| `mobi08` | ZERO | ZERO ZERO ZERO ZERO ZERO | 5/5 | yes |
| `mobi41` | ZERO | ZERO ZERO ZERO ZERO ZERO | 5/5 | yes |
| `tv07` | ZERO | DEFLECT DEFLECT DEFLECT DEFLECT ZERO | 5/5 | NO |
| `tv32` | ZERO | DEFLECT DEFLECT DEFLECT DEFLECT DEFLECT | 5/5 | yes (differs from audit) |
| `tv38` | ZERO | ZERO ZERO ZERO ZERO ZERO | 5/5 | yes |
| `tv62` | ZERO | ZERO ZERO ZERO ZERO ZERO | 5/5 | yes |
| `bb26` | DEFLECT | FULL FULL FULL FULL FULL | 3/5 | yes (differs from audit) |
| `mobi02` | FULL | FULL FULL FULL FULL FULL | 5/5 | yes |
| `naj01` | FULL | FULL FULL FULL FULL FULL | 5/5 | yes |
| `bb02` | FULL | FULL FULL FULL FULL FULL | 5/5 | yes |
| `tv01` | FULL | ZERO ZERO DEFLECT ZERO ZERO | 5/5 | NO |
| `bb01` | DEFLECT | FULL FULL FULL FULL FULL | 4/5 | yes (differs from audit) |
| `bb03` | DEFLECT | DEFLECT DEFLECT DEFLECT DEFLECT DEFLECT | 1/5 | yes |
| `bb04` | DEFLECT | FULL FULL FULL FULL FULL | 2/5 | yes (differs from audit) |

## Summary

- **17/20 questions gave the same verdict in every run.**
- Run-verdict mix across all 100 answers: ZERO 42, FULL 40, DEFLECT 18.
- Of the 13 confirmed-error questions on the panel, **7 reproduce a wrong/incomplete answer in every run** — i.e. the audit's flagged errors are predominantly *stable knowledge defects*, not sampling noise.

## Questions with unstable or shifted verdicts

### `naj32` — Kolikšna je priključna taksa za storitev Ena številka?
Baseline (audit): **DEFLECT**
- run 1 **ZERO** (recall 0.0): ✨ Priključna taksa za sklenitev novega naročniškega razmerja, kot je storitev Ena številka, znaša 10,95 EUR z DDV. Če gre za spremembo obstoječega paketa, se ta znesek ne zaračuna. Potrebujete še kakš…
- run 2 **ZERO** (recall 0.0): ✨ Priključna taksa za storitev Ena številka znaša 10,95 EUR z DDV. Če potrebujete še kakšno informacijo, kar povejte 😊
- run 3 **ZERO** (recall 0.0): ✨ Priključna taksa za storitev Ena številka znaša 10,95 EUR z DDV. Če potrebujete še kakšno informacijo, kar povejte 😊
- run 4 **ZERO** (recall 0.0): ✨ Priključna taksa za storitev Ena številka znaša 10,95 EUR z DDV. Če želite, vam lahko dodatno razložim postopek vključitve ali pogoje uporabe. Potrebujete še kakšno informacijo? Kar povejte 😊
- run 5 **ZERO** (recall 0.0): ✨ Priključna taksa za storitev Ena številka znaša 10,95 EUR z DDV. Če želite, lahko razložim še kaj podrobneje ali pomagam pri drugih vprašanjih. Potrebujete še kakšno informacijo? Kar povejte 😊

### `naj33` — Koliko stane mesečna naročnina storitve SIM 2 (Brezskrbni)?
Baseline (audit): **ZERO**
- run 1 **FULL** (recall 1.0): ✨ Mesečna naročnina za storitev SIM 2 Brezskrbni znaša 14,99 EUR. Cena velja za pakete Naj A, Naj B, Naj C in Naj 5G.    Potrebujete še kakšno informacijo? Kar povejte 😊
- run 2 **FULL** (recall 1.0): ✨ Mesečna naročnina za SIM 2 brezskrbni je 14,99 EUR. Ta cena velja za uporabo s paketi Naj A, Naj B, Naj C ali Naj 5G. Potrebujete še kakšno informacijo? Kar povejte 😊
- run 3 **FULL** (recall 1.0): ✨ Mesečna naročnina za SIM 2 brezskrbni znaša 14,99 EUR, če jo uporabljate s paketi Naj A, Naj B, Naj C ali Naj 5G. Če imate enotni ali podatkovni paket, je mesečna naročnina 11,99 EUR. Potrebujete še…
- run 4 **FULL** (recall 1.0): ✨ Mesečna naročnina za SIM 2 brezskrbni znaša 14,99 EUR, če jo uporabljate s paketi Naj A, Naj B, Naj C ali Naj 5G. Če imate enotni ali podatkovni paket, je cena 11,99 EUR na mesec. Potrebujete še kak…
- run 5 **FULL** (recall 1.0): ✨ Mesečna naročnina za SIM 2 brezskrbni je 14,99 EUR, če jo dodate k paketom Naj A, Naj B, Naj C ali Naj 5G. Če imate enotni ali podatkovni paket, je mesečna naročnina 11,99 EUR. Potrebujete še kakšno…

### `naj46` — Koliko GB v EU-tarifi lahko brezplačno porabim s paketom Naj B?
Baseline (audit): **ZERO**
- run 1 **ZERO** (recall 0.0): ✨ Za informacijo o količini podatkov, ki jih lahko brez doplačil porabite v EU-tarifi s paketom Naj B, prosim preverite pogoje vašega paketa ali obiščite 👉 eu-pribitki.   Potrebujete še kakšno informa…
- run 2 **DEFLECT** (recall 0.0): ✨ Trenutno nimam podatka o točno dovoljeni količini GB za paket Naj B v EU-tarifi. Priporočam, da preverite svoj paket ali me prosim dopolnite, če potrebujete podrobnosti o drugem paketu. Več informac…
- run 3 **DEFLECT** (recall 0.0): ✨ Trenutno nimam podatka o točno dovoljeni količini GB za brezplačno uporabo v EU-tarifi pri paketu Naj B. Priporočam, da preverite podrobnosti svojega paketa na naši spletni strani ali v Moj Telekom …
- run 4 **ZERO** (recall 0.0): ✨ Za točen podatek o količini brezplačnih GB v EU-tarifi pri paketu Naj B preverite pogoje vašega paketa, saj se lahko količina razlikuje glede na paket in morebitne spremembe. Več informacij najdete …
- run 5 **DEFLECT** (recall 0.0): ✨ Informacija o količini podatkov, ki jih lahko brezplačno porabite v EU-tarifi s paketom Naj B, ni navedena v moji bazi znanja. Priporočam, da preverite svoj paket v Moj Telekom ali vprašate mojega s…

### `mobi05` — Po koliko GB se v paketu Mobi C zniža hitrost prenosa?
Baseline (audit): **ZERO**
- run 1 **FULL** (recall 1.0): ✨ V paketu Mobi C se hitrost prenosa podatkov zniža po porabljenih 200 GB v Sloveniji. Nato je hitrost omejena na 64/64 kbit/s do naslednjega zakupa. Vam lahko še kaj dodatno pojasnim?
- run 2 **FULL** (recall 1.0): ✨ V paketu Mobi C se hitrost prenosa podatkov zniža po porabljenih 200 GB v Sloveniji. Nato znaša hitrost 64/64 kbit/s do naslednjega zakupa.    Potrebujete še kakšno informacijo? Kar povejte 😊
- run 3 **FULL** (recall 1.0): ✨ Pri paketu Mobi C se hitrost prenosa podatkov zniža po porabljenih 200 GB v Sloveniji. Nato je hitrost omejena na 64/64 kbit/s do naslednjega zakupa. Vam lahko še kaj dodatno pojasnim?
- run 4 **FULL** (recall 1.0): ✨ V paketu Mobi C se hitrost prenosa podatkov zniža po porabljenih 200 GB v Sloveniji. Po tej meji je hitrost omejena na 64/64 kbit/s do naslednjega zakupa. Vam lahko še kaj dodatno pojasnim?
- run 5 **FULL** (recall 1.0): ✨ V paketu Mobi C se hitrost prenosa podatkov zniža po porabljenih 200 GB v Sloveniji. Po tem je hitrost omejena na 64/64 kbit/s do naslednjega zakupa. V tujini (EU-tarifa) velja enaka omejitev po dos…

### `tv07` — Koliko stane samostojni TV paket NEO TV brez interneta?
Baseline (audit): **ZERO**
- run 1 **DEFLECT** (recall 0.0): ✨ Ali vas zanima več o naših Internet in TV storitvah 🏠 ali pa morda o mobilnih storitvah 📱? Tako vam lahko natančneje pomagam!
- run 2 **DEFLECT** (recall 0.0): ✨ Ali vas zanima samo TV paket brez interneta 🏠 ali pa morda tudi mobilne storitve 📱? Tako vam lahko bolje pomagam!
- run 3 **DEFLECT** (recall 0.0): ✨ Ali vas zanima več o naših Internet in TV storitvah 🏠 ali pa zgolj o mobilnih storitvah 📱? Tako vam lahko bolje pomagam!
- run 4 **DEFLECT** (recall 0.0): ✨ Ali vas zanima več o naših Internet in TV storitvah 🏠 ali pa iščete informacije o mobilnih storitvah 📱? Prosim, sporočite, da vas lahko usmerim naprej!
- run 5 **ZERO** (recall 0.0): ✨ Za samostojne TV pakete, kot je NEO TV brez interneta, je najbolje, da preverimo možnosti v kategoriji Internet in TV storitev.    Ali želite, da nadaljujem z informacijami o teh paketih? 🏠

### `tv32` — Koliko stane samostojni TV paket NEO TV (brez interneta)?
Baseline (audit): **ZERO**
- run 1 **DEFLECT** (recall 0.0): ✨ Za samostojni TV paket NEO TV (brez interneta) je najbolje, da preverim podrobnosti. Ali vas zanimajo Internet in TV storitve 🏠, da lahko nadaljujem?
- run 2 **DEFLECT** (recall 0.0): ✨ Na voljo imamo različne TV pakete, vključno s samostojnim paketom NEO TV.    Ali vas zanima več o Internet in TV storitvah 🏠 ali pa morda o mobilnih storitvah 📱? Tako vam lahko bolje pomagam! 😊
- run 3 **DEFLECT** (recall 0.0): ✨ Ali vas zanima več o naših 🏠 Internet in TV storitvah ali 📱 mobilnih storitvah? Tako vam lahko bolje pomagam!
- run 4 **DEFLECT** (recall 0.0): ✨ Na voljo imamo različne TV pakete, vključno s samostojnim paketom NEO TV.    Ali vas zanima več o Internet in TV storitvah 🏠 ali pa morda o mobilnih storitvah 📱? Tako vam lahko natančneje pomagam. 😊
- run 5 **DEFLECT** (recall 0.0): ✨ Ali vas zanima več o naših Internet in TV storitvah 🏠 ali morda o mobilnih storitvah 📱? Tako vam lahko bolje pomagam!

### `bb26` — Kakšna je redna mesečna cena paketa NEO A?
Baseline (audit): **DEFLECT**
- run 1 **FULL** (recall 1.0): ✨ Redna mesečna cena paketa NEO A je 49 EUR. Če potrebujete še kakšno informacijo, kar povejte 😊
- run 2 **FULL** (recall 1.0): ✨ Redna mesečna cena paketa NEO A je 49 EUR. Če potrebujete še kakšno informacijo, mi prosim sporočite 😊
- run 3 **FULL** (recall 1.0): ✨ Redna mesečna cena paketa NEO A znaša 49 EUR. Če potrebujete še kakšno informacijo, kar povejte 😊
- run 4 **FULL** (recall 1.0): ✨ Redna mesečna cena paketa NEO A znaša 49 EUR. Če potrebujete še kakšno informacijo, kar povejte 😊
- run 5 **FULL** (recall 1.0): ✨ Redna mesečna cena paketa NEO A je 49 EUR. Če potrebujete še kakšno informacijo, mi prosim sporočite 😊

### `tv01` — Koliko TV programov vključuje paket NEO A?
Baseline (audit): **FULL**
- run 1 **ZERO** (recall 0.0): ✨ Paket NEO A vključuje osnovni nabor TV programov, ki se lahko občasno spreminja. Za točno število in seznam programov priporočamo ogled aktualne prodajne ponudbe na naši spletni strani ali v Moj Tel…
- run 2 **ZERO** (recall 0.0): ✨ Paket NEO A vključuje osnovni nabor TV programov, število pa se lahko občasno spreminja glede na ponudbo in pravice predvajanja. Za točno aktualno število programov priporočamo ogled uradne prodajne…
- run 3 **DEFLECT** (recall 0.0): ✨ Paket NEO A vključuje osnovni nabor TV programov, vendar točno število programov ni navedeno v razpoložljivi bazi znanja. Priporočam, da preverite aktualen seznam programov na naši uradni spletni st…
- run 4 **ZERO** (recall 0.0): ✨ Paket NEO A vključuje osnovni nabor TV programov, ki jih lahko spremljate na NEO Smartboxu, v aplikaciji NEO in na drugih napravah. Točno število programov se lahko spreminja, zato priporočamo, da p…
- run 5 **ZERO** (recall 0.0): ✨ Paket NEO A vključuje osnovni nabor TV programov, ki so prilagojeni za osnovno spremljanje televizije. Točno število programov se lahko spreminja, zato priporočamo, da preverite aktualen seznam prog…

### `bb01` — Kakšna je najvišja hitrost optičnega interneta pri paketih NEO?
Baseline (audit): **DEFLECT**
- run 1 **FULL** (recall 1.0): ✨ Najvišja hitrost optičnega interneta pri paketih NEO (A, B, C) je do 1 Gbit/s. Vsi paketi omogočajo tudi nadgradnjo hitrosti do 5 Gbit/s. Potrebujete še kakšno informacijo? Kar povejte 😊
- run 2 **FULL** (recall 1.0): ✨ Najvišja hitrost optičnega interneta pri vseh paketih NEO (A, B, C) je do 1 Gbit/s. Vsi paketi omogočajo nadgradnjo hitrosti do 5 Gbit/s. Potrebujete še kakšno informacijo? Kar povejte 😊
- run 3 **FULL** (recall 1.0): ✨ Najvišja hitrost optičnega interneta pri vseh paketih NEO (A, B, C) je do 1 Gbit/s. Vsi paketi omogočajo tudi nadgradnjo hitrosti do 5 Gbit/s. Potrebujete še kakšno informacijo? Kar povejte 😊
- run 4 **FULL** (recall 1.0): ✨ Najvišja hitrost optičnega interneta pri paketih NEO (NEO A, NEO B, NEO C) je do 1 Gbit/s. Vsi paketi omogočajo tudi nadgradnjo hitrosti do 5 Gbit/s. Potrebujete še kakšno informacijo? Kar povejte 😊
- run 5 **FULL** (recall 1.0): ✨ Najvišja hitrost optičnega interneta pri vseh paketih NEO (A, B, C) je do 1 Gbit/s. Vsi paketi omogočajo tudi nadgradnjo hitrosti do 5 Gbit/s. Potrebujete še kakšno informacijo? Kar povejte 😊

### `bb04` — Kakšna je hitrost internetnega paketa Net na optiki?
Baseline (audit): **DEFLECT**
- run 1 **FULL** (recall 1.0): ✨ Paket Net na optiki omogoča hitrost do 1 Gbit/s za prenos k uporabniku in do 100 Mbit/s za prenos od uporabnika. Več informacij najdete tukaj 👉 internet.   Potrebujete še kakšno informacijo? Kar pov…
- run 2 **FULL** (recall 1.0): ✨ Paket Net na optiki omogoča hitrosti do 1 Gbit/s za prenos k uporabniku in do 100 Mbit/s za prenos od uporabnika. Več informacij najdete tukaj 👉 internet.   Potrebujete še kakšno informacijo? Kar po…
- run 3 **FULL** (recall 1.0): ✨ Paket Net na optiki omogoča hitrosti do 1 Gbit/s za prenos k uporabniku in do 100 Mbit/s za prenos od uporabnika. Več informacij najdete tukaj 👉 internet.   Potrebujete še kakšno informacijo? Kar po…
- run 4 **FULL** (recall 1.0): ✨ Paket Net na optiki omogoča hitrost do 1 Gbit/s za prenos k uporabniku in do 100 Mbit/s za prenos od uporabnika. Več informacij najdete tukaj 👉 internet.   Potrebujete še kakšno informacijo? Kar pov…
- run 5 **FULL** (recall 1.0): ✨ Paket Net na optiki omogoča hitrost do 1 Gbit/s za prenos k uporabniku in do 100 Mbit/s za prenos od uporabnika. Več informacij najdete tukaj 👉 internet.   Potrebujete še kakšno informacijo? Kar pov…

