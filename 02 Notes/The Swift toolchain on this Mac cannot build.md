---
type: note
tags:
  - note
  - seed
maturity: seed
---

# The Swift toolchain on this Mac cannot build

The Command Line Tools SDK is missing headers, so Swift source will not compile here. Finished, correct Swift code fails at build time for reasons that have nothing to do with the code.

## How to apply

Build native app bundles with `osacompile` instead. It wraps a launcher script in a real `.app` and needs no compiler. That is how [[Year 11 Study Deck]] ships.

Do not spend time debugging the Swift error. It is environmental.

## Connects to

- [[Year 11 Study Deck]]
- [[Systems and Tools]]
