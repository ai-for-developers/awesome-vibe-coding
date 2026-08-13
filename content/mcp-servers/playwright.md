---
title: "Playwright"
description: "Drives real Chromium, Firefox, and WebKit browsers through structured accessibility-tree snapshots, letting an agent click, fill forms, and navigate pages without screenshots or vision models."
category: "Browser Automation"
publisher: "Microsoft"
website: "https://github.com/microsoft/playwright-mcp"
install: "npx @playwright/mcp@latest"
tags: ["browser", "automation", "testing", "playwright"]
weight: 100
---

Playwright MCP gives an agent structured control over a real browser — Chromium, Firefox, or WebKit — using Playwright's accessibility tree instead of pixel-based screenshots. It exposes tools for navigation, clicking, form filling, and page inspection so an agent can complete multi-step web tasks deterministically.

## Why it matters

Reading the accessibility tree rather than rendering screenshots makes it faster and cheaper on tokens than vision-based automation, which is a large part of why it's become the most widely used browser MCP server in the ecosystem.

## Good for

End-to-end web testing, scraping behind login walls, and any workflow where an agent needs to operate a real website the way a human would.
