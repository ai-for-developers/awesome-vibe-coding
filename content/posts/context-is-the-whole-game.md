---
title: "Context Is the Whole Game"
description: "Most disappointing AI output traces back to one cause: the agent didn't have the context a competent human would have had. Here's how to fix that systematically."
date: 2026-02-02
series: ["Prompting Patterns"]
series_order: 1
tags: ["prompting", "context"]
---

When an agent produces something wrong, the instinct is to blame the model. Most of the time, the real cause is upstream: it was missing context a human in the same seat would have had automatically.

## What "context" actually includes

- **The codebase itself** — conventions, existing patterns, related files it should have read but didn't
- **The "why"** behind the task — a bug fix without knowing the original intent often gets "fixed" in a way that breaks something else
- **Constraints** — performance budgets, browser support, style guides, things that never show up in the code itself

## Feeding context deliberately

Don't assume the agent has read everything relevant. Point it at specific files, explain the constraint that isn't visible in the code, and state what's out of scope as clearly as what's in scope. A sentence like "don't touch the payment flow, it's mid-migration" prevents an entire class of bad diffs.

## The payoff

Every minute spent front-loading context is a minute saved reviewing a wrong-direction diff. This is the highest-leverage habit in vibecoding — more than any specific prompt phrasing.

Next: how to break large, ambiguous tasks into steps an agent can actually execute well.
