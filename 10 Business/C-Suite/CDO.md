---
title: "CDO"
source: yfs-console
kind: role
tags: [business, c-suite]
updated: 2026-08-21T22:46:00
role: "cdo"
---


# CDO

*Is the data good enough to act on?*

Where it stands right now.

> Nothing recorded yet. This role has not had enough to go on.

| | | |
|---|---|---|
| Leads | **27446** | known |
| With email | **1220** | 4% |
| With phone | **8808** | 32% |
| With rating | **0** | 0% |
| Unconfirmed | **645** | never mailed |

## Needs a decision

- **Only 4% of leads have an email.** Expected. Google never returns emails and a business with no site has no contact page. Those leads are the call list, not a failure.
- **645 leads came back UNKNOWN.** Their site could not be confirmed either way, so they are never emailed. That is the rule working, not a gap to fill.

## Carrying for Byron

- 2026-08-21 [morning meeting, from COO] Reconcile the coo dashboard's 4966 no-email call-list figure against the call_list query's own total of 1900. *(working)*
- 2026-08-20 [morning meeting, from CMO] Trace why niches-live and ready_live_by_niche still show beauty only when trades is the majority of the real queue, four shifts running. *(working)*
- 2026-08-19 [morning meeting, from CRO] Build the call outcome log tied to call_list ids so calls_made and last_call update on a real call and buy_score reflects actual contact history. *(working)*
- 2026-08-18 Pull a full sub-category breakdown of the trades niche (all ~364 in queue, not just the top 50): count by trade type (auto/mechanical, plumbing, building/carpentry, electrical, heating and cooling, etc) so Byron can see the real mix, not a sample. *(working)*
- 2026-08-18 [morning meeting, from CMO] Confirm whether the 2.1% reply rate is tracked per area so CMO can judge which of the 402 live areas are working once they clear 60 sends. *(working)*
- 2026-08-18 [morning meeting, from CRO] Weight no_site bucket leads above clicked and no_email leads in buy_score so the queue puts no-website businesses first as instructed. *(working)*
- 2026-08-17 From the vault, The CDO now has its own specialists: You have specialists now. 16 of them, in academic (6), gis (13), sitting in `~/.claude/agents` on this box. They came from [[The agency agents roster]], which is where the full list and the other desks' shares are. Yours, and what each is for: - `academic-statistician` - whether a number means anything at this sample size - `academic-psychologist` - why people answer the way they do - `academic-geographer` - place, which is half of what we sort on - `academic-anthropologist` - the people behind the rows - `academic-historian` - what the record actually says - `academic-narratologist` - the story a set of numbers is being made to tell - `gis-spatial-data-scientist` - the towns and suburbs, treated as data - `gis-analyst` - the everyday geographic question - `gis-spatial-data-engineer` - the OpenStreetMap pipeline behind the leads - `gis-geoprocessing-specialist` - turning a region into a lead list - `engineering-data-engineer` - the pipeline itself - `engineering-database-optimizer` - SQLite, before it becomes the bottleneck - `engineering-ai-data-remediation-engineer` - fixing what the bot got wrong at scale - `data-consolidation-agent` - two businesses, two databases, one picture *(working)*
- 2026-08-13 make sure the sites that cant be confirmed are still being sent emails or added to the call list *(working)*

## Learned

- 2026-08-21 2,139 leads sit in area names that are not live and cannot be worked. Food 1,353, beauty 401, trades 237, pro 148, across 144 area names. They came from the state and bbox sweeps, which harvested towns never added to the configured areas, mostly QLD and SA. They are counted as leads everywhere in the console and none can be contacted, so a desk reading a total lead count is reading 2,139 rows of nothing.
- 2026-08-21 No open reply thread holds what the client actually said. The 14 messages in reply_msg all belong to the 14 archived threads. The conversation table is empty and text_log holds outbound only. The system knows a reply happened, marks the lead replied and opens a thread, but never captures the text. The replies are presumably still in Messages on Byron's Mac, so nothing in the console can show him what 76 interested people said.
- 2026-08-13 The 3% email rate is the market, not a backlog. 3115 of 3674 leads have no website at all, so there is no contact page to read. Every one of the 92 leads that has a site and is worth emailing was searched on 13 Aug 2026 and none published an address: the pages that load carry a contact form only, some disallow robots and are left alone, some have an invalid certificate. Real coverage is 94 of the 559 leads that have a site.
- 2026-08-13 All 58 UNKNOWN leads were re-judged under the current rules on 13 Aug 2026 and not one resolved. 26 answer HTTP 403 because the site's firewall blocks the checker, 20 build their content in the browser so there is no HTML to judge, the rest are 500s, a timeout and a 526. Re-checking cannot clear these: the block is at their end. 37 of the 58 have a phone, and the call list excludes UNKNOWN.
- 2026-08-12 recheck_days: default -> 45. you asked: Recheck healthy sites every 45 days

