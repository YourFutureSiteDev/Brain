---
source: yfs-console
kind: department
role: coo
tags: [memory, departments]
---

# COO

What this desk believes about its department, as of 2026-08-19. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: coo` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** cycles today: 30 on 2026-08-18 to 37 on 2026-08-19 (up, 2 days)

## The bot never pauses, everything else does

*working, revised 1 time, learned 2026-08-18 from brief.*

Add a second failure mode alongside blackouts: an account that gets killed by its own sending pattern, not by a scheduled pause. Before trusting the current 51 daily cap, confirm with CCO whether this Gmail account went through a slow ramp or jumped straight to near-cap volume, since about a third of all mail ever sent from it went out in a single day. If there was no real ramp, the fix is to drop the daily cap back toward 20 to 30 for a couple of weeks and let it climb, because losing this account costs the same weeks of rebuilding that a bad blackout does, and this failure is self-inflicted 

> Evidence: Deliverability guides recommend starting new senders at 5 to 10 emails a day, ramping by 5 to 10 a day over 2 to 4 weeks before reaching 50 to 100; this account shows sent_total 143 against sent_today 49, meaning most volume arrived in one day rather than a gradual climb. [read outside, Saleshandy 'Warmup Email Account' guide and Mailreach 'Gmail Warmup Guide 2026' (both retrieved 2026-08-18), cro

## Real capacity is nine months a year, not twelve

*working, revised 1 time, learned 2026-08-18 from brief.*

Discount working months by utilization too, not just blackout weeks. On a normal working day, plan on roughly 60 to 70 percent of hours as available for actual build minutes, the rest goes to the call queue, sorting leads, checking the bot, and replying to prospects, none of which is a $99 or $1,000 job getting built. When setting how many jobs to promise in a month, apply both discounts: strip the blackout months to get 9 working months, then strip non build hours from each working day before committing to a job count.

> Evidence: Jobbers.io 2026: full time freelancers average 26 of 44 hours billable, 59 percent. Clockify and Freelancers Union: established freelancers bill 60 to 75 percent of hours, remainder is admin and business development, about 6 hours a week on admin alone. [read outside, Jobbers.io 'The Freelance Benchmark Report 2026' (retrieved 2026-08-19); Clockify 'How Freelancers Spend Time' (2025/2026); Freelan

## The call list tile overstates the working queue

*working, revised 1 time, learned 2026-08-18 from shift.*

Two shifts running, 100 of 100 sampled call_list records are NO_SITE with queue_total 365. Zero UNKNOWN-status records have shown up in either sample. That is strong, repeated evidence the call list build filters to status=NO_SITE only and drops the 454 UNKNOWN leads with a phone number entirely, rather than queuing them. Still cannot confirm from here, I have no tool to read the build query itself. Stop asking CDO to check, this is answered by the data: escalate to Byron to look at the query directly if CDO cannot access it either.

> Evidence: This shift: 50/50 call_list records, all status NO_SITE, queue_total 365, zero UNKNOWN. Last shift: same 50/50 pattern. CDO tile separately shows 454 leads UNKNOWN, never mailed.

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
