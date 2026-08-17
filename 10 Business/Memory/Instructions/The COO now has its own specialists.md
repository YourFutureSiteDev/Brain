---
title: The COO now has its own specialists
role: coo
picked_up: 2026-08-17T22:47:28
---

You have specialists now. 16 of them, in
engineering (58), project-management (7), testing (9), support (4), sitting in `~/.claude/agents` on this box. They
came from [[The agency agents roster]], which is where the full list and the
other desks' shares are.

Yours, and what each is for:

- `engineering-sre` - the box staying up
- `engineering-incident-response-commander` - when it does not
- `engineering-devops-automator` - the services and the deploys
- `engineering-code-reviewer` - before a change goes on the droplet
- `engineering-minimal-change-engineer` - the smallest edit that does the job
- `engineering-email-intelligence-engineer` - parsing what comes back into the inbox
- `engineering-rag-pipeline-engineer` - if the vault ever needs retrieval
- `engineering-multi-agent-systems-architect` - how these 255 should be wired together
- `engineering-prompt-engineer` - the wording the desks run on
- `testing-reality-checker` - does the thing actually do what it says
- `testing-evidence-collector` - proof, rather than a claim that it worked
- `testing-workflow-optimizer` - where the cycle wastes its half hour
- `project-management-project-shepherd` - keeping a job moving to done
- `project-management-experiment-tracker` - what was tried and what it did
- `support-infrastructure-maintainer` - the unglamorous upkeep
- `operations-manager` - the whole machine, above any one part

`testing-evidence-collector` and `testing-reality-checker` are the two to take seriously first. Twice on 16 August a script reported a change it had never made, and both times the cause was a script deciding it had worked from its own control flow instead of reading the file back.

What I want back is short. Name the three you would actually use, say what each
one would put on my desk, and say plainly if the answer is none. A desk holding
16 tools it never opens is worse off than one holding three it does.
