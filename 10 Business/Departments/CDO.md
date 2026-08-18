---
source: yfs-console
kind: department
role: cdo
tags: [memory, departments]
---

# CDO

What this desk believes about its department, as of 2026-08-18. Written by the desk itself, one entry per thing it can point at evidence for.

**This note is a mirror, not a door.** The desk rewrites it every time it learns something, so anything you type here is lost at the next shift, and nothing reads it back. To correct a desk, write a note in Instructions with `role: cdo` in its frontmatter. That is the door, and it lands in the same inbox the CEO delegates through.

**Scoreboard.** leads with a usable verdict %: 97.96 on 2026-08-18 to 97.96 on 2026-08-18 (flat, 1 days)

## Every capacity number in the plan is a guess, not a fact

*tried, revised 0 times, learned 2026-08-18 from brief.*

Track real data against the model's assumptions (60 percent care attach, 50 percent hour usage, 12.5 hours a week) as jobs actually happen, and flag to CEO the moment reality diverges instead of letting the plan stand unchallenged.

> Evidence: Section 5 opens with assumptions stated so they can be argued with, and the whole ceiling calculation rests on attach rate and usage rate nobody has observed yet.

## No timer means the three hour rule is currently unmeasured

*tried, revised 0 times, learned 2026-08-18 from brief.*

Until actual minutes are logged per job, treat every effective-hourly-rate figure in the brief as unverified. Push for the minutes field to exist and start recording from job one.

> Evidence: Section 8 point 2 and decision 2: the first ten recorded jobs settle whether the $99 is a real product, and nothing in the document can be verified without this.

## The active care client count is a live trigger, not a stat

*tried, revised 0 times, learned 2026-08-18 from brief.*

Keep an exact, current count of active care clients and monthly care hours delivered. This number alone decides when the $99 comes off the site, so it must be right every time it's asked for.

> Evidence: Section 5 triggers: stop selling the $99 at 30 active care clients or 12 care hours a month, whichever comes first.

## One system of record, no second place for truth to live

*tried, revised 0 times, learned 2026-08-18 from brief.*

Keep lead and job data in the pipeline app only. If a spreadsheet, note, or second tool starts holding numbers that matter, treat that as a data integrity problem to fix, not a convenience.

> Evidence: Section 8: adding Notion, Trello or similar is explicitly wrong here because it creates a second place where truth lives, which a 12 hour a week solo operator cannot maintain.

## All the lead and client data lives on one school laptop

*tried, revised 0 times, learned 2026-08-18 from brief.*

Treat this as the standing top risk to the data itself. Any report on backups, git pushes, or database dumps for the pipeline app is worth surfacing immediately, since a lost machine means a lost database.

> Evidence: Section 8: the business runs on one Jamf managed MacBook owned by a school, which can be locked or wiped, losing the lead database and the bot with it.

## Care Pro's margin depends on clients not using their hours

*tried, revised 0 times, learned 2026-08-18 from brief.*

Watch actual hours used per care client against the plan. If usage climbs toward the full allotment, that is the data signal to bring to CFO for repricing, not something to wait on until it shows up in revenue.

> Evidence: Section 5: Care Pro returns $24.62 an hour if fully used, below the $99 job, and is only profitable because most clients do not use their hours.

## UNKNOWN leads: no confirmed route to the call list

*tried, revised 0 times, learned 2026-08-18 from shift.*

Do not treat 'UNKNOWN leads are never emailed, that's the rule working' as the full answer. That only covers the email side. Confirm whether UNKNOWN-status leads with a phone number are added to the call queue, or silently dropped once the site-confirm check fails. Keep checking this until it's answered.

> Evidence: call_list sample shows 50 of 364 queued entries, all status NO_SITE, 0 UNKNOWN. The one UNKNOWN row visible in the leads sample, Hawkesbury & Nepean Plumbing, has both phone and email blank, so some UNKNOWN leads are genuinely dead ends, but the sample is too small to know how many of the 452 have a phone and are being missed.

Back to [[Memory]].
