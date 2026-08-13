---
title: "Stripe"
description: "Connects an agent to the Stripe API — customers, payments, subscriptions, and invoices — letting it query and manage billing data through function calls instead of raw API requests."
category: "Dev Tools"
publisher: "Stripe"
website: "https://github.com/stripe/agent-toolkit"
install: "npx -y @stripe/mcp --tools=all --api-key=YOUR_STRIPE_SECRET_KEY"
tags: ["payments", "billing", "api"]
weight: 150
---

Stripe's official MCP server exposes its payments API — customers, charges, subscriptions, refunds, invoices — as tools an agent can call directly, available as a local npx package or Stripe's hosted remote endpoint. It's part of Stripe's broader agent toolkit for LLM framework integration.

## Why it matters

It lets an agent debug a failed payment, check a customer's subscription status, or issue a refund without a developer manually digging through the Stripe dashboard.

## Good for

Debugging billing issues, testing payment flows during development, and building support tooling on top of Stripe data.
