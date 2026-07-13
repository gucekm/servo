# Maks deflection-quality & link audit

Captured 2026-07-13 13:29 UTC. The 51 questions the main audit scored as deflections were re-asked over the raw Boost API (so hyperlinks survive), and every URL Maks emitted was health-checked.

## What a deflection offers the customer

- **18/51 answered outright on the re-ask** — no deflection phrasing at all; the bot's knowledge/coverage shifted since the audit run.
- Of the 33 that still deflect, **22 are *actionable*** — they hand the customer at least one concrete channel (agent, app, link, phone, shop) —
- and **11 are dead ends** — only a clarifying counter-question or a generic apology, with no way forward.

| channel offered | count |
|---|---|
| live agent hand-off | 16 |
| website / link | 8 |
| Moj Telekom app | 5 |

## URL health

- 7 distinct URLs checked; **7 OK, 0 broken**.

| status | URL | note |
|---|---|---|
| OK 200 | https://moj.telekom.si/ | redirects to https://prijava.telekom.si/prijava/realms/telekom/protocol/openid-connect/auth?client_id=mojtelekom-prod-mvc&redirect_uri=https%3A%2F%2Fmoj.telekom.si%3A443%2Fsignin-oidc&response_type=code&scope=openid&code_challenge=k877sZT0G80L-fszBbAWIWcUHUPspZgShLSHsCUzXDE&code_challenge_method=S256&nonce=639195463870598306.YTIzZGIxYzMtOTg0My00ZTU3LTk0NDEtZDk3NWFhNGJhNjM4Nzc2YjlmN2QtNzdkMC00YmMxLTk5M2EtMzExMWE4MmIxNmRm&state=CfDJ8AuekMRTL8BPpw6dvGq1gPzUW0bjhDR7K60PRzQozKkQ7UCZRaeXcD72agdR-yDdIumbhOxZWZltzyJKEfE6mtIJa4cdIMR_HfAyqNKmNnhBEi-3YyTYnPbhr7lriqh2aWCcfdX8fs2evduSf-ChDlwToKhtXXY5-xw3wDkdn-srchNbqgmHg-EFGhmTOrOmp_pNZ9IoiMVg1qYMBXWVwaLjd9e4yW3fpIidrtz2iuvDL6Bji8-NJ-VbL5S1svcW2x0Q_cRXC1ZflgUnHKShzFON1-6xna1g13_bh48ILk1avONpjyWT-Aa0kGo6Hu5Gv2N83GG3ZB6FZCjkusZ2tQLL9SkkRqfnqEdlEFbTEL1dY8W6w_UTR0O4O9A_OPi0qg&x-client-SKU=ID_NET8_0&x-client-ver=8.17.0.0 |
| OK 200 | https://moj.telekom.si/sl/BroadbandDashboard/BroadbandSpeed/Index/$_razmerje_$ | redirects to https://prijava.telekom.si/prijava/realms/telekom/protocol/openid-connect/auth?client_id=mojtelekom-prod-mvc&redirect_uri=https%3A%2F%2Fmoj.telekom.si%3A443%2Fsignin-oidc&response_type=code&scope=openid&code_challenge=SAFb6mEPcYiMq9cXmDPGGp4peU5VfnnPkPfB2B4wsd4&code_challenge_method=S256&nonce=639195463895012508.OGEwZDBjMTctNzdjMy00MjQxLThlNzgtYmI0NDRmODNjY2NlZWE1YzYyZTgtYTVlOC00Zjg0LTk4NDMtNjFlMDM0NTM1ODJm&state=CfDJ8AuekMRTL8BPpw6dvGq1gPxX-heSdHMuqic4glGPFngrZfdA_sGm1Fw1fTeknV-QF12ENr9IxFpAR2AmZ6OiTaeJRd9-blarqMXmVOAjAZCtwPVBfKuVEAH7nCLY3Chmc3GEaDmCTFhA2l3bxFF94Z0jFUACR1VX7EC-KV7ieS3Q786fId8kq-IJa5rD2pDY-dIcHrjaeBhr_BN8AaIv85tLtrJJZ5epblgNePEgREe3y63r5ej7jN5QiRkBZX0Gk9txdOYvr4e-ui9pJcqd5C-PLeW25hGLOwoaNyoqf1NUi7mFWgrmGCT3fTjPaBgqQxm59gQjYwDlTQdLkjFqaa15WshoLHoxt2Fu0LBqjsIJowrxOKvpfnP9rnQ-1uZLDETibw2XsCQ_YVT8-DA_haNNEb_uVwADDkgA6UAvYLfZERSYkjtM0PSC1XNQGm0BVw&x-client-SKU=ID_NET8_0&x-client-ver=8.17.0.0 |
| OK 200 | https://www.telekom.si/internet |  |
| OK 200 | https://www.telekom.si/internet/naj-net |  |
| OK 200 | https://www.telekom.si/media/i5rbkfz3/cenik_klasi%C4%8Dne_storitve_cene_klicev.pdf |  |
| OK 200 | https://www.telekom.si/mobilno/pokritost-mobilnega-omrezja |  |
| OK 200 | https://www.telekom.si/neo/optika |  |

