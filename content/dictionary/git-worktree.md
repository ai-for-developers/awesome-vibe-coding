---
title: "Git Worktree"
description: "A Git feature that checks out another branch of the same repository into a separate folder, so work on that branch doesn't disturb your main checkout."
related: ["sandboxing", "subagent", "diff-review"]
---

Normally, a Git repository has one working directory tied to whichever branch you've checked out — switching branches changes the files on disk. A worktree lets you attach a second (or third) working directory to the same repository, each checked out to a different branch, all sharing the same underlying Git history.

This has become a common way to run AI agents: give an agent its own worktree to work in, and it can make changes, run commands, and even commit — all without touching the files you currently have open, and without the risk of it stepping on work you haven't committed yet. Running several agents in parallel, each in its own worktree, is a common pattern for tackling independent tasks at once.

## Why it matters

A dedicated worktree gives an agent room to experiment freely while keeping your own working directory untouched, and mergeable back only when you're ready to review it via [diff review](/dictionary/diff-review).
