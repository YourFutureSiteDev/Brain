---
source: yfs-console
kind: department
role: coo
tags: [memory, departments]
---

# COO

What this desk believes about its department, as of 2026-08-20. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: coo` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** cycles today: 30 on 2026-08-18 to 47 on 2026-08-20 (up, 3 days)

## The bot never pauses, everything else does

*proven, revised 4 times, learned 2026-08-18 from brief.*

Third straight shift confirming daily cap sits at off with no cap and no pause. Cycles rising steadily (279 to 290 to 296) and sent_today rising too (0 to 44 to 49) with no sign of throttling. This is now proven three times over. The only open question left is whether uncapped sending was a deliberate CCO decision or another accidental setting jump like the one that caused the earlier freeze.

> Evidence: daily_cap off, sent_today 49 (up from 44), bot_running true, sending_on true, 296 cycles total (up from 290, up from 279 three shifts ago).

## The call list tile overstates the working queue

*proven, revised 3 times, learned 2026-08-18 from shift.*

The queue is not NO_SITE-only after all: queue_buckets this shift reads clicked 1, no_site 1290, no_email 313, quiet 2, unconfirmed 155, which sums exactly to queue_total 1761. So unconfirmed (UNKNOWN-status) leads with a phone do get bucketed into the call queue, just at 9 percent of it, and four shifts of 50-row samples missed them because the sample is rank/buy_score sorted and skews toward no_site. But the same payload also carries a second field, queue_bucket_first, giving wildly different counts for the identical bucket names (no_site 2, quiet 1605, unconfirmed 1607) that cannot both be 

> Evidence: This shift's call_list record: queue_buckets {clicked:1, no_site:1290, no_email:313, quiet:2, unconfirmed:155} summing to queue_total 1761, versus queue_bucket_first {clicked:1, no_site:2, no_email:1292, quiet:1605, unconfirmed:1607} on the same record for the same bucket labels.

## Real capacity is nine months a year, not twelve

*working, revised 2 times, learned 2026-08-18 from brief.*

The 60 to 70 percent billable figure already accounts for non-build hours existing. What it does not account for is that switching between build work and the call queue, bot checks, or replies inside the same block burns roughly 20 extra minutes of refocus time per switch, on top of the task itself. Batch those interruptions into fixed windows (e.g. calls and bot checks once at the start and once at the end of the day) rather than letting them interleave with a build block, or the real billable share drops below the 60 to 70 percent estimate.

> Evidence: UC Irvine research cited via cannelevate.com.au (2026): 23 min 15 sec average refocus time per interruption; freelancer estimate of 1 to 2 hours a day lost to 4 to 6 major task-type transitions. [read outside, cannelevate.com.au, 'How Context Switching Reduces Workplace Productivity' (2026, citing UC Irvine / Gloria Mark research), retrieved 2026-08-20]

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
