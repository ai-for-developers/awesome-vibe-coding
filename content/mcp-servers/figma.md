---
title: "Figma"
description: "Connects an agent to a Figma file's Dev Mode data — component structure, styles, and layout — so it can generate code that matches an actual design instead of guessing."
category: "Dev Tools"
publisher: "Figma"
website: "https://developers.figma.com/docs/figma-mcp-server/"
install: "Enable Dev Mode MCP server in the Figma desktop app (local endpoint http://127.0.0.1:3845/mcp)"
tags: ["design", "frontend", "dev-mode", "ui"]
weight: 140
---

Figma's Dev Mode MCP server exposes a selected frame or component's structure, styles, and metadata directly to a coding agent, from either the Figma desktop app or a hosted endpoint. It lets an agent generate frontend code grounded in the real design file instead of a screenshot or description of it.

## Why it matters

It closes the design-to-code gap by giving an agent structured access to real design tokens and layout data, producing UI code that matches specs more closely than screenshot-based approaches.

## Good for

Turning a Figma design into React/CSS scaffolding and keeping implemented UI in sync with an evolving design file.
