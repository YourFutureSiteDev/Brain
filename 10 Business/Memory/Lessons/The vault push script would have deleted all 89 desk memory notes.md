---
source: yfs-console
kind: lesson
role: coo
subject: sync-hazard
noted: "2026-08-21T09:47:22"
tags: [memory, lesson, coo]
---

# The vault push script would have deleted all 89 desk memory notes

The vault push script would have deleted all 89 desk memory notes. It rsyncs Byron's Obsidian vault to the droplet with delete enabled, and its header stated that nothing on the droplet could remove a note. That stopped being true on 13 Aug when the vault became a symlink to the brain repo, which the desks commit to every thirty minutes. A dry run on 21 Aug showed 103 files, 90 of them notes, 66 under Memory. Fixed by excluding the business folder. The general form: a one way sync is safe only while one side is the sole author.

Learned by the [[COO]] on 2026-08-21, about sync-hazard.

Back to [[Memory]].
