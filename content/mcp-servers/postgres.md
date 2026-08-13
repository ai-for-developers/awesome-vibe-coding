---
title: "Postgres"
description: "Read-only access to a Postgres database's schema and data, so an agent can answer questions and write queries grounded in your real data."
category: "Data & Storage"
publisher: "Community"
website: "https://github.com/modelcontextprotocol/servers-archived/tree/main/src/postgres"
install: "npx -y @modelcontextprotocol/server-postgres postgresql://localhost/mydb"
tags: ["database", "sql", "data"]
weight: 30
---

The Postgres server gives an agent introspection into a database's schema — tables, columns, relationships — and the ability to run read-only queries against it.

## Why it matters

Without this, an agent writing SQL is guessing at your schema from memory or from whatever you paste in. With direct, read-only access, it can verify a query actually runs and returns the shape of data you expect before you ever run it yourself.

## Good for

Writing and debugging SQL, exploring an unfamiliar schema, and building reports or dashboards grounded in real table structure.
