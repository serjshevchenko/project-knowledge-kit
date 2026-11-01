#!/usr/bin/env python3
"""Scaffold an AI-agnostic knowledge core and the selected runtime bootstrap."""
import argparse
from datetime import date
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
CORE = ROOT / "core" / "templates" / "project"
ADAPTERS = {
    "openai/chatgpt-project": ("platforms/openai/chatgpt-project.md", "PROJECT_INSTRUCTIONS.md"),
    "openai/codex": ("platforms/openai/codex.md", "AGENTS.md"),
    "anthropic/claude-project": ("platforms/anthropic/claude-project.md", "PROJECT_INSTRUCTIONS.md"),
    "anthropic/claude-code": ("platforms/anthropic/claude-code.md", "CLAUDE.md"),
    "google/gemini-app": ("platforms/google/gemini-app.md", "PROJECT_INSTRUCTIONS.md"),
    "google/gemini-cli": ("platforms/google/gemini-cli.md", "GEMINI.md"),
}

def render(content, values):
    for old, new in values.items():
        content = content.replace(old, new)
    return content

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--name", required=True)
    p.add_argument("--slug", required=True)
    p.add_argument("--platform", required=True, choices=sorted(ADAPTERS))
    p.add_argument("--storage-provider", required=True, choices=["github", "google-drive", "local", "other"])
    p.add_argument("--storage-root", default="UNCONFIGURED")
    p.add_argument("--rules-index-url", default="{{RULES_INDEX_URL}}")
    p.add_argument("--output", default="./out")
    a = p.parse_args()

    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", a.slug):
        p.error("slug must use lowercase letters, numbers, and hyphens")
    destination = Path(a.output).resolve() / a.slug
    if destination.exists():
        p.error(f"destination already exists: {destination}")
    source, bootstrap_name = ADAPTERS[a.platform]
    adapter = ROOT / source
    if not CORE.is_dir() or not adapter.is_file():
        p.error("core template or selected platform adapter missing")

    values = {
        "{{PROJECT_NAME}}": a.name,
        "{{INSTALL_DATE}}": date.today().isoformat(),
        "{{STORAGE_ROOT}}": a.storage_root,
        "{{RULES_INDEX_URL}}": a.rules_index_url,
    }
    items = []
    for file in sorted(CORE.rglob("*")):
        if file.is_file():
            relative = file.relative_to(CORE)
            content = file.read_text(encoding="utf-8")
            if relative == Path("README.md"):
                content = content.replace("PROJECT_INSTRUCTIONS.md", bootstrap_name)
            items.append((relative, render(content, values)))
    items.append((Path(bootstrap_name), render(adapter.read_text(encoding="utf-8"), values)))
    for path, content in items:
        out = destination / path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(content, encoding="utf-8")
    print(f"SCAFFOLDED {destination}")
    print(f"AI PLATFORM: {a.platform}; STORAGE PROVIDER: {a.storage_provider}")
    print(f"BOOTSTRAP: {bootstrap_name}")
    print("NEXT: publish files, apply bootstrap, verify target access and configuration")

if __name__ == "__main__":
    main()
