---
title: "Chrome DevTools"
description: "Gives an agent direct access to Chrome DevTools — network requests, console messages, and performance traces — for debugging and profiling live pages, not just clicking through them."
category: "Browser Automation"
publisher: "Google"
website: "https://github.com/ChromeDevTools/chrome-devtools-mcp"
install: "npx chrome-devtools-mcp@latest"
tags: ["browser", "debugging", "performance", "devtools"]
weight: 110
---

Chrome DevTools MCP connects a coding agent to a live Chrome instance, exposing the same network, console, and performance-tracing tools available in DevTools. It lets an agent navigate pages, inspect requests, read console errors, and record performance traces from inside its own workflow.

## Why it matters

It closes the loop between writing frontend code and verifying it actually works and performs well in a real browser, rather than an agent guessing at runtime behavior.

## Good for

Debugging console errors, diagnosing slow page loads, and inspecting network activity while iterating on frontend code.
