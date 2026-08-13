---
title: "Notion"
description: "Connects an agent to a Notion workspace's pages, databases, and blocks through Notion's own API, letting it search, read, and edit workspace content directly."
category: "Productivity"
publisher: "Notion Labs"
website: "https://github.com/makenotion/notion-mcp-server"
install: "npx -y @notionhq/notion-mcp-server"
tags: ["productivity", "notes", "wiki", "database"]
weight: 120
---

Notion MCP exposes a workspace's pages, databases, and blocks to an agent through Notion's API, so it can search, read, and edit content without a human copying text back and forth. It's available both as a locally run npm package and a hosted remote endpoint.

## Why it matters

Notion is a default home for specs, docs, and trackers at many teams, so giving an agent native read/write access turns it into a live source of context rather than a copy-pasted snapshot.

## Good for

Pulling requirements or specs into a coding session and writing notes, task updates, or documentation back into a team's Notion workspace.
