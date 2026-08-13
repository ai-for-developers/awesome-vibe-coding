---
title: "Subagent"
description: "A secondary AI agent that a main agent spins up to handle part of a task — often with its own clean context — then reports results back to the main conversation."
related: ["agentic-loop", "context-rot", "context-window"]
---

Instead of one agent doing everything in a single, ever-growing context, a main agent can delegate a self-contained piece of work — researching how a library's API works, searching a large codebase for a pattern — to a subagent. That subagent runs its own mini [agentic loop](/dictionary/agentic-loop) in an isolated context, then returns a summary, keeping the noisy intermediate steps (file reads, failed searches) out of the main conversation.

This multi-agent pattern is increasingly common in coding tools as a way to manage [context rot](/dictionary/context-rot): a focused subagent can dig through fifty files and only the useful conclusion comes back, rather than all fifty files' worth of tokens.

## Why it matters

Subagents keep the main task focused and let work happen in parallel, but each one adds coordination overhead and cost — they're worth it for genuinely separable side-quests, not every small step.
