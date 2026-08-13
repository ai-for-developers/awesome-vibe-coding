---
title: "CI Fix Skill"
description: "Curated Codex skill that diagnoses and fixes failing GitHub Actions CI runs."
category: "DevOps"
platform: "OpenAI Codex"
website: "https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci"
tags: ["github-actions", "ci", "devops"]
weight: 590
---

This curated Codex skill diagnoses and fixes failing GitHub Actions CI runs directly from the failure logs.

## Why a skill for this

CI failures are usually diagnosable from the log output alone, but pulling and parsing that log by hand is tedious. A skill that already knows how to fetch and read Actions logs shortens the loop from red CI to a fix.

## Good for

Quickly recovering from a broken CI run without manually digging through Actions logs first.
