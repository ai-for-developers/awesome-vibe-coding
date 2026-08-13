---
title: "Retrieval-Augmented Generation (RAG)"
description: "A technique where a model looks up relevant information from an outside source — docs, code, a database — before answering, instead of relying only on what it memorized during training."
related: ["context-window", "embedding", "vector-database"]
---

RAG combines a search step with a generation step. Before the model writes its answer, a separate process retrieves the most relevant chunks of text from an external source — a set of docs, a codebase, a knowledge base — and inserts them into the [context window](/dictionary/context-window). The model then answers using that retrieved material rather than guessing from memory alone.

This is how many coding tools answer questions about a specific codebase or a library's current documentation: they don't expect the model to have memorized your repo, so they search it first and hand the model the relevant snippets. It's also how many "chat with your docs" products work.

## Why it matters

RAG is one of the main defenses against [hallucination](/dictionary/hallucination) — a model grounded in retrieved, real text is far less likely to invent an API that doesn't exist.