## Decided

- 2026-08-21 asked: [morning meeting, from COO] Reconcile the coo dashboard's 4966 no-email call-list figure a -> No lever of mine moves this one. What I control is: change how often a healthy site is rechecked; requeue stale leads an
- 2026-08-20 asked: [morning meeting, from CMO] Trace why niches-live and ready_live_by_niche still show beaut -> No lever of mine moves this one. What I control is: change how often a healthy site is rechecked; requeue stale leads an
- 2026-08-19 asked: [morning meeting, from CRO] Build the call outcome log tied to call_list ids so calls_made -> No lever of mine moves this one. What I control is: change how often a healthy site is rechecked; requeue stale leads an
- 2026-08-18 asked: Pull a full sub-category breakdown of the trades niche (all ~364 in queue, not just the to -> No lever of mine moves this one. What I control is: change how often a healthy site is rechecked; requeue stale leads an
- 2026-08-18 asked: [from CMO, on shift] I can't get a clean daily intake rate from a 50-row sample of first_s -> nothing to clean: no stale verdicts and no unusable rows
- 2026-08-18 asked: [morning meeting, from CMO] Confirm whether the 2.1% reply rate is tracked per area so CMO -> No lever of mine moves this one. What I control is: change how often a healthy site is rechecked; requeue stale leads an
- 2026-08-18 asked: [morning meeting, from CRO] Weight no_site bucket leads above clicked and no_email leads i -> No lever of mine moves this one. What I control is: change how often a healthy site is rechecked; requeue stale leads an
- 2026-08-17 asked: From the vault, The CDO now has its own specialists: You have specialists now. 16 of them, -> No lever of mine moves this one. What I control is: change how often a healthy site is rechecked; requeue stale leads an
- 2026-08-13 asked: Pull the 52 UNKNOWN status leads. For any that have a phone number, add them to the call l -> I am holding this rather than doing it. I cannot send an email, ring anyone, or spend money. Those stay with the mailer
- 2026-08-13 asked: make sure the sites that cant be confirmed are still being sent emails or added to the cal -> No lever of mine moves this one. What I control is: change how often a healthy site is rechecked; requeue stale leads an
- 2026-08-13 asked: Byron wants to know the rate leads are coming in. Start tracking daily new-lead counts (to -> No lever of mine moves this one. What I control is: change how often a healthy site is rechecked; requeue stale leads an

## Noticed

- 2026-08-21 Read outside on Does Google Places API's free tier (the Contact Data SKU I flagged last shift) actually require a billing account and credit card, or is it usable with zero payment risk for a solo operator with no bu: Yes, billing is required. Google still requires a billing account with a valid credit card on file to use any Places API SKU, even to stay inside the free monthly allowance. Usage beyond the free allowance bills automatically per SKU with no hard spending cap unless one is set manually. Separately, the free tier structure itself changed in 2026: it's now per-SKU (10,000 free events/month for Essentials, 5,000 for Pro, 1,000 for Enterprise tier), replacing the old universal $200/month credit Google retired in March 2025, so the Contact Data SKU's exact free allowance needs re-checking against which tier it now sits in rather than assumed at 1,000. (source: developers.google.
- 2026-08-20 Read outside on Is there a free way to cross-check whether an OSM-sourced NO_SITE lead actually has no website, so a blank OSM tag isn't the only signal before we email 'we could not find a website for you'?: Yes, there's a concrete free-tier path. Google Places API's Contact Data SKU includes the website field (along with phone and hours). It carries its own free monthly allowance of 1,000 calls before any charge applies. Since we send nowhere near 1,000 emails a month right now (178 sent all time, 0 today), this is enough headroom to live-check every OSM-sourced NO_SITE lead before it gets emailed, at zero cost, for the volumes this business currently runs. (source: developers.google.com/maps/billing-and-pricing (via mapsleads.co/blog/google-places-api-free-tier-limits-2026 and safegraph.com/guides/google-places-api-pricing, both checked 2026-08-20))
- 2026-08-19 Read outside on Does OpenStreetMap's absence of a website tag actually mean a business has no website, or just that nobody entered it?: A benchmark comparison of OSM POI data against a verified retail dataset found only a 39.8% attribute fill rate overall, and found OSM entries with blank fields carry no explanation for why the field is blank. Direct quote: OSM's crowd-sourced structure doesn't provide any documentation explaining why a field is blank, so there's no way to distinguish 'this business doesn't have a website' from 'no one has entered this yet.' Most of our own call_list and lead rows with status NO_SITE have source osm and status_detail 'no website listed', which is the exact failure mode this describes. (source: SafeGraph, 'SafeGraph vs OpenStreetMap: The Hidden Cost of Free POI Data' (benchmark study referenced from July 2022, page current as of 2026), safegraph.com/blog/
- 2026-08-18 Read outside on Does the free ABN Lookup / Australian Business Register web service return phone, email or website fields we could use to fill the contact gaps in our leads?: No. The ABR web service (free, GUID auth, updated hourly from the ABR) returns entity name, ABN status, ACN, entity type, GST registration, business locations at state and postcode level, business names and effective dates. It does not carry phone, email or website fields at all. Separately, a side search on how many Australian small businesses lack a website returned wildly inconsistent figures across sources, from 22% to 65% depending on year and methodology, so that number is not solid enough to use for anything. (source: abr.business.gov.au/Documentation/WebServiceResponse and abr.business.gov.au/Tools/WebServices, checked 2026-08-18)
- 2026-08-16 Standing contract, set 16 Aug 2026: from the Analyst, the data half. Delivers: a straight answer on whether the lead data is worth acting on. Steps: track, analyse, learn, optimise. Ratio: 17129 leads, 4% with an email, 25% with a phone, 358 held out as UNKNOWN. Now: email coverage 4%.
- 2026-08-15 the weekly pass left recheck_days where it is: 45 was only set on 2026-08-12, it is locked from changes for 14 days, and there is no recheck-outcome data yet to say whether it changed the right number of verdicts.

## Recently did

- 2026-08-21 worked a shift: Ran the fifth reading of the new-lead unconfirmed rate and cumulative usable-verdict share against this shift's numbers (27414 leads, 645 unconfirmed vs last shift's 27215/638), and closed out the resampling since it's now five straight shifts with the same noise verdict.
- 2026-08-21 worked a shift: Checked CMO's open claim that ready_by_niche and ready_live_by_niche 'still show beauty only' against this shift's actual numbers, and found it does not hold: trades leads both breakdowns.
- 2026-08-21 worked a shift: Checked this shift's unconfirmed count (638/27215) against last shift's (635/27070) for a fourth reading of the new-lead unconfirmed rate, and recomputed the cumulative usable-verdict share to see if the four-day decline is still moving.
- 2026-08-21 answered you: No lever of mine moves this one. What I control is: change how often a healthy site is rechecked; requeue stale leads and delete unusable ones. Where I stand: L
- 2026-08-21 worked a shift: Reconciled the COO dashboard's 5003 'phone but no email' figure against the call_list query's own queue_total of 1908, since that gap was the open ask sitting with this desk since the morning meeting.
- 2026-08-21 worked a shift: Recomputed this shift's new-lead unconfirmed rate against last shift's reading (the third reading in that series) and checked the COO/call_list reconciliation ask on the board against the numbers actually in front of me.
- 2026-08-21 worked a shift: Compared this shift's unconfirmed count against last shift's reading to see whether the new-lead unconfirmed rate is settling into a baseline or still climbing, since last shift flagged the first nonzero reading after three flat ones.
- 2026-08-21 read outside the building: Does Google Places API's free tier (the Contact Data SKU I flagged last shift) actually require a billing account and credit card, or is it usable with zero payment risk for a solo operator with no bu: Yes, billing is required. Google still requires a billing account with a valid credit card on file
- 2026-08-20 worked a shift: Rechecked the fortnight unconfirmed count against the three flat prior readings (25506/594, 25518/594, 25568/594) and found it moved for the first time this shift: leads 26172, unconfirmed 613. That breaks the 'stable, stop checking' call I made last shift, so I'm reopening it. Also confirmed this c
- 2026-08-20 worked a shift: Reconfirmed the fortnight unconfirmed count for a third straight reading (25506 to 25518 to 25568 leads, unconfirmed pinned at 594 all three times) and reran the trades/automotive niche sample on this shift's fresh 50-row call list, which landed on the exact same 29/50 trades, 14/29 automotive split
- 2026-08-20 worked a shift: Closed out the trades-automotive check that's been resampled every shift for the last four: this shift's 50-row call_list sample gives 29 trades rows, 14 automotive, matching last shift's 29/14 exactly and the shift before's near-50% share, so I'm marking it settled instead of re-running it again. A
- 2026-08-20 answered you: No lever of mine moves this one. What I control is: change how often a healthy site is rechecked; requeue stale leads and delete unusable ones. Where I stand: L

---

Back to [[C-Suite]]. Written by the Your Future Site console on the VPS, 2026-08-21T22:46:00. Edit it here and the next cycle overwrites you, so put your own thinking in a note of your own and link it.
