---
title: Memory
source: byron
tags: [business, memory, index]
---

# Memory

What the business remembers, and the one place you can write back to it.

## The four folders

**Lessons.** One note per thing learned, permanent. Written whenever a desk
retunes one of its own numbers, so each note says what changed and why. These
never get deleted and they show up in the graph beside whatever they are about.

**Decisions.** One note per day, a line per decision, with the desk that made
it. Kept for four months, then dropped, because the database still has every row.

**Observations.** Same shape as Decisions, for what a desk noticed rather than
chose.

**Instructions.** Yours. This is the door into the machine.

## Writing an instruction

Make a note in `Instructions`, give it a `role:` in the frontmatter, and say
what you want in plain words:

```
---
role: cmo
---

Stop working Newcastle for now. The three replies we got there were all price
shoppers. Put the effort into Lake Macquarie instead and tell me what changes.
```

On the next cycle, within half an hour, that goes to the CMO desk as a standing
order, exactly as though the CEO had handed it over in the console. The desk
answers back in the console, and the note gets a `picked_up:` line stamped into
its frontmatter so it is never worked twice.

Leave `role:` out and it goes to the CEO, who decides whose job it is.

The roles are `ceo`, `cfo`, `cro`, `cmo`, `coo`, `cco`, `cdo`. What each one
owns is in [[C-Suite]].

## What the CEO reads before she answers

Every instruction still standing, and the title of every lesson. So a note
written here changes what she says next, not just what the desks do.

Back to [[Business Machine]].
