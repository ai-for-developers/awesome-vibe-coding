---
title: "Prompt Engineering"
description: "The practice of structuring instructions to an AI model to reliably get the output you actually want."
related: ["system-prompt", "context-window"]
---

Prompt engineering is the practice of writing instructions — wording, structure, examples, constraints — so a model produces the output you actually intend, reliably, rather than something that merely looks plausible.

## What it looks like in coding contexts

For coding agents, this usually means being specific about scope ("only touch the auth module"), providing constraints that aren't visible in the code ("this needs to support offline mode"), and stating the definition of done rather than just a vague goal.

## A common misconception

Prompt engineering isn't about finding a magic phrase. The bigger lever is almost always context — pointing the agent at the right files, explaining the "why" behind a task — over any particular wording trick. See [Context Is the Whole Game](/posts/context-is-the-whole-game/).
