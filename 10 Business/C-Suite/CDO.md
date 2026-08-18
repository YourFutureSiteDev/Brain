---
title: "CDO"
source: yfs-console
kind: role
tags: [business, c-suite]
updated: 2026-08-18T18:54:06
role: "cdo"
---


# CDO

*Is the data good enough to act on?*

Where it stands right now.

> Nothing recorded yet. This role has not had enough to go on.

| | | |
|---|---|---|
| Leads | **22276** | known |
| With email | **955** | 4% |
| With phone | **5600** | 25% |
| With rating | **0** | 0% |
| Unconfirmed | **454** | never mailed |

## Needs a decision

- **Only 4% of leads have an email.** Expected. Google never returns emails and a business with no site has no contact page. Those leads are the call list, not a failure.
- **454 leads came back UNKNOWN.** Their site could not be confirmed either way, so they are never emailed. That is the rule working, not a gap to fill.

## Carrying for Byron

- 2026-08-18 Pull a full sub-category breakdown of the trades niche (all ~364 in queue, not just the top 50): count by trade type (auto/mechanical, plumbing, building/carpentry, electrical, heating and cooling, etc) so Byron can see the real mix, not a sample. *(working)*
- 2026-08-18 [morning meeting, from CMO] Confirm whether the 2.1% reply rate is tracked per area so CMO can judge which of the 402 live areas are working once they clear 60 sends. *(working)*
- 2026-08-18 [morning meeting, from CRO] Weight no_site bucket leads above clicked and no_email leads in buy_score so the queue puts no-website businesses first as instructed. *(working)*
- 2026-08-17 From the vault, The CDO now has its own specialists: You have specialists now. 16 of them, in academic (6), gis (13), sitting in `~/.claude/agents` on this box. They came from [[The agency agents roster]], which is where the full list and the other desks' shares are. Yours, and what each is for: - `academic-statistician` - whether a number means anything at this sample size - `academic-psychologist` - why people answer the way they do - `academic-geographer` - place, which is half of what we sort on - `academic-anthropologist` - the people behind the rows - `academic-historian` - what the record actually says - `academic-narratologist` - the story a set of numbers is being made to tell - `gis-spatial-data-scientist` - the towns and suburbs, treated as data - `gis-analyst` - the everyday geographic question - `gis-spatial-data-engineer` - the OpenStreetMap pipeline behind the leads - `gis-geoprocessing-specialist` - turning a region into a lead list - `engineering-data-engineer` - the pipeline itself - `engineering-database-optimizer` - SQLite, before it becomes the bottleneck - `engineering-ai-data-remediation-engineer` - fixing what the bot got wrong at scale - `data-consolidation-agent` - two businesses, two databases, one picture *(working)*
- 2026-08-13 make sure the sites that cant be confirmed are still being sent emails or added to the call list *(working)*
- 2026-08-13 Byron wants to know the rate leads are coming in. Start tracking daily new-lead counts (total and by source/niche) so this can be answered with a real number instead of reading timestamps off a snapshot. *(working)*

## Learned

- 2026-08-13 The 3% email rate is the market, not a backlog. 3115 of 3674 leads have no website at all, so there is no contact page to read. Every one of the 92 leads that has a site and is worth emailing was searched on 13 Aug 2026 and none published an address: the pages that load carry a contact form only, some disallow robots and are left alone, some have an invalid certificate. Real coverage is 94 of the 559 leads that have a site.
- 2026-08-13 All 58 UNKNOWN leads were re-judged under the current rules on 13 Aug 2026 and not one resolved. 26 answer HTTP 403 because the site's firewall blocks the checker, 20 build their content in the browser so there is no HTML to judge, the rest are 500s, a timeout and a 526. Re-checking cannot clear these: the block is at their end. 37 of the 58 have a phone, and the call list excludes UNKNOWN.
- 2026-08-12 recheck_days: default -> 45. you asked: Recheck healthy sites every 45 days

## Decided

