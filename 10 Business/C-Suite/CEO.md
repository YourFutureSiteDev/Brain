---
title: "CEO"
source: yfs-console
kind: role
tags: [business, c-suite]
updated: 2026-08-19T09:53:05
role: "ceo"
---


# CEO

*Is this working, and what needs deciding?*

Where it stands right now.

> 144 emailed, 2 replies, too few replies to read a pattern. Sending is on.

| | | |
|---|---|---|
| Won | **$0** | 0 paid |
| In play | **$142,500** | 137 live |
| Emailed | **144** | all time |
| Replies | **2** | 1.4% |
| To call | **50** | queued now |
| Leads known | **22503** | researched |

## Needs a decision

- **50 calls waiting.** Follow-up calls are the highest converting thing available and only you can make them.

## Learned

- 2026-08-19 UNKNOWN status leads never route to call list or get emailed and sit stuck at stage found, confirmed across three shifts now. CDO's tile frames the no-email part as working as intended, but that doesn't cover why UNKNOWN leads with a phone number don't reach the call list either. This is a code fix to the call list and email queries, not a desk lever, same shape as the CCO checks-passing tile bug and the CMO areas live and niches live tile bug.
- 2026-08-19 UNKNOWN status leads never route to call list or get emailed, stuck at stage found. Confirmed three shifts running. This is a call list query bug, not a data quality gap, and needs Claude/code, not a desk lever. COO checked this shift per Byron, no fix reported yet.
- 2026-08-19 CMO areas live and niches live tiles reading wrong is the same dashboard bug shape as CCO checks-passing, third time this pattern has been logged. Needs a code fix, not a desk lever, since ready_by_niche data underneath is fine.
- 2026-08-19 CMO areas live and niches live tiles are unreliable, same shape of bug as the CCO checks-passing tile. Niches live showed 2 while ready_by_niche had live data for 4 niches (pro, beauty, trades, food) with no logged config change. Treat ready_by_niche as the trustworthy source until the tile is fixed. This is a code fix, not a desk lever.
- 2026-08-18 CMO's sweep is area based (osm:<suburb>) per niche, not trade-keyword based. Requests like 'add concreters as a search term' don't map to a real lever, that trade is already covered under trades niche once the bot runs. Frame future asks about sub-trade coverage this way.

## Decided

