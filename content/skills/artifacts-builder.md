---
title: "Artifacts Builder"
description: "Structured guidance for building well-formed interactive artifacts — self-contained HTML apps, visualizations, and documents."
category: "Development"
platform: "Claude"
website: "https://github.com/anthropics/skills"
tags: ["artifacts", "frontend", "html"]
weight: 70
---

The Artifacts Builder skill covers the conventions for producing standalone, self-contained interactive outputs — inlined styles and scripts, responsive layout, no external dependencies that would break in a sandboxed viewer.

## Why a skill for this

Artifacts run in a constrained environment with specific rules about what they can and can't depend on. A skill that encodes those constraints up front avoids the trial-and-error of generating something that looks right locally but fails in the actual runtime.

## Good for

Interactive demos, data visualizations, and small self-contained tools meant to be shared as a single, working artifact rather than a project you have to set up.
