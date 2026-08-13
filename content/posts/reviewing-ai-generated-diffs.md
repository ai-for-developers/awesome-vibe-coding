---
title: "How to Review AI-Generated Diffs Without Rubber-Stamping Them"
description: "Skimming an AI's output and hitting accept is how bugs slip through. A concrete checklist for reviewing agent-written code fast, without going slow."
date: 2026-01-26
series: ["Getting Started with Vibecoding"]
series_order: 3
tags: ["fundamentals", "review"]
---

The single most common failure mode in vibecoding isn't a bad prompt — it's a good diff that nobody actually read. Agents are confident, and confident wrong code is easy to approve on autopilot.

## What to actually check

**Scope.** Did the agent touch only what the task required, or did it "helpfully" refactor unrelated code along the way? Unrequested scope creep is the fastest way to introduce regressions you didn't ask for.

**Edge cases.** Agents are good at the happy path and inconsistent at the edges — empty inputs, network failures, concurrent access. Read for what's *missing*, not just what's there.

**Assumptions baked into the diff.** Did the agent guess at an API shape, a config value, or a business rule instead of asking? These guesses read as confident code and are the easiest thing to miss.

**Tests, if any were written.** Do the tests actually exercise the behavior that changed, or do they just restate the implementation?

## A workflow that scales

1. Ask the agent to explain its plan *before* it edits, for anything non-trivial.
2. Review the diff in small units, not as one giant patch.
3. Run the actual code path yourself — don't trust a description of what it does.
4. If something feels off, ask the agent to explain its reasoning rather than silently fixing it yourself — the answer often reveals a wrong assumption worth correcting at the source.

This closes out the "Getting Started" series. From here, the [Prompting Patterns](/posts/) series goes deeper on directing agents for specific kinds of work.
