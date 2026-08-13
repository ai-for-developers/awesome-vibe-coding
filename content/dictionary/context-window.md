---
title: "Context Window"
description: "The amount of text — code, conversation, files — a model can 'see' at once when generating a response."
related: ["token", "repo-map", "hallucination"]
---

The context window is the maximum amount of text a model can hold in memory at one time, measured in tokens. Everything the model reasons about — your prompt, the conversation history, any files it has read — has to fit inside this window.

## Why it matters for vibecoding

When a codebase is larger than the context window, an agent can't just "read everything." It has to be selective — using search, file summaries, or a [repo map](/dictionary/repo-map) to decide what's relevant. This is a common source of mistakes: the agent edits code based on an incomplete picture because the relevant file was never loaded into context.

Feeding an agent the right files explicitly, rather than assuming it found them on its own, is one of the highest-leverage habits in prompting.
