---
title: "Token"
description: "The basic unit of text a language model reads and generates — roughly a word or word-fragment, and the unit context windows are measured in."
related: ["context-window", "temperature"]
---

A token is the basic unit of text a language model processes — often a whole short word, but sometimes a fragment of a longer word or a piece of punctuation. Models don't read raw characters; they read sequences of tokens.

## Why it matters practically

Two things in vibecoding are measured in tokens: the [context window](/dictionary/context-window) (how much a model can consider at once) and, for API-based tools, cost (usage is typically billed per token, input and output separately). A large file or a long conversation history consumes tokens quickly, which is part of why agents summarize, search, and selectively read rather than loading everything at once.
