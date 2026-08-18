---
source: yfs-console
kind: department
role: cro
tags: [memory, departments]
---

# CRO

What this desk believes about its department, as of 2026-08-18. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: cro` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** calls waiting: 50 on 2026-08-18 to 50 on 2026-08-18 (flat, 1 days)

## Fifth of the enabled areas are in the wrong time zone for the call plan

*working, revised 1 time, learned 2026-08-18 from brief.*

Add a time-of-day rule on top of the time zone fix: call each area's local 9 to 10am or 3 to 4pm block, skip 12 to 2pm entirely, never before 8am or after 6pm local, and load Tuesday to Thursday first. This is US office-worker data, not proven on Australian tradies or beauty operators who are often on tools or with a client, so treat it as a starting window to test against our own call outcomes, not gospel.

> Evidence: Close.com and Revenue.io 2026 cold call studies, both citing PhoneBurner call data, converging on 9 to 10am/3 to 4pm as peak and a 35 percent answer-rate drop over lunch [read outside, Close.com 'Best Days & Times to Cold Call (Data-Backed) in 2026'; PhoneBurner data cited via Revenue.io 'Best Time to Cold Call Prospects in 2026']

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

## A script written for a plumber cannot be read to the leads on the list

*tried, revised 0 times, learned 2026-08-18 from brief.*

Before running any call block, confirm which niche the leads actually came from and use that trade's language, not a generic tradie script.

> Evidence: Section A1 item 8: plumber was deliberately dropped from the config because every agency already targets it, so a plumber-flavoured script does not match the mechanic, food, beauty or pro leads the bot is actually producing.

## 50 queued calls are not follow-ups, they are mostly cold opens

*tried, revised 0 times, learned 2026-08-18 from shift.*

Only 3 of the 50 in today's call queue have actually received a mockup email (GP Mechanical, Outback Barber, Plush Diamond). The other 47 are no-email leads who have never been contacted at all. Script these two groups differently: the 3 with a mockup sent get a real follow-up call referencing what was emailed and the $500/$1,000 price already quoted; the other 47 get a cold open, no mockup to reference, no price stated unless asked. Do not read one script to both.

> Evidence: Counted stage across all 50 call_list entries: 3 stage=emailed (GP Mechanical sent 2026-08-18, Outback Barber sent 2026-08-14, Plush Diamond sent 2026-08-14), 47 stage=found with sent_at null and no email address.

## What it used to believe

- **The written price has no monthly care number attached, the call has to introduce it fresh** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.

Back to [[Memory]].
