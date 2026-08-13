---
title: "Context7"
description: "Fetches current, version-specific documentation and code examples for a named library straight into an agent's context, instead of relying on stale training data."
category: "Dev Tools"
publisher: "Upstash"
website: "https://github.com/upstash/context7"
install: "npx -y @upstash/context7-mcp"
tags: ["documentation", "libraries", "context"]
weight: 170
---

Context7 resolves a library name (like "Next.js" or "shadcn/ui") to a version-specific ID, then pulls current documentation and code snippets straight from the source into an agent's prompt. It works with no signup for basic usage, with a free API key available for higher rate limits.

## Why it matters

Coding agents routinely hallucinate APIs for libraries that shipped after their training cutoff or moved fast; Context7 fixes that by grounding answers in documentation fetched live rather than from memory.

## Good for

Working with fast-moving frameworks and libraries where an agent's built-in knowledge is likely outdated or wrong.