- 2026-08-19 asked: A task from the handover list. Do it if you can. Title: [Data lead] UNKNOWN leads may be -> This is the same UNKNOWN-routing gap flagged the last three shifts, and it's not something any desk can fix with their l
- 2026-08-19 asked: A task from the handover list. Do it if you can. Title: [CRO] Call from the ranked queue, -> CRO owns the call queue ordering, so I've sent this to them. The fix is queue discipline: the top of call_list by buy_sc
- 2026-08-19 CRO tasked with enforcing ranked top to bottom order on the call queue. Actual calling stays with Byron. Next call should be Damien Seton Mechanical, 0404 977 607.
- 2026-08-19 asked: A task from the handover list. Do it if you can. Title: [Data lead] UNKNOWN leads may be -> Three from the handover list, quick rundown. CMO tile bug: same read as before, this is a dashboard code problem not a
- 2026-08-19 CRO instructed to work call_list top to bottom by buy_score going forward, not ad hoc. Actual dialing stays with Byron.
- 2026-08-19 asked: A task from the handover list. Do it if you can. Title: [CRO] Call from the ranked queue, -> Two tasks. First, CMO tiles: this is the same dashboard bug already flagged against CCO's checks-passing tile, areas liv
- 2026-08-19 asked: A task from the handover list. Do it if you can. Title: [CMO] CMO sweep tiles (niches liv -> This one is a dashboard bug, not a sweep change. Ready_by_niche still shows live data for 4 niches, pro 8, beauty 60, tr
- 2026-08-19 asked: A task from the handover list. Do it if you can. Title: [Data lead] UNKNOWN leads may be -> handed to CFO
- 2026-08-19 asked: A task from the handover list. Do it if you can. Title: [CRO] Call from the ranked queue, -> handed to CMO
- 2026-08-19 asked: A task from the handover list. Do it if you can. Title: [CMO] CMO sweep tiles (niches liv -> handed to CMO
- 2026-08-19 asked: and change the 1,500 to 1,000 dollars -> CFO flagged the remake price is already sitting at $3, so that instruction was already current, nothing to redo there. N
- 2026-08-19 New website price moved from $1500 to $1000 AUD, per Byron on 2026-08-19. Remake price confirmed still at $3.

## Noticed

- 2026-08-19 8 calls made so far went to leads outside the top 50 ranked call_list (Windsor NSW, Tamworth chainsaw shop) instead of top buy_score leads like Damien Seton Mechanical (95, Dubbo, already opened demo). Queue was not being worked top to bottom.
- 2026-08-19 CMO tile bug (areas live, niches live) confirmed same shape as CCO checks-passing tile bug. Both are dashboard read issues, not fixable by any desk lever. Needs Claude to check the query behind these tiles.
- 2026-08-19 CRO's first 8 calls were made outside the ranked call_list top 50, missing top buy_score leads like Damien Seton Mechanical (95). Sent CRO the instruction to work the list top down from here.
- 2026-08-19 Read outside on what reply rate should a small cold email business expect, and does targeting size change it (B2B cold email benchmarks 2026): Industry benchmark for 2026 puts typical B2B cold email reply rates at 1 to 3 percent, with 4 to 8 percent being strong. Our 2 replies from 143 emails (1.4 percent) sits at the low end of average, not a broken campaign. The sharper number: campaigns sent to under 50 recipients at a time average a 5.8 percent reply rate versus 2.1 percent for large blasts, because the list is tighter to one audience. (source: Puzzle Inbox, 'Cold Email Reply Rate Benchmarks 2026: B2B / SaaS / Agency', and Martal, 'B2B Cold Email Statistics 2026: Benchmarks & What Works Now', both accessed 19 Aug 2026)
- 2026-08-18 Read outside on what regional Australian freelancers and small agencies actually charge for a small business website in 2026: Market floor is well above our prices. Local Australian freelancers run $1,500 to $2,500 and up per project, small agencies start at $3,000 to $7,000, and small business websites average $5,000 to $10,000. Even the cheapest local freelancer segment sits at $500 to $2,000 for a basic build. We charge $500 for a remake and $1,000 for a new build, below even the bottom of the freelancer range. (source: Rockingweb 'Website Costs Australia 2026' and Spark Interact 'Web Designers Cost: Australia Pricing (2026 Guide)', both accessed 18 Aug 2026)
- 2026-08-18 Byron asked to start the bot again on 2026-08-18, following up on the concreters/builders/landscapers request. Bot was stopped at 11:50 that day.
- 2026-08-18 2026-08-18: bot_running was false through this whole exchange. Zero new leads found in the 5 minutes Byron asked about, purely because the bot was off, unrelated to the concreters/landscapers search term question.
- 2026-08-18 Trades niche sample (50 of 364 queued) skews heavily to auto/mechanical repair, then plumbing, then a long tail of builders, carpenters, electricians, HVAC, appliance repair, pool builders, cabinet makers, welders.

## Recently did

- 2026-08-19 answered you: This is the same UNKNOWN-routing gap flagged the last three shifts, and it's not something any desk can fix with their levers. The CDO tile calls it working as
- 2026-08-19 answered you: CRO owns the call queue ordering, so I've sent this to them. The fix is queue discipline: the top of call_list by buy_score is Damien Seton Mechanical in Dubbo,
- 2026-08-19 handed a job to CRO: Enforce that the call queue is worked strictly top to bottom by buy_score, not by whatever lead happens to surface. Confirm the ranked order
- 2026-08-19 answered you: Three from the handover list, quick rundown. CMO tile bug: same read as before, this is a dashboard code problem not a CMO lever. Areas live and niches live fl
- 2026-08-19 handed a job to CRO: Work the call_list in buy_score order, top to bottom, not wherever a lead surfaces. Top of list right now: Damien Seton Mechanical, Dubbo NS
- 2026-08-19 answered you: Two tasks. First, CMO tiles: this is the same dashboard bug already flagged against CCO's checks-passing tile, areas live and niches live are reading wrong whil
- 2026-08-19 handed a job to CRO: Reorder how the call queue is worked: pull from call_list top to bottom by buy_score, not ad hoc. Damien Seton Mechanical (Dubbo, score 95,
- 2026-08-19 answered you: handed to CFO
- 2026-08-19 answered you: handed to CMO
- 2026-08-19 answered you: This one is a dashboard bug, not a sweep change. Ready_by_niche still shows live data for 4 niches, pro 8, beauty 60, trades 31, food 11, but the CMO tile says
- 2026-08-19 handed a job to CMO: Do not act on the areas live or niches live tiles until they are fixed, they are known unreliable. Confirm from the actual sweep config, not
- 2026-08-19 answered you: handed to CFO

---

Back to [[C-Suite]]. Written by the Your Future Site console on the VPS, 2026-08-19T09:53:05. Edit it here and the next cycle overwrites you, so put your own thinking in a note of your own and link it.
