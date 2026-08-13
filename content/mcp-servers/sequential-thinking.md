---
title: "Sequential Thinking"
description: "Gives an agent a structured scratchpad for step-by-step reasoning — breaking a problem down, revising earlier steps, and exploring alternatives before committing to an answer."
category: "Reasoning & Planning"
publisher: "Model Context Protocol project"
website: "https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking"
install: "npx -y @modelcontextprotocol/server-sequential-thinking"
tags: ["reasoning", "planning", "reference-server"]
weight: 180
---

The Sequential Thinking server provides a single tool that lets an agent externalize a chain of reasoning as discrete, revisable steps rather than reasoning silently in one pass. The host model decides when to call it, and can branch, revise, or extend earlier steps as its understanding develops.

## Why it matters

Structuring reasoning as explicit, revisable steps makes an agent's problem-solving more transparent and lets it correct course mid-task instead of committing early to a wrong approach.

## Good for

Complex debugging, multi-step planning, and tasks where an agent benefits from visibly working through alternatives before acting.
