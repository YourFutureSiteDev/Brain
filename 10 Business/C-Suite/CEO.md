---
title: "CEO"
source: yfs-console
kind: role
tags: [business, c-suite]
updated: 2026-08-22T11:06:34
role: "ceo"
---


# CEO

*Is this working, and what needs deciding?*

Where it stands right now.

> 274 emailed, 3 replies, too few replies to read a pattern. Sending is on.

| | | |
|---|---|---|
| Won | **$0** | 0 paid |
| In play | **$443,000** | 412 live |
| Emailed | **274** | all time |
| Replies | **3** | 1.1% |
| To call | **50** | queued now |
| Leads known | **27896** | researched |

## Needs a decision

- **50 calls waiting.** Follow-up calls are the highest converting thing available and only you can make them.

## Learned

- 2026-08-21 Messaging replies about fifteen times better than email. 581 leads messaged returned 75 replies at 12.9 percent; 239 emailed returned 2 at 0.84 percent. So any reply rate computed across both channels is mostly reporting which channel that group happened to get, not how good the leads were. Two decisions have already been made on such a figure: the 19 Aug order to aim the scraping at trades cited 24 percent, and a call queue directive cited beauty at 28. Neither survives the split. Before believing a reply rate, ask which channel it came from.
- 2026-08-19 UNKNOWN status leads never route to call list or get emailed and sit stuck at stage found, confirmed across three shifts now. CDO's tile frames the no-email part as working as intended, but that doesn't cover why UNKNOWN leads with a phone number don't reach the call list either. This is a code fix to the call list and email queries, not a desk lever, same shape as the CCO checks-passing tile bug and the CMO areas live and niches live tile bug.
- 2026-08-19 UNKNOWN status leads never route to call list or get emailed, stuck at stage found. Confirmed three shifts running. This is a call list query bug, not a data quality gap, and needs Claude/code, not a desk lever. COO checked this shift per Byron, no fix reported yet.
- 2026-08-19 CMO areas live and niches live tiles reading wrong is the same dashboard bug shape as CCO checks-passing, third time this pattern has been logged. Needs a code fix, not a desk lever, since ready_by_niche data underneath is fine.
- 2026-08-19 CMO areas live and niches live tiles are unreliable, same shape of bug as the CCO checks-passing tile. Niches live showed 2 while ready_by_niche had live data for 4 niches (pro, beauty, trades, food) with no logged config change. Treat ready_by_niche as the trustworthy source until the tile is fixed. This is a code fix, not a desk lever.
- 2026-08-18 CMO's sweep is area based (osm:<suburb>) per niche, not trade-keyword based. Requests like 'add concreters as a search term' don't map to a real lever, that trade is already covered under trades niche once the bot runs. Frame future asks about sub-trade coverage this way.

## Decided

- 2026-08-22 asked: [from CRO, on shift] You've now put three different call-queue orderings in play: Byron's -> handed to CMO
- 2026-08-22 messages report: Reply rate roughly quadrupled between the 14th and the 20th, from 8% to 41%, and trades an -> fix: The plain website line is carrying the whole board at 40 percent while every other variant drags the average down, so th
- 2026-08-21 asked: [from CRO, on shift] Withdraw the beauty-repliers-first call order rule or say explicitly -> handed to CMO
- 2026-08-21 asked: [from CRO, on shift] The beauty-repliers-first sort rule you issued and Byron's repeated t -> handed to CMO
- 2026-08-21 messages report: Beauty is carrying the board at 24% replies while food drags at 8%, and reply rate is tren -> fix: Reorder the call queue so beauty repliers are called first, since beauty replies at 24 percent against trades 13 percent
- 2026-08-20 messages report: Reply rate is trending up on the days old enough to judge, and one message wording is doin -> fix: Kill the menu specific text for food and pro leads and replace it everywhere with the original line, since it sits at 8
- 2026-08-19 messages report: Beauty and the plain 'see your work' text are carrying every reply that matters, food is d -> fix: Reorder the call queue so beauty and trades repliers get called before food and pro repliers, since beauty replies at 28
- 2026-08-19 asked: A task from the handover list. Do it if you can. Title: [Data lead] UNKNOWN leads may be -> This is the same UNKNOWN-routing gap flagged the last three shifts, and it's not something any desk can fix with their l
- 2026-08-19 asked: A task from the handover list. Do it if you can. Title: [CRO] Call from the ranked queue, -> CRO owns the call queue ordering, so I've sent this to them. The fix is queue discipline: the top of call_list by buy_sc
- 2026-08-19 CRO tasked with enforcing ranked top to bottom order on the call queue. Actual calling stays with Byron. Next call should be Damien Seton Mechanical, 0404 977 607.
- 2026-08-19 asked: A task from the handover list. Do it if you can. Title: [Data lead] UNKNOWN leads may be -> Three from the handover list, quick rundown. CMO tile bug: same read as before, this is a dashboard code problem not a
- 2026-08-19 CRO instructed to work call_list top to bottom by buy_score going forward, not ad hoc. Actual dialing stays with Byron.

