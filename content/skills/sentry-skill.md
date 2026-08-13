---
title: "Sentry Triage Skill"
description: "Curated Codex skill for pulling and triaging error reports from Sentry."
category: "DevOps"
platform: "OpenAI Codex"
website: "https://github.com/openai/skills/tree/main/skills/.curated/sentry"
tags: ["sentry", "observability", "errors"]
weight: 620
---

This curated Codex skill pulls and triages error reports directly from Sentry, connecting production error data to the code that's causing it.

## Why a skill for this

Triaging errors well means correlating a stack trace with the actual code path and recent changes — something that's faster with direct Sentry access than copy-pasting error reports into a prompt.

## Good for

Debugging production errors surfaced in Sentry without manually transcribing stack traces.
