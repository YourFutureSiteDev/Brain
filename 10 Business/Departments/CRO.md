---
source: yfs-console
kind: department
role: cro
tags: [memory, departments]
---

# CRO

What this desk believes about its department, as of 2026-08-20. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: cro` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** calls waiting: 50 on 2026-08-18 to 50 on 2026-08-20 (flat, 3 days)

## The 50-call queue is head of a 365-deep backlog, not the whole list

*proven, revised 3 times, learned 2026-08-18 from shift.*

The mobile sweep burst that took queue_total from 398 to 1646 has not repeated. Growth since has been a slow trickle: 1646, then roughly 1760, 1765, now 1769, single digits a shift. Read queue growth as burst-then-flat, not creeping. Keep working top to bottom by buy_score once the ordering bug is fixed; the backlog itself is not the urgent part right now, the flatlined calling is.

> Evidence: queue_total on this shift's 50-item pull reads 1769 (queue_buckets: no_site 1297, no_email 313, quiet 3, unconfirmed 155, clicked 1, sum 1769), up only 4 to 9 from the last two readings of roughly 1760 and 1765, versus the earlier single-shift jump from 398 to 1646.

## Calls made are not landing on the priority queue

*working, revised 2 times, learned 2026-08-19 from shift.*

This is now a three day flatline, not two. Keep flagging it as a tool gap, not something this desk can fix by reading again. Whatever calling Byron is doing off to the side is not writing back to call_list, so the queue looks idle even if work is happening.

> Evidence: Department number line: calls waiting 50 on 2026-08-18, 50 on 2026-08-19, 50 on 2026-08-20, flat for 3 days. pipeline.called is still 8, unchanged across all three readings. All 50 call_list entries in this pull still show calls_made 0 and last_call null. Meanwhile queue_total behind the top 50 grew from 1646 to 1765 in the same window, so the backlog is moving even though the worked list looks fr

## Fifth of the enabled areas are in the wrong time zone for the call plan

*working, revised 1 time, learned 2026-08-18 from brief.*

Add a time-of-day rule on top of the time zone fix: call each area's local 9 to 10am or 3 to 4pm block, skip 12 to 2pm entirely, never before 8am or after 6pm local, and load Tuesday to Thursday first. This is US office-worker data, not proven on Australian tradies or beauty operators who are often on tools or with a client, so treat it as a starting window to test against our own call outcomes, not gospel.

> Evidence: Close.com and Revenue.io 2026 cold call studies, both citing PhoneBurner call data, converging on 9 to 10am/3 to 4pm as peak and a 35 percent answer-rate drop over lunch [read outside, Close.com 'Best Days & Times to Cold Call (Data-Backed) in 2026'; PhoneBurner data cited via Revenue.io 'Best Time to Cold Call Prospects in 2026']

## A script written for a plumber cannot be read to the leads on the list

*working, revised 1 time, learned 2026-08-18 from brief.*

Add a specific line for the 'I've got Facebook, I don't need a website' objection, which will come up often on this list since most leads are beauty and trades with no site at all. Say it plainly: Facebook doesn't come up when someone Googles the trade and the suburb, and the business doesn't own that page, Meta does. A site is what backs up word of mouth once someone goes looking. Do not argue against Facebook itself, most of these owners like it fine, just point out it can't do the one job a search result can.

> Evidence: Buildify NZ and Groundwork Digital 2026: Facebook rarely appears for local trade searches, page ownership sits with Meta not the business, organic reach on Facebook pages has dropped significantly. [read outside, Buildify NZ 'Do Tradies Need a Website in 2026' (buildifysites.co.nz) and Groundwork Digital 'Do Tradies Need a Website' (groundworkdigital.co.nz), both 2026]

## 50 queued calls are not follow-ups, they are mostly cold opens

*working, revised 1 time, learned 2026-08-18 from shift.*

Add to the cold-open script for the 47 no-email leads: write a 20 to 25 second voicemail line for every one of them, because most calls to a small business mobile will not be answered but two thirds of unknown-number voicemails still get checked. Name, business name, the one fault found (no website), and a callback number, no price stated. Do not skip the voicemail just because the call did not connect, that is not a failed call, it is a delivered one.

> Evidence: Aussie AI Agency 2026: 81% of unknown-number calls go to voicemail, 67% of those voicemails get checked, voicemail-to-conversation conversion 4-11% for Australian small business [read outside, Aussie AI Agency, 'Missed Call Statistics Australia 2026' (aussieaiagency.com.au), cross-checked against CloudTalk 'Cold Calling Statistics 2026' and Scrap.io 'Cold Calling Success Rate in 2026: 200K+ Calls 

## Call queue order breaks below the top score

*working, revised 1 time, learned 2026-08-19 from shift.*

Second consecutive shift with the exact same broken sequence. Position 1 (Damien Seton Mechanical, 95) is correct, but from position 2 on the order is not sorted: 81, 81, 80, 81, 81, 80, 81, 81, 80, 80, 78, 80, 80, 78, 80, 80, 78, 80, 80, 78, 80, 80, 78, 80, then 77 repeated 25 times, with lower scores followed by higher ones seven times in the first 26 rows. This is stable, not noise, so it is a query bug, not a data timing issue. Byron's standing instruction to work strictly top to bottom by buy_score cannot be honoured past row 1 until the query is fixed.

> Evidence: call_list buy_score sequence read this shift: 95,81,81,80,81,81,80,81,81,80,80,78,80,80,78,80,80,78,80,80,78,80,80,78,80,77x25 - matches the identical sequence recorded last shift word for word.

## The pipeline is not a lead count, it is a dial count

*tried, revised 0 times, learned 2026-08-18 from brief.*

Do not report leads generated as progress. Track how many are actually called or emailed, because that is the only number that turns into a job.

> Evidence: Brief says it is early with almost nothing sent and nothing banked, and the whole CTO/CEO section on the bot shows discovery and mockups are automated but the human step, the call, is the one nobody has timed or measured.

## The quote in the prospect's inbox is $500 or $1,000, never say a different number on the call

*tried, revised 0 times, learned 2026-08-18 from brief.*

Always open config.json pricing before a call or a script gets written, and never quote $99 or $250 for a local job. That number does not exist anymore for that lead.

> Evidence: Section A1 item 1: config.json sets remake at $500 and newbuild at $1,000, already sent in every email, while three officers' scripts and tables argued over $99 and $250.

## The old 59 percent no-website line is dead, our own data replaces it

*tried, revised 0 times, learned 2026-08-18 from brief.*

Do not use the GoDaddy or Yellow stat on a call. Pull the real count of faults found from the areas actually being worked and use that instead.

> Evidence: Section A1 item 7 and B3: the figure is seven years old and falsifiable in one sentence, and the brief names the better replacement, our own data in the bot's database, current and local.

## What it used to believe

- **The written price has no monthly care number attached, the call has to introduce it fresh** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.

Back to [[Memory]].