## Answered outright on the re-ask (deflection in the audit)

- **`naj08`** (postpaid) — Kakšna je najvišja hitrost prenosa do uporabnika pri paketih Naj?
  - Maks: ✨ Najvišja hitrost prenosa do uporabnika pri paketu Naj Net je 2 Mbit/s, z možnostjo nadgradnje do 150 Mbit/s v mobilnem omrežju. Za več informacij o paketih Naj Net obiščite 👉 internet.   Potrebujete še kakšno informaci…
- **`bb01`** (broadband) — Kakšna je najvišja hitrost optičnega interneta pri paketih NEO?
  - Maks: ✨ Najvišja hitrost optičnega interneta pri vseh paketih NEO (NEO A, NEO B, NEO C) je do 1 Gbit/s. Vsi paketi omogočajo tudi nadgradnjo hitrosti do 5 Gbit/s. Potrebujete še kakšno informacijo? Kar povejte 😊
- **`bb04`** (broadband) — Kakšna je hitrost internetnega paketa Net na optiki?
  - Maks: ✨ Paket Net na optiki omogoča hitrost do 1 Gbit/s za prenos k uporabniku in do 100 Mbit/s za prenos od uporabnika. Več informacij najdete tukaj 👉 internet.   Potrebujete še kakšno informacijo? Kar povejte 😊
- **`bb06`** (broadband) — Kakšna je akcijska cena fiksnih paketov NEO ob 24-mesečni vezavi?
  - Maks: ✨ Akcijska cena fiksnih paketov NEO ob 24-mesečni vezavi za nove naročnike z mobilnim paketom Naj ali SUPR je 32,99 EUR/mesec. Ta cena velja 24 mesecev v omrežju Telekoma Slovenije ali 12 mesecev v omrežjih alternativnih…
- **`bb15`** (broadband) — Ali priklop NEO 5G zahteva vrtanje ali posege v dom?
  - Maks: ✨ Priklop NEO 5G ne zahteva vrtanja ali posegov v vaš dom. Modem preprosto priklopite sami, brez dodatnih del v stanovanju ali hiši. Želite še kaj dodatno izvedeti? Kar vprašajte 😊
- **`bb21`** (broadband) — Kakšna je redna mesečna cena paketa NEO A?
  - Maks: ✨ Redna mesečna cena paketa NEO A je 49 EUR. Za nove naročnike so na voljo promocijske cene. Potrebujete še kakšno informacijo? Kar povejte 😊
- **`tv25`** (iptv) — Do kdaj je NEO TV Lite brezplačen ob nakupu izbranega televizorja?
  - Maks: ✨ NEO TV Lite je ob nakupu izbranega televizorja brezplačen do 31. 12. 2026, če ga aktivirate do 31. 8. 2026.    Potrebujete še kakšno informacijo? Kar povejte 😊
- **`naj32`** (postpaid) — Kolikšna je priključna taksa za storitev Ena številka?
  - Maks: ✨ Priključna taksa za storitev Ena številka znaša 10,95 EUR z DDV. Če potrebujete še kakšno informacijo, kar povejte 😊
- **`naj48`** (postpaid) — Kolikšen dodatek se zaračuna za SMS iz Slovenije v tuja omrežja?
  - Maks: ✨ Za SMS sporočila, poslana iz Slovenije v tuja omrežja, se obračuna dodatek v višini 0,15 EUR na sporočilo. Ta cena velja za uporabnike naših mobilnih storitev.   Če potrebujete dodatne informacije ali imate še kakšno v…
