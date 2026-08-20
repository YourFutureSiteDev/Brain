---
title: "CRO"
source: yfs-console
kind: role
tags: [business, c-suite]
updated: 2026-08-21T04:39:33
role: "cro"
---


# CRO

*Where does the pipeline stall?*

Where it stands right now.

> 50 in the call queue; chasing at 11 days

| | | |
|---|---|---|
| Emailed | **225** | businesses |
| Replied | **2** | 0.9% |
| Called | **8** | at least once |
| Won | **0** | paid |

## Needs a decision

- **50 follow-up calls queued.** A call two or three days after a mockup lands is a different conversation from a cold call. This is where the pipeline moves.

## Carrying for Byron

- 2026-08-20 [morning meeting, from CFO] Push some of the 50 queued follow-up calls to an actual close so pricing can be checked against a real paid job instead of pipeline value. *(working)*
- 2026-08-19 Enforce that the call queue is worked strictly top to bottom by buy_score, not by whatever lead happens to surface. Confirm the ranked order Damien Seton Mechanical (95) then GP Mechanical Nambour (78) then Whitten's Plumbing Warragul (78) is what gets presented next, and flag if anything in the call flow lets a lead outside the top 50 jump the queue. *(working)*
- 2026-08-19 Work the call_list in buy_score order, top to bottom, not wherever a lead surfaces. Top of list right now: Damien Seton Mechanical, Dubbo NSW, score 95, already opened the demo. Then GP Mechanical Repairs (Nambour QLD, 78) and Whitten's Plumbing (Warragul VIC, 78). Flag it if the queue view isn't sorted by buy_score by default, that would explain why the last 8 calls went to Windsor and Tamworth instead of the top of the list. *(working)*
- 2026-08-19 Reorder how the call queue is worked: pull from call_list top to bottom by buy_score, not ad hoc. Damien Seton Mechanical (Dubbo, score 95, already opened the demo) goes first, then the 77 to 78 scored trades and beauty leads below it. The two calls already made outside this order (Windsor NSW, Tamworth chainsaw shop) stay logged as made, just don't keep pulling from outside the ranked 50. *(working)*
- 2026-08-17 From the vault, The CRO now has its own specialists: You have specialists now. 14 of them, in sales (9), product (5), sitting in `~/.claude/agents` on this box. They came from [[The agency agents roster]], which is where the full list and the other desks' shares are. Yours, and what each is for: - `sales-pipeline-analyst` - where deals die, by stage - `sales-outbound-strategist` - the outbound motion itself - `sales-discovery-coach` - the call after the mockup lands - `sales-deal-strategist` - one deal, worked properly - `sales-proposal-strategist` - the quote that follows a yes - `sales-offer-lead-gen-strategist` - what the offer should be - `sales-account-strategist` - the accounts worth keeping - `sales-coach` - how the calls are being run - `sales-engineer` - the technical half of a sale - `sales-outreach` - first contact, written - `sales-data-extraction-agent` - pulling structure out of a prospect's own site - `product-behavioral-nudge-engine` - the behavioural science of why people drop off - `product-feedback-synthesizer` - what the replies are actually saying - `customer-success-manager` - keeping the ones who bought Fifty follow-up calls are queued and no email has been replied to yet. `sales-pipeline-analyst` and `product- *(working)*
- 2026-08-13 Set up a fast way for Byron to log call outcome (answered, no answer, not interested, call back, quoted, won) against each lead right after he calls, so conversion by niche and area becomes visible instead of guessed. *(working)*
- 2026-08-13 Keep the call queue ordered with no-website (rank 3, no_site bucket) leads first. They're the top-priority calls and currently fill 11 of the 14 slots. *(working)*

## What it has tuned

| Setting | Now | Why |
|---|---|---|
| chase_days | 11 | you asked: Once Byron starts working the 50 queued calls, track call outcomes against niche |

## Learned

- 2026-08-13 chase_days: default -> 11. you asked: Once Byron starts working the 50 queued calls, track call outcomes against niche
- 2026-08-12 chase_days: 8.0 -> 7. you asked: Flag anything quiet for 7 days
- 2026-08-12 chase_days: 11.0 -> 8. you asked: Nobody is replying
- 2026-08-12 chase_days: default -> 11. you asked: Chase silent leads sooner

## Decided

- 2026-08-20 asked: [morning meeting, from CFO] Push some of the 50 queued follow-up calls to an actual close -> No lever of mine moves this one. What I control is: change how many silent days before a lead is flagged for a call; pus
- 2026-08-19 asked: Enforce that the call queue is worked strictly top to bottom by buy_score, not by whatever -> No lever of mine moves this one. What I control is: change how many silent days before a lead is flagged for a call; pus
- 2026-08-19 asked: Work the call_list in buy_score order, top to bottom, not wherever a lead surfaces. Top of -> No lever of mine moves this one. What I control is: change how many silent days before a lead is flagged for a call; pus
- 2026-08-19 asked: Reorder how the call queue is worked: pull from call_list top to bottom by buy_score, not -> No lever of mine moves this one. What I control is: change how many silent days before a lead is flagged for a call; pus
- 2026-08-17 asked: From the vault, The CRO now has its own specialists: You have specialists now. 14 of them, -> No lever of mine moves this one. What I control is: change how many silent days before a lead is flagged for a call; pus
- 2026-08-15 asked: From the vault, Every desk should be able to say what it delivers: I have kept a note in t -> No lever of mine moves this one. What I control is: change how many silent days before a lead is flagged for a call; pus
- 2026-08-13 asked: make sure the sites that cant be confirmed are still being sent emails or added to the cal -> No lever of mine moves this one. What I control is: change how many silent days before a lead is flagged for a call; pus
- 2026-08-13 asked: do you want to start recording the calls for you so you can -> Emailed 15, Replied 0, Called 0, Won 0. No replies from any email yet: Either the message is not landing or the leads ar
- 2026-08-13 asked: Set up a fast way for Byron to log call outcome (answered, no answer, not interested, call -> No lever of mine moves this one. What I control is: change how many silent days before a lead is flagged for a call; pus
- 2026-08-13 asked: Once Byron starts working the 50 queued calls, track call outcomes against niche and area -> chasing sooner: 14 silent days down to 11. nothing is stalled past that yet.
- 2026-08-13 asked: Keep the call queue ordered with no-website (rank 3, no_site bucket) leads first. They're -> No lever of mine moves this one. What I control is: change how many silent days before a lead is flagged for a call; pus
- 2026-08-12 asked: We need more leads in the pipeline -> Noted and standing. I cannot do this directly - what I control is: change how many silent days before a lead is flagged

## Noticed

- 2026-08-21 Read outside on how many times should a lead be called before moving on, and when do call attempts stop paying off: Cognism's 2025 State of Cold Calling Report: on average it takes 3 attempts to connect with a lead, 93 percent of all connects happen by the third call, and 98 percent happen by the fifth. Calls beyond the fifth attempt are effectively wasted. (source: Cognism 'B2B Cold Calling Statistics' (cognism.com), citing its 2025 State of Cold Calling Report, cross-referenced with RAIN Group Top Performance in Sales Prospecting Benchmark Report)
- 2026-08-20 Read outside on when a small business owner cold called about a website says no, what is the actual objection and is there a solid rebuttal that fits a one person, no-ad-spend business: The most common no is not price, it is 'I already get enough work from word of mouth or my Facebook page, I don't need a website.' The specific counter that holds up: Facebook pages do not show up when someone searches Google for the trade plus suburb, and the business does not own that page, Meta controls who sees it and organic reach on it has been falling for years. A website is not a replacement for word of mouth or Facebook, it is what confirms the business is legitimate once someone has heard the name and gone looking. (source: Buildify NZ 'Do Tradies Need a Website in 2026' (buildifysites.co.nz) and Groundwork Digital 'Do Tradies Need a Website' (groundworkdigital.co.nz), both 2026)
- 2026-08-19 Read outside on When a cold call to an Australian small business owner's mobile goes unanswered, do they actually check the voicemail, or is leaving one a wasted 20 seconds: 81 percent of calls from unknown numbers go to voicemail rather than being answered, but 67 percent of people still check a voicemail left by an unknown number. Voicemail-to-conversation conversion sits at 4 to 11 percent for Australian small business calls, and industry missed-call rate for Aussie small business runs 22 to 47 percent. So most of the 47 cold-open calls in today's queue will not be answered live, but a real majority of those will still be heard. (source: Aussie AI Agency, 'Missed Call Statistics Australia 2026' (aussieaiagency.com.au), cross-checked against CloudTalk 'Cold Calling Statistics 2026' and Scrap.io 'Cold Calling Success Rate in 2026: 200K+ Calls Analyzed')
- 2026-08-18 Read outside on What time of day gets the highest answer rate when cold calling small business owners like tradies, beauty and food operators: US sales-call data across several 2026 studies converge on the same window: best connect rates are 9 to 10am and 3 to 4pm, Tuesday through Thursday. Calls made 12 to 2pm see about a 35 percent drop in answers because owner-operators are on lunch or with a client. Calls before 8am or after 6pm mostly miss. Monday connect rates run about 21 percent below midweek. (source: Close.com 'Best Days & Times to Cold Call (Data-Backed) in 2026'; PhoneBurner data cited via Revenue.io 'Best Time to Cold Call Prospects in 2026')
- 2026-08-16 Standing contract, set 16 Aug 2026: from the Analyst, and from the Hook Writer until the message has a desk of its own. Delivers: leads actually moving toward a paid job, and an opener worth answering. Steps: track, analyse, learn, optimise; and draft, cut, hand off. Ratio: 80 emailed, 0 replied, 50 in the call queue, 0 won; and the hook writer's 10 written, 3 survive, 1 sends, against our 1 written, 1 sent. Now: 50 waiting to be called, one opener, never tested.
- 2026-08-15 the weekly pass left chase_days where it is: Queue has held flat at 50 for three straight days at 11 days and Byron still has not worked through it, so cutting the chase window further only piles more calls onto a queue that is not moving.

## Recently did

- 2026-08-21 worked a shift: Checked the open instructions sitting with this desk against today's call_list rows: the CEO's new rule (sort beauty repliers before trades, food or pro repliers, regardless of order) directly conflicts with Byron's repeated instruction to work strictly top to bottom by buy_score with Damien Seton M
- 2026-08-21 read outside the building: how many times should a lead be called before moving on, and when do call attempts stop paying off: Cognism's 2025 State of Cold Calling Report: on average it takes 3 attempts to connect with a lead, 93 percent of all connects happen by the third call, and 98 percent happen by the fifth. Calls beyon
- 2026-08-20 worked a shift: Cross-checked queue_total against the last three shift readings and pipeline.called: the flat trickle broke today, queue_total jumped from 1769 to 1814 (+45, no_site bucket 1297 to 1342), driven by new hotfrog:pest control directory-sweep leads landing this afternoon (Macca's Pumps, Matty's Window T
- 2026-08-20 worked a shift: Rechecked the 50-item call queue against buy_score order and against call activity for a third straight shift: the interleaved-score break past position 1 is byte-identical to the last two readings, and all 50 rows still show calls_made 0 and last_call null while pipeline.called stays at 8.
- 2026-08-20 worked a shift: Re-checked the top 50 call_list against buy_score ordering and re-verified queue_total growth: order is still broken past position 1 in the identical pattern as the last two shifts (95, then 81,81,80,81,81,80,81,81,80,80,78... repeating), and cross-referenced queue_total against the last three readi
- 2026-08-20 answered you: No lever of mine moves this one. What I control is: change how many silent days before a lead is flagged for a call; push stalled leads into the call queue on t
- 2026-08-20 worked a shift: Rechecked today's 50-item call queue against Byron's top-to-bottom buy_score instruction and against the last three shift readings: the interleaved-score break below position 1 is identical to last shift's reading, and calls_made is still 0 with last_call null on all 50 rows.
- 2026-08-20 worked a shift: Cross checked the 50 queued call_list entries against the buy_score order Byron wants enforced, and checked whether call activity moved since the last two readings.
- 2026-08-20 read outside the building: when a small business owner cold called about a website says no, what is the actual objection and is there a solid rebuttal that fits a one person, no-ad-spend business: The most common no is not price, it is 'I already get enough work from word of mouth or my Facebook page, I don't need a website.'
- 2026-08-19 worked a shift: Rechecked the top 50 call_list entries against Byron's repeated instruction to work strictly top to bottom by buy_score, and checked queue growth (1646 to 1760, called still 8, all 50 calls_made 0, last_call null).
- 2026-08-19 worked a shift: Re-checked the 50-name call queue against buy_score ordering and queue_total: ordering still holds (Damien Seton Mechanical 95 on top, the rest 81 down to 77 in order), but queue_total has quadrupled since the last two readings (365 then 398, now 1646), while pipeline.called is still 8 and all 50 sh
- 2026-08-19 worked a shift: Rechecked the call_list top 50 for buy_score ordering and cross-referenced queue_total against last shift's reading: ordering still holds (Damien Seton Mechanical at 95 sits above all 49 no_site leads at 74-78) and calls made is still stuck at pipeline.called=8, but queue_total on every record has m

---

Back to [[C-Suite]]. Written by the Your Future Site console on the VPS, 2026-08-21T04:39:33. Edit it here and the next cycle overwrites you, so put your own thinking in a note of your own and link it.
