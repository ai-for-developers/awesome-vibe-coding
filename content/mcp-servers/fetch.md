---
title: "Fetch"
description: "Retrieves a URL's content and converts it to clean markdown for an agent to read, with chunked pagination for long pages."
category: "Search & Web"
publisher: "Model Context Protocol project"
website: "https://github.com/modelcontextprotocol/servers/tree/main/src/fetch"
install: "uvx mcp-server-fetch"
tags: ["web", "scraping", "reference-server"]
weight: 190
---

The Fetch server retrieves a given URL and converts its HTML into clean markdown sized for an LLM context window, with a start-index parameter so an agent can page through long documents in chunks. It's one of the official reference servers in the modelcontextprotocol/servers repo.

## Why it matters

It gives an agent a simple, dependable way to read a specific webpage on demand — a targeted complement to a general search server like [Brave Search](/mcp-servers/brave-search).

## Good for

Pulling in a specific doc page, changelog, or article an agent has already been pointed to, rather than open-ended web search.
