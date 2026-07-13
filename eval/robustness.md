# Maks paraphrase-robustness test

**20 facts** Maks answered perfectly in the main audit, each re-asked in **6 phrasings** (120 fresh conversations), captured 2026-07-13 13:32 UTC. ✓ = all reference facts recalled · ✗ = fact missing/wrong · D = deflected.

| fact | formal | colloquial | nodiacritics | typo | terse | english | robust |
|---|---|---|---|---|---|---|---|
| `rb01` (mobi02) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | yes |
| `rb02` (mobi04) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | yes |
| `rb03` (mobi10) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | yes |
| `rb04` (mobi12) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | yes |
| `rb05` (mobi16) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | yes |
| `rb06` (naj01) | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | NO |
| `rb07` (naj03) | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | NO |
| `rb08` (naj04) | ✓ | D | ✓ | ✓ | ✗ | ✗ | NO |
| `rb09` (naj13) | ✓ | ✓ | ✓ | ✓ | ✓ | D | NO |
| `rb10` (naj14) | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ | NO |
| `rb11` (bb05) | ✓ | D | D | D | D | ✗ | NO |
| `rb12` (bb22) | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | NO |
| `rb13` (bb23) | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | NO |
| `rb14` (bb17) | ✓ | ✗ | ✓ | ✓ | D | ✓ | NO |
| `rb15` (bb02) | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | NO |
| `rb16` (tv01) | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | NO |
| `rb17` (tv03) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | yes |
| `rb18` (tv10) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | yes |
| `rb19` (tv13) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | yes |
| `rb20` (tv08) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | yes |

## Hit rate by phrasing style

| phrasing | facts recalled |
|---|---|
| formal | 19/20 |
| colloquial | 15/20 |
| nodiacritics | 18/20 |
| typo | 19/20 |
| terse | 16/20 |
| english | 12/20 |

**9/20 facts survived every phrasing.** Facts below flipped on at least one variant — the gap between the audit score and what a real (informal) user receives.

### `rb06` (source `naj01`) — facts: [['20,99']]
- **english → MISS** — “What is the regular monthly price of the Naj A plan?”
  - Maks: Would you like to continue the conversation with one of my colleagues?

### `rb07` (source `naj03`) — facts: [['27,99']]
- **english → MISS** — “How much is the Naj B plan per month?”
  - Maks: ✨ The Naj B plan costs €25.99 per month. If you're already a subscriber, you might also benefit from additional discounts or promotions. 😊    Would you like more details about this plan?

### `rb08` (source `naj04`) — facts: [['200 gb']]
- **colloquial → DEFLECT** — “Kdaj mi pri Naj B upočasnijo internet?”
  - Maks: ✨ Pri paketu Naj B se hitrost interneta upočasni, ko porabite vključeno količino prenosa podatkov. Če želite natančne informacije o omejitvah ali dodatnih opcijah, mi prosim sporočite, ali vas zanima …
- **terse → MISS** — “Naj B omejitev GB?”
  - Maks: ✨ Omejitev za prenos podatkov v tujini lahko nastavite v znesku od 0 do 1.000 EUR. Ko dosežete izbrani limit, se prenos podatkov samodejno ustavi in prejmete obvestilo. Potrebujete še kakšno informaci…
- **english → MISS** — “After how many GB does Naj B slow down the data speed?”
  - Maks: Would you like to explore additional add-ons for home or abroad?

### `rb09` (source `naj13`) — facts: [['5 eur', '5,00']]
- **english → DEFLECT** — “How big is the Poveži in prihrani discount?”
  - Maks: ✨ Hvala za vaše vprašanje! Višina popusta v okviru naše ponudbe Poveži in prihrani je odvisna od izbranih storitev in paketov, ki jih združite. Za natančne informacije glede višine popusta vam priporo…

### `rb10` (source `naj14`) — facts: [['1 eur', '1,00']]
- **colloquial → MISS** — “Koliko me stane, da imam eno številko na dveh SIM karticah?”
  - Maks: ✨ Ena telefonska številka ne more biti hkrati aktivna na dveh SIM-karticah. Lahko pa uporabite dve rešitvi:    Naj naprava: omogoča dodatno SIM (ali eSIM) za uporabo podatkov in SMS/MMS na drugi napra…
