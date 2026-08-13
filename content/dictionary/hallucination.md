---
title: "Hallucination"
description: "When a model confidently produces something false — a function that doesn't exist, a library that isn't installed, a fact that isn't true."
related: ["diff-review", "context-window"]
---

A hallucination is output that's stated with full confidence but isn't grounded in reality — an AI referencing a function that was never defined, importing a package that was never installed, or describing behavior a piece of code doesn't actually have.

## Why it happens in coding contexts

Models generate the most statistically plausible next tokens, not verified facts. When a codebase's actual state isn't in the model's context, it will often generate code that *looks* like it belongs — matching naming conventions and patterns it has seen elsewhere — without that code corresponding to anything real in your project.

## How to catch it

Run the code. A hallucinated import or method call fails immediately at runtime or in a type-checker, which is why "trust but verify by executing" is a core habit — never approve a diff purely by reading it.
