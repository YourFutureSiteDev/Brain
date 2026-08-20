---
source: yfs-console
kind: department
role: coo
tags: [memory, departments]
---

# COO

What this desk believes about its department, as of 2026-08-20. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: coo` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** cycles today: 30 on 2026-08-18 to 21 on 2026-08-20 (down, 3 days)

## The bot never pauses, everything else does

*proven, revised 5 times, learned 2026-08-18 from brief.*

sent_today is a per-day counter that resets to zero at the date boundary, it is not a running total. This shift it dropped from 49 to 0 while cycles kept rising 296 to 318 and bot_running, sending_on and cap-off all held steady. Do not read a sent_today drop across shifts as a jam, only a same-day drop with cycles still rising would be. The open question stands: whether uncapped sending is a deliberate CCO choice, still sitting with Byron as a task not COO work.

> Evidence: sent_today 49 last shift to 0 this shift on 2026-08-20, cycles 296 to 318 over the same gap, daily_cap off both shifts, bot_running true both shifts.

## The call list tile overstates the working queue

*proven, revised 3 times, learned 2026-08-18 from shift.*

The queue is not NO_SITE-only after all: queue_buckets this shift reads clicked 1, no_site 1290, no_email 313, quiet 2, unconfirmed 155, which sums exactly to queue_total 1761. So unconfirmed (UNKNOWN-status) leads with a phone do get bucketed into the call queue, just at 9 percent of it, and four shifts of 50-row samples missed them because the sample is rank/buy_score sorted and skews toward no_site. But the same payload also carries a second field, queue_bucket_first, giving wildly different counts for the identical bucket names (no_site 2, quiet 1605, unconfirmed 1607) that cannot both be 

> Evidence: This shift's call_list record: queue_buckets {clicked:1, no_site:1290, no_email:313, quiet:2, unconfirmed:155} summing to queue_total 1761, versus queue_bucket_first {clicked:1, no_site:2, no_email:1292, quiet:1605, unconfirmed:1607} on the same record for the same bucket labels.

## Real capacity is nine months a year, not twelve

*working, revised 2 times, learned 2026-08-18 from brief.*

The 60 to 70 percent billable figure already accounts for non-build hours existing. What it does not account for is that switching between build work and the call queue, bot checks, or replies inside the same block burns roughly 20 extra minutes of refocus time per switch, on top of the task itself. Batch those interruptions into fixed windows (e.g. calls and bot checks once at the start and once at the end of the day) rather than letting them interleave with a build block, or the real billable share drops below the 60 to 70 percent estimate.

> Evidence: UC Irvine research cited via cannelevate.com.au (2026): 23 min 15 sec average refocus time per interruption; freelancer estimate of 1 to 2 hours a day lost to 4 to 6 major task-type transitions. [read outside, cannelevate.com.au, 'How Context Switching Reduces Workplace Productivity' (2026, citing UC Irvine / Gloria Mark research), retrieved 2026-08-20]

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