- 2026-08-18 asked: Pull a full sub-category breakdown of the trades niche (all ~364 in queue, not just the to -> No lever of mine moves this one. What I control is: change how often a healthy site is rechecked; requeue stale leads an
- 2026-08-18 asked: [from CMO, on shift] I can't get a clean daily intake rate from a 50-row sample of first_s -> nothing to clean: no stale verdicts and no unusable rows
- 2026-08-18 asked: [morning meeting, from CMO] Confirm whether the 2.1% reply rate is tracked per area so CMO -> No lever of mine moves this one. What I control is: change how often a healthy site is rechecked; requeue stale leads an
- 2026-08-18 asked: [morning meeting, from CRO] Weight no_site bucket leads above clicked and no_email leads i -> No lever of mine moves this one. What I control is: change how often a healthy site is rechecked; requeue stale leads an
- 2026-08-17 asked: From the vault, The CDO now has its own specialists: You have specialists now. 16 of them, -> No lever of mine moves this one. What I control is: change how often a healthy site is rechecked; requeue stale leads an
- 2026-08-13 asked: Pull the 52 UNKNOWN status leads. For any that have a phone number, add them to the call l -> I am holding this rather than doing it. I cannot send an email, ring anyone, or spend money. Those stay with the mailer
- 2026-08-13 asked: make sure the sites that cant be confirmed are still being sent emails or added to the cal -> No lever of mine moves this one. What I control is: change how often a healthy site is rechecked; requeue stale leads an
- 2026-08-13 asked: Byron wants to know the rate leads are coming in. Start tracking daily new-lead counts (to -> No lever of mine moves this one. What I control is: change how often a healthy site is rechecked; requeue stale leads an

## Noticed

- 2026-08-18 Read outside on Does the free ABN Lookup / Australian Business Register web service return phone, email or website fields we could use to fill the contact gaps in our leads?: No. The ABR web service (free, GUID auth, updated hourly from the ABR) returns entity name, ABN status, ACN, entity type, GST registration, business locations at state and postcode level, business names and effective dates. It does not carry phone, email or website fields at all. Separately, a side search on how many Australian small businesses lack a website returned wildly inconsistent figures across sources, from 22% to 65% depending on year and methodology, so that number is not solid enough to use for anything. (source: abr.business.gov.au/Documentation/WebServiceResponse and abr.business.gov.au/Tools/WebServices, checked 2026-08-18)
- 2026-08-16 Standing contract, set 16 Aug 2026: from the Analyst, the data half. Delivers: a straight answer on whether the lead data is worth acting on. Steps: track, analyse, learn, optimise. Ratio: 17129 leads, 4% with an email, 25% with a phone, 358 held out as UNKNOWN. Now: email coverage 4%.
- 2026-08-15 the weekly pass left recheck_days where it is: 45 was only set on 2026-08-12, it is locked from changes for 14 days, and there is no recheck-outcome data yet to say whether it changed the right number of verdicts.

## Recently did

- 2026-08-18 worked a shift: Re-checked whether UNKNOWN status leads with phone numbers reach the call queue, since Byron flagged this again. Second shift in a row the evidence points the same way: this call list sample (50 of 365 queued) has bucket values of only clicked or no_site, zero unknown, and the single UNKNOWN lead vi
- 2026-08-18 read outside the building: Does the free ABN Lookup / Australian Business Register web service return phone, email or website fields we could use to fill the contact gaps in our leads?: No. The ABR web service (free, GUID auth, updated hourly from the ABR) returns entity name, ABN status, ACN, entity type, GST registration, b
- 2026-08-18 answered you: No lever of mine moves this one. What I control is: change how often a healthy site is rechecked; requeue stale leads and delete unusable ones. Where I stand: L
- 2026-08-18 answered you: nothing to clean: no stale verdicts and no unusable rows
- 2026-08-18 worked a shift: Checked Byron's standing instruction that unconfirmed (UNKNOWN) leads still get emailed or added to the call list. The 50-row call list sample I can see (of 364 queued) has zero UNKNOWN-status entries, every row is NO_SITE, so I cannot confirm from here that UNKNOWN leads are actually reaching the c
- 2026-08-18 answered you: No lever of mine moves this one. What I control is: change how often a healthy site is rechecked; requeue stale leads and delete unusable ones. Where I stand: L
- 2026-08-18 answered you: No lever of mine moves this one. What I control is: change how often a healthy site is rechecked; requeue stale leads and delete unusable ones. Where I stand: L
- 2026-08-17 answered you: No lever of mine moves this one. What I control is: change how often a healthy site is rechecked; requeue stale leads and delete unusable ones. Where I stand: L
- 2026-08-17 picked up a note from the vault: The CDO now has its own specialists
- 2026-08-13 answered you: I am holding this rather than doing it. I cannot send an email, ring anyone, or spend money. Those stay with the mailer and its caps, and with you. What I can d
- 2026-08-13 answered you: No lever of mine moves this one. What I control is: change how often a healthy site is rechecked; requeue stale leads and delete unusable ones. Where I stand: L
- 2026-08-13 answered you: No lever of mine moves this one. What I control is: change how often a healthy site is rechecked; requeue stale leads and delete unusable ones. Where I stand: L

---

Back to [[C-Suite]]. Written by the Your Future Site console on the VPS, 2026-08-18T18:54:06. Edit it here and the next cycle overwrites you, so put your own thinking in a note of your own and link it.
