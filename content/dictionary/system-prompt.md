---
title: "System Prompt"
description: "The standing set of instructions that shapes an AI model's behavior before any user message — tone, rules, tool access, and constraints."
related: ["prompt-engineering", "agentic-loop"]
---

A system prompt is a set of instructions given to a model before any conversation begins, establishing how it should behave, what tools it can use, and what rules it must follow — as distinct from the individual messages a user sends afterward.

## Why it matters for coding agents

In coding tools, the system prompt is typically where safety rules live: when to ask before running a destructive command, how to format diffs, whether to auto-commit changes. It's largely invisible to the end user but shapes the agent's behavior far more consistently than any single conversational prompt.

Understanding that a system prompt exists explains behavior that otherwise seems mysterious — like an agent consistently asking for confirmation before certain actions regardless of how you phrase your request.
