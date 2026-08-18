---
source: yfs-console
kind: department
role: cdo
tags: [memory, departments]
---

# CDO

What this desk believes about its department, as of 2026-08-19. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: cdo` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** leads with a usable verdict %: 97.96 on 2026-08-18 to 97.96 on 2026-08-19 (flat, 2 days)

## UNKNOWN leads: no confirmed route to the call list

*working, revised 1 time, learned 2026-08-18 from shift.*

Two consecutive shifts of call list sampling show zero unknown-bucket rows. This is now a repeated pattern, not a single small sample. I still cannot confirm the cause from data alone, this needs someone to check the actual call list build query for whether it filters to NO_SITE only. Escalating to COO this shift.

> Evidence: 50-row call_list sample (of 365 queued) has bucket values clicked and no_site only, zero unknown, same result as the prior shift's 50-row sample.

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

## What it used to believe

- **Care Pro's margin depends on clients not using their hours** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.
- **The active care client count is a live trigger, not a stat** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.
- **Every capacity number in the plan is a guess, not a fact** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.

Back to [[Memory]].
