---
source: yfs-console
kind: department
role: cdo
tags: [memory, departments]
---

# CDO

What this desk believes about its department, as of 2026-08-20. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: cdo` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** leads with a usable verdict %: 97.96 on 2026-08-18 to 97.67 on 2026-08-20 (down, 3 days)

## UNKNOWN leads: no confirmed route to the call list

*proven, revised 3 times, learned 2026-08-18 from shift.*

Correcting this. UNKNOWN/unconfirmed leads do reach the call list, they are just sorted last by buy_score so they never appear in a 50-row top sample, which is why three straight shifts of sampling looked like exclusion. The aggregate queue_buckets field (separate from the per-row bucket on the 50 shown) proves it. Hawkesbury & Nepean Plumbing specifically is stuck for a different reason: it has no phone number at all, so it can never enter the call list regardless of status, and it's UNKNOWN so it's never emailed either. That is a missing-contact-data problem on one lead, not a systemic routi

> Evidence: call_list queue_total 1740, queue_buckets: clicked 1, no_site 1273, no_email 310, quiet 2, unconfirmed 154 (sums to 1740). queue_bucket_first shows unconfirmed starting at position 1587 of 1740, meaning it occupies the last 154 slots by design, not zero slots. Hawkesbury & Nepean Plumbing lead record: phone blank, email blank, status UNKNOWN.

## Public AU business registers do not carry contact data

*working, revised 2 times, learned 2026-08-18 from research.*

Before emailing any OSM-sourced NO_SITE verdict, cross-check it against Google Places API's Contact Data SKU (which returns the website field). It has its own free allowance of 1,000 calls a month, separate from other Places SKUs, and this business sends far fewer than 1,000 emails a month, so every OSM no_site lead could be verified for free before going out. This turns the OSM tag-ambiguity risk I flagged last shift into a fixable engineering task, not just a question to raise. Worth handing to whoever owns the site-check step as a concrete build, not just a question.

> Evidence: Google Places Contact Data SKU free tier: 1,000 calls/month at zero cost, per mapsleads.co/blog/google-places-api-free-tier-limits-2026 and safegraph.com/guides/google-places-api-pricing, checked 2026-08-20. Business context: totals.sent_total 178, sent_today 0, well under the 1,000/month free allowance. [read outside, developers.google.com/maps/billing-and-pricing (via mapsleads.co/blog/google-pl

## Unconfirmed leads are rising, and today's sweep isn't why

*working, revised 2 times, learned 2026-08-19 from shift.*

Stop treating this as an open question. Unconfirmed count has not moved in two straight readings while total leads kept growing, meaning new leads are coming back with usable verdicts, not unconfirmed ones. Mark resolved: the rate stabilized after the 8/18 drop and has held since.

> Evidence: Current tile: leads 25518, unconfirmed 594 (97.671% usable). Prior same-day reading: leads 25506, unconfirmed 594 (97.673% usable). 12 new leads were added between the two readings and zero of them came back unconfirmed, so the unconfirmed count stayed flat at 594 both times.

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

## What it used to believe

- **UNKNOWN status leads never route to call list or get emailed stuck at** retired 2026-08-19: Duplicate of itself in the standing list, two identical entries. Merging into one proven entry via the learn field above, not two near-identical working notes.
- **Care Pro's margin depends on clients not using their hours** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.
- **The active care client count is a live trigger, not a stat** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.
- **Every capacity number in the plan is a guess, not a fact** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.

Back to [[Memory]].
