---
title: "YOLO Mode"
description: "A setting that lets an AI agent take actions — edits, commands, commits — without asking for approval on each one."
related: ["diff-review", "agentic-loop"]
---

YOLO mode (also called auto-approve or auto-accept in different tools) lets an agent execute its planned actions — file edits, shell commands, even commits — without pausing to ask for confirmation on each step.

## The trade-off

It's faster: a well-scoped task can complete in one shot instead of a dozen approval prompts. It's also riskier: without a human checkpoint at each step, a wrong early decision can compound across several subsequent actions before anyone notices.

## When it's reasonable

YOLO mode is more defensible in a sandboxed environment, on a task with a very tight, well-understood scope, or when working in a disposable branch you'll review as a whole afterward — via [diff review](/dictionary/diff-review) — rather than step by step. It's harder to justify against a shared branch or in a codebase you haven't built strong intuition for yet.
