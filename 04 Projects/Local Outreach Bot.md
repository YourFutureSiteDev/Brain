---
type: project
tags:
  - project
  - status/active
area: "[[Business]]"
started: 2026-08-12
status: active
---

# Local Outreach Bot

Researches local businesses, finds the ones whose website is missing, broken or years out of date, emails them a personalised mockup, and builds a call queue.

## Outcome

A queue of warm callbacks that fills itself while Byron is at school.

## Division of labour

**The bot emails. Byron calls.** Set deliberately, not a limitation.

## Next action

- [ ] Review a batch of drafted emails in `out/outbox/` before deciding on sending

## How it runs

Always on. A LaunchAgent starts `run.sh --loop --interval 1800` at login with `KeepAlive`, so one long-lived process cycles every thirty minutes and launchd restarts it if it dies or the Mac wakes.

Stopping and starting is **a button at the bottom of the app's menu**, not a terminal command. State lives in `data/bot_state.json` and survives reboots, so stopped stays stopped. Stopping pauses the loop rather than killing the process. See [[An always-on job needs a stop button in the app, not the terminal]].

## Where it lives

`~/Library/Application Support/YourFutureSite/localbot`, symlinked from `~/Desktop/Claude/YourFutureSite/outreach/localbot`.

It lives there rather than the Desktop because of [[LaunchAgents cannot run from the Desktop]].

## Pipeline app

`./run-app.sh` serves `localhost:8787` and the Mac's LAN IP, so it opens on a phone mid call. Panels: today's calls, dashboard, sales, campaigns, all leads. No login by design, so it must never be exposed beyond the local network.

## Wired or not

| Thing | State |
|---|---|
| SMTP | Working. App password in Keychain, service `yfs-gmail` |
| Sending | **Off.** `send.enabled: false`. Emails written to `out/outbox/*.eml` |
| Demos | Live, linked per niche from every email |
| Places API | Not used and not needed |
| Stripe | Not configured |

## The discovery that mattered

Google Maps through a browser replaces the Places API entirely. No key, no billing. Details and the second finding in [[Page one Maps results are the wrong prospects]].

## Blocked on

Nothing technical. Sending is a decision, not a bug.

## Links

[[Your Future Site]] · [[Niche Demo Sites]] · [[AI and Automation MOC]]
