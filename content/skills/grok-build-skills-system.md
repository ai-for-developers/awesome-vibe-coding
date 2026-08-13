---
title: "Grok Build Skills System"
description: "xAI Grok Build's SKILL.md skills system, reading .grok/skills/, plugin skill dirs, and directly Claude Code-compatible."
category: "Development"
platform: "xAI Grok"
website: "https://docs.x.ai/build/features/skills-plugins-marketplaces"
tags: ["grok", "xai", "skill-md"]
weight: 690
---

Grok Build's skills system reads SKILL.md skills from `.grok/skills/`, `~/.grok/skills/`, and plugin directories — and is directly Claude Code-compatible, reading `.claude/skills` and `CLAUDE.md` with zero extra configuration.

## Why a skill for this

Direct compatibility with Claude Code's own skill and config files means a project that's already set up for Claude Code works in Grok Build without any migration step.

## Good for

Teams already using Claude Code skills who want to try Grok Build without re-authoring anything.
