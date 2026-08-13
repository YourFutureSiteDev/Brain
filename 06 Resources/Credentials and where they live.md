---
type: note
tags:
  - note
---

# Credentials and where they live

**No secret is ever written in this vault.** This note records only where things are kept, so nothing has to be hunted for.

## Keychain

| What | Service | Account |
|---|---|---|
| Gmail app password for outreach | `yfs-gmail` | `yourfuturesitedev@gmail.com` |

Read one back with `security find-generic-password -s <service> -w`.

## In browser storage

| What | Where |
|---|---|
| Google OAuth client id for the study app | `localStorage`, key `studydeck.gclient.v1` |

Access tokens are memory only by design and are never written to disk.

## Not configured

- Stripe, only needed once a client says yes
- Google Places API, deliberately never set up. Not needed, see [[Page one Maps results are the wrong prospects]]

## Rule

If a credential ever needs to move, it moves into Keychain. Not into a note, not into a config file, not into chat.

## Links

[[Systems and Tools]]
