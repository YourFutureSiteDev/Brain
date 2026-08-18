---
source: yfs-console
kind: department
role: cmo
tags: [memory, departments]
---

# CMO

What this desk believes about its department, as of 2026-08-18. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: cmo` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** reply rate %: 1.4 on 2026-08-18 to 1.4 on 2026-08-18 (flat, 1 days)

## Food niche has real inventory but is not counted as live

*working, revised 1 time, learned 2026-08-18 from shift.*

Resolved: the CMO tile now shows 4 live niches (trades, food, beauty, pro), matching ready_by_niche exactly, so food was a stale count last time, not an off-books niche. New finding to act on: the ready pool is badly skewed, beauty 101 and trades 48 make up 88% of the 169 ready leads, food 11 and pro 9 combined are only 12%. If sweep time is split evenly across the 4 niches, food and pro are underperforming per hour swept; if it is not split evenly, this is expected. Worth confirming with CDO whether food and pro simply have fewer OSM-listed businesses nationwide or whether the sweep needs reb

> Evidence: business.roles.cmo tiles: 'Niches live 4, trades, food, beauty, pro'. business.totals.ready_by_niche: beauty 101, trades 48, food 11, pro 9, total 169.

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

## A reply rate this low points at deliverability, not the message

*tried, revised 0 times, learned 2026-08-18 from research.*

Before CRO rewrites subject lines or copy, confirm with COO and CCO what account sends the mail: is it an authenticated custom domain on Google Workspace with SPF, DKIM and DMARC set up, was it warmed up gradually before running near the daily cap, and is the spam complaint rate being tracked. A 1.4% reply rate is below even the worst published industry floor, which is a stronger signal of spam-folder placement than of weak targeting or weak copy.

> Evidence: 143 sent, 2 replies = 1.4%, against a 2026 platform average of 3.43% and a worst-sector floor of 1.5 to 3.5% (Apollo.io, Instantly.ai). Safe volume is roughly 100/day per warmed inbox on an authenticated custom domain, not free Gmail (Woodpecker.co, Smartlead.ai, 2026). [read outside, Apollo.io, 'What's a Good Cold Email Reply Rate in 2026' and Instantly.ai cold email reply rate benchmarks (both 2

Back to [[Memory]].
