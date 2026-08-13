---
type: note
tags:
  - note
  - grown
maturity: grown
---

# LaunchAgents cannot run from the Desktop

macOS privacy protection blocks a LaunchAgent from executing anything stored in the Desktop folder. It fails at login with `Operation not permitted`, before a single line runs.

## Why it matters

The failure looks like a broken script, so the debugging goes in entirely the wrong direction.

## How to apply

Anything that must start at login lives in `~/Library/Application Support/`, symlinked back to the working folder if convenient. That is exactly why [[Local Outreach Bot]] lives where it does.

Related trap from the same family: launchd uses a minimal PATH, so `command -v python3` finds the CommandLineTools build rather than the framework one. Probe explicit paths instead.

## Connects to

- [[Desktop files carry provenance that blocks writes]]
- [[Systems and Tools]]
