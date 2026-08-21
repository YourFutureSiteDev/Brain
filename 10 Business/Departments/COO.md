---
source: yfs-console
kind: department
role: coo
tags: [memory, departments]
---

# COO

What this desk believes about its department, as of 2026-08-21. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: coo` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** cycles today: 30 on 2026-08-18 to 25 on 2026-08-21 (down, 4 days)

## The bot never pauses, everything else does

*proven, revised 5 times, learned 2026-08-18 from brief.*

sent_today is a per-day counter that resets to zero at the date boundary, it is not a running total. This shift it dropped from 49 to 0 while cycles kept rising 296 to 318 and bot_running, sending_on and cap-off all held steady. Do not read a sent_today drop across shifts as a jam, only a same-day drop with cycles still rising would be. The open question stands: whether uncapped sending is a deliberate CCO choice, still sitting with Byron as a task not COO work.

> Evidence: sent_today 49 last shift to 0 this shift on 2026-08-20, cycles 296 to 318 over the same gap, daily_cap off both shifts, bot_running true both shifts.

## The call list tile overstates the working queue

*proven, revised 5 times, learned 2026-08-18 from shift.*

This is now confirmed a third time and directly answers both open CDO asks: the call list build does not filter to NO_SITE only, it includes UNKNOWN-status leads that have a phone number, consistently at 8 to 9 percent of the queue. Treat this as settled, stop re-asking it, and read the queue_total tile as NO_SITE plus a small UNKNOWN-with-phone slice, not a NO_SITE-only count.

> Evidence: This shift's queue_buckets: clicked 1 + no_site 1431 + no_email 313 + quiet 3 + unconfirmed 155 = 1903, exactly matching queue_total 1903. Unconfirmed share 155/1903 = 8.1%, versus 8.2% two shifts ago and 8.8% three shifts ago, same pattern each time.

## Real capacity is nine months a year, not twelve

*proven, revised 3 times, learned 2026-08-18 from brief.*

Revise the billable share downward. The working estimate was 60 to 70 percent; broader freelancer data puts sustainable utilization at 50 to 65 percent, with the average solo freelancer landing around 22 to 26 billable hours in a 40 to 44 hour week. When sizing how many $500 or $1,500 jobs Byron can actually carry in a month, plan against the low to mid 50s percent, not 60 to 70, especially once call queue time and bot checks are added on top.

> Evidence: solohourly.com (2026): 10,000+ freelancers averaged 22.4 billable hours/week, sustainable target 20 to 30 hours (50 to 65 percent utilization). Separate 2026 freelancer survey cited via web search: average full time freelancer bills 26 of 44 hours (59 percent), top ($150k+) earners around 80 percent. [read outside, solohourly.com, 'How Many Billable Hours is Realistic? (20-30 Hour Rule)', updated 

## First real case of the same-day sent_today drop the jam-check was watching for

*proven, revised 3 times, learned 2026-08-20 from shift.*

Resolved as far as this console can take it. Sends are happening, not stuck: sent_today rose 47 to 49 while cycles rose 357 to 364, all on 2026-08-21. But the counter did not reset to 0 at the day boundary the way it should have, it just kept incrementing from the pre-midnight value. That is a counter bug, not a delivery jam. This console cannot read the reset logic, so it stays a task for Byron, not a repeat tile check.

> Evidence: sent_today 47 at cycles 357 (last cycle 11:56, 2026-08-21), now 49 at cycles 364 (last cycle 15:38, 2026-08-21). Cycles gained 7, sent_today gained only 2, and it started from 47 not 0 on the new day.

## Cycle throughput is falling as the lead pool saturates

*working, revised 1 time, learned 2026-08-20 from shift.*

Still a real slowdown but it is not a flat cliff: today's cycle count ticked up from 18 to 21 and this shift's gain was +4 (320 to 324) versus +2 last shift, both still far below the +22 baseline from three shifts ago. Keep reading this as the search grid running low on new ground, not a bot jam, since bot_running, sending_on and cap-off all held steady through the whole run. Still sits with CMO's sweep config, not a COO fix.

> Evidence: cycles today 30 (2026-08-18) to 18 (previous check) to 21 (this shift); total cycles gain +2 (318 to 320) last shift vs +4 (320 to 324) this shift, both bot_running true and cap off.

## A $99 job only works if the clock actually started

*tried, revised 0 times, learned 2026-08-18 from brief.*

Refuse to log a job as started until payment, intake and tested logins are all confirmed. Do not let 'we will start it now and sort access later' happen.

> Evidence: Section 1 and 4.1: the start gate, missing logins cost an extra hour, gate is zero build minutes.

## 180 minutes is a hard stop, not a target

*tried, revised 0 times, learned 2026-08-18 from brief.*

Once a $99 job timer hits 180 minutes, ship what exists and log why, rather than quietly finishing it right.

> Evidence: Section 4.1: if a block overruns by more than 20 percent, stop, ship what exists, log why.

## Never run a $500 and a $1,000 job in the same month

*tried, revised 0 times, learned 2026-08-18 from brief.*

When scheduling builds, check the month's tier mix before confirming a second big job and push it to the next month if one Pro or Storefront is already booked.

> Evidence: Section 5: 'Also stop doing this' - 22 plus 12 hours leaves nothing for care, calls or anything going wrong.

## No actual minutes logged means the three hour rule is unverified

*tried, revised 0 times, learned 2026-08-18 from brief.*

Push for every job to close with real timer minutes recorded, and treat any job closed without them as a gap in the evidence, not a completed data point.

> Evidence: Section 8, decision 2: without recorded actual minutes the three hour rule is an opinion, not a fact.

## What it used to believe

- **Every care client sold subtracts from next month's build hours** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.

Back to [[Memory]].
