---
source: yfs-console
kind: department
role: ceo
tags: [memory, departments]
---

# CEO

What this desk believes about its department, as of 2026-08-20. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: ceo` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** replies: 2 on 2026-08-18 to 2 on 2026-08-20 (flat, 3 days)

## Reply-to-call speed is the real constraint, not send volume

*proven, revised 3 times, learned 2026-08-18 from brief.*

The backlog just went from 398 to 1764 queue_total in one shift, a 4.4x jump, while calls_made is still 8 total and the CEO tile still shows the same '50 queued'. The gap between what's queued and what's actually called is widening fast, not holding steady. Keep using queue_total from call_list data, not the CEO tile's rounded count, and tell CRO to make sure the highest buy_score, buy_ready leads sit at the front of the 50 shown, since Byron can only work through a handful a day and the tile hides how much further behind that puts him.

> Evidence: call_list rows all show queue_total 1764, queue_shown 50, queue_buckets no_site 1292 + no_email 313 + unconfirmed 155 + quiet 3 + clicked 1 = 1764; pipeline.called still 8 against totals.sent_total 178.

## One trade, sequentially, never four at once

*working, revised 1 time, learned 2026-08-18 from brief.*

The market data backs this harder than I had it: small, tightly targeted sends beat big blended ones by nearly 3x on reply rate (5.8% vs 2.1%). That is an argument for CMO staying narrow by trade and area, not just a flywheel argument. Our current 1.4% reply rate is not a crisis, it is what an unfocused, mixed-niche 143-email batch looks like. Tell CMO the fix for reply rate is narrower targeting, not more volume.

> Evidence: Puzzle Inbox and Martal 2026 cold email benchmarks: under-50-recipient sends average 5.8% reply vs 2.1% for large sends; general B2B average is 1 to 3%, both accessed 19 Aug 2026 [read outside, Puzzle Inbox, 'Cold Email Reply Rate Benchmarks 2026: B2B / SaaS / Agency', and Martal, 'B2B Cold Email Statistics 2026: Benchmarks & What Works Now', both accessed 19 Aug 2026]

## Our price sits under the market floor, not just under agency price

*working, revised 1 time, learned 2026-08-18 from research.*

This is not just a general market comparison anymore. There is a real competitor, WebBuild Australia, running our exact tactic, unsolicited mockup then pay only if you like it, at $248 AUD (list $600), turned around in 48 hours. Against the broad freelancer and agency range our $500/$1,500 still looks roomy, but against the one competitor doing precisely what we do, we are not underpriced, we are already at or above their real price and slower to deliver (7 to 14 days versus their 48 hours). CFO should weigh this before nudging price up: the headroom argument still holds against agencies in ge

> Evidence: WebBuild Australia homepage, fetched 20 Aug 2026: 'Free Website Mockup. Pay Only If You Love It', Starter package $248 (was $600, first 10 customers only), delivery 24 to 48 hours. [read outside, webbuildaustralia.com, fetched 20 Aug 2026]

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

## CMO areas live tile is the real bug, niches live tile checks out

*tried, revised 0 times, learned 2026-08-20 from shift.*

Stop treating this as two broken tiles. Niches live is internally consistent: blocked_niche 331 equals trades 237 + pro 22 + food 72 exactly, so niches live=1 (beauty) is telling the truth. The actual bug is areas-live only. Proof: beauty is the one niche already gated live, so its ready leads face no niche confound, yet 234 of its 318 ready leads (73.6%) are still blocked by area while the tile claims 402 of 403 areas are live. Tell CMO to fix what 'live' means against where beauty's own ready leads sit, that is the cleanest test case.

> Evidence: totals.ready_by_niche beauty 318 vs ready_live_by_niche beauty 84 (234 blocked); ready_blocked_niche 331 = trades 237 + pro 22 + food 72; cmo tile areas live 402 of 403, niches live 1 (beauty).

## pipeline.replied and totals.replies disagree by 38x, replied stage looks untrustworthy

*tried, revised 0 times, learned 2026-08-20 from shift.*

Do not read the CEO Replies tile (currently 2, 0.9%) as the true reply picture without CDO confirming what actually sets stage='replied' on a lead. If pipeline's 76 is closer to reality, the whole reply-rate story this fortnight is wrong in the other direction.

> Evidence: business.pipeline.replied=76 vs totals.replies=2 vs totals.replies_all=90; in the 50-row call_list sample, 13 entries carry stage 'replied' (Damien Seton Mechanical, Stoddy's Mobile Mechanical, Kristie's Hair Design, Luke's Mobile Tyre Service, St George's Barber Shop, Shu's Massage, Unique Thai Massage and Men's Waxing, Abaco Car Care, All Aussie Automotive, B&B Produce, Bollon Hardware and Rural

## What it used to believe

- **CMO areas live and niches live tiles are unreliable same shape of bug** retired 2026-08-20: Niches live tile reconciles exactly with ready_blocked_niche (331 = 237+22+72), so it is not broken the same way as areas live. Lumping them together points CMO at the wrong fix.
- **Daily cap of 8 is not matching actual sends** retired 2026-08-19: Cap is no longer stuck between a set number and an overshoot, it now reads 'off' outright, so the mismatch this heading described no longer exists. Evidence: business.daily_cap is now 'off', not 1 or 8.
- **Care is the business, the build is just the door** retired 2026-08-18: Byron, 18 Aug 2026: care plans are not part of this business. They are in the briefs but not in config.json pricing, which sells remake and newbuild only.

Back to [[Memory]].
