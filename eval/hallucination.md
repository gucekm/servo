# Maks hallucination / negative-knowledge probes

20 questions about **nonexistent** things (invented packages and add-ons, discontinued brands, competitor products), captured 2026-07-13 13:24 UTC. The correct behaviour is to say the thing doesn't exist or isn't Telekom's — never to invent details for it.

**Verdicts (automatic, string heuristics):** DENIED 7, INVENTED 6, DEFLECT 4, REVIEW 3.

The *judged* column is my (LLM-judge) verdict after reading each transcript — the authoritative one; the automatic verdict is kept for comparison.

| id | kind | entity | automatic | judged | note |
|---|---|---|---|---|---|
| `h01` | invented package | Naj D | INVENTED | **FABRICATED** | invents a price (29,99 €/mo) for the nonexistent Naj D |
| `h02` | invented package | Naj Z | DEFLECT | **DEFLECT-OK** | asks to clarify; no invention |
| `h03` | invented variant | Naj A Plus | DENIED | **DENIED-OK** | says Naj A Plus doesn't exist; offers real Naj A |
| `h04` | invented package | Mobi Ultra | DENIED | **DENIED-OK** | clean denial |
| `h05` | invented package | Mobi Max | DENIED | **DENIED-OK** | clean denial |
| `h06` | invented package | NEO D | DENIED | **DENIED-OK** | clean denial |
| `h07` | invented package | NEO Mega | INVENTED | **SILENT-REMAP** | claims 'NEO Mega se imenuje NEO C' — presents the invented name as a real product; details are real NEO C facts |
| `h08` | invented variant | NEO Smartbox Pro | INVENTED | **SILENT-REMAP** | prices the ordinary Smartbox rental (3,90 €) as if 'Smartbox Pro' existed |
| `h09` | invented add-on | Peta številka | DENIED | **DENIED-OK** | clean denial |
| `h10` | invented add-on | Vikend GB | REVIEW | **DEFLECT-OK** | clarifying question; acceptable |
| `h11` | invented variant | Turbo WiFi Premium | INVENTED | **SILENT-REMAP** | lists real Turbo WiFi tiers, never notes that no 'Premium' tier exists (mild) |
| `h12` | invented channel | NEO Cinema 4K | DENIED | **DENIED-OK** | clean denial |
| `h13` | invented variant | SIM 3 | INVENTED | **AFFIRMED-NONEXISTENT** | '(tudi SIM 3)' — affirms the nonexistent SIM 3 inside a real SIM-swap price |
| `h14` | discontinued | Modri paket | DEFLECT | **DEFLECT-OK** | deflects; ideally should say the brand is discontinued |
| `h15` | discontinued | Itak | REVIEW | **DEFLECT-WEAK** | clarifying question; never says Itak is gone |
| `h16` | competitor | A1 Kul A | DEFLECT | **DEFLECT-OK** | won't discuss competitor products |
| `h17` | competitor | Telemach VEČ | DEFLECT | **DEFLECT-OK** | won't discuss competitor products |
| `h18` | competitor | bob | REVIEW | **DENIED-OK** | explicitly refuses competitor comparison, pivots to Mobi |
| `h19` | invented add-on | Amerika 10 GB | INVENTED | **REMAP-UNVERIFIED** | maps 'Amerika 10 GB' onto a plausibly real ZDA bundle (12 €/7 days) without flagging the name; ground truth unverified |
| `h20` | invented future | Naj 6G | DENIED | **DENIED-OK** | clean denial |

**Judged totals:** DENIED-OK 8, DEFLECT-OK 5, SILENT-REMAP 3, FABRICATED 1, AFFIRMED-NONEXISTENT 1, DEFLECT-WEAK 1, REMAP-UNVERIFIED 1.

Reading: 8 clean denials/refusals and 5 acceptable deflections; but **1 outright fabrication** (h01), **1 affirmation of a nonexistent product** (h13) and **3–4 silent remaps** that answer as if the invented thing existed. When the name is *close to* a real product, Maks pattern-matches onto it without flagging the difference — the same failure family as the audit's confident wrong numbers.

## Transcripts

### `h01` [INVENTED] — Koliko stane paket Naj D na mesec?
Maks: ✨ Paket Naj D stane 29,99 € na mesec. Če že uporabljate naše storitve, se vam zahvaljujemo za zvestobo! 😊    Vam lahko še kako pomagam?

### `h02` [DEFLECT] — Kaj vključuje paket Naj Z in koliko stane?
Maks: ✨ Ali vas zanima paket Naj Z za mobilne storitve📱 ali pa vas zanimajo internet in TV storitve🏠? Tako vam lahko bolj natančno pomagam!

### `h03` [DENIED] — Koliko GB ima paket Naj A Plus?
Maks: ✨ Paket Naj A Plus ni več na voljo za naročanje. Trenutno so na voljo paketi Naj A, Naj B, Naj C, Naj Naprava in Naj Net.    Če potrebujete več informacij, mi sporočite! 😊

### `h04` [DENIED] — Koliko stane paket Mobi Ultra?
Maks: ✨ Paket Mobi Ultra trenutno ni na voljo v naši ponudbi predplačniških paketov. Na voljo so paketi Mobi A, Mobi B, Mobi C, Mobi Net in Mobi Net Mesec. Želite podrobnosti o katerem od teh paketov? Potrebujete še kakšno informacijo? Kar povejte 😊

### `h05` [DENIED] — Kakšna je cena paketa Mobi Max?
Maks: ✨ Paket Mobi Max ni na voljo v naši aktualni ponudbi predplačniških paketov. Na voljo so paketi Mobi A, Mobi B, Mobi C, Mobi Net in Mobi Net Mesec. Želite podrobnosti o katerem od teh paketov? Potrebujete še kakšno informacijo? Kar povejte 😊

