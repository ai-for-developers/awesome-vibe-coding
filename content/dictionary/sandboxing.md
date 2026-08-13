---
title: "Sandboxing"
description: "Running an agent's commands and file changes inside an isolated environment — a container, VM, or restricted filesystem — so mistakes or malicious actions can't touch your real system."
related: ["yolo-mode", "tool-use", "prompt-injection"]
---

A sandbox limits what an agent's actions can actually affect: it might run in a disposable container with no network access, a copy of your repo instead of the original, or an OS-level permission boundary that blocks writes outside a specific folder. If something goes wrong — a bad command, a misunderstood instruction, a [prompt injection](/dictionary/prompt-injection) — the damage is contained to the sandbox instead of your real machine or production systems.

Many coding-agent tools offer this as a configurable setting, trading some convenience (the agent may need to ask before crossing the sandbox boundary) for a much smaller worst case.

## Why it matters

Sandboxing is what makes higher-autonomy settings like [YOLO mode](/dictionary/yolo-mode) reasonable to use at all — without it, letting an agent act without approval is a much bigger risk.
