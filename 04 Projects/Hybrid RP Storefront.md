---
type: project
tags:
  - project
  - status/blocked
area: "[[Business]]"
started: 2026-08-05
status: blocked
---

# Hybrid RP Storefront

A brand-new FiveM roleplay server, Season One, whitelisted. The site is a Tebex storefront.

## Outcome

A store page that sells packages, on a site that looks nothing like a default Tebex theme.

## Blocked on

**Packages.** The storefront reported no packages found for the store category, because the project had none in it. Nothing else can be finished until they exist.

- [ ] Add packages in Tebex

## Copy rule

All copy reads as a **new** server. No invented history, no backstory, nothing "since 2021". This was rejected outright once already.

## Decisions made, not to be re-litigated

- Cart and package restyling happens through the **Theme panel only**, never CSS targeting Tebex internal classes
- Palette is `#7C3AED`, `#A78BFA`, `#0A0A16`
- **No fake store.** Real Tebex package blocks handle purchases
- Subpages: Connect and Store. A suggestion box comes last
- Navigation is a hover-expand side rail, 56px icons expanding to 212px with labels, placed in the global Header so it appears everywhere

## Platform limits

Tebex's Custom HTML strips JavaScript and renders inside a sandboxed iframe. Both shape everything buildable here. See [[Tebex Custom HTML strips JavaScript]].

## Assets

The logo source is only 102 by 98 with an opaque black background and no alpha, so it is framed as a bordered emblem rather than floated. A transparent PNG at around 512px would let that framing be dropped.

## Files

`~/Desktop/Claude/hybrid-rp/`. `tebex-block.html` is the master, the page files are generated from it. The original full-JavaScript version still exists and is the better artefact if the site is ever hosted outside Tebex.

## Publishing

Saving a draft is fine. **Publish is Byron's call, never automatic.**

## Links

[[Business MOC]] · [[Web Development MOC]] · [[Money]]
