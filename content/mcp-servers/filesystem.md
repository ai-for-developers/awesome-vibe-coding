---
title: "Filesystem"
description: "Gives an agent read/write access to a specified local directory tree, with configurable path allow-listing."
category: "Dev Tools"
publisher: "Anthropic (reference server)"
website: "https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem"
install: "npx -y @modelcontextprotocol/server-filesystem /path/to/allowed/dir"
tags: ["files", "local", "reference"]
weight: 10
---

The Filesystem server exposes a sandboxed slice of your local disk to an agent — reading, writing, listing, and searching files within directories you explicitly allow.

## Why it matters

It's one of the original reference MCP servers, and the clearest example of the protocol's core promise: instead of every agent vendor writing its own file-access layer, any MCP-compatible client can use this one server.

## Good for

Local automation tasks — bulk file operations, project scaffolding, log inspection — where you want tight control over exactly which directories an agent can touch.
