---
type: note
tags:
  - note
  - grown
maturity: grown
---

# Always test IPv4 and IPv6 separately

When a connection is slow, run `curl -4` and `curl -6` against the same host and compare. One of them is usually fine.

## Why it matters

A single speed test averages the two and hides which stack is broken. That average produced a confident and completely wrong diagnosis once already.

Split the test and the answer is immediate: if `-4` is fast and `-6` hangs, the problem is IPv6 routing, not bandwidth, not the ISP, not the machine.

## Connects to

- [[Systems and Tools]]
