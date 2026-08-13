---
type: project
tags:
  - project
  - status/active
area: "[[Business]]"
started: 2026-08-12
status: active
---

# Niche Demo Sites

Four demo sites, one per outreach niche, each modelled on a real site chosen for its layout and motion. The businesses are fictional on purpose, so nothing impersonates the reference companies.

## Outcome

Every cold email carries a link to a site that looks like it was built for that trade.

## The four

| Folder | Business | Modelled on | Shape |
|---|---|---|---|
| `trade/` | Kingsford Build Co. | ADCO | 5 pages |
| `food/` | Aoi Sydney | Nobu Sydney | Single scroll |
| `beauty/` | Ironwood Barber Co. | Marked Barber | Single scroll |
| `pro/` | Northline Advisory | Keeping Company | 5 pages |

`index.html` at the root is a gallery linking all four.

## Design DNA

Kept in case they need extending.

- **Trade**: condensed uppercase display, brand blue `#0047BB`, angular shapes over a video hero, sections that swap background colour on scroll
- **Food**: Poppins bold uppercase, charcoal `#333` with bronze `#886E42` and stone `#DCD7CC`, the `TITLE : SUBTITLE` colon heading pattern
- **Beauty**: IBM Plex Mono throughout, letter-spacing from 3.6px to 10px, off-white `#FFFEFA`, near-black `#222`, coral `#FA5553`
- **Pro**: Open Sans Light at large sizes, cyan `#33C9FF` with orange `#F6653C`, a multi-step quote calculator as the signature interaction

## Contrast traps

Both caught during the build and worth remembering. See [[Contrast fails hide inside brand colours]].

## Gotcha

The bot's niche key is `trades`. The demo folder is `trade`. They do not match and that is intentional in the mapping.

## Files

`~/Desktop/Claude/niche-demos/`, served on port 8747 via the `niche-demos` launch entry.

## Links

[[Your Future Site]] · [[Local Outreach Bot]] · [[Web Development MOC]]
