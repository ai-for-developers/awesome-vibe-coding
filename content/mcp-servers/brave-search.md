---
title: "Brave Search"
description: "Web and local search grounded in Brave's independent search index, giving agents up-to-date information beyond their training data."
category: "Search & Web"
publisher: "Brave"
website: "https://github.com/modelcontextprotocol/servers-archived/tree/main/src/brave-search"
install: "npx -y @modelcontextprotocol/server-brave-search"
tags: ["search", "web"]
weight: 60
---

The Brave Search server gives an agent access to web and local search results through Brave's Search API, without routing through another AI vendor's index.

## Why it matters

Models have a training cutoff and no innate awareness of anything after it. A search connector lets an agent verify current information — a library's latest version, a recent API change, a live status — instead of confidently guessing from stale training data.

## Good for

Fact-checking, researching current library versions and APIs before writing code against them, and any task where freshness matters more than the model's internal knowledge.
