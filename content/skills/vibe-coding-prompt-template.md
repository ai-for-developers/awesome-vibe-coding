---
title: "Vibe-Coding Prompt Template"
description: "Five-step planning workflow that turns an idea into a PRD, a technical design, and the AGENTS.md instruction files an AI coding agent builds from."
category: "Development"
platform: "Cross-platform"
website: "https://github.com/KhazP/vibe-coding-prompt-template"
tags: ["planning", "spec-driven", "agents-md"]
weight: 700
---

Vibe-Coding Prompt Template covers the part of the workflow that happens before any code is written. Three staged prompts run in any chat tool take an idea through deep research, a PRD, and a technical design, each one making the model ask clarifying questions before it produces a document. A fourth step compiles those answers into `AGENTS.md` and `agent_docs/`.

The `npx vibeworkflow` CLI installs the planning skills into the agent and drives steps 1-4 as an interview, so the same workflow runs without copy-pasting prompts.

## Why a skill for this

Agents produce more consistent results when the scope, stack, and constraints are settled in a document they can re-read, rather than re-derived from chat history each session. Packaging the planning stages as skills makes that the starting point instead of an optional habit.

## Good for

New projects where the shape of the MVP is still open, and teams who want the same planning artifacts regardless of which agent does the building.