- **`naj52`** (postpaid) — Koliko časa velja enotna akcijska cena Naj v aplikaciji Moj Telekom?
  - Maks: ✨ Akcijska cena paketa Naj v aplikaciji Moj Telekom velja do preklica ali do zaključka promocijske akcije. Za natančne informacije o trajanju določene akcije priporočamo, da preverite podrobnosti v aplikaciji Moj Telekom…
- **`naj60`** (postpaid) — Kolikšna je priključna taksa ob sklenitvi paketa Naj?
  - Maks: ✨ Priključna taksa ob sklenitvi paketa Naj znaša 29,99 €. Če imate še kakšno vprašanje, sem tukaj, da pomagam! 😊
- **`naj74`** (postpaid) — Kolikšna je cena minute klica iz Slovenije v EU po ceniku (Naj naprava)?
  - Maks: Vas zanimajo dodatni zakupi doma ali v tujini?
- **`bb26`** (broadband) — Kakšna je redna mesečna cena paketa NEO A?
  - Maks: ✨ Redna mesečna cena paketa NEO A je 49 EUR. Če potrebujete še kakšno informacijo, kar povejte 😊
- **`bb30`** (broadband) — Kakšna je akcijska cena fiksnih paketov NEO ob 24-mesečni vezavi?
  - Maks: ✨ Akcijska cena za pakete NEO A, NEO B, NEO C in NEO TV ob 24-mesečni vezavi je 32,99 EUR/mesec za nove naročnike z mobilnim paketom Naj ali SUPR. Brez mobilnega paketa velja akcijska cena 6 mesecev, nato redna cena. Red…
- **`bb36`** (broadband) — Koliko stane fiksni paket Naj Net na mesec?
  - Maks: ✨ Paket Naj Net je mobilni internet in stane 13,99 EUR na mesec. Vključuje neomejen prenos podatkov v omrežju Telekoma Slovenije s hitrostjo do 2/1 Mbit/s. Možna je nadgradnja hitrosti z doplačilom. 👉 Več o Naj Net   Pot…
- **`bb41`** (broadband) — Ali priklop NEO 5G zahteva vrtanje ali posege v dom?
  - Maks: ✨ Priklop NEO 5G ne zahteva vrtanja ali posegov v vaš dom. Modem preprosto priklopite v nekaj korakih in že ste povezani. Namestitev je hitra in enostavna. Potrebujete še kakšno informacijo? Kar povejte 😊
- **`bb74`** (broadband) — Katera telefonska številka je za pomoč pri internetu?
  - Maks: Telefonska številka CPU Telekoma Slovenije je +386 41 700 700.
- **`tv44`** (iptv) — Do kdaj je NEO TV Lite brezplačen ob nakupu izbranega televizorja?
  - Maks: ✨ NEO TV Lite je ob nakupu izbranega televizorja brezplačen do 31. 12. 2026. Potrebna je aktivacija na izbranem televizorju do 31. 8. 2026. Potrebujete še kakšno informacijo? Kar povejte 😊

## Dead-end deflections (no channel offered)

- **`naj11`** (postpaid) — Koliko stane sprememba naročniškega paketa?
  - Maks: Da bom lažje našel najboljšo rešitev, mi povejte, ali želite spremeniti mobilni paket 📱 ali paket s televizijo in internetom 🏠
- **`naj12`** (postpaid) — Kje lahko spremenim svoj naročniški paket Naj?
  - Maks: Da bom lažje našel najboljšo rešitev, mi povejte, ali želite spremeniti mobilni paket 📱 ali paket s televizijo in internetom 🏠
- **`bb03`** (broadband) — Koliko stane paket Net (samo internet) na mesec?
  - Maks: Da bom lažje našel najboljšo rešitev, mi povejte, ali se zanimate za fiksni 🏠 ali mobilni 📱 internet.
- **`bb12`** (broadband) — Kakšna je hitrost do uporabnika pri paketu NEO A na optiki?
  - Maks: ✨ Pri paketu NEO A na optiki (FTTH) je hitrost do uporabnika do 1 Gbit/s, hitrost od uporabnika pa do 40 Mbit/s. Želite izvedeti še kaj o vsebini paketa ali cenah? Potrebujete še kakšno informacijo? Kar povejte 😊
