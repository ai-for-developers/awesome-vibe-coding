---
title: "Plan Mode"
description: "A mode where an agent explores and analyzes a codebase but is blocked from editing files or running commands until you review and approve its plan."
related: ["diff-review", "yolo-mode", "agentic-loop"]
---

In plan mode, an agent is restricted to read-only actions — it can read files, search the codebase, and ask clarifying questions, but it can't make edits or run state-changing commands. What it produces instead is a written plan: what it understands the task to be, which files it intends to touch, and the approach it plans to take. You can then approve it, correct it, or send it back before any code changes.

It sits at the opposite end of the spectrum from [YOLO mode](/dictionary/yolo-mode): instead of trusting the agent to act and reviewing the result afterward, you review the intent before anything happens.

## Why it matters

Catching a misunderstood task or a bad approach at the plan stage is far cheaper than catching it after reviewing a large, already-written [diff](/dictionary/diff-review).
