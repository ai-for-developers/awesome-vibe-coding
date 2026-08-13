---
title: "Embedding"
description: "A numeric representation of a piece of text that captures its meaning, so a computer can measure how similar two pieces of text are."
related: ["vector-database", "retrieval-augmented-generation", "repo-map"]
---

An embedding is a list of numbers (a vector) that a model produces for a piece of text, positioned so that texts with similar meaning end up with similar vectors — even if they don't share any of the same words. Comparing two embeddings mathematically gives a rough measure of how semantically related two pieces of text are.

Code search tools use this to find relevant code by meaning rather than exact keyword match — a search for "user login logic" can surface a function named `authenticate_session` because their embeddings are close, even though no words overlap.

## Why it matters

Understanding embeddings explains why an agent's search sometimes finds conceptually related code with none of your search terms in it — and also why it occasionally returns something superficially similar but actually irrelevant.
