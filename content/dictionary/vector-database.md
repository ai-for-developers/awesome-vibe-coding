---
title: "Vector Database"
description: "A database built to store embeddings and quickly find the ones most similar to a given query — the engine behind most semantic search and RAG systems."
related: ["embedding", "retrieval-augmented-generation", "repo-map"]
---

A vector database indexes [embeddings](/dictionary/embedding) so that, given a new query, it can quickly return the most similar entries out of potentially millions — a search that would be far too slow to do by brute-force comparison. It's the storage-and-retrieval layer that most semantic search and [RAG](/dictionary/retrieval-augmented-generation) systems sit on top of.

When a coding tool says it has "indexed your codebase" for AI search, it typically means it generated embeddings for your files or functions and stored them in a vector database, so it can retrieve relevant code fast when the agent needs context.

## Why it matters

If a tool's codebase search feels stale after a big refactor, it's often because the vector database's index hasn't caught up yet — worth knowing when an agent seems to be working from outdated code.