- **english → MISS** — “How much does the Ena številka service cost per month?”
  - Maks: ✨ I’m not sure I understood your question fully. Are you asking about the cost of a specific Telekom Slovenije service? Could you clarify the name of the service or provide more details?

### `rb11` (source `bb05`) — facts: [['13,99']]
- **colloquial → DEFLECT** — “Koliko pride Naj Net mesečno?”
  - Maks: ✨ Ali vas zanima paket Naj Net za mobilne storitve 📱 ali za internet in TV storitve 🏠? Tako vam lahko bolje pomagam!
- **nodiacritics → DEFLECT** — “koliko stane paket naj net mesecno”
  - Maks: Da bom lažje našel najboljšo rešitev, mi povejte, ali se zanimate za fiksni 🏠 ali mobilni 📱 internet.
- **typo → DEFLECT** — “Kolko stane pakt Naj Net?”
  - Maks: Da bom lažje našel najboljšo rešitev, mi povejte, ali se zanimate za fiksni 🏠 ali mobilni 📱 internet.
- **terse → DEFLECT** — “Naj Net cena?”
  - Maks: Da bom lažje našel najboljšo rešitev, mi povejte, ali se zanimate za fiksni 🏠 ali mobilni 📱 internet.
- **english → MISS** — “What is the monthly price of the Naj Net fixed internet plan?”
  - Maks: ✨ The monthly price details for the Naj Net fixed internet plan are not provided here. Would you like me to guide you to more information about our 🏠 Internet and TV services?

### `rb12` (source `bb22`) — facts: [['58 eur', '58,00', '58 €']]
- **colloquial → MISS** — “Koliko pa je NEO B na mesec brez akcije?”
  - Maks: ✨ Cena paketa NEO B brez akcije je 56,99 € na mesec. Če potrebujete dodatne informacije ali želite preveriti trenutno ponudbo, mi sporočite! 😊

### `rb13` (source `bb23`) — facts: [['63 eur', '63,00', '63 €']]
- **english → MISS** — “How much does the NEO C package cost per month at the regular price?”
  - Maks: ✨ The regular monthly price for the NEO C package is €56.99.    If you're interested in additional details or promotions, feel free to ask! 😊

### `rb14` (source `bb17`) — facts: [['150 mbit', '150']]
- **colloquial → MISS** — “Do kakšne hitrosti lahko pridem z Naj Net, če doplačam?”
  - Maks: ✨ Z doplačilom lahko pri paketih NEO Net dosežete naslednje hitrosti:    Do 80 Mbit/s / 40 Mbit/s (VDSL) za 5 €/mesec. Do 1 Gbit/s / 300 Mbit/s (FTTH) za 10 €/mesec. Do 2 Gbit/s / 100 Mbit/s (FTTH) za…
- **terse → DEFLECT** — “Naj Net max hitrost?”
  - Maks: Hitrost interneta, ki je vključena v vašem paketu, lahko preverite spodaj 👇 💡 Če dostopa do Mojega Telekoma še nimate, si ga čim prej zagotovite. Moj Telekom vam omogoča, da vsa svoja razmerja urejate…

### `rb15` (source `bb02`) — facts: [['5 gbit', '5 gb/s']]
- **terse → MISS** — “NEO optika max hitrost?”
  - Maks: ✨ Na optičnem omrežju NEO lahko nadgradite hitrost do 2 Gbit/s / 100 Mbit/s za doplačilo. Največja hitrost je odvisna od tehničnih zmogljivosti linije.

### `rb16` (source `tv01`) — facts: [['150']]
- **formal → MISS** — “Koliko TV programov vključuje paket NEO A?”
  - Maks: ✨ Paket NEO A vključuje osnovni nabor TV-programov, vendar točno število programov ni navedeno v razpoložljivih podatkih. Za podrobnejši seznam programov priporočamo, da preverite aktualno programsko …
- **nodiacritics → MISS** — “koliko tv programov vkljucuje paket neo a”
  - Maks: ✨ Paket NEO A vključuje osnovni nabor TV-programov, ki zajema več kot 120 TV-programov različnih žanrov. Točen seznam programov lahko preverite v naši aktualni programski shemi. Potrebujete še kakšno …
- **english → MISS** — “How many TV channels are included in the NEO A package?”
  - Maks: ✨ The exact number of TV channels included in the NEO A package is not specified in the knowledge base. Would you like me to connect you with a colleague for more details?

