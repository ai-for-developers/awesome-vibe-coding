---
title: "Slack GIF Creator"
description: "Builds animated GIFs sized and optimized for Slack — emoji or message dimensions, frame rate, color count — using frame-by-frame generation and validation utilities."
category: "Design"
platform: "Cross-platform"
website: "https://github.com/anthropics/skills"
tags: ["gif", "slack", "animation"]
weight: 160
---

Slack GIF Creator packages Slack's specific GIF constraints — 128×128 for emoji, 480×480 for messages, 10–30fps, 48–128 colors, sub-3-second emoji duration — along with a frame-building workflow and validation tools, so requests like "make a GIF of X doing Y for Slack" produce a file that actually fits Slack's limits.

## Why a skill for this

Slack's dimension, frame-rate, and file-size constraints are easy to get wrong without a reference, and re-deriving them per request wastes iteration. Packaging the constraints plus a working frame-builder gets to a compliant GIF in one pass.

## Good for

Custom Slack emoji or message GIFs where the output needs to meet Slack's upload constraints on the first try.
