---
title: "Security Best Practices Skill"
description: "Curated Codex skill encoding secure-coding checklists applied during code generation and review."
category: "Development"
platform: "OpenAI Codex"
website: "https://github.com/openai/skills/tree/main/skills/.curated/security-best-practices"
tags: ["security", "code-review"]
weight: 600
---

This curated Codex skill applies a secure-coding checklist during code generation and review, catching common vulnerability classes as code is written.

## Why a skill for this

Security issues are cheaper to prevent during generation than to catch in a later review pass. Baking a checklist into the generation step catches classes of bugs before they're ever committed.

## Good for

Codebases that want baseline secure-coding practices enforced automatically rather than relying on a separate security review step.
