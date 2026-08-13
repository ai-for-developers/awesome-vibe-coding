---
title: "GitHub PR Review Skill"
description: "Curated Codex skill that reads GitHub PR review comments and drives the fixes back into the branch."
category: "DevOps"
platform: "OpenAI Codex"
website: "https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments"
tags: ["github", "pull-requests", "review"]
weight: 580
---

This curated Codex skill reads a GitHub pull request's review comments and drives the corresponding fixes back into the branch.

## Why a skill for this

Addressing review feedback is a mechanical loop — read a comment, make the matching change, reply — that's a good fit for automation once the skill knows how to map comments to specific diffs.

## Good for

Working through a batch of PR review comments without manually copying each one into a prompt.
