---
type: note
tags:
  - note
  - grown
up: "[[Hybrid RP Storefront]]"
maturity: grown
---

# Tebex Custom HTML strips JavaScript

Tebex's Custom HTML block silently removes `<script>` tags. CSS applies normally. There is no error and no warning, so the first symptom is a feature that simply does nothing.

## Why it matters

It rules out every interaction that needs code. Anything dynamic has to be built from CSS alone: `:hover`, `:focus-within`, `:target`, checkbox and radio state, and transitions.

The block also renders inside a **content-height sandboxed iframe**. That kills `position: fixed`, viewport units behave unexpectedly, and scroll-driven reveals never fire because the frame does not scroll.

## How to apply

Design for it from the start rather than discovering it late. A hover-expand nav rail works. A scroll-triggered animation does not.

## Connects to

- [[Hybrid RP Storefront]]
- [[Web Development MOC]]
