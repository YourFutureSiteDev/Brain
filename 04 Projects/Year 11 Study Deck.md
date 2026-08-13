---
type: project
tags:
  - project
  - status/active
area: "[[School]]"
started: 2026-08-11
status: active
---

# Year 11 Study Deck

A study app seeded with Preliminary flashcards and summaries for all six subjects. Built to accept generated content rather than ship a fixed deck.

## Outcome

Every subject has current cards, and adding more takes under a minute.

## Next action

- [ ] Generate cards for whatever topic is currently being taught

## How to add content

Ask for material as JSON in the shape shown in the app's **Add content** tab, then paste it in. Subject ids: `hms`, `maths`, `eng`, `dt`, `eco`, `bus`.

## The step everyone forgets

Source of truth is `~/Desktop/Claude/study-app.html`, a single self-contained file. `~/Desktop/Claude/studydeck-src/build-app.sh` copies it into `~/Desktop/Year 11 Study Deck.app`.

**Re-run that script after every edit to the HTML**, or the app keeps serving the old copy.

## Serving and sign in

The app is served from `http://127.0.0.1:8788` by a Python server the bundle's launcher starts, because Google will not issue OAuth tokens to a `file://` page. Sign in uses Google Identity Services with the `drive.readonly` scope. If the port ever changes, the authorised JavaScript origins in Google Cloud Console must change with it or sign in fails on a redirect URI mismatch.

## Not yet possible

A native WKWebView version is written and finished but cannot be compiled. See [[The Swift toolchain on this Mac cannot build]]. The HTML already carries the bridge it needs and falls back to localStorage in a browser.

## Links

[[School]] · [[School MOC]]