## Noticed

- 2026-08-22 Read outside on what do regional Australian small business websites actually cost from the broader market, not just the two free-mockup competitors already on file: Multiple 2026 pricing guides put a professional small business website in Australia at $5,000 to $10,000, with regional freelancers charging $50 to $100 an hour and pricing 20 to 40 percent below Sydney and Melbourne agencies. Our newbuild at $1,500 sits at roughly a fifth to a tenth of that regional floor, not just under the two mockup-tactic operators already noted. (source: Aggregated from sparkinteract.com.au, keentodesign.com.au, rockingweb.com.au and paramark.com.au 2026 web design cost guides, search run 22 Aug 2026)
- 2026-08-21 Read outside on Is WebBuild Australia a one-off outlier, or do other web design sellers in Australia use the same free-mockup, pay-only-if-you-like-it tactic aimed at small service businesses, and at what price?: Found a second real competitor running the identical tactic: Web Panther (Sydney), targeting the same customer we do, service-based small business owners. Their hook is a free custom mockup, explicitly anchored at 'Worth $1,200', with no obligation to buy. No paid price is published on the page, it converts to a custom quote after the mockup lands. Unlike WebBuild, this is inbound (a landing page people find), not unsolicited cold outreach, so it does not compete with us on delivery speed the same way. It does confirm the free-mockup tactic itself is now a recognised pattern in this market, not one operator's trick, and shows a second data point on how that mockup gets priced in
- 2026-08-20 Read outside on who else in Australia runs the exact same play, an unsolicited free mockup with pay-only-if-you-like-it, and what do they charge: Found a direct same-tactic competitor: WebBuild Australia, Melbourne-based. Their offer is word for word the same model we run: 'Free Website Mockup. Pay Only If You Love It,' mockup delivered in 24 to 48 hours, no cost if you walk away. Current price is a 'Flash Sale, 48 hrs only' Starter package at $248 AUD, marked down from $600, capped at the first 10 customers. Delivery is inside 48 hours. (source: webbuildaustralia.com, fetched 20 Aug 2026)
- 2026-08-19 8 calls made so far went to leads outside the top 50 ranked call_list (Windsor NSW, Tamworth chainsaw shop) instead of top buy_score leads like Damien Seton Mechanical (95, Dubbo, already opened demo). Queue was not being worked top to bottom.
- 2026-08-19 CMO tile bug (areas live, niches live) confirmed same shape as CCO checks-passing tile bug. Both are dashboard read issues, not fixable by any desk lever. Needs Claude to check the query behind these tiles.
- 2026-08-19 CRO's first 8 calls were made outside the ranked call_list top 50, missing top buy_score leads like Damien Seton Mechanical (95). Sent CRO the instruction to work the list top down from here.
- 2026-08-19 Read outside on what reply rate should a small cold email business expect, and does targeting size change it (B2B cold email benchmarks 2026): Industry benchmark for 2026 puts typical B2B cold email reply rates at 1 to 3 percent, with 4 to 8 percent being strong. Our 2 replies from 143 emails (1.4 percent) sits at the low end of average, not a broken campaign. The sharper number: campaigns sent to under 50 recipients at a time average a 5.8 percent reply rate versus 2.1 percent for large blasts, because the list is tighter to one audience. (source: Puzzle Inbox, 'Cold Email Reply Rate Benchmarks 2026: B2B / SaaS / Agency', and Martal, 'B2B Cold Email Statistics 2026: Benchmarks & What Works Now', both accessed 19 Aug 2026)
- 2026-08-18 Read outside on what regional Australian freelancers and small agencies actually charge for a small business website in 2026: Market floor is well above our prices. Local Australian freelancers run $1,500 to $2,500 and up per project, small agencies start at $3,000 to $7,000, and small business websites average $5,000 to $10,000. Even the cheapest local freelancer segment sits at $500 to $2,000 for a basic build. We charge $500 for a remake and $1,000 for a new build, below even the bottom of the freelancer range. (source: Rockingweb 'Website Costs Australia 2026' and Spark Interact 'Web Designers Cost: Australia Pricing (2026 Guide)', both accessed 18 Aug 2026)

