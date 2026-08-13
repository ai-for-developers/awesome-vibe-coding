---
title: "DOCX"
description: "Gives an agent structured knowledge of the Word document format, so it can create and edit .docx files with correct formatting and styles."
category: "Document Processing"
platform: "Claude"
website: "https://github.com/anthropics/skills"
tags: ["word", "documents"]
weight: 20
---

The DOCX skill covers creating and editing Microsoft Word documents programmatically — headings, styles, tables, tracked changes — in a way that produces files that open correctly in Word rather than malformed XML.

## Why a skill for this

The .docx format is a zipped bundle of XML with its own conventions for styling and structure. Getting it right without dedicated guidance is easy to get subtly wrong — broken styles, missing metadata, documents that "look fine" but corrupt in Word.

## Good for

Generating reports, contracts, or letters from structured data, and making precise edits to existing Word documents without breaking their formatting.
