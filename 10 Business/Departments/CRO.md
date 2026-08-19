---
source: yfs-console
kind: department
role: cro
tags: [memory, departments]
---

# CRO

What this desk believes about its department, as of 2026-08-19. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: cro` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** calls waiting: 50 on 2026-08-18 to 50 on 2026-08-19 (flat, 2 days)

## The 50-call queue is head of a 365-deep backlog, not the whole list

*working, revised 2 times, learned 2026-08-18 from shift.*

The backlog is not creeping, it jumped: queue_total went 365 to 398 over one prior reading, then 398 to 1646 today, a 4x jump in a single shift. Cause is visible in the data itself: most of the new call_list rows carry search_term sweep:mobile and first_seen 2026-08-19, meaning a big OSM mobile sweep landed today and every no-email result from it joined the call queue at once. Keep working top to bottom by buy_score, that part is fine, but stop reading queue growth as steady. It moves in bursts tied to sweep size, and a sweep can outpace calling capacity in one day.

> Evidence: queue_total on all 50 call_list entries reads 1646 this shift versus 398 two readings ago; queue_buckets sums to 1646 (no_site 1273, no_email 253, unconfirmed 117, quiet 2, clicked 1); most new rows show first_seen 2026-08-19T11:25 or 15:04 with search_term sweep:mobile.

## Fifth of the enabled areas are in the wrong time zone for the call plan

*working, revised 1 time, learned 2026-08-18 from brief.*

Add a time-of-day rule on top of the time zone fix: call each area's local 9 to 10am or 3 to 4pm block, skip 12 to 2pm entirely, never before 8am or after 6pm local, and load Tuesday to Thursday first. This is US office-worker data, not proven on Australian tradies or beauty operators who are often on tools or with a client, so treat it as a starting window to test against our own call outcomes, not gospel.

> Evidence: Close.com and Revenue.io 2026 cold call studies, both citing PhoneBurner call data, converging on 9 to 10am/3 to 4pm as peak and a 35 percent answer-rate drop over lunch [read outside, Close.com 'Best Days & Times to Cold Call (Data-Backed) in 2026'; PhoneBurner data cited via Revenue.io 'Best Time to Cold Call Prospects in 2026']

## 50 queued calls are not follow-ups, they are mostly cold opens

*working, revised 1 time, learned 2026-08-18 from shift.*

Add to the cold-open script for the 47 no-email leads: write a 20 to 25 second voicemail line for every one of them, because most calls to a small business mobile will not be answered but two thirds of unknown-number voicemails still get checked. Name, business name, the one fault found (no website), and a callback number, no price stated. Do not skip the voicemail just because the call did not connect, that is not a failed call, it is a delivered one.

> Evidence: Aussie AI Agency 2026: 81% of unknown-number calls go to voicemail, 67% of those voicemails get checked, voicemail-to-conversation conversion 4-11% for Australian small business [read outside, Aussie AI Agency, 'Missed Call Statistics Australia 2026' (aussieaiagency.com.au), cross-checked against CloudTalk 'Cold Calling Statistics 2026' and Scrap.io 'Cold Calling Success Rate in 2026: 200K+ Calls 

## Calls made are not landing on the priority queue

*working, revised 1 time, learned 2026-08-19 from shift.*

This is now a two day flatline, not a one time snapshot. Whatever calling is happening (called=8 total, unchanged) is not writing back to call_list, and the 50 queued leads show zero contact activity across both readings. The fix is not more checking from this desk, it is the outcome-logging tool Byron already asked for. Keep flagging this until that exists.

> Evidence: CRO fortnight number: calls waiting 50 on 2026-08-18 to 50 on 2026-08-19, flat. pipeline.called=8 both readings. All 50 call_list entries: calls_made 0, last_call null, both days.

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

## Call queue order breaks below the top score

*tried, revised 0 times, learned 2026-08-19 from shift.*

The call_list as delivered is not actually sorted by buy_score past the very first entry. Working it top to bottom is not the same as working it by buy_score until the sort is fixed, which contradicts what earlier shifts reported ('ordering still holds'). This needs to go to whoever owns the query, not another read from this desk.

> Evidence: buy_score sequence across the 50 queued: 95, 81, 81, 80, 81, 81, 80, 81, 81, 80, 80, 78, 80, 80, 78, 80, 80, 78, 80, 80, 78, 80, 80, 78, 80, then 77 x25. Position 4 (80) is followed by position 5 (81), and this pattern of a lower score followed by a higher one repeats seven times in the first 26 rows.

## What it used to believe

- **The written price has no monthly care number attached, the call has to introduce it fresh** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.

Back to [[Memory]].
