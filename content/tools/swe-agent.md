---
title: "SWE-agent"
description: "An open-source agent from Princeton NLP that autonomously resolves GitHub issues by giving an LLM a purpose-built interface for browsing, editing, and testing code."
category: "AI Coding Agent"
website: "https://swe-agent.com"
pricing: "Open source, free (bring your own model API key)"
tags: ["open-source", "research", "issue-resolution"]
weight: 590
rank: 5
---

SWE-agent wraps an LLM in an "Agent-Computer Interface" — a constrained set of commands for viewing, searching, and editing files and running tests — so it can work through real GitHub issues end-to-end. It's the reference agent behind much of the SWE-bench benchmark work.

## Why it stands out

- **Purpose-built tool interface**, rather than a raw shell, which the Princeton team found meaningfully improves how reliably the model edits and verifies code.
- **Benchmark pedigree.** It's the agent most closely associated with SWE-bench, the standard academic benchmark for autonomous issue resolution.
- **Fully open source**, so researchers and teams can inspect, fork, and swap in their own models or tool definitions.

## Good for

Researchers and engineers who want a transparent, hackable reference implementation of an autonomous issue-resolving coding agent.
