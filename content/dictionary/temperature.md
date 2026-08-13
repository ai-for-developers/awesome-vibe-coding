---
title: "Temperature"
description: "A setting that controls how random or deterministic a model's output is — low for consistency, high for variety."
related: ["hallucination", "token"]
---

Temperature is a parameter that controls how much randomness a model applies when choosing its next output token. Low temperature makes output more deterministic and focused; high temperature makes it more varied and, at the extreme, less coherent.

## Why it matters for coding

Most coding agents default to a low temperature, because code benefits from consistency far more than creative variety — you generally want the same reasonable answer each time, not a different stylistic take on every run. Higher temperatures show up more in brainstorming or naming suggestions than in actual code generation.

Temperature isn't something most vibecoding workflows need to touch directly, but it explains why the same prompt to the same model can occasionally produce slightly different results.
