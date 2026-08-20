---
source: yfs-console
kind: department
role: cro
tags: [memory, departments]
---

# CRO

What this desk believes about its department, as of 2026-08-21. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: cro` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** calls waiting: 50 on 2026-08-18 to 50 on 2026-08-21 (flat, 4 days)

## The 50-call queue is head of a 365-deep backlog, not the whole list

*proven, revised 4 times, learned 2026-08-18 from shift.*

Revise the burst-then-flat read: growth is not purely flat between bursts, it steps up whenever a new sweep or directory source lands. Today's hotfrog:pest control sweep added 45 to queue_total in one shift, all landing in no_site. Keep working top to bottom by buy_score once the ordering bug is fixed; treat each new source type (mobile sweep, directory sweep) as a fresh small burst to expect, not noise.

> Evidence: queue_total went 1646 (burst) then 1760, 1765, 1769 (flat, single digits) then 1814 this shift, +45, matching queue_buckets no_site rising from 1297 to 1342. New rows in this pull carry search_term hotfrog:pest control and first_seen 2026-08-20, a source not seen in prior readings.

## Calls made are not landing on the priority queue

*proven, revised 3 times, learned 2026-08-19 from shift.*

Now a four day flatline, not three. Keep flagging as a tool gap, not something this desk fixes by reading again. The cost of the gap is compounding: the worked list looks frozen at 50 while the unworked backlog behind it keeps absorbing every new sweep, so each day this stays broken means more leads pile up stale before a human ever dials them.

> Evidence: calls waiting: 50 on 2026-08-18, 50 on 08-19, 50 on 08-20, 50 on 08-21, flat 4 days. pipeline.called still 8, unchanged across all four readings. All 50 call_list rows this pull still show calls_made 0 and last_call null. queue_total grew 1814 to 1900 in this shift alone (+86), no_site bucket 1342 to 1428, matching new hotfrog:pest control rows first_seen 2026-08-21.

## Call queue order breaks below the top score

*working, revised 2 times, learned 2026-08-19 from shift.*

Third consecutive shift, identical broken sequence: 95, 81,81,80,81,81,80,81,81,80,80,78,80,80,78,80,80,78,80,80,78,80,80,78,80,77(repeated). This is now proven stable, not noise or a timing fluke. It cannot be fixed by re-reading or by any desk here, it needs the sort query itself fixed. Stop re-verifying it every shift, it has been confirmed enough; the only thing left to do is get it in front of someone who can edit the query.

> Evidence: call_list buy_score sequence this pull: 95,81,81,80,81,81,80,81,81,80,80,78,80,80,78,80,80,78,80,80,78,80,80,78,80,77x25, matching the last two shifts word for word, plus a third day flat at calls waiting 50 and pipeline.called unchanged at 8.

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

## Each queued lead needs up to three call attempts, not one

*tried, revised 0 times, learned 2026-08-21 from research.*

Do not mark a lead worked after a single unanswered call. Cycle back and try each of the 50 up to 3 times before dropping it down the list, since that is where 93 percent of connects happen. Stop at 5 attempts, going further than that is wasted dialing time better spent on the next name. Pair this with the voicemail line already agreed: leave it on the attempt that does not connect, do not wait for a final attempt to leave one.

> Evidence: Cognism 2025 State of Cold Calling Report: average 3 attempts to connect, 93% of connects by call 3, 98% by call 5, additional calls beyond that ineffective [read outside, cognism.com 'B2B Cold Calling Statistics', 2025 data] [read outside, Cognism 'B2B Cold Calling Statistics' (cognism.com), citing its 2025 State of Cold Calling Report, cross-referenced with RAIN Group Top Performance in Sales Pr

## CEO's beauty-first call order contradicts Byron's buy_score order

*tried, revised 0 times, learned 2026-08-21 from shift.*

Do not apply the CEO's beauty-repliers-first rule until this is resolved. Under it, four beauty replier rows at buy_score 80 would be dialled before Damien Seton Mechanical, trades, buy_score 95, already replied, whom Byron has named as top of the list in four separate messages. The two instructions cannot both govern the same queue.

> Evidence: call_list this pull: Kristie's Hair Design, Shu's Massage, St George's Barber Shop and Unique Thai Massage are all niche beauty, stage replied, buy_score 80. Damien Seton Mechanical is niche trades, stage replied, buy_score 95. CEO instruction text: sort beauty niche repliers before trades, food or pro repliers regardless of when. Byron's four messages all name Damien Seton Mechanical, score 95, a

## What it used to believe

- **The written price has no monthly care number attached, the call has to introduce it fresh** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.

Back to [[Memory]].
