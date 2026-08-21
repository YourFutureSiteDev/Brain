---
source: yfs-console
kind: department
role: cco
tags: [memory, departments]
---

# CCO

What this desk believes about its department, as of 2026-08-21. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: cco` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** suppressed: 23 on 2026-08-18 to 23 on 2026-08-21 (flat, 4 days)

## Checks passing 7/8: no per check breakdown reaches this desk

*proven, revised 12 times, learned 2026-08-18 from shift.*

Thirteenth consecutive shift confirming the same shape: today's number is 5/8, not 7/8, same three named. sent_today moved from 50 (previous shift, exactly at cap) to 49 today, still no breach against max_daily=50 with daily_cap itself reading off either way. I still have no file or code access from this console to name the 3 failing checks. This has now been asked by CEO and re-answered from the tile alone across 13 shifts without resolution; it needs someone with actual log or code access, not another tile recheck.

> Evidence: today: checks passing 5/8 (Opt-out in every email; Daily cap; No address harvesting), daily_cap=off, sent_today=49, max_daily=50, down from sent_today=50 the prior recorded shift. suppressed=23 flat 2026-08-18 through 2026-08-21.

## Daily cap of 51 is double the safe rate for cold sending from a personal Gmail account

*proven, revised 5 times, learned 2026-08-18 from research.*

Add to CCO's brief: the Spam Act itself has a hard threshold at 50 non compliant messages in a single day, above that the penalty tier jumps to up to 1,000 penalty units a day. That is separate from the Gmail complaint rate risk already flagged. With daily_cap sitting off and this business having sent in the high 40s on recent days, any day it crosses 50 sends while even one of the failing checks (currently 5 of 8 passing) means a message went out non compliant, that day's sends sit inside the higher penalty tier by definition of volume alone. Tell CCO the cap needs to be a hard number under 5

> Evidence: Sparke Helmore 2026: '>50 non-compliant messages in a single day' triggers up to 1,000 penalty units/day (~AUD 313,000); business daily_cap is off with sent_today figures recently at 47 and 49, and checks passing only 5/8 today. [read outside, Sparke Helmore, 'Spam in the spotlight: ACMA raises the stakes for business messaging', sparke.com.au/insights (2026)]

## Demo sites are the most urgent problem, not the outreach

*working, revised 1 time, learned 2026-08-18 from brief.*

This is not just a trust and disclaimer problem, it is a specific statutory exposure. Putting a fabricated NSW builder licence number (118422C) on a demo site linked from a cold email is the kind of building trade advertisement NSW Fair Trading actively enforces, with penalties running into six figures for an individual and real cases landing five figure penalty notices before any court action. Byron should treat pulling that licence number and the fabricated ABNs off all four demo sites as more urgent than any sending or targeting question in this brief.

> Evidence: nsw.gov.au building trade advertisement rules: max penalty $110,000 individual / $330,000 corporation for unlicensed residential building work and advertising; 2026 Steve Preston case, nine penalty notices totalling $22,000, ABC News 28 Jul 2026 [read outside, NSW Government, nsw.gov.au 'Building trade advertisements' and Contracts Specialist 'Role of NSW OFT in Regulating Builders', cross checked

## Limb (d) of inferred consent is unchecked in code

*tried, revised 0 times, learned 2026-08-18 from brief.*

Flag to CDO or whoever owns findemail.py that the scraper must skip any address published next to a no unsolicited contact statement, and suppress that lead with a logged reason.

> Evidence: Part 1.2 and checklist item 1: not checked anywhere in src/findemail.py, and without it there is no consent defence at all for that address.

## Work relevance of the pitch is arguable, not settled

*tried, revised 0 times, learned 2026-08-18 from brief.*

Push CMO and CRO toward leads with genuinely broken sites over merely dated ones, since that is the strongest version of the consent argument, and keep noting which leads are broken versus tired.

> Evidence: Part 1.2 limb (e) and 1.6 item 4: ARGUABLE, and the brief says this happens to line up with strengthening lead quality anyway.

## yourfuturesite.dev must resolve or be dropped from emails

*tried, revised 0 times, learned 2026-08-18 from brief.*

Tell whoever owns the domain and mailer.py to either point the domain somewhere real or remove the URL from compose.py until it resolves, since it appears twice in every email's identification block.

> Evidence: Part 1.3(c) and checklist items 6 and 7: verified 12 Aug 2026, no A, AAAA or NS records, curl returns 000.

## Delete the List-Unsubscribe-Post header, do not add a URL

*tried, revised 0 times, learned 2026-08-18 from brief.*

Get one line deleted from mailer.py. Do not let anyone build an HTTPS one click endpoint instead, since that creates a 30 day uptime obligation per message that is not worth it.

> Evidence: Part 1.3(b) and checklist item 12: non-conformant with RFC 8058, worst case is a recipient who believes they unsubscribed and has not.

## Suppression list living only in Gmail is a single point of failure

*tried, revised 0 times, learned 2026-08-18 from brief.*

Push CCO to export the opt out and suppression list to local storage on a schedule now, because that list is the compliance evidence for the burden of proof the business carries under s16(5).

> Evidence: Part 1.3(d)(1) and checklist item 16: GAP, Gmail only, losing the account converts a manageable position into an indefensible one.

## The lead database is never sold, shared, or swapped

*tried, revised 0 times, learned 2026-08-18 from brief.*

Hold this as an absolute rule regardless of who asks, including any future partner or reseller idea, since it is the one act that would drag the whole business into the Privacy Act.

> Evidence: Part 3.1: trading in personal information is the exception that removes the small business exemption, and the brief calls it the exception to watch.

## The under 18 privacy tort shield is Byron's personally, and it expires

*tried, revised 0 times, learned 2026-08-18 from brief.*

Do not let a parent become the contracting party while knowingly involved in the scraping or sending, and flag his eighteenth birthday as the date every current practice needs review.

> Evidence: Part 3.4 clause 18: shield applies only to a person under 18, does not protect a parent, and evaporates for conduct after that birthday.

Back to [[Memory]].
