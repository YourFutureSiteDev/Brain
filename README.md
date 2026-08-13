# Byron's brain

One Obsidian vault, living on the Your Future Site VPS at `/home/byron/brain`,
tracked with git so nothing is ever lost and every change has a date on it.

It holds two things that used to be kept apart.

**His own notes**, folders `00` to `09`. Written by him, in Obsidian, on
whatever machine he is at. The machine never edits these.

**What the business knows**, folder `10 Business`. Written by the console on the
VPS: the seven desks, what each one decided, what it learned, and a log of every
day. See [[Business Machine]].

The two halves are in one vault on purpose. A lesson the CMO learns should sit
in the graph next to the project it is about, not in a database on a droplet
that nobody opens on a Sunday.

## It reads as well as writes

Anything written into `10 Business/Memory/Instructions` is picked up by the
machine on its next cycle, half an hour at most, and handed to the desk it
names. Write a note on a phone, and the business acts on it without the console
being opened. See [[Memory]] for how to write one.

## Where it lives

| | |
|---|---|
| On the VPS | `/home/byron/brain` (the original) |
| Reached by the console as | `bots/localbot/data/vault` and `out/brain` |
| History | git, committed every cycle and hourly |
| On the PC | pulled into `Desktop\Claude\Brain` by `tools\pull-brain.ps1` |

The vault on the VPS is the one that is always on. The PC copy is a copy.
