---
source: yfs-console
kind: department
role: coo
tags: [memory, departments]
---

# COO

What this desk believes about its department, as of 2026-08-18. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: coo` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** cycles today: 21 on 2026-08-18 to 21 on 2026-08-18 (flat, 1 days)

## The bot never pauses, everything else does

*working, revised 1 time, learned 2026-08-18 from brief.*

Add a second failure mode alongside blackouts: an account that gets killed by its own sending pattern, not by a scheduled pause. Before trusting the current 51 daily cap, confirm with CCO whether this Gmail account went through a slow ramp or jumped straight to near-cap volume, since about a third of all mail ever sent from it went out in a single day. If there was no real ramp, the fix is to drop the daily cap back toward 20 to 30 for a couple of weeks and let it climb, because losing this account costs the same weeks of rebuilding that a bad blackout does, and this failure is self-inflicted 

> Evidence: Deliverability guides recommend starting new senders at 5 to 10 emails a day, ramping by 5 to 10 a day over 2 to 4 weeks before reaching 50 to 100; this account shows sent_total 143 against sent_today 49, meaning most volume arrived in one day rather than a gradual climb. [read outside, Saleshandy 'Warmup Email Account' guide and Mailreach 'Gmail Warmup Guide 2026' (both retrieved 2026-08-18), cro

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

## Real capacity is nine months a year, not twelve

*tried, revised 0 times, learned 2026-08-18 from brief.*

Plan and report against 9 working months. Do not let a monthly capacity number ignore the roughly 150 hours blackouts remove annually.

> Evidence: Section 7: four blackouts a year cost about 150 hours, close to three months of capacity.

## No actual minutes logged means the three hour rule is unverified

*tried, revised 0 times, learned 2026-08-18 from brief.*

Push for every job to close with real timer minutes recorded, and treat any job closed without them as a gap in the evidence, not a completed data point.

> Evidence: Section 8, decision 2: without recorded actual minutes the three hour rule is an opinion, not a fact.

## The call list tile overstates the working queue

*tried, revised 0 times, learned 2026-08-18 from shift.*

3020 is the raw pool of phone-no-email leads, not the actual queue. Every call_list record returned this shift shows queue_total 365, a gap of 2655 leads that are counted on my tile but not in the buy-ready queue CRO actually works. Do not quote 3020 as callable capacity. Needs CDO to confirm what is filtering that gap out, since the 451 UNKNOWN-status-with-phone leads Byron is asking about could be sitting entirely inside it.

> Evidence: COO tile: 'Call list 3020, no email found.' Call_list array this shift: 50/50 records show queue_total 365, queue_shown 50, all status NO_SITE, zero UNKNOWN.

## What it used to believe

- **Every care client sold subtracts from next month's build hours** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.

Back to [[Memory]].
