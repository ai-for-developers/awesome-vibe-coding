---
title: "Tool Use (Function Calling)"
description: "The mechanism that lets a model call external functions — read a file, run a command, query an API — instead of only producing text."
related: ["agentic-loop", "model-context-protocol", "sandboxing"]
---

On its own, a language model just predicts text. Tool use (also called function calling) is the layer that lets it take real actions: the model is given a list of available functions with descriptions of what they do, and when it decides one is needed, it outputs a structured request to call it — the surrounding system executes the function and feeds the result back in.

This is the mechanical foundation underneath every AI coding agent's ability to read files, edit code, or run a test suite. [Model Context Protocol](/dictionary/model-context-protocol) is one standardized way of exposing tools to a model; tool use is the more general capability that makes it possible.

## Why it matters

Knowing exactly which tools an agent has been given tells you the real blast radius of what it can do to your system — not just what it can say.
