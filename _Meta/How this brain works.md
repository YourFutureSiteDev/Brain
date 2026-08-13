---
type: meta
tags:
  - meta
---

# How this brain works

Four moves, in order. Everything else is decoration.

1. **Capture** anything, immediately, into [[Inbox]]. No thinking, no filing.
2. **Clarify** it later. What is this actually? A task, an idea, a fact, a project?
3. **Connect** it. Give it a home, then link it to at least one thing already here.
4. **Retrieve** it. Start at [[Home]] or a map in `09 Maps`, follow links outward.

The value is not in the notes. It is in the links between them. A note with no links is a note you will never see again.

## The folders

| Folder | What goes in it | When it leaves |
|---|---|---|
| `00 Inbox` | Raw capture. Anything, unsorted. | Empty it weekly. Nothing lives here. |
| `01 Daily` | One note per day. Log, scratchpad, tasks. | Never. It is a record. |
| `02 Notes` | Permanent notes. One idea each, in your words. | Never. This is the brain. |
| `03 Sources` | What other people said. Books, videos, articles, syllabuses. | Never. |
| `04 Projects` | Work with an end state and a deadline. | Archive when finished. |
| `05 Areas` | Ongoing responsibilities with no end. School, business, money. | Never. |
| `06 Resources` | Reference you did not write and did not read as a source. | Archive when stale. |
| `07 People` | One note per person who matters. | Never. |
| `08 Archive` | Finished or abandoned. Out of sight, still searchable. | Never. |
| `09 Maps` | Maps of content. Hand-built index notes into a topic. | Never. |
| `_Templates` | Templates for new notes. | n/a |
| `_Meta` | Notes about the brain itself. | n/a |

## Projects versus areas

The distinction people get wrong, and the one that makes the system work.

A **project** has a finish line. "Ship the outreach bot" is a project. You will one day be done.

An **area** has a standard to maintain. "School" is an area. You are never done with school, you just keep it above a line.

If you cannot name the moment it is finished, it is an area.

## Permanent notes

The core of it, and the part that takes discipline.

- **One idea per note.** If the title needs "and", split it.
- **Title it as a claim, not a topic.** Not "Contrast". Instead: [[Contrast fails hide inside brand colours]]. The title should be the thing you would say out loud.
- **Write it in your own words.** Copy and paste teaches you nothing.
- **Link it as you write.** Two or three links minimum, or it is orphaned.

## Naming

Plain sentence case. No dates in the title, no numeric prefixes, no underscores. The file name is the link text, so it should read naturally inside a sentence.

Good: `Page one Maps results are the wrong prospects`
Bad: `2026-08-12_maps-research-v2-FINAL`

Daily notes are the one exception: `YYYY-MM-DD`.

## Tags versus links

Links are the real structure. Tags are a coarse filter on top.

Use tags only for **type** and **status**, never for topic. Topic belongs in a map of content, where you can add context. See [[Tag index]].

## The weekly review

Fifteen minutes, once a week. Non negotiable, because it is the only thing that stops the brain rotting.

Open [[Weekly Review]] and run it. Empty the inbox, check every active project has a next action, archive what is done.

## The views that maintain themselves

Four `.base` files in `_Meta` query the vault live, so no index is ever written down twice.

| View | What it answers |
|---|---|
| [[Projects.base\|Projects]] | What is active, blocked, someday. |
| [[Notes.base\|Notes]] | Which permanent notes are still seeds. |
| [[Growth.base\|Growth]] | What the vault is quietly losing: orphans, stale notes, inbox backlog. |
| [[Library.base\|Library]] | Sources, people, areas. |

A new project appears in the Projects view the moment its frontmatter says `status: active`. Nothing else to update.

The maps in `09 Maps` stay hand-written on purpose. A generated list tells you what exists. A map tells you what matters.

## When it gets big

Read [[How this brain grows]] when search starts failing you, not before. It covers what to change at each size and, more usefully, what not to change yet.
