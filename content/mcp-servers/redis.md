---
title: "Redis"
description: "Connects an agent to a Redis instance — keys, hashes, lists, streams, and vector search — through Redis's own natural-language MCP interface."
category: "Data & Storage"
publisher: "Redis"
website: "https://github.com/redis/mcp-redis"
install: "uvx --from redis-mcp-server@latest redis-mcp-server --url redis://localhost:6379/0"
tags: ["database", "cache", "vector-search"]
weight: 200
---

Redis's official MCP server lets an agent read and write Redis data structures — strings, hashes, lists, sets, streams — and run vector similarity search, using natural language instead of raw Redis commands. It connects to any reachable Redis instance via a connection URL.

## Why it matters

It gives an agent direct, structured access to the cache or session store an application actually runs on, useful for debugging state or wiring up retrieval without leaving the coding session.

## Good for

Inspecting and debugging cached or session data, and building or testing Redis-backed vector search during development.
