---
title: "Memory"
description: "A simple knowledge-graph server that gives an agent persistent memory across sessions instead of starting from zero every conversation."
category: "Data & Storage"
publisher: "Anthropic (reference server)"
website: "https://github.com/modelcontextprotocol/servers/tree/main/src/memory"
install: "npx -y @modelcontextprotocol/server-memory"
tags: ["memory", "reference", "persistence"]
weight: 70
---

The Memory server stores facts as a local knowledge graph — entities, relationships, observations — that persists between sessions, giving an agent a lightweight, inspectable form of long-term memory.

## Why it matters

Without persistence, every new conversation starts with zero context about you, your preferences, or past decisions. A local, file-backed memory store closes that gap without relying on a specific vendor's built-in memory feature.

## Good for

Personal assistants and long-running projects where an agent benefits from remembering user preferences, past decisions, or project facts across many separate sessions.
