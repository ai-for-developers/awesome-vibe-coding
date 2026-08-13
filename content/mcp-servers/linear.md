---
title: "Linear"
description: "Connects an agent to Linear's issue tracker — creating, searching, and updating issues, projects, and cycles — through Linear's own hosted MCP endpoint."
category: "Productivity"
publisher: "Linear"
website: "https://linear.app/docs/mcp"
install: "claude mcp add --transport sse linear-server https://mcp.linear.app/sse"
tags: ["productivity", "issue-tracking", "project-management"]
weight: 130
---

Linear MCP is Linear's own hosted server, reachable at mcp.linear.app, that lets an agent create, update, and search issues, projects, and cycles in natural language instead of through the UI. It authenticates via OAuth on first connection rather than a static API token.

## Why it matters

It lets a coding agent close the loop on its own work — filing the bug it just found or updating the ticket it was assigned — without leaving the terminal.

## Good for

Agents that need to triage bugs, update ticket status, or turn code review findings directly into tracked issues.
