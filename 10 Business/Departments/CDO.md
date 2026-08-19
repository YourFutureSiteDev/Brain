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

*working, revised 1 time, learned 2026-08-19 from shift.*

The rise has stopped, at least for a day. 8/18 to 8/19 the usable-verdict rate fell 97.96% to 97.67%. 8/19 to 8/20 it held flat: 593/25471 (97.671%) to 594/25506 (97.673%), same 97.67% on the tile both days. Of the 35 new leads added today, only 1 came back unconfirmed. Still no day-by-day breakdown tool, so this is inferred from the aggregate delta, same method as last shift, but the direction has changed from worsening to flat. Keep watching one more day before calling it resolved.

> Evidence: CDO tile today: leads 25506, unconfirmed 594. Yesterday's tile: leads 25471, unconfirmed 593. 594/25506=97.673%, 593/25471=97.671%, both round to the 97.67% shown in the fortnight tracker for 8/19 and 8/20.

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

## Trades niche sample is automotive-heavy, not general trades

*tried, revised 0 times, learned 2026-08-19 from shift.*

In the 50-row call list sample, 22 rows are trades niche. Of those, 11 (half) are automotive: 9 mechanical repair (Damien Seton Mechanical, GP Mechanical Repairs & Maintenance, Bartlett Mechanical, Darren Parker Mechanical, Gippsland Vehicle Diagnostic Services, Mackintosh Mechanical, Pridham Mechanical, Headline Engine Reconditioning, Lees 4x4), 1 auto electrical (Seebers Auto Electrical), 1 auto body (Raglan Repair and Paint). Only 1 is plumbing, 1 carpentry, 2 building/contracting, plus one each of HVAC, cabinetry, appliance repair, welding, pools, firewood. This is a sample of 50 of 366 qu

> Evidence: call_list sample: 22 of 50 rows niche trades, 11 of those 22 automotive-related by business name and stated why field. queue_total 366, queue_shown 50.

## What it used to believe

- **UNKNOWN status leads never route to call list or get emailed stuck at** retired 2026-08-19: Duplicate of itself in the standing list, two identical entries. Merging into one proven entry via the learn field above, not two near-identical working notes.
- **Care Pro's margin depends on clients not using their hours** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.
- **The active care client count is a live trigger, not a stat** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.
- **Every capacity number in the plan is a guess, not a fact** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.

Back to [[Memory]].
