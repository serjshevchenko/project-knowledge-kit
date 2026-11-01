#!/usr/bin/env python3
"""Validate Project Knowledge Kit scaffold files and runtime placeholders."""
import argparse
from pathlib import Path

REQUIRED = ["README.md", "CHANGELOG.md", "PROJECT_INSTRUCTIONS.md",
"agent-rules/INDEX.md", "agent-rules/context-routing.md",
"agent-rules/project-specific.md", "agent-rules/source-management.md",
"agent-rules/changelog-policy.md", "agent-rules/storage-rules.md",
"agent-rules/documentation-style.md", "sources/overview.md"]

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("directory", type=Path)
    p.add_argument("--runtime-ready", action="store_true")
    a = p.parse_args()
    root = a.directory
    errors = [f"missing {f}" for f in REQUIRED if not (root/f).is_file()]
    if a.runtime_ready:
        for f in root.rglob("*.md"):
            s = f.read_text(encoding="utf-8")
            if "{{" in s or "}}" in s: errors.append(f"unresolved template in {f}")
        config = root/"agent-rules/project-specific.md"
        if config.is_file() and "UNCONFIGURED" in config.read_text(encoding="utf-8"):
            errors.append("storage root is UNCONFIGURED")
    if errors: raise SystemExit("VALIDATION FAILED:\n" + "\n".join(errors))
    print("STRUCTURE VALID; remote links and ChatGPT settings require separate verification")

if __name__ == "__main__": main()
