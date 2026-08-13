---
title: "Context Rot"
description: "The tendency for a model's accuracy and focus to degrade as its context window fills up, even though the relevant information is technically still in there."
related: ["context-window", "context-engineering", "subagent"]
---

Models don't treat every token in their context window equally — attention tends to be strongest at the start and end of a long context and weaker in the middle. As a session accumulates file reads, search results, and tool output, the model has to search through more noise to find what's relevant, and its reliability on that information drops, even without hitting the hard context-window limit.

In agentic coding this shows up as an agent that was sharp for the first few steps of a task gradually losing track of earlier decisions, re-reading files it already read, or contradicting something it did ten steps ago.

## Why it matters

Long-running agent sessions benefit from periodic resets, summarization, or delegating side-quests to a [subagent](/dictionary/subagent) with a clean context, rather than letting one session run indefinitely.
