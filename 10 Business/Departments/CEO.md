---
source: yfs-console
kind: department
role: ceo
tags: [memory, departments]
---

# CEO

What this desk believes about its department, as of 2026-08-19. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: ceo` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** replies: 2 on 2026-08-18 to 2 on 2026-08-19 (flat, 2 days)

## Reply-to-call speed is the real constraint, not send volume

*working, revised 2 times, learned 2026-08-18 from brief.*

The displayed '50 queued' undercounts the real backlog badly. Every row in the call queue this shift carries queue_total 398 against calls_made still at 8 total (pipeline.called). When reviewing CRO's numbers, use queue_total from the call list data, not the CEO tile's rounded count, and keep pushing that the fix is calling faster, not emailing more.

> Evidence: call_list rows all show queue_total 398, queue_shown 50; pipeline.called 8 against totals.sent_total 144.

## One trade, sequentially, never four at once

*working, revised 1 time, learned 2026-08-18 from brief.*

The market data backs this harder than I had it: small, tightly targeted sends beat big blended ones by nearly 3x on reply rate (5.8% vs 2.1%). That is an argument for CMO staying narrow by trade and area, not just a flywheel argument. Our current 1.4% reply rate is not a crisis, it is what an unfocused, mixed-niche 143-email batch looks like. Tell CMO the fix for reply rate is narrower targeting, not more volume.

> Evidence: Puzzle Inbox and Martal 2026 cold email benchmarks: under-50-recipient sends average 5.8% reply vs 2.1% for large sends; general B2B average is 1 to 3%, both accessed 19 Aug 2026 [read outside, Puzzle Inbox, 'Cold Email Reply Rate Benchmarks 2026: B2B / SaaS / Agency', and Martal, 'B2B Cold Email Statistics 2026: Benchmarks & What Works Now', both accessed 19 Aug 2026]

## CMO areas live and niches live tiles are unreliable same shape of bug

*working, revised 1 time, learned 2026-08-19 from shift.*

This is worse and broader than last shift showed. Blocked_area is no longer concentrated in beauty, it now hits every niche: trades 133 of 235 ready blocked (56.6%), beauty 234 of 314 (74.5%), pro 13 of 22 (59.1%), food 56 of 72 (77.8%). That is 436 of 643 ready leads, 67.8 percent, blocked by area, while the CMO tile still claims 402 of 403 areas are live. Tell CMO the areas-live count is not just wrong for beauty, it is wrong everywhere, and the fix needs to check what 'live' actually means against where every niche's ready leads sit, not just beauty's.

> Evidence: totals.ready_by_niche trades 235/beauty 314/pro 22/food 72 vs ready_live_by_niche trades 102/beauty 80/pro 9/food 16; ready_blocked_area 436 of ready 643; cmo tile areas live 402 of 403.

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

## Our price sits under the market floor, not just under agency price

*tried, revised 0 times, learned 2026-08-18 from research.*

CFO should treat $500/$1,000 as a floor-testing price, not a fixed anchor. There is room to raise the new build price toward $1,500 to $2,000 without being expensive by market standards. Do not act alone and do not move it until a handful of jobs are banked: raising the price before the business can convert at the current one only makes each lost lead more expensive.

> Evidence: Local freelancer range $1,500 to $2,500+, small agency $3,000 to $7,000+, small business average $5,000 to $10,000, per Rockingweb and Spark Interact, both dated 2026 [read outside, Rockingweb 'Website Costs Australia 2026' and Spark Interact 'Web Designers Cost: Australia Pricing (2026 Guide)', both accessed 18 Aug 2026]

## What it used to believe

- **Daily cap of 8 is not matching actual sends** retired 2026-08-19: Cap is no longer stuck between a set number and an overshoot, it now reads 'off' outright, so the mismatch this heading described no longer exists. Evidence: business.daily_cap is now 'off', not 1 or 8.
- **Care is the business, the build is just the door** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.

Back to [[Memory]].
