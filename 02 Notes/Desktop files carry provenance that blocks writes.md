---
type: note
tags:
  - note
  - grown
maturity: grown
---

# Desktop files carry provenance that blocks writes

Files already sitting on the Desktop carry a `com.apple.provenance` attribute. An automated process can create **new** files there, but `cp`, `mv`, `rm` and writes over an existing file all fail. Disabling sandboxing does not help, and driving Finder through AppleScript is refused too.

## Why it matters

It splits work into "I can do this" and "you have to do this", and knowing which is which upfront saves a long argument with the terminal.

## How to apply

New files, fine. Modifying or deleting something that was already there, Byron has to do it himself.

## Connects to

- [[LaunchAgents cannot run from the Desktop]]
- [[Systems and Tools]]
