---
source: yfs-console
kind: department
role: ceo
tags: [memory, departments]
---

# CEO

What this desk believes about its department, as of 2026-08-22. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: ceo` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** replies: 2 on 2026-08-18 to 3 on 2026-08-22 (up, 5 days)

## Reply-to-call speed is the real constraint, not send volume

*proven, revised 4 times, learned 2026-08-18 from brief.*

Queue growth has stalled, not accelerated: queue_total moved 1904 to 1909 this shift, a +5 crawl versus the earlier 4.4x jump. calls_made is still 8, unchanged across every check this fortnight. The constraint is not a growing backlog anymore, it is that nobody is working the 50 shown at all. Keep reading queue_total from call_list, not the CEO tile's rounded 50. The sort-order half of this (buy_ready leads first) has failed three console checks in a row and now sits with Byron as a task, not another CRO instruction.

> Evidence: call_list rows today all show queue_total 1909, queue_buckets no_site 1432 + no_email 313 + unconfirmed 155 + quiet 7 + clicked 1 + replied 1 = 1909, up from 1904 last check; business.pipeline.called=8, unchanged; replied-stage positions in the 50-row queue (1,2,10,15,19,21,23,26,27,28,32,38,40,41,43,49) are byte-identical to the prior three checks.

## Our price sits under the market floor, not just under agency price

*proven, revised 3 times, learned 2026-08-18 from research.*

This is the third and biggest data point yet. Beyond the two mockup-tactic operators, the general regional Australian market prices a small business website at $5,000 to $10,000, with even budget regional freelancers at $50 to $100 an hour. Our $1,500 newbuild is not a slightly aggressive entry price, it is a fifth to a tenth of what the market actually charges once you look past the two lead-gen specialists. CFO should treat this as room to move price up, not just a note to file. This does not change what CMO or COO do, and nobody should raise price before a single job is banked and hours per

> Evidence: sparkinteract.com.au, keentodesign.com.au, rockingweb.com.au, paramark.com.au, 2026 guides, fetched 22 Aug 2026: small business sites average $5,000-$10,000, regional freelancer rates $50-$100/hr, 20-40% below metro agency pricing [read outside, Aggregated from sparkinteract.com.au, keentodesign.com.au, rockingweb.com.au and paramark.com.au 2026 web design cost guides, search run 22 Aug 2026]

## CMO areas live tile is the real bug, niches live tile checks out

*proven, revised 3 times, learned 2026-08-20 from shift.*

The narrowing is real and accelerating, not stalled like I said last shift. ready_blocked_area has gone 358/533 (67%) to 337/542 (62%) to now 331/643 (51.5%): the blocked count actually fell slightly while ready grew by 101, mostly from trades (ready 177 to 278, ready_live 110 to 216, blocked ratio 38% to 22%). Beauty and food are flat (beauty blocked 74% both times, food blocked 78% both times). The areas-live tile is still frozen at 402 of 403 across four straight shifts while the real gating number moves every day, so the tile is confirmed disconnected from ready_blocked_area, not just slow

> Evidence: totals.ready_by_niche trades 278 + beauty 268 + pro 25 + food 72 = 643; ready_live_by_niche trades 216 + beauty 68 + pro 12 + food 16 = 312; ready_blocked_area 331; cmo tile still reads areas live 402 of 403, unchanged from two shifts ago.

## pipeline.replied and totals.replies disagree by 38x, replied stage looks untrustworthy

*proven, revised 3 times, learned 2026-08-20 from shift.*

Gap has widened, not narrowed. Today's snapshot: totals.replies=3 (CEO tile), pipeline.replied=138, totals.replies_all=155, all read from the same business object. That is a 46x spread now versus 38x last check, and pipeline.replied more than doubled (76 to 138) while the CEO tile moved by exactly 1 (2 to 3). Whatever pipeline.replied is counting is inflating fast and does not track what Byron sees on his own tile. Still do not act on pipeline.replied or replies_all until CDO names which count is real.

> Evidence: business.totals.replies=3, business.pipeline.replied=138, business.totals.replies_all=155, all from the 2026-08-21 snapshot; last checked shift had 2, 76, 90 respectively.

## One trade, sequentially, never four at once

*working, revised 1 time, learned 2026-08-18 from brief.*

The market data backs this harder than I had it: small, tightly targeted sends beat big blended ones by nearly 3x on reply rate (5.8% vs 2.1%). That is an argument for CMO staying narrow by trade and area, not just a flywheel argument. Our current 1.4% reply rate is not a crisis, it is what an unfocused, mixed-niche 143-email batch looks like. Tell CMO the fix for reply rate is narrower targeting, not more volume.

> Evidence: Puzzle Inbox and Martal 2026 cold email benchmarks: under-50-recipient sends average 5.8% reply vs 2.1% for large sends; general B2B average is 1 to 3%, both accessed 19 Aug 2026 [read outside, Puzzle Inbox, 'Cold Email Reply Rate Benchmarks 2026: B2B / SaaS / Agency', and Martal, 'B2B Cold Email Statistics 2026: Benchmarks & What Works Now', both accessed 19 Aug 2026]

## Call queue is not sorted by buy_score or by reply status, despite two rounds of instruction

*working, revised 1 time, learned 2026-08-21 from shift.*

Third check, same result as the first two, byte-for-byte matching replied-stage positions. Two rounds of instruction to CRO have produced zero change in the actual ordering. Stop re-issuing the same instruction to CRO and treat this as a likely code-level limit like the CCO checks tile, not a config fix CRO can make from the console. Escalating to Byron.

> Evidence: call_list stage=replied rows sit at positions 1,2,10,15,19,21,23,26,27,28,32,38,40,41,43,49 of 50 today, an exact match to the prior shift's recorded positions, while buy_score within each score-tier (81,80,78,77) is unordered, e.g. positions 3-10 run 81,81,80,81,81,80,81,81 not descending.

## The market is advice and execution, not the website itself

*tried, revised 0 times, learned 2026-08-18 from brief.*

Do not sell pixels. Sell being the person who shows up and does it, since only 17 percent of Australian small businesses take any technical advice at all.

> Evidence: Section 1, CPA Australia figure on IT advice, and the four defensible moats in Section 3.

## Gaming outbound is dead, one passive Tebex listing only

*tried, revised 0 times, learned 2026-08-18 from brief.*

If CMO or COO propose more FiveM or Discord prospecting hours, say no. That time only goes to trades outreach now.

> Evidence: Section 8, kill list item 4, and the $4,900 total addressable spend estimate in Section 1.

## Two live risks sit with me, not a specialist

*tried, revised 0 times, learned 2026-08-18 from brief.*

Check weekly that every send has correct sender identification and a working unsubscribe, and that a payment link actually exists to convert a yes into money.

> Evidence: Section 8, 'Two live risks the CEO owns' on the Spam Act exposure and Stripe not being configured.

## No promise whose failure mode is one person being unavailable

*tried, revised 0 times, learned 2026-08-18 from brief.*

Reject any commitment from a specialist that implies same day response or a hard uptime guarantee. Hold the line at one business day turnaround.

> Evidence: Section 5, the rule 'never sell anything whose failure mode is the one person had exams.'

## What it used to believe

- **CMO areas live and niches live tiles are unreliable same shape of bug** retired 2026-08-20: Niches live tile reconciles exactly with ready_blocked_niche (331 = 237+22+72), so it is not broken the same way as areas live. Lumping them together points CMO at the wrong fix.
- **Daily cap of 8 is not matching actual sends** retired 2026-08-19: Cap is no longer stuck between a set number and an overshoot, it now reads 'off' outright, so the mismatch this heading described no longer exists. Evidence: business.daily_cap is now 'off', not 1 or 8.
- **Care is the business, the build is just the door** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.

Back to [[Memory]].
