---
title: "Agentic Loop"
description: "The plan → act → observe → repeat cycle an AI agent runs through to complete a multi-step task without a new prompt at every step."
related: ["repo-map", "yolo-mode", "context-window"]
---

An agentic loop is the repeating cycle an AI coding agent uses to complete a task on its own: it plans a next step, takes an action (reads a file, edits code, runs a command), observes the result, and decides what to do next — looping until the task is done or it needs your input.

This is what separates an "agent" from a plain chat assistant. A chat model answers one prompt at a time; an agent keeps going, using the output of its own actions to decide its next move.

## Why it matters

Understanding the loop helps you predict where an agent might go wrong: if an early step produces a bad observation (a misread file, a failed command it didn't notice), every subsequent step compounds that mistake. Reviewing intermediate steps — not just the final diff — catches this early.
