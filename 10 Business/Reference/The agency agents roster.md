---
title: The agency agents roster
source: byron
tags: [business, roles, agents, reference]
---

# The agency agents roster

255 specialist agents live in `~/.claude/agents` on the droplet, from
[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents).
Installed 17 August 2026. They are not code agents: they are the fractional
hires nobody here has got round to, sitting in a folder.

Each desk owns the divisions that answer its own question. Nothing is shared
between two desks, because an agent everybody owns is an agent nobody uses.

| Desk | Its question | Its divisions |
|---|---|---|
| [[CFO]] | Are we actually making money, and where does it leak? | finance (5) |
| [[CRO]] | Where does the pipeline stall? | sales (9), product (5) |
| [[CMO]] | Which areas and niches deserve the bot's time? | marketing (36), paid-media (7), design (10) |
| [[COO]] | Is the machine running, and where does it jam? | engineering (58), project-management (7), testing (9), support (4) |
| [[CCO]] | Can this get the Gmail account killed, or us sued? | security (12) |
| [[CDO]] | Is the data good enough to act on? | academic (6), gis (13) |
| [[CEO]] | Is this working, and what needs deciding? | strategy, the strategic half of specialized |

## Two things worth knowing

**The names had to be rewritten.** The repo ships every agent with a display
name in its frontmatter, `name: AI Citation Strategist`. Claude Code will not
load a name that is not lowercase and hyphens, and it fails quietly. Every
`name:` was rewritten to its own filename, so `marketing-ai-citation-strategist`
is what you call. Re-running the repo's own installer would put the broken names
back and none of these would load.

**They are advisors, not operators.** An agent here reads, reasons and hands
back an answer. It does not send an email, ring anybody or move money. Sending
stays behind the switches it has always been behind.

## Given to nobody, on purpose

| Division | Count | Why it sits idle |
|---|---|---|
| game-development | 6 | economy, level and narrative designers. No game. |
| spatial-computing | 6 | visionOS, XR and Metal. No headset, no spatial product. |
| healthcare | 3 | clinical evidence and health systems. Not our field, and the compliance surface alone would be a business. |
| the industry tail in specialized | ~25 | loan officers, medical billing, real estate, study abroad, retail returns, hospitality. Each is somebody's whole company and none of them is ours. |

They stay installed because deleting them saves nothing and the day a client
turns up in one of those trades the agent is already there. Nobody is expected
to have read them.
