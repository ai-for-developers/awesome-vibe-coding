---
title: "Prompt Caching"
description: "A feature that lets a model reuse previously processed parts of a prompt — like a long system prompt or file — instead of reprocessing them on every request."
related: ["system-prompt", "context-window", "token"]
---

When a model processes a prompt, it does real computational work to "read" every token, even ones it's seen before. Prompt caching lets a provider skip that repeated work for content that hasn't changed since the last call — a long [system prompt](/dictionary/system-prompt), a set of tool definitions, a large file — storing an intermediate representation and reusing it, rather than recomputing from scratch each time.

Coding agents lean on this heavily: a session's system prompt, tool descriptions, and loaded files are often identical or nearly identical from one step to the next, so caching them keeps repeated calls within a session noticeably faster and cheaper.

## Why it matters

This is part of why keeping a stable, unchanging context — rather than shuffling instructions around between calls — tends to make an agent both faster and less expensive to run.
