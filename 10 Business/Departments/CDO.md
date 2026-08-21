---
source: yfs-console
kind: department
role: cdo
tags: [memory, departments]
---

# CDO

What this desk believes about its department, as of 2026-08-21. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: cdo` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** leads with a usable verdict %: 97.96 on 2026-08-18 to 97.66 on 2026-08-21 (down, 4 days)

## Unconfirmed leads are rising, and today's sweep isn't why

*proven, revised 7 times, learned 2026-08-19 from shift.*

Fourth reading, still bouncing not settling: 3.1%, 2.75%, 1.16%, now 2.07% (3 new unconfirmed out of 145 new leads this shift). No cluster, no trend, treat as noise in a 1-3% band. But the second half of this note needs updating: the cumulative unconfirmed share has stopped creeping. Last shift it was 635/27070 = 97.654% usable, this shift it's 638/27215 = 97.656% usable, a tick up not down. The fortnight tracker line itself shows the same thing, 97.65% recorded last shift now reads 97.66%. That breaks the four-day decline from 97.96% (18 Aug). One more flat shift and the 'still creeping up' f

> Evidence: This shift: leads 27215, unconfirmed 638. Last shift: leads 27070, unconfirmed 635. Delta 145 new leads, 3 new unconfirmed = 2.07%. Usable-verdict: 97.654% last shift vs 97.656% this shift. Fortnight tracker in this shift's header: 97.96% (18 Aug) to 97.66% (21 Aug).

## UNKNOWN leads: no confirmed route to the call list

*proven, revised 3 times, learned 2026-08-18 from shift.*

Correcting this. UNKNOWN/unconfirmed leads do reach the call list, they are just sorted last by buy_score so they never appear in a 50-row top sample, which is why three straight shifts of sampling looked like exclusion. The aggregate queue_buckets field (separate from the per-row bucket on the 50 shown) proves it. Hawkesbury & Nepean Plumbing specifically is stuck for a different reason: it has no phone number at all, so it can never enter the call list regardless of status, and it's UNKNOWN so it's never emailed either. That is a missing-contact-data problem on one lead, not a systemic routi

> Evidence: call_list queue_total 1740, queue_buckets: clicked 1, no_site 1273, no_email 310, quiet 2, unconfirmed 154 (sums to 1740). queue_bucket_first shows unconfirmed starting at position 1587 of 1740, meaning it occupies the last 154 slots by design, not zero slots. Hawkesbury & Nepean Plumbing lead record: phone blank, email blank, status UNKNOWN.

## Public AU business registers do not carry contact data

*proven, revised 3 times, learned 2026-08-18 from research.*

Before this goes anywhere near a build ticket: a credit card has to go on file with Google and the free tier is not a hard cap, it auto-bills past it. This business's rule is nobody spends money without Byron doing it himself, so this can't be wired up as a silent automatic check. If Byron wants it, he needs to add the card himself and someone (CFO or CCO) needs to confirm a manual spending cap gets set at signup, not left open. Also re-verify which SKU tier Contact Data falls into now that Google moved to per-SKU free allowances in 2026, the 1,000/month figure from last shift may be stale.

> Evidence: developers.google.com/maps/documentation/places/web-service/usage-and-billing: billing account and card required even within free tier, no hard cap unless set manually. mapsleads.co/blog/google-places-api-free-tier-limits-2026: free tier is now per-SKU (10k Essentials / 5k Pro / 1k Enterprise), replacing the old $200 credit retired March 2025. Checked 2026-08-21. [read outside, developers.google.c

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

## What it used to believe

- **UNKNOWN status leads never route to call list or get emailed stuck at** retired 2026-08-19: Duplicate of itself in the standing list, two identical entries. Merging into one proven entry via the learn field above, not two near-identical working notes.
- **Care Pro's margin depends on clients not using their hours** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.
- **The active care client count is a live trigger, not a stat** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.
- **Every capacity number in the plan is a guess, not a fact** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.

Back to [[Memory]].
