---
title: "FFUF Web Fuzzing"
description: "Integrates the ffuf web fuzzer so Claude can run authenticated fuzzing, auto-calibration, and vulnerability analysis during penetration tests."
category: "Testing & QA"
platform: "Claude Code"
website: "https://github.com/jthack/ffuf_claude_skill"
tags: ["security", "pentesting", "fuzzing"]
weight: 220
---

This skill integrates the ffuf web fuzzer, letting Claude run authenticated fuzzing scans, auto-calibrate for noisy responses, and analyze results for real vulnerabilities during a penetration test.

## Why a skill for this

Fuzzing tools have enough flags and calibration nuance that getting authenticated, low-noise scans right by hand takes real fuzzer expertise. Packaging that expertise as a skill makes competent fuzzing runs repeatable for anyone using it.

## Good for

Authorized penetration testing engagements that need automated web endpoint fuzzing as part of the workflow.
