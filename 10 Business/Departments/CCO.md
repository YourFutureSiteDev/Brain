---
source: yfs-console
kind: department
role: cco
tags: [memory, departments]
---

# CCO

What this desk believes about its department, as of 2026-08-19. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: cco` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** suppressed: 23 on 2026-08-18 to 23 on 2026-08-19 (flat, 2 days)

## Demo sites are the most urgent problem, not the outreach

*working, revised 1 time, learned 2026-08-18 from brief.*

This is not just a trust and disclaimer problem, it is a specific statutory exposure. Putting a fabricated NSW builder licence number (118422C) on a demo site linked from a cold email is the kind of building trade advertisement NSW Fair Trading actively enforces, with penalties running into six figures for an individual and real cases landing five figure penalty notices before any court action. Byron should treat pulling that licence number and the fabricated ABNs off all four demo sites as more urgent than any sending or targeting question in this brief.

> Evidence: nsw.gov.au building trade advertisement rules: max penalty $110,000 individual / $330,000 corporation for unlicensed residential building work and advertising; 2026 Steve Preston case, nine penalty notices totalling $22,000, ABC News 28 Jul 2026 [read outside, NSW Government, nsw.gov.au 'Building trade advertisements' and Contracts Specialist 'Role of NSW OFT in Regulating Builders', cross checked

## Checks passing 7/8: no per check breakdown reaches this desk

*working, revised 1 time, learned 2026-08-18 from shift.*

Fifth time this has been asked (Byron's notes this shift alone repeat it four times) and it still cannot be answered from tile data. Also flagging a discrepancy: Byron's note cites 51 sent against a cap of 15, but the live numbers this shift show sent_today=49 and daily_cap="off" with my own settings at max_daily=50. Either the cap of 15 was set and reverted intra-day, or that figure is stale. Escalating both to Byron directly since repeating the same gap in the playbook has not produced the dashboard change needed.

> Evidence: cco tile: ["Checks passing","7/8","see below"], no names; business snapshot this shift: sent_today 49, daily_cap "off", settings max_daily=50, not 51 vs 15.

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

## Daily cap of 51 is double the safe rate for cold sending from a personal Gmail account

*tried, revised 0 times, learned 2026-08-18 from research.*

Tell COO the 500 a day hard cap is the wrong number to size against. The real ceiling for a personal (non-Workspace) inbox doing cold outreach is about 25 a day once warmed up, and this account is sending 49 to 51 a day right now. That gap does not risk the hard suspension threshold, but it does raise spam complaint and throttling risk before the account ever gets near 500. Either bring the daily cap down toward 25, or treat a move to Google Workspace with SPF, DKIM and DMARC properly set up as the way to safely keep sending near 50 a day. Also worth knowing: the 5,000 a day bulk sender rules 

> Evidence: Woodpecker and Overloop 2026 sending limit guides: 500/day hard cap on personal Gmail but 10-20/day warmup scaling to ~25/day safe cold sending rate, plus 5% bounce and 0.3% complaint rate as separate suspension triggers; PowerDMARC confirms bulk sender authentication rules only apply at 5,000+ emails/day [read outside, Woodpecker "Email Sending Limits in 2026" and Overloop "Gmail Sending Limits i

Back to [[Memory]].
