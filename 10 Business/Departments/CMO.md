---
source: yfs-console
kind: department
role: cmo
tags: [memory, departments]
---

# CMO

What this desk believes about its department, as of 2026-08-22. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: cmo` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** reply rate %: 1.4 on 2026-08-18 to 1.09 on 2026-08-22 (down, 5 days)

## Food niche has real inventory but is not counted as live

*proven, revised 8 times, learned 2026-08-18 from shift.*

Keep telling Byron food and pro are excluded from active outreach, but sharpen it: the block sits on new leads entering the no_site/messaged queue, not on the whole pipeline. A food or pro lead that already replied still surfaces (rank 1, bucket replied) because reply status outranks the niche filter. Pro still has zero rows at any stage for 7 straight shifts, that part is unchanged.

> Evidence: This shift's call_list: 28 trades, 21 beauty, 1 food (sweetie-pies-bake-shop, stage=replied), 0 pro. ready_by_niche still carries food 72 and pro 25, ready_live_by_niche food 16 and pro 12, none of which reach the queue except this one replied food lead.

## CMO areas live and niches live tiles are unreliable same shape of bug

*proven, revised 3 times, learned 2026-08-19 from shift.*

This is now the 8th consecutive shift with the identical call_list shape (28 trades, 21 beauty, 1 food replied-only, 0 pro) while the tile still claims 4 niches live. Eight identical readings in a row means this is a static miscalculation, not noisy data, and it is not something I can fix from CMO levers since niche/area targeting settings aren't wrong, the tile query itself is. Route the actual fix to whoever owns the pipeline/tile query, most likely CDO or COO, and stop treating this as a CMO watch item until that query is checked.

> Evidence: This shift's call_list: 28 trades, 21 beauty, 1 food (sweetie-pies-bake-shop, stage replied), 0 pro, identical to the prior 2 shifts' exact counts. Tiles still read niches_live 4 (trades, food, beauty, pro) and ready_by_niche still carries pro 25 and food 72 that never reach the queue.

## Cold email is the one channel currently breaking Australian law

*working, revised 1 time, learned 2026-08-18 from brief.*

This is not just an email problem. The Spam Act covers SMS the same way, and the bot is already texting mobiles at higher volume than it emails, 360 messaged against 218 emailed in the current pipeline. The CCO's compliance checklist only lists 'Opt-out in every email' as a check, there is no equivalent check for a working 'Reply STOP' on the text channel. Tell CCO to confirm the SMS side has the same three things the email side needs: sender identified, functional opt-out, and suppression honoured within days of a STOP reply, before texting keeps running at this volume.

> Evidence: Spam Act 2003 defines commercial electronic message to include SMS/MMS, requiring identification and a working unsubscribe in every message, same as email. Business's own messaged count (360) already exceeds emailed count (218), and CCO's 'Checks passing 5/8' tile names an email opt-out check but no SMS one. [Sprintlaw, 'Spam Act 2003: Electronic Marketing Law'; Monster SMS, 'SMS Compliance in Aus

## A reply rate this low points at deliverability, not the message

*working, revised 1 time, learned 2026-08-18 from research.*

Add open-rate tracking (a tracking pixel, which most sending tools already support) before the CRO touches copy again. Reply rate alone cannot tell you if mail is landing in spam or landing and being ignored. Once opens are visible, compare against 35 to 40% as the local-services benchmark; if opens are far below that, it is spam placement and stays with COO and CCO to fix the sending setup; if opens are near benchmark but replies stay near zero, it is a message problem and belongs with CRO.

> Evidence: Cleverly.co, 16 Apr 2026 (mod. 28 Jul 2026): real estate/local services cold email averages 35-40% open, 48%+ is good, 5-7% reply. This business currently tracks sent, replied and clicks only, no opens, so there is no way to tell the two failure modes apart. [read outside, cleverly.co, 'Cold Email Benchmarks by Industry', published 16 Apr 2026, modified 28 Jul 2026]

## CMO lead area field mismatches the lead's own location, not just the tile totals

*working, revised 1 time, learned 2026-08-20 from shift.*

This is not scattered noise, it clusters by batch. All 7 leads slugged griffith-nsw from the sweep:mobile batch (first_seen 2026-08-19) are tagged with different Victorian suburbs (Melbourne, Pakenham, Yarra Glen, Mornington), none of them Griffith NSW. If area targeting reads this field it is working off a batch-level bug, not lead-level typos. Whoever owns the scraper (CDO or COO) should check what area value gets attached during a sweep:mobile run, this looks fixable at the source rather than something to patch lead by lead.

> Evidence: 7 of the 50 call_list rows share slug root griffith-nsw: bills-hi-tech (area Melbourne VIC), rays-euro-tech (Pakenham VIC), adeles-relaxing-therapy (Pakenham VIC), tonys-barbershop (Yarra Glen VIC), aap-scaffolding (Mornington VIC), abaco-car-care (Melbourne VIC), b-masters-plumbing (Mornington VIC). None read Griffith NSW or anywhere near it.

## GBP beats organic SEO for this business, act accordingly

*tried, revised 0 times, learned 2026-08-18 from brief.*

Put setup time into the Google Business Profile first (video verify, service area, hours, categories) before any content or ranking work. It is nearly free, delivers leads in 4 to 8 weeks, and sits on the local pack surface AI Overviews barely touch.

> Evidence: Section 1 and 2: Whitespark's 540 query study shows local intent triggers local pack 93% of the time versus AI Overview 15%. Section 6 channel table ranks GBP highest confidence, fastest result.

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

## Replies landing on Byron's phone are invisible to the board

*tried, revised 0 times, learned 2026-08-20 from msgchain.*

Treat the reply-text field as incomplete, not zero. When judging which wording or niche is really working, confirm with Byron directly on any batch where the sync looks thin, don't take a low written-reply count as proof a message failed.

> Evidence: Of the 12 most recent replies noticed, 0 have the actual reply text on this box, the rest were texted back on Byron's phone and never reached the database.

Back to [[Memory]].
