---
title: How to write an instruction
source: byron
tags: [memory, howto]
---

# How to write an instruction

Notes in this folder are read by the machine on the VPS and handed to a desk.
This one is not: anything whose filename starts with an underscore is skipped,
so the instructions here stay instructions rather than becoming a job.

Copy the shape below into a new note in this folder.

```
---
role: cmo
---

Say what you want in plain words. One thing per note.
```

Then leave it. The cycle runs every thirty minutes. When it has been handed over
the note gains a `picked_up:` line, and the desk's answer appears in the console
under that desk's conversation.

**One thing per note.** A note holding four instructions goes to one desk as one
order, and the three that belonged elsewhere get lost in it.

**Say the outcome, not the setting.** "Stop working Newcastle, the replies are
all price shoppers" is something a desk can act on and learn from. "Set the area
weight to 0.3" is you doing its job with less information than it has.

**It is not a chat.** For a conversation, open the console and talk to the CEO.
This is for the thing you thought of on the bus.

Back to [[Memory]].
