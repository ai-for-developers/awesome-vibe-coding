---
title: "MCP (Model Context Protocol)"
description: "An open standard that lets AI agents connect to external tools and data sources — databases, APIs, file systems — through a common interface."
related: ["agentic-loop", "context-window"]
---

MCP (Model Context Protocol) is an open standard for connecting AI agents to external systems — a database, a project management tool, an internal API — through a single, consistent interface instead of a custom integration for every tool.

## Why it matters

Before MCP, giving an agent access to, say, your ticketing system meant a bespoke integration for each agent and each tool. MCP standardizes this: any MCP-compatible agent can talk to any MCP-compatible server, so tool authors build one integration and every supporting agent can use it.

In practice, this is what lets a coding agent reach beyond the local filesystem — checking a linked issue tracker, querying a database schema, or pulling design specs — without hand-rolled glue code.
