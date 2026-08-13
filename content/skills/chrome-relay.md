---
title: "Chrome Relay"
description: "Drives the user's already-signed-in Chrome session (cookies, SSO, localhost) through a local CLI bridge, as a real-browser counterpart to Playwright automation."
category: "Testing & QA"
platform: "Claude Code"
website: "https://chrome-relay.kushalsm.com/"
tags: ["browser", "automation", "chrome"]
weight: 370
---

Chrome Relay drives the user's already-signed-in Chrome session — cookies, SSO, localhost included — through a local CLI bridge, as a real-browser counterpart to headless Playwright automation.

## Why a skill for this

Some flows only work correctly inside an authenticated, already-logged-in browser session — SSO-gated internal tools, for instance. Relaying through the real Chrome session sidesteps re-authenticating a separate automated browser.

## Good for

Testing or automating flows that depend on an existing logged-in session rather than a fresh, unauthenticated browser.
