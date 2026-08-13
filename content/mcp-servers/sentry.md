---
title: "Sentry"
description: "Pulls real error data and stack traces from Sentry directly into an agent's context, so bug fixes are grounded in what's actually failing."
category: "Dev Tools"
publisher: "Sentry"
website: "https://github.com/getsentry/sentry-mcp"
tags: ["errors", "monitoring", "debugging"]
weight: 90
---

The Sentry server gives an agent access to issues, stack traces, and event details from a Sentry project, so it can investigate a production error with the same data a human engineer would open the dashboard to see.

## Why it matters

Debugging from a vague description ("users are seeing errors on checkout") produces guesswork. Debugging from an actual stack trace, affected user count, and recent deploy correlation produces a targeted fix.

## Good for

Triaging production incidents, writing fixes grounded in real stack traces, and closing the loop between "an error happened" and "here's the diff that fixes it."
