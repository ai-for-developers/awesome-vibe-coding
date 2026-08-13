---
title: "Repo Map"
description: "A lightweight summary of a codebase's structure that lets an agent reason about files it hasn't fully read into context."
related: ["context-window", "agentic-loop"]
---

A repo map is a condensed representation of a codebase — file names, function and class signatures, import relationships — that gives an agent a sense of the overall structure without loading every file's full contents into its [context window](/dictionary/context-window).

## Why it exists

Most real codebases are far larger than any model's context window. A repo map lets an agent make reasonable decisions about *where* to look before it commits to reading full files — similar to how a human skims a project's folder structure before diving into a specific module.

## Where you'll see it

Tools like Aider popularized explicit repo maps, but the underlying idea — search and summarize before reading everything — shows up across most terminal and IDE-based coding agents in some form.
