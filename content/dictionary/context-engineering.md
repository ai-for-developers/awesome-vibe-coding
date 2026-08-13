---
title: "Context Engineering"
description: "The practice of deliberately curating what information goes into an agent's context window — and what gets left out — rather than just wording a single prompt well."
related: ["context-window", "repo-map", "context-rot"]
---

Context engineering is [prompt engineering](/dictionary/prompt-engineering)'s broader successor. Instead of focusing only on how you phrase an instruction, it's about managing the whole working set the agent sees: which files get loaded, which past turns are kept or summarized, which tool outputs are retained, and what gets trimmed. As agents run longer, multi-step tasks, this curation matters more than any single sentence of instruction.

In practice this looks like giving an agent a [repo map](/dictionary/repo-map) instead of dumping every file, summarizing a long tool output before it re-enters context, or writing progress notes to a file so the agent doesn't need to hold everything in memory at once.

## Why it matters

A well-curated context often produces a better result than a longer, more detailed prompt — what the agent can see matters as much as what it's told to do.
