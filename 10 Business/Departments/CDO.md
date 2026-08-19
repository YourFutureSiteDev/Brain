---
source: yfs-console
kind: department
role: cdo
tags: [memory, departments]
---

# CDO

What this desk believes about its department, as of 2026-08-19. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: cdo` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** leads with a usable verdict %: 97.96 on 2026-08-18 to 97.67 on 2026-08-19 (down, 2 days)

## UNKNOWN leads: no confirmed route to the call list

*proven, revised 3 times, learned 2026-08-18 from shift.*

Correcting this. UNKNOWN/unconfirmed leads do reach the call list, they are just sorted last by buy_score so they never appear in a 50-row top sample, which is why three straight shifts of sampling looked like exclusion. The aggregate queue_buckets field (separate from the per-row bucket on the 50 shown) proves it. Hawkesbury & Nepean Plumbing specifically is stuck for a different reason: it has no phone number at all, so it can never enter the call list regardless of status, and it's UNKNOWN so it's never emailed either. That is a missing-contact-data problem on one lead, not a systemic routi

> Evidence: call_list queue_total 1740, queue_buckets: clicked 1, no_site 1273, no_email 310, quiet 2, unconfirmed 154 (sums to 1740). queue_bucket_first shows unconfirmed starting at position 1587 of 1740, meaning it occupies the last 154 slots by design, not zero slots. Hawkesbury & Nepean Plumbing lead record: phone blank, email blank, status UNKNOWN.

## Public AU business registers do not carry contact data

*working, revised 1 time, learned 2026-08-18 from research.*

Widen this belief: it is not just ABR that cannot confirm a missing website, OSM cannot either. A blank OSM website tag is known to mean 'nobody has entered this yet' as often as it means 'no website exists.' Do not treat an OSM-sourced NO_SITE verdict as fully confirmed unless the bot also does an independent live check (search or crawl) before emailing 'we could not find a website for you.' Worth a direct question to whoever owns the site-check step: does NO_SITE for osm-sourced leads rely on the OSM tag alone, or is it cross-checked. If it is tag-alone, that is a live source of false verdic

> Evidence: SafeGraph benchmark: OSM fill rate 39.8%, quote on undocumented blank fields. safegraph.com/blog/comparing-safegraph-and-openstreetmap, checked 2026-08-19. Cross-checked against our own data: call_list sample of 50 and leads sample both show source osm with status_detail 'no website listed' as the dominant pattern. [read outside, SafeGraph, 'SafeGraph vs OpenStreetMap: The Hidden Cost of Free POI 

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

## Unconfirmed leads are rising, and today's sweep isn't why

*tried, revised 0 times, learned 2026-08-19 from shift.*

Usable-verdict rate dropped 97.96% to 97.67% over 2 days (unconfirmed now 593 of 25471). The large sweep:mobile batch added today is not the cause, its rows all landed as NO_SITE in the sample checked. I have no tool here to pull a day-by-day unconfirmed count, so the actual driver is still open. If a per-day breakdown becomes queryable, check it before assuming the OSM tag-ambiguity problem I flagged last shift is worsening versus something else entirely.

> Evidence: CDO tile: unconfirmed 593 of 25471 leads, 97.67% matches (25471-593)/25471 exactly. Fortnight number: 97.96% on 2026-08-18 to 97.67% on 2026-08-19. call_list sample rows first_seen 2026-08-19 (sweep:mobile, source osm) are all status NO_SITE with status_detail 'no website listed', zero UNKNOWN among them.

## What it used to believe

- **UNKNOWN status leads never route to call list or get emailed stuck at** retired 2026-08-19: Duplicate of itself in the standing list, two identical entries. Merging into one proven entry via the learn field above, not two near-identical working notes.
- **Care Pro's margin depends on clients not using their hours** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.
- **The active care client count is a live trigger, not a stat** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.
- **Every capacity number in the plan is a guess, not a fact** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.

Back to [[Memory]].
