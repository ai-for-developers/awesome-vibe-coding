#!/usr/bin/env python3
"""Generate README.md (Awesome Vibe Coding list) from content/ front matter.

Run from the repo root: python3 scripts/generate_readme.py
"""

import os
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(REPO_ROOT, "content")
BASE_URL = "https://vibecoding.rest"

SECTIONS = [
    {"dir": "tools", "title": "Tools", "group_field": "category", "use_rank": True},
    {"dir": "models", "title": "Models", "group_field": "provider", "use_rank": True},
    {"dir": "mcp-servers", "title": "MCP Servers", "group_field": "category", "use_rank": False},
    {"dir": "skills", "title": "Skills", "group_field": "category", "use_rank": False},
    {"dir": "resources", "title": "Resources", "group_field": "category", "use_rank": False},
]


def strip_quotes(value):
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
        return value[1:-1]
    return value


def parse_value(value):
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [strip_quotes(v) for v in inner.split(",")]
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    try:
        return int(value)
    except ValueError:
        pass
    if value in ("true", "false"):
        return value == "true"
    return strip_quotes(value)


def parse_front_matter(text):
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, text
    fm_lines = []
    body_start = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            body_start = i + 1
            break
        fm_lines.append(line)
    if body_start is None:
        return {}, text
    data = {}
    for line in fm_lines:
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, _, value = line.partition(":")
        data[key.strip()] = parse_value(value)
    return data, "\n".join(lines[body_start:])


def load_entries(section):
    section_dir = os.path.join(CONTENT_DIR, section["dir"])
    entries = []
    for filename in sorted(os.listdir(section_dir)):
        if not filename.endswith(".md") or filename == "_index.md":
            continue
        slug = filename[:-3]
        with open(os.path.join(section_dir, filename), encoding="utf-8") as f:
            data, _ = parse_front_matter(f.read())
        entries.append(
            {
                "title": data.get("title", slug),
                "description": (data.get("description") or "").strip(),
                "website": data.get("website"),
                "group": data.get(section["group_field"]) or "Other",
                "rank": data.get("rank", 0) or 0,
                "weight": data.get("weight", 0) or 0,
                "url": f"{BASE_URL}/{section['dir']}/{slug}/",
            }
        )
    return entries


def sort_key(entry, use_rank):
    if use_rank:
        return (-entry["rank"], entry["title"].lower())
    return (entry["weight"], entry["title"].lower())


def md_escape(text):
    return (text or "").replace("\n", " ").strip()


def build_readme():
    lines = []
    lines.append("# Awesome Vibe Coding")
    lines.append("")
    lines.append("[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
    lines.append("")
    lines.append(
        "> A curated, GitHub-style awesome list of AI coding tools, models, MCP "
        "servers, skills, and resources for vibe coding — building software by "
        f"collaborating with AI. Auto-generated from [vibecoding.rest]({BASE_URL}), "
        "which also has full write-ups, filtering, and a blog."
    )
    lines.append("")
    lines.append("## Contents")
    lines.append("")
    for section in SECTIONS:
        anchor = section["title"].lower().replace(" ", "-")
        lines.append(f"- [{section['title']}](#{anchor})")
    lines.append("")

    for section in SECTIONS:
        entries = load_entries(section)
        groups = {}
        for entry in entries:
            groups.setdefault(entry["group"], []).append(entry)

        lines.append(f"## {section['title']}")
        lines.append("")
        for group_name in sorted(groups.keys()):
            lines.append(f"### {group_name}")
            lines.append("")
            group_entries = sorted(
                groups[group_name], key=lambda e: sort_key(e, section["use_rank"])
            )
            for entry in group_entries:
                title = md_escape(entry["title"])
                desc = md_escape(entry["description"])
                website = entry["website"]
                review_url = entry["url"]
                if website:
                    lines.append(
                        f"- [{title}]({website}) — {desc} "
                        f"([review]({review_url}))"
                    )
                else:
                    lines.append(f"- [{title}]({review_url}) — {desc}")
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(
        f"Generated automatically from the content on [vibecoding.rest]({BASE_URL}). "
        "Do not edit this file by hand — changes will be overwritten."
    )
    lines.append("")
    return "\n".join(lines)


def main():
    readme = build_readme()
    with open(os.path.join(REPO_ROOT, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme)
    print(f"Wrote README.md ({len(readme)} bytes)")


if __name__ == "__main__":
    main()
