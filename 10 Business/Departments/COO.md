---
source: yfs-console
kind: department
role: coo
tags: [memory, departments]
---

# COO

What this desk believes about its department, as of 2026-08-19. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: coo` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** cycles today: 30 on 2026-08-18 to 27 on 2026-08-19 (down, 2 days)

## The bot never pauses, everything else does

*proven, revised 3 times, learned 2026-08-18 from brief.*

Daily cap has gone from stuck at 1 to fully off, not a gradual ramp. 44 sent today already, cycles total 290 up from 279. The freeze this lesson worried about is over, but nobody ramped it, it just got switched off outright. Still needs a CCO check that going straight to uncapped is deliberate and safe, not another accidental setting jump like the one that caused the freeze.

> Evidence: daily_cap off, sent_today 44, bot_running true, sending_on true, 290 cycles total (up from 279 two shifts ago). Prior state was daily_cap 1 with 0 sent.

## The call list tile overstates the working queue

*working, revised 2 times, learned 2026-08-18 from shift.*

Fourth sample running the same result: 50/50 NO_SITE, zero UNKNOWN, and now queue_total 398 sits nowhere near the COO tile's 3036. I have no tool to open the build query itself, so more sampling from this desk adds nothing new. This is now a task for Byron, not another shift of re-checking.

> Evidence: This shift's call_list array: 50/50 records status NO_SITE, queue_total 398. COO tile: Call list 3036 (no email found). CDO tile: 456 unconfirmed leads never mailed. Same pattern held last two shifts at queue_total 365 and tile 3020.

## Real capacity is nine months a year, not twelve

*working, revised 1 time, learned 2026-08-18 from brief.*

Discount working months by utilization too, not just blackout weeks. On a normal working day, plan on roughly 60 to 70 percent of hours as available for actual build minutes, the rest goes to the call queue, sorting leads, checking the bot, and replying to prospects, none of which is a $99 or $1,000 job getting built. When setting how many jobs to promise in a month, apply both discounts: strip the blackout months to get 9 working months, then strip non build hours from each working day before committing to a job count.

> Evidence: Jobbers.io 2026: full time freelancers average 26 of 44 hours billable, 59 percent. Clockify and Freelancers Union: established freelancers bill 60 to 75 percent of hours, remainder is admin and business development, about 6 hours a week on admin alone. [read outside, Jobbers.io 'The Freelance Benchmark Report 2026' (retrieved 2026-08-19); Clockify 'How Freelancers Spend Time' (2025/2026); Freelan

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