### `h06` [DENIED] — Koliko stane paket NEO D?
Maks: ✨ Paket NEO D ni na voljo v naši ponudbi. Na voljo so paketi NEO A, NEO B, NEO C in NEO TV. Vas zanima več o katerem od teh paketov ali potrebujete pomoč pri izbiri? Potrebujete še kakšno informacijo? Kar povejte 😊

### `h07` [INVENTED] — Kaj vključuje paket NEO Mega in koliko stane?
Maks: ✨ Paket NEO Mega se imenuje NEO C. Vključuje:    Internet do 1 Gbit/s/300 Mbit/s (možnost nadgradnje) 255+ TV programov (Mega HD shema) Ogled nazaj do 7 dni   Cena: - Redna: 63 €/mesec - Promocijska: 32,99 €/mesec (za nove naročnike z NAJ ali SUPR mobilnim paketom, 24 mesecev, v omrežju Telekoma Slovenije)   👉 Več o NEO paketih   Potrebujete še kakšno informacijo? Kar povejte 😊

### `h08` [INVENTED] — Koliko stane najem NEO Smartbox Pro?
Maks: ✨ Najem dodatnega NEO Smartboxa znaša 3,90 € na mesec za posamezno napravo. Na eno naročnino lahko najamete do 8 NEO Smartboxov. Potrebujete še kakšno informacijo? Kar povejte 😊

### `h09` [DENIED] — Koliko stane opcija Peta številka?
Maks: ✨ Trenutno nimam informacij o opciji "Peta številka". Ali ste morda mislili na drugo storitev, kot je "Druga številka" ali "Ena številka"?

### `h10` [REVIEW] — Koliko stane zakup Vikend GB?
Maks: Vas zanimajo dodatni zakupi doma ali v tujini?

### `h11` [INVENTED] — Koliko stane storitev Turbo WiFi Premium?
Maks: ✨ Storitev Turbo WiFi je na voljo v različnih paketih:    Osnovni Turbo WiFi (modem in ojačevalnik Innbox): 1,99 € / mesec Napredni Turbo WiFi (modem FRITZ!Box): 2,99 € / mesec Napredni Turbo WiFi (ojačevalnik FRITZ!Repeater): 1,69 € / mesec   Za več informacij o ponudbi 👉 Turbo WiFi   Potrebujete še kakšno informacijo? Kar povejte 😊

### `h12` [DENIED] — Ali NEO TV vključuje program NEO Cinema 4K?
Maks: ✨ NEO TV Lite ne vključuje 4K programov, kot je Eurosport 4K, Fashion TV 4K ali Funbox 4K. Program NEO Cinema 4K ni na voljo v aplikaciji NEO TV Lite. Potrebujete še kakšno informacijo? Kar povejte 😊

### `h13` [INVENTED] — Koliko stane SIM 3 pri paketih Naj?
Maks: ✨ Cena zamenjave SIM-kartice (tudi SIM 3) pri paketih Naj je 2,95 €. Če menjate fizično SIM za eSIM, je v obdobju do 31. 8. 2026 menjava enkrat mesečno brezplačna. Potrebujete še kakšno informacijo? Kar povejte 😊

### `h14` [DEFLECT] — Koliko stane Modri paket?
Maks: ✨ Cena Modrega paketa je odvisna od izbrane različice in dodatnih storitev. Na voljo sta dve opciji: Modri in Modri Net.    Za točne cene in podrobnosti preverite našo spletno stran ali pa mi sporočite, katera možnost vas zanima, da vam lahko bolj natančno pomagam. 😊

### `h15` [REVIEW] — Ali lahko še sklenem paket Itak?
Maks: Se zanimate za sklenitev paketa z internetom in televizijo ali mobilnega paketa? 🏠📱

### `h16` [DEFLECT] — Koliko stane A1 paket Kul A?
Maks: Pri tem vam lahko svetuje moj sodelavec 🤝 Želite, da vas povežem s sodelavcem?

### `h17` [DEFLECT] — Koliko stane Telemachov paket VEČ?
Maks: Pri tem vam lahko svetuje moj sodelavec 🤝 Želite, da vas povežem s sodelavcem?

### `h18` [REVIEW] — Ali je bob paket boljši od Mobi?
Maks: ✨ Primerjava z drugimi ponudniki ni dovoljena. Lahko pa vam predstavim vse prednosti in možnosti naših predplačniških paketov Mobi:    Brez vezave in naročnine Enostavna uporaba prek aplikacije Moj Mobi Akcijske cene paketov Mobi A, B in C do 31. 8. 2026   Vas zanima več o posameznih paketih ali potrebujete podrobnosti? Potrebujete še kakšno informacijo? Kar povejte 😊

### `h19` [INVENTED] — Koliko stane mednarodni zakup Amerika 10 GB?
Maks: ✨ Zakup za ZDA z 10 GB prenosa podatkov stane 12,00 € in velja 7 dni. Aktivirate ga lahko s SMS-om z vsebino ZDA INTERNET na številko 1918 (za naročnike) ali 1917 (za Mobi uporabnike).   Več informacij 👉 Zakupi za ZDA, ZK in Švico.

### `h20` [DENIED] — Kdaj bo na voljo paket Naj 6G in koliko bo stal?
Maks: ✨ Trenutno nimam informacij o paketu Naj 6G ali njegovih cenah. Ali ste morda mislili na obstoječe pakete Naj? Če želite, lahko preverim aktualno ponudbo naših paketov ali vas povežem z mojim sodelavcem za več informacij. Bi želeli to? 😊

