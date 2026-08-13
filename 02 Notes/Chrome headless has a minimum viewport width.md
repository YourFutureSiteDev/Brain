---
type: note
tags:
  - note
  - grown
maturity: grown
---

# Chrome headless has a minimum viewport width

Headless Chrome will not render below roughly 500px wide. Ask for a narrower screenshot and you get something other than what you asked for.

## Why it matters

It makes true mobile screenshots impossible by that route, which matters whenever a mockup is meant to show a phone view.

The second failure is worse because it looks like success: **scroll-triggered reveals photograph as blank**. The element is in the DOM, the animation never fired, the screenshot is a clean empty box. Always include a failsafe that forces revealed state before capture.

## Connects to

- [[Niche Demo Sites]]
- [[Web Development MOC]]
