---
title: "Diff Review"
description: "The practice of reading exactly what an AI agent changed, line by line, before accepting it — the core review discipline of vibecoding."
related: ["yolo-mode", "hallucination"]
---

Diff review is reading the precise set of changes an agent proposes — added lines, removed lines, touched files — before they're applied or committed. It's the same discipline as reviewing a human teammate's pull request, applied to AI output.

## Why it's non-negotiable

Agents are fluent, which makes bad code easy to mistake for good code at a glance. A diff that "looks right" can still introduce an off-by-one error, drop an edge case, or quietly change behavior in a file you didn't expect it to touch. Diff review is the checkpoint that catches this before it ships.

See our [guide to reviewing AI-generated diffs](/posts/reviewing-ai-generated-diffs/) for a concrete checklist.
