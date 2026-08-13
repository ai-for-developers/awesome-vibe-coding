---
title: "Claude API"
description: "Reference for building Claude-powered applications — current model IDs, pricing, streaming, tool use, MCP, and SDK usage patterns, used to counter stale training-data assumptions about the API."
category: "Development"
platform: "Cross-platform"
website: "https://github.com/anthropics/skills"
tags: ["api", "sdk", "llm", "reference"]
weight: 110
---

The Claude API skill is a language-aware reference for the Anthropic SDK and Messages API — model selection, adaptive thinking, streaming, prompt caching, token counting, and tool/MCP integration — with explicit guidance to verify API shapes against live docs rather than a model's memorized training data.

## Why a skill for this

Claude API surfaces like model names, parameters, and SDK method signatures change faster than a model's training cutoff, so ad hoc prompting reliably produces outdated model IDs or deprecated call patterns. Packaging current reference material and a "verify before writing" rule avoids that drift.

## Good for

Any task that adds or modifies code calling the Claude/Anthropic SDK, agent or MCP tool definitions, or LLM-powered application logic.
