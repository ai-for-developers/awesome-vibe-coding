---
title: "Webapp Testing"
description: "Teaches an agent to actually verify a web app in a browser — clicking through flows and checking console output — before calling a task done."
category: "Development"
platform: "Cross-platform"
website: "https://github.com/anthropics/skills"
tags: ["testing", "browser", "qa"]
weight: 80
---

The Webapp Testing skill packages a verification workflow: launching a dev server, driving a browser through the golden path and edge cases, and checking console and network output for errors — rather than declaring a UI change complete after just reading the code.

## Why a skill for this

Type checks and unit tests verify correctness, not feature correctness. This skill closes that gap by making "did I actually see it work" a standard step rather than something that only happens if explicitly requested.

## Good for

Frontend changes, form flows, and any UI work where the definition of done includes "I watched it work in a real browser."