- **`bb16`** (broadband) — Kakšna je hitrost paketa Naj Net in ali je prenos neomejen?
  - Maks: Da bom lažje našel najboljšo rešitev, mi povejte, ali se zanimate za fiksni 🏠 ali mobilni 📱 internet.
- **`naj65`** (postpaid) — Kje lahko spremenim naročniški paket Naj?
  - Maks: Da bom lažje našel najboljšo rešitev, mi povejte, ali želite spremeniti mobilni paket 📱 ali paket s televizijo in internetom 🏠
- **`bb29`** (broadband) — Koliko stane paket Net (samo internet) na mesec?
  - Maks: Da bom lažje našel najboljšo rešitev, mi povejte, ali se zanimate za fiksni 🏠 ali mobilni 📱 internet.
- **`bb51`** (broadband) — Ali lahko internet dobim prek mobilnega omrežja, če ni optike?
  - Maks: Da bom lažje našel najboljšo rešitev, mi povejte, ali se zanimate za fiksni 🏠 ali mobilni 📱 internet.
- **`bb56`** (broadband) — Kolikšen popust na naročnino NEO A prinaša akcija (16 EUR)?
  - Maks: Ali že imate pri nas kakšno naročniko razmerje ali se zanimate za sklenitev novega? 😊
- **`tv33`** (iptv) — Koliko programov ima samostojni paket NEO TV?
  - Maks: ✨ Samostojni paket NEO TV omogoča spremljanje televizijskih programov, vendar nimam podatka o točnem številu programov v tem paketu. Če vas zanima uporaba NEO TV Lite, lahko na njem spremljate vse TV-programe, ki so na v…
- **`tv59`** (iptv) — Kolikšen popust na naročnino prinaša akcija pri paketu NEO TV?
  - Maks: Ali že imate pri nas kakšno naročniko razmerje ali se zanimate za sklenitev novega? 😊

## Per-question detail

| id | answered now? | channels | urls | phones |
|---|---|---|---|---|
| `naj08` | yes | web | 1 | — |
| `naj11` | no | — | 0 | — |
| `naj12` | no | — | 0 | — |
| `naj23` | no | web | 1 | — |
| `mobi21` | no | agent | 0 | — |
| `bb01` | yes | — | 0 | — |
| `bb03` | no | — | 0 | — |
| `bb04` | yes | web | 1 | — |
| `bb06` | yes | — | 0 | — |
| `bb07` | no | agent, web | 1 | — |
| `bb09` | no | agent | 0 | — |
| `bb10` | no | agent | 0 | — |
| `bb12` | no | — | 0 | — |
| `bb15` | yes | — | 0 | — |
| `bb16` | no | — | 0 | — |
| `bb19` | no | agent | 0 | — |
| `bb21` | yes | — | 0 | — |
| `tv24` | no | agent | 0 | — |
| `tv25` | yes | — | 0 | — |
| `naj32` | yes | — | 0 | — |
| `naj48` | yes | — | 0 | — |
| `naj50` | no | web | 1 | — |
| `naj52` | yes | moj_telekom | 0 | — |
| `naj60` | yes | — | 0 | — |
| `naj65` | no | — | 0 | — |
| `naj74` | yes | — | 0 | — |
| `mobi52` | no | agent | 0 | — |
| `mobi61` | no | moj_telekom | 0 | — |
| `bb26` | yes | — | 0 | — |
| `bb29` | no | — | 0 | — |
| `bb30` | yes | — | 0 | — |
| `bb36` | yes | web | 1 | — |
| `bb40` | no | agent, web | 1 | — |
| `bb41` | yes | — | 0 | — |
| `bb43` | no | agent | 0 | — |
| `bb50` | no | agent, moj_telekom | 0 | — |
| `bb51` | no | — | 0 | — |
| `bb52` | no | moj_telekom, web | 1 | — |
| `bb55` | no | agent | 0 | — |
| `bb56` | no | — | 0 | — |
| `bb61` | no | moj_telekom, web | 1 | — |
| `bb64` | no | agent | 0 | — |
| `bb65` | no | web | 1 | — |
| `bb69` | no | agent | 0 | — |
| `bb74` | yes | — | 0 | — |
| `tv33` | no | — | 0 | — |
| `tv44` | yes | — | 0 | — |
| `tv47` | no | agent | 0 | — |
| `tv57` | no | agent, moj_telekom, web | 0 | — |
| `tv59` | no | — | 0 | — |
| `tv73` | no | agent | 0 | — |
