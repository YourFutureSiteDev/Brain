---
type: note
tags:
  - note
  - grown
maturity: grown
---

# Contrast fails hide inside brand colours

A brand colour that looks strong is often unreadable under white text. The failure is invisible to the eye and obvious to a contrast checker.

## Why it matters

Nobody checks the accent colour, because the accent colour is the one that was chosen on purpose. That is exactly why it fails.

## Evidence

Both caught while building [[Niche Demo Sites]]:

- White on orange `#F6653C` measures 3.05:1, below the 4.5:1 floor. Buttons use `#C2410C` instead.
- Coral `#FA5553` on off-white measures 3.2:1. So coral fills are paired with near-black text rather than white.

The fix is never to drop the brand colour. It is to darken it for text-bearing surfaces and keep the original for large decorative areas.

## Connects to

- [[Design References]]
- [[Niche Demo Sites]]
