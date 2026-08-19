---
source: yfs-console
kind: department
role: cmo
tags: [memory, departments]
---

# CMO

What this desk believes about its department, as of 2026-08-20. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: cmo` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** reply rate %: 1.4 on 2026-08-18 to 1.12 on 2026-08-20 (down, 3 days)

## Food niche has real inventory but is not counted as live

*proven, revised 5 times, learned 2026-08-18 from shift.*

Widen this claim: it is not just food. Pro shows the same pattern. Keep treating niches-live and ready totals as untrustworthy, always hand count the actual call_list. Until CDO or COO trace why ready leads in food and pro never route to the working queue, tell Byron the machine is really only working trades and beauty, whatever the tile says.

> Evidence: Fourth shift in a row hand counting: this shift's 50 row call_list is 29 trades, 21 beauty, 0 food, 0 pro, while ready_by_niche shows food 64 and pro 19 ready, and ready_live_by_niche shows food 15 and pro 9 ready_live. Niches-live tile claims trades, food, beauty, pro all live. None of that food or pro inventory has ever appeared in an actual counted queue across four checks.

## A reply rate this low points at deliverability, not the message

*working, revised 1 time, learned 2026-08-18 from research.*

Add open-rate tracking (a tracking pixel, which most sending tools already support) before the CRO touches copy again. Reply rate alone cannot tell you if mail is landing in spam or landing and being ignored. Once opens are visible, compare against 35 to 40% as the local-services benchmark; if opens are far below that, it is spam placement and stays with COO and CCO to fix the sending setup; if opens are near benchmark but replies stay near zero, it is a message problem and belongs with CRO.

> Evidence: Cleverly.co, 16 Apr 2026 (mod. 28 Jul 2026): real estate/local services cold email averages 35-40% open, 48%+ is good, 5-7% reply. This business currently tracks sent, replied and clicks only, no opens, so there is no way to tell the two failure modes apart. [read outside, cleverly.co, 'Cold Email Benchmarks by Industry', published 16 Apr 2026, modified 28 Jul 2026]

## GBP beats organic SEO for this business, act accordingly

*tried, revised 0 times, learned 2026-08-18 from brief.*

Put setup time into the Google Business Profile first (video verify, service area, hours, categories) before any content or ranking work. It is nearly free, delivers leads in 4 to 8 weeks, and sits on the local pack surface AI Overviews barely touch.

> Evidence: Section 1 and 2: Whitespark's 540 query study shows local intent triggers local pack 93% of the time versus AI Overview 15%. Section 6 channel table ranks GBP highest confidence, fastest result.

## Cold email is the one channel currently breaking Australian law

*tried, revised 0 times, learned 2026-08-18 from brief.*

Flag to the CCO and COO immediately that the bot needs a working unsubscribe, correct sender ID, and a scraper skip rule for sites refusing marketing before it sends again. This is not a marketing nice to have, it is a legal exposure that can end the business.

> Evidence: Section 5: Spam Act 2003 has no volume threshold and no B2B exemption on identification or unsubscribe, per ACMA.

## Niche pages cap at 8 to 12, suburb pages cap at 3

*tried, revised 0 times, learned 2026-08-18 from brief.*

Never approve or request a page built by swapping a suburb or trade name with no unique content. Each page needs a live demo, a real price, and 200 words that exist nowhere else on the site, sourced from actual outreach calls.

> Evidence: Section 4: Google's scaled content and doorway page policies, and Mueller's line that swapping the city name makes a page a doorway page. Building 300 pages risks the whole domain.

## Reviews compound, nothing else in this plan does

*tried, revised 0 times, learned 2026-08-18 from brief.*

Push every desk to protect the review pipeline: ask on delivery day, never incentivize or gate, reply within 24 hours. Track toward ten reviews at 4.8 or higher with three in the trailing 90 days at all times.

> Evidence: Section 8: BrightLocal 2026 survey, 31% of consumers will only use a business rated 4.5 or higher, up from 17%, and 74% filter for recency. Section 2: reviews are 20% of local pack weighting, the only factor that compounds.

## Free mockup is the strongest asset and it is being wasted on email one

*tried, revised 0 times, learned 2026-08-18 from brief.*

Push the CRO to hold the mockup back for email two, not give it away in the first touch. Email one should name one specific, verifiable problem and offer the mockup as the payoff.

> Evidence: Section 5: 42% of cold email replies arrive after email one, and naming a concrete gap plus a visual outperforms generic asks by roughly 5 to 10x in vendor data.

## No social media, but community answers are fair game and now a discovery channel

*tried, revised 0 times, learned 2026-08-18 from brief.*

Keep an eye on whether any Discord or forum activity for the business drifts from answering real questions into posting promo or building a following. The line is activity type, not platform.

> Evidence: Section 7: 48% of AI citations trace to community platforms, Reddit alone 21 to 24% of AI Overview citations, but the brief draws a hard line between answering questions and content creation.

## Food niche and its menu wording both underperform, don't keep feeding it volume

*tried, revised 0 times, learned 2026-08-19 from msgchain.*

Shift daily texting volume from food toward beauty and trades until food's reply rate closes the gap, and retire the menu specific wording outright.

> Evidence: food 59 sent 4 replied 7% versus beauty 134 sent 37 replied 28%, and the menu wording is 8 sent 0 replied

## CMO areas live and niches live tiles are unreliable same shape of bug

*tried, revised 0 times, learned 2026-08-19 from shift.*

Keep hand counting the call_list every shift, do not read niches-live or ready_live_by_niche either way. Today the tile undercounts in the opposite direction from before: it claims only beauty is live and ready_live_by_niche shows 0 for trades, but trades is 29 of 50 rows in the actual working queue, more than half. The tile has now been wrong both by overclaiming niches (food, pro) that never appear in queue, and by underclaiming a niche (trades) that is clearly the majority of queue volume. It is not a food or pro specific bug, the tile and ready_live_by_niche are simply disconnected from th

> Evidence: This shift's 50 row call_list hand count: 29 trades, 21 beauty, 0 food, 0 pro. Tile reads niches live 1 (beauty). ready_live_by_niche reads beauty 80 only, no entry for trades despite trades being the largest slice of the actual queue.

## Replies landing on Byron's phone are invisible to the board

*tried, revised 0 times, learned 2026-08-20 from msgchain.*

Treat the reply-text field as incomplete, not zero. When judging which wording or niche is really working, confirm with Byron directly on any batch where the sync looks thin, don't take a low written-reply count as proof a message failed.

> Evidence: Of the 12 most recent replies noticed, 0 have the actual reply text on this box, the rest were texted back on Byron's phone and never reached the database.

Back to [[Memory]].
