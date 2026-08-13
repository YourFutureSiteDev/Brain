---
type: note
tags:
  - note
  - grown
maturity: grown
---

# An always-on job needs a stop button in the app, not the terminal

A background process that only stops via a terminal command is a process that never gets stopped, because the moment you want it stopped is the moment you are not at a terminal.

## Why it matters

Stopping has to be reachable from wherever the work is happening. In [[Local Outreach Bot]] that is a button at the bottom of the app menu, usable from a phone.

Two things make it actually work:

- **State persists.** It lives in a state file, so stopped stays stopped across a reboot.
- **Stop pauses, it does not kill.** The process stays alive and idle, so starting again is instant and launchd is not fighting you.

## Connects to

- [[Automate the boring half, keep the human half]]
- [[Local Outreach Bot]]
