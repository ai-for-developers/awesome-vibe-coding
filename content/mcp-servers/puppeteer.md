---
title: "Puppeteer"
description: "Browser automation for agents — navigate pages, click, fill forms, and take screenshots through a headless Chrome instance."
category: "Browser Automation"
publisher: "Community"
website: "https://github.com/modelcontextprotocol/servers-archived/tree/main/src/puppeteer"
install: "npx -y @modelcontextprotocol/server-puppeteer"
tags: ["browser", "automation", "testing"]
weight: 50
---

The Puppeteer server gives an agent control of a real (or headless) Chrome browser — navigating to URLs, clicking elements, filling in forms, and capturing screenshots as it goes.

## Why it matters

Some tasks can only be verified by actually looking at rendered output — a UI change, a broken layout, a JavaScript-heavy page that a plain HTTP fetch can't render. Browser automation closes that verification gap.

## Good for

End-to-end testing, scraping content from JS-rendered sites, and visually confirming that a frontend change actually looks right.
