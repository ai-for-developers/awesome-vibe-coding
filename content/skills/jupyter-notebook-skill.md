---
title: "Jupyter Notebook Skill"
description: "Curated Codex skill for authoring and editing Jupyter notebooks programmatically."
category: "Data & Analytics"
platform: "OpenAI Codex"
website: "https://github.com/openai/skills/tree/main/skills/.curated/jupyter-notebook"
tags: ["jupyter", "notebooks", "data"]
weight: 630
---

This curated Codex skill authors and edits Jupyter notebooks programmatically, handling the notebook's cell-and-metadata JSON structure correctly.

## Why a skill for this

Notebook files are structured JSON with execution metadata and outputs, not plain text — editing them without understanding that structure easily corrupts the file. A skill that knows the format keeps notebooks valid while editing.

## Good for

Data analysis or ML work that lives in Jupyter notebooks rather than plain scripts.
