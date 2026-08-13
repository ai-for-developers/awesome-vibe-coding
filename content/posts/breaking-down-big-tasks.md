---
title: "Breaking Big Tasks Into Agent-Sized Steps"
description: "'Build me a dashboard' is a wish, not a task. A practical method for decomposing large asks into steps an AI agent can actually execute reliably."
date: 2026-02-09
series: ["Prompting Patterns"]
series_order: 2
tags: ["prompting", "workflow"]
---

Vague, large prompts produce vague, large diffs — and vague diffs are the hardest kind to review. The fix isn't a cleverer prompt; it's decomposition.

## Signs a task is too big

- You can't describe what "done" looks like in one sentence
- The task touches more than two or three unrelated parts of the system
- You'd need to check in multiple times even if a human were doing it

If any of these are true, break it down before prompting.

## A decomposition pattern that works

1. **State the end goal in one sentence**, even if the path there is multi-step.
2. **List the components** the goal actually requires — data layer, API, UI, tests — and order them by dependency.
3. **Hand the agent one component at a time**, reviewing before moving to the next.
4. **Reassess after each step** — the plan for step 3 often changes based on what step 1 revealed.

This is slower than firing off one giant prompt and hoping. It is also the difference between a working feature and an afternoon spent untangling a diff that touched twelve files for the wrong reasons.

That wraps the "Prompting Patterns" series for now — more installments coming as new patterns prove out in practice.
