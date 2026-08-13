---
title: "Cloudflare"
description: "Connects an agent to a Cloudflare account — Workers, D1 databases, KV, R2 storage, and DNS — through Cloudflare's unified hosted MCP server."
category: "Dev Tools"
publisher: "Cloudflare"
website: "https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/"
install: "Remote endpoint https://mcp.cloudflare.com/mcp (connect via mcp-remote or a client's native remote-MCP support)"
tags: ["cloud", "infrastructure", "workers"]
weight: 160
---

Cloudflare's official MCP server gives an agent access to a Cloudflare account — deploying Workers, querying D1 databases, managing KV namespaces and R2 buckets, and more — through a single hosted endpoint using code-execution-style tools.

## Why it matters

It lets an agent manage real cloud infrastructure conversationally, from deploying a Worker to inspecting DNS records, without switching to the dashboard or CLI.

## Good for

Deploying and debugging Cloudflare Workers, managing edge storage, and infrastructure tasks during active development.
