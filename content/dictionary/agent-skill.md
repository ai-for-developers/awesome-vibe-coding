---
title: "Agent Skill"
description: "A packaged set of instructions, and optionally scripts or reference files, that extends what an AI agent knows how to do — loaded only when relevant."
related: ["model-context-protocol", "agentic-loop", "system-prompt"]
---

An agent skill is a self-contained folder of instructions — plus, optionally, helper scripts or reference documents — that teaches an agent a specific procedure it wouldn't reliably do well from a generic [system prompt](/dictionary/system-prompt) alone, such as formatting a spreadsheet correctly or scaffolding an MCP server.

## How it differs from an MCP server

An [MCP](/dictionary/model-context-protocol) server gives an agent new capabilities — a connection to a database, an API, a file system. A skill doesn't add capabilities; it adds know-how, refining how the agent uses the abilities it already has for a specific kind of task.

## Why the packaging matters

Skills are only loaded into context when their description matches the task at hand, rather than sitting in the system prompt at all times. That keeps unrelated instructions from crowding out context on tasks that don't need them — see the full [Skills](/skills/) directory for examples.
