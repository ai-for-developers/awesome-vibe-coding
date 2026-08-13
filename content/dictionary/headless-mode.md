---
title: "Headless Mode"
description: "Running an AI coding agent from a script or command line, without its interactive chat interface, so it can be triggered automatically — for example, in a CI pipeline."
related: ["yolo-mode", "sandboxing", "tool-use"]
---

Most coding agents default to an interactive mode: you type a request, watch it work, and respond to prompts. Headless mode strips that interface away — you pass in a task via a command-line flag or script, the agent runs to completion (or a defined stopping point) unattended, and the result comes back as output you can capture programmatically.

This is what makes it possible to wire an agent into automation: a CI job that asks an agent to fix a failing lint check, a script that runs the same review task across dozens of repos, or a scheduled job that summarizes new issues every morning.

## Why it matters

Headless runs are convenient for automation but remove the human-in-the-loop checkpoint entirely, so they're worth pairing with [sandboxing](/dictionary/sandboxing) and a tightly scoped task rather than an open-ended one.
