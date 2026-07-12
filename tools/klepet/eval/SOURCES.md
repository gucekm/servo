# Sources & grounding

All reference facts used to score the Maks answers were taken from first-party
Telekom Slovenije sources, captured **2026-07-12**. Prices and offers change, so
this is a point-in-time snapshot.

## Bot under test

- **Maks** chat assistant, reached via its public Boost.ai Chat API:
  `https://telekom-slovenije.boost.ai/api/chat/v2` (one fresh conversation per
  question, language `sl-SI`).

## Product pages (HTML → visible text)

- https://www.telekom.si/mobilno
- https://www.telekom.si/mobilno/paketi-naj      — Naj A/B/C, Naj naprava, EU allowances, throttle speeds, priključna taksa
- https://www.telekom.si/mobilno/mobi            — Mobi A/B/C, Mobi Net, activation, refill, per-unit tariffs
- https://www.telekom.si/mobilno/supr
- https://www.telekom.si/mobilno/naj-naprava
- https://www.telekom.si/internet                — NEO A/B/C, Net, speeds, optika availability
- https://www.telekom.si/internet/naj-net
- https://www.telekom.si/neo                     — NEO packages, programme counts, schemes, NEO TV, NEO TV Lite
- https://www.telekom.si/neo/enotna-izkusnja
- https://www.telekom.si/pomoc/ceniki            — price-list hub

## Price lists (ceniki, PDF → text via PyMuPDF)

- /media/2eajxbcs/cenik_povezane_storitve.pdf                                  — NEO fixed packages, TV-komunikator (3,90 €/29 €), SIM 2, extra phone number (1,27 €)
- /media/jwrpeuk5/2_cenik_..._ena_stevilka.pdf                                 — Ena številka 1,00 €/mo, connection fee FREE
- /media/bemammug/2_cenik_..._sim_2.pdf                                        — SIM 2 11,99 €/mo, taksa 10,95 €, 100 MB
- /media/hevlvzgh/2_cenik_..._varen_splet.pdf                                  — Varen splet 0,99 €/mo
- /media/yg2pwmti/2_cenik_..._zavarovanje_naprav.pdf                           — device-insurance tiers (Premium)
- /media/etspx05m/2_cenik_..._programske_opcije_.pdf                           — NEO igre 7,99 €, Da Vinci Kids free
- /media/d2bor0pl/4_cenik_mobi_storitve.pdf                                    — Mobi per-unit + bundles
- /media/zuupjirp/3_cenik_..._gostovanje_v_tujini.pdf                          — roaming

(`/media/...` paths are under `https://www.telekom.si`.)

## Example grounding lines (behind the flagged errors)

- Naj B/C throttle: *"po doseženem limitu 200 GB … zniža na 2/1 Mb/s"* (paketi-naj) — Maks said 64 kbps for Naj.
- Naj B EU: *"paket Naj B vključuje 41,71 GB … v državah EU-tarife"* — Maks said 13 GB.
- Mobi C throttle: *"po doseženem limitu 200 GB … 64/64 kbit/s"* (mobi) — Maks said 1 GB.
- Ena številka: *"Priključna taksa … brezplačno"* (cenik) — Maks said 10,95 €.
- Extra phone number: *"Dodatna telefonska številka … 1,27"* (povezane) — Maks said 2 €.
- SIM 2: *"Naročnina … 11,99"* (cenik) — Maks said 4,99 €.

## What was NOT independently verified

Numbers Maks volunteered that were outside the reference set — e.g. "99 % 5G
coverage", specific roaming-bundle prices, the Da Vinci vs Da Vinci Kids split,
and which SIM 2 variant applies — were marked *unverified but plausible* rather
than asserted right or wrong.