## Recently did

- 2026-08-22 answered you: handed to CMO
- 2026-08-22 sent a fix to the CRO: The plain website line is carrying the whole board at 40 percent while every other variant drags the average down, so the fix is to make follow up ordering on repliers who got a non plain variant the top priority this week, since they replied despite a weaker message and are the likeliest to convert
- 2026-08-22 worked a shift: Rechecked queue_total growth against the last shift's recorded 1904 and found it barely moved to 1909 (+5), a sharp slowdown from the earlier 398 to 1764 jump, while pipeline.called is still stuck at exactly 8. Also confirmed the call queue sort is still unchanged on a fourth check, so I'm putting t
- 2026-08-22 read outside the building: what do regional Australian small business websites actually cost from the broader market, not just the two free-mockup competitors already on file: Multiple 2026 pricing guides put a professional small business website in Australia at $5,000 to $10,000, with regional freelancers charging $50 to $10
- 2026-08-21 worked a shift: Recomputed the 50-row call queue against the buy_score and reply-first sort instructions for the third time: replied-stage leads still sit scattered at positions 1,2,10,15,19,21,23,26,27,28,32,38,40,41,43,49, identical pattern to the last two checks, while queue_total kept growing (1764 to 1904) and
- 2026-08-21 answered you: handed to CMO
- 2026-08-21 worked a shift: Rechecked whether the 50-row call queue is finally sorted (it is not: stage=replied leads sit at positions 1,2,10,15,19,21,23,26,27,28,32,38,40,41,43,49 of 50, still scattered, third check running) and recompared the three reply counts against today's snapshot.
- 2026-08-21 worked a shift: Recomputed CMO's ready vs ready_live by niche against the last two shifts and rechecked whether the 50 row call queue is finally sorted by buy_score or reply stage after two prior rounds of instruction to CRO.
- 2026-08-21 answered you: handed to CMO
- 2026-08-21 worked a shift: Checked the 50-row call queue against the two standing sort instructions (buy_score top-to-bottom, repliers-first) instead of just noting them as open, and confirmed neither is applied in the live data.
- 2026-08-21 worked a shift: Rechecked the CEO reply numbers against the full business object rather than just the call_list sample, and found a third reply count I had not seen before, totals.replies_all=90, sitting alongside totals.replies=2 and pipeline.replied=76.
- 2026-08-21 sent a fix to the CRO: Reorder the call queue so beauty repliers are called first, since beauty replies at 24 percent against trades 13 percent and food 8 percent, meaning beauty repliers are the highest value leads sitting in the queue right now.

---

Back to [[C-Suite]]. Written by the Your Future Site console on the VPS, 2026-08-22T11:06:34. Edit it here and the next cycle overwrites you, so put your own thinking in a note of your own and link it.
