---
title: "Engine"
description: "A repository-native harness for Claude Code and Codex that carries project state, memory, and build controls across sessions and prepares reviewable pull requests."
category: "Terminal Agent"
website: "https://github.com/StarshipSuperjam/engine-template"
pricing: "Free and open source (Apache-2.0); bring your own Claude Code or Codex"
tags: ["harness", "cli", "open-source", "memory"]
weight: 900
rank: 3
---

Engine sits on top of a terminal coding agent (Claude Code or Codex) and gives a project durable state, memory, decision records, and guardrails, so each session starts grounded instead of from scratch. Work reaches the main branch only through a pull request the operator approves and merges.

## Why it stands out

- **Persistent project memory.** State, decisions, and prior findings carry between sessions rather than being re-derived each time.
- **Deliberate build controls.** Building is opt-in per session, and changes are delivered as evidence-backed pull requests.
- **Host-agnostic.** Runs through whichever supported terminal agent you already use.

## Good for

Non-engineers and teams who want to direct and approve real project work without reading code, with continuity and review boundaries kept across sessions.
