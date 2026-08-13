---
title: "GitHub"
description: "Connects an agent to GitHub — issues, pull requests, repo search, and code — through the GitHub API rather than raw git commands."
category: "Dev Tools"
publisher: "GitHub"
website: "https://github.com/github/github-mcp-server"
install: "npx -y @modelcontextprotocol/server-github"
tags: ["github", "git", "issues"]
weight: 20
---

The GitHub MCP server lets an agent create and comment on issues, open pull requests, search code and repositories, and manage branches — all through GitHub's API instead of shelling out to `git` and `gh` directly.

## Why it matters

Because it goes through the API, actions are consistent regardless of what's checked out locally, and it works for agents that don't have local git access at all — including cloud-based ones.

## Good for

Issue triage, PR description generation, and any workflow where the agent needs to interact with GitHub state beyond what's in your local clone.
