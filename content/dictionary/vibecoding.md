---
title: "Vibecoding"
description: "Building software primarily by directing an AI coding agent in natural language, while still applying engineering judgment to review and steer its output."
related: ["diff-review", "prompt-engineering", "agentic-loop"]
---

Vibecoding is the practice of building software primarily through natural-language direction of an AI agent — describing intent, letting the agent write and edit code, and steering the result — while still applying the judgment of an experienced engineer: reviewing diffs, verifying behavior, and making architectural calls.

## What it isn't

It isn't blindly accepting whatever an AI produces without review, and it isn't a synonym for "no longer needing to understand code." Both of those describe a failure mode of the practice, not the practice itself.

## The core skills

- Framing tasks with enough context that an agent can execute them well
- [Reviewing diffs](/dictionary/diff-review) critically rather than rubber-stamping them
- Knowing when to decompose a task versus hand it over whole
- Verifying behavior by running code, not just reading a description of it

See [What Vibecoding Actually Means](/posts/what-is-vibecoding/) for a fuller treatment.
