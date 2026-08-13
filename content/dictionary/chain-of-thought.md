---
title: "Chain of Thought"
description: "The step-by-step reasoning a model produces on the way to an answer, rather than jumping straight from question to conclusion."
related: ["extended-thinking", "prompt-engineering", "hallucination"]
---

Chain of thought refers to breaking a problem into intermediate reasoning steps instead of answering in one leap — either because the model does this naturally or because it's explicitly prompted to ("think step by step"). It's the underlying technique that [extended thinking](/dictionary/extended-thinking) builds on: the model is more likely to reach a correct answer on a multi-step problem when it works through the intermediate logic rather than pattern-matching straight to an output.

You'll see this referenced constantly in discussions of how models solve coding problems — a model that reasons "first check what the function currently returns, then trace where it's called, then decide what breaks" is using chain of thought, whether or not that reasoning is shown to you.

## Why it matters

When an agent gets something wrong, the chain of thought — if visible — usually shows you where the reasoning went off track, often more useful for debugging its behavior than the final answer alone.
