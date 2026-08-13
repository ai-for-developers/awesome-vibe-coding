---
title: "Extended Thinking"
description: "A mode where a model spends extra computation reasoning through a problem step by step before giving its final answer, often shown to the user as a separate thinking section."
related: ["chain-of-thought", "temperature", "prompt-engineering"]
---

Extended thinking is a setting, available in several current coding-agent tools, that lets a model work through a harder problem in a visible intermediate stage before committing to a final response or action. Rather than answering immediately, it reasons out loud — weighing tradeoffs, checking assumptions — and that reasoning is often surfaced to the user as a collapsible "thinking" block separate from the final answer.

It tends to help most on genuinely hard problems — debugging a subtle failure, choosing between architectural approaches — and costs more time and tokens, so it's typically not worth turning on for simple, mechanical edits.

## Why it matters

Reading the thinking trace, not just the final diff, is one of the best ways to catch a flawed plan before the agent acts on it.
