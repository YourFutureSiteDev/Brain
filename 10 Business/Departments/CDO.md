---
source: yfs-console
kind: department
role: cdo
tags: [memory, departments]
---

# CDO

What this desk believes about its department, as of 2026-08-22. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: cdo` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** leads with a usable verdict %: 97.96 on 2026-08-18 to 97.66 on 2026-08-22 (down, 5 days)

## Unconfirmed leads are rising, and today's sweep isn't why

*proven, revised 8 times, learned 2026-08-19 from shift.*

Fifth reading, same conclusion, settling this. New-lead unconfirmed rate this shift: 7 new unconfirmed out of 199 new leads = 3.52%, joining the series 3.1%, 2.75%, 1.16%, 2.07%. The band is wider than I last said (1-3.5%, not 1-3%) but there's still no cluster and no direction. Cumulative usable share ticked back down to 97.65% this shift from 97.66% last shift, so it's bouncing both ways, not settling either up or down. Stop resampling this every shift. Only worth another look if a single shift's new-lead rate clears 5% or the cumulative usable share moves outside 97.5-98%.

> Evidence: This shift: leads 27414, unconfirmed 645. Last shift: leads 27215, unconfirmed 638. Delta 199 new leads, 7 new unconfirmed = 3.52%. Usable this shift (27414-645)/27414=97.65%, last shift (27215-638)/27215=97.66%.

## Public AU business registers do not carry contact data

*proven, revised 4 times, learned 2026-08-18 from research.*

The 1,000/month free-call figure for Contact Data is confirmed current, not stale, so the earlier caution stands as originally stated with no change needed to the number itself. The open items are unchanged: a card has to go on file with Google with no automatic hard cap, so this cannot be wired up as a silent build. If Byron wants it, he adds the card himself, and CFO or CCO confirms a manual spending cap is set at signup.

> Evidence: mapsleads.co/blog/google-places-api-free-tier-limits-2026, checked 2026-08-22: Contact Data (phone, website, hours) prices at the Enterprise SKU tier, 1,000 free calls a month, versus 10,000 for Essentials and 5,000 for Pro. [read outside, mapsleads.co/blog/google-places-api-free-tier-limits-2026, checked 2026-08-22]

## UNKNOWN leads: no confirmed route to the call list

*proven, revised 3 times, learned 2026-08-18 from shift.*

Correcting this. UNKNOWN/unconfirmed leads do reach the call list, they are just sorted last by buy_score so they never appear in a 50-row top sample, which is why three straight shifts of sampling looked like exclusion. The aggregate queue_buckets field (separate from the per-row bucket on the 50 shown) proves it. Hawkesbury & Nepean Plumbing specifically is stuck for a different reason: it has no phone number at all, so it can never enter the call list regardless of status, and it's UNKNOWN so it's never emailed either. That is a missing-contact-data problem on one lead, not a systemic routi

> Evidence: call_list queue_total 1740, queue_buckets: clicked 1, no_site 1273, no_email 310, quiet 2, unconfirmed 154 (sums to 1740). queue_bucket_first shows unconfirmed starting at position 1587 of 1740, meaning it occupies the last 154 slots by design, not zero slots. Hawkesbury & Nepean Plumbing lead record: phone blank, email blank, status UNKNOWN.

## Trades niche sample is automotive-heavy, not general trades

*working, revised 1 time, learned 2026-08-19 from shift.*

Stop resampling this every shift, it's held at roughly the same ~48-50% automotive share across three separate 50-row pulls now (22/50 trades with 11 automotive, then 29/50 with 14 automotive, now 29/50 with 14 automotive again). Treat it as settled: if CMO wants trades split into real subcategories for targeting, that's a CMO build decision now, not something more sampling here will sharpen further.

> Evidence: This shift's call_list: 29 of 50 rows niche trades, 14 of those 29 automotive by name (Damien Seton Mechanical, Bill's HI-TECH Smash Repairs, Ray's Euro Tech, Springall's Mechanical, Stoddy's Mobile Mechanical, Bushy's Georgetown Tyre & Mechanical, GP Mechanical Repairs & Maintenance, Luke's Mobile Tyre Service, Abaco Car Care, All Aussie Automotive, Anthony Rickard Mechanical Repairs, BH Tyres, B

## No timer means the three hour rule is currently unmeasured

*tried, revised 0 times, learned 2026-08-18 from brief.*

Until actual minutes are logged per job, treat every effective-hourly-rate figure in the brief as unverified. Push for the minutes field to exist and start recording from job one.

> Evidence: Section 8 point 2 and decision 2: the first ten recorded jobs settle whether the $99 is a real product, and nothing in the document can be verified without this.

## One system of record, no second place for truth to live

*tried, revised 0 times, learned 2026-08-18 from brief.*

Keep lead and job data in the pipeline app only. If a spreadsheet, note, or second tool starts holding numbers that matter, treat that as a data integrity problem to fix, not a convenience.

> Evidence: Section 8: adding Notion, Trello or similar is explicitly wrong here because it creates a second place where truth lives, which a 12 hour a week solo operator cannot maintain.

## All the lead and client data lives on one school laptop

*tried, revised 0 times, learned 2026-08-18 from brief.*

Treat this as the standing top risk to the data itself. Any report on backups, git pushes, or database dumps for the pipeline app is worth surfacing immediately, since a lost machine means a lost database.

> Evidence: Section 8: the business runs on one Jamf managed MacBook owned by a school, which can be locked or wiped, losing the lead database and the bot with it.

## COO's 5003 no-email tile and the 1908 call queue count different populations

*tried, revised 0 times, learned 2026-08-21 from shift.*

The 5003 counts every lead in the whole 27159 database that has a phone and no email, regardless of whether it needs outreach. The call_list queue_total of 1908 is already filtered to leads with an open reason to contact (no_site 1435, no_email 313, quiet 3, unconfirmed 155, clicked 1, replied 1, sums exact). Leads with phone and no email but status OK (site is fine) sit in the 5003 but never enter the queue because they don't need a call. This is two different denominators, not a broken query.

> Evidence: Leads sample: Penrith City Plumbing Services (status OK, phone 0422 720 132, email blank) and RPM Dubbo (status OK, phone (02) 6885 5123, email blank) both count toward the 5003 but are absent from the call_list, which only holds leads needing action. call_list queue_buckets for this shift: no_site 1435 + no_email 313 + quiet 3 + unconfirmed 155 + clicked 1 + replied 1 = 1908, matching queue_total

## ready_by_niche and ready_live_by_niche already show trades as majority, not beauty only

*tried, revised 0 times, learned 2026-08-21 from shift.*

CMO's open trace request assumes trades is missing or suppressed from these two views. It is not, in this shift's data. Trades leads both. Tell CMO to recheck whichever view they were actually reading when they logged 'beauty only four shifts running', since the underlying figures already carry trades on top.

> Evidence: ready_by_niche: trades 279, beauty 268, pro 25, food 72, sums to ready 644 exactly, trades ahead by 11. ready_live_by_niche: trades 217, beauty 68, pro 12, food 16, sums to ready_live 313 exactly, trades is 69.3% of that total against beauty's 21.7%.

## What it used to believe

- **UNKNOWN status leads never route to call list or get emailed stuck at** retired 2026-08-19: Duplicate of itself in the standing list, two identical entries. Merging into one proven entry via the learn field above, not two near-identical working notes.
- **Care Pro's margin depends on clients not using their hours** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.
- **The active care client count is a live trigger, not a stat** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.
- **Every capacity number in the plan is a guess, not a fact** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.

Back to [[Memory]].
