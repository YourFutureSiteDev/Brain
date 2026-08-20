---
source: yfs-console
kind: department
role: cco
tags: [memory, departments]
---

# CCO

What this desk believes about its department, as of 2026-08-20. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: cco` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** suppressed: 23 on 2026-08-18 to 23 on 2026-08-20 (flat, 3 days)

## Checks passing 7/8: no per check breakdown reaches this desk

*proven, revised 8 times, learned 2026-08-18 from shift.*

Ninth consecutive shift confirming the same shape: today's number is 5/8, not 7/8, so Byron's open question naming 7/8 is reading a stale figure. Keep telling Byron the failing-check identity needs someone to open the check code or config directly since neither this console nor any other desk console has file read tools. Flag that the 7/8 and 51-vs-15 figures in his open board items are both stale versus today's actual 5/8 and 47-vs-50.

> Evidence: today: checks passing 5/8 (Opt-out in every email; Daily cap; No address harvesting), daily_cap=off, sent_today=47, max_daily=50. No breach today: 47 is under 50, not over it, and not the 51-vs-15 figure on the board.

## Daily cap of 51 is double the safe rate for cold sending from a personal Gmail account

*proven, revised 4 times, learned 2026-08-18 from research.*

Volume alone is not what gets a personal Gmail account killed, complaint rate is, and 0.3% is the hard line with 0.08% the safe number. That means the real gap in this business is not just daily_cap sitting off, it is that nobody tracks spam complaints at all: CCO's 8 checks name a daily cap check but no complaint rate check. Tell CCO to add a complaint rate measure (Gmail Postmaster Tools or equivalent) alongside fixing the cap, because a cap with no complaint visibility is a guess, not a control.

> Evidence: gmass.co and litemail.ai (2026): bulk sender rules apply from 5,000/day, far above this business's volume, but the 0.3% complaint ceiling and 0.08% safe threshold apply regardless of volume; business has sent 178 total, 49 today, with zero complaint rate visibility anywhere in the CCO tile. [read outside, gmass.co/blog/gmail-bulk-sender-guidelines (2026), litemail.ai/blog/google-email-sender-guide

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
