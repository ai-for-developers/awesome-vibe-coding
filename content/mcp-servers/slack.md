---
title: "Slack"
description: "Lets an agent read channel history, search messages, and post to Slack — useful for status updates, triage bots, and workspace search."
category: "Productivity"
publisher: "Community"
website: "https://github.com/modelcontextprotocol/servers-archived/tree/main/src/slack"
install: "npx -y @modelcontextprotocol/server-slack"
tags: ["slack", "messaging", "productivity"]
weight: 40
---

The Slack server connects an agent to a workspace — listing channels, reading recent messages, searching history, and posting replies — using a bot token scoped to whatever permissions you grant it.

## Why it matters

A lot of project context lives in Slack threads, not in the codebase. Giving an agent read access closes that gap for tasks like "what did we decide about X" without you manually copy-pasting a thread into the prompt.

## Good for

Summarizing discussion threads, posting automated status updates, and building lightweight triage or notification bots.
