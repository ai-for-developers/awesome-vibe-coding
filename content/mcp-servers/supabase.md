---
title: "Supabase"
description: "Connects an agent to a Supabase project's Postgres schema, table data, Edge Functions, and configuration through Supabase's own MCP server."
category: "Data & Storage"
publisher: "Supabase"
website: "https://github.com/supabase-community/supabase-mcp"
install: "npx -y @supabase/mcp-server-supabase@latest --read-only --project-ref=<your-project-ref>"
tags: ["database", "postgres", "backend"]
weight: 210
---

Supabase's official MCP server gives an agent access to a Supabase project's Postgres schema and data, Edge Functions, and project configuration, with a read-only mode for safer exploratory use. It's built and maintained directly by the Supabase team.

## Why it matters

It lets an agent building on Supabase inspect and modify the actual backend it's targeting — schema, data, functions — instead of working from a developer's description of it.

## Good for

Schema-aware code generation, debugging data issues, and managing a Supabase-backed app's backend from within a coding session.
