---
type: meta
tags:
  - meta
---

# How this brain grows

The structure in [[How this brain works]] is built to survive getting big. This note is what to change, and more importantly **when**, so nothing gets reorganised early for no reason.

## The rule underneath all of it

**Never reorganise ahead of the pain.** Every folder you add before you need it is a decision you have to make on every future capture. Add structure the day it stops working, not the day you imagine it might.

## Stage one, under 100 notes

Where the vault is now.

Everything is findable by name. `Cmd+O` beats any folder tree. The only real job is building the habit: capture without filing, then file weekly.

**Do not** add folders. **Do not** add plugins. **Do** write notes.

The signal you have left this stage: you search for something you know you wrote and it takes more than one guess.

## Stage two, 100 to 500 notes

Search stops being enough, and links start carrying the weight.

- **Maps of content earn their keep.** A map is hand-built and curated, which is exactly why it beats a tag. It says *how* things relate.
- **Split a map past roughly 20 links.** [[Business MOC]] becomes a map per venture. The parent keeps the five links to its children.
- **Seeds become the backlog.** `Notes.base` view "Seeds to grow" is the queue. One a week is plenty.
- **Orphans become the real problem.** A note nothing links to is a note you have lost. The Orphans view in `Growth.base` finds them.

## Stage three, past 500 notes

Structure stops being the bottleneck and judgment starts.

- Archive ruthlessly. `08 Archive` is free, and a small active vault thinks faster.
- Areas start spawning sub-areas. Let them, one level only, never two.
- If a topic has produced 30 notes, it is not a topic. It is an area, and it needs a standard.

## The part that does its own bookkeeping

Four `.base` files in `_Meta` query the vault live. They never go stale, because nothing is written down twice.

- **[[Projects.base|Projects]]** groups every project by status. Adding `status: active` to a new project is all it takes to appear.
- **[[Notes.base|Notes]]** separates seeds from grown notes.
- **[[Growth.base|Growth]]** is the maintenance panel: inbox backlog, orphans, blocked work, oldest untouched, recently touched.
- **[[Library.base|Library]]** holds sources, people and areas.

These replace the job people usually do by hand, badly: maintaining an index. The curated maps in `09 Maps` stay hand-written on purpose. A generated list tells you what exists. A map tells you what matters.

## Making a new view

Open any `.base` file, click the view dropdown, add one. Or write the YAML directly. The vocabulary:

- `file.inFolder("02 Notes")`, `file.hasTag("project")`, `file.hasLink("Business")`
- `note.status == "active"`, `note.maturity == "seed"`
- `file.backlinks.isEmpty()` finds orphans, `file.mtime` finds stale work
- View types: `table`, `cards`, `list`

## Tracking the growth itself

`_Meta/vault-stats.sh` appends a dated row to [[Vault Stats]]. Run it monthly during [[Monthly Review]]. The number that matters is not note count, it is **links per note**. A brain that gains notes without gaining links is just a folder.

## When to add a community plugin

Not yet. Core Obsidian does everything above. The honest triggers:

- **Templater**, when template placeholders stop being enough and you need logic
- **Dataview**, only if Bases genuinely cannot express a view you need
- **Excalidraw**, when you start thinking in diagrams

Adding these before the trigger fires is how a vault becomes a hobby instead of a tool.

## Links

[[How this brain works]] · [[Weekly Review]] · [[Monthly Review]]
