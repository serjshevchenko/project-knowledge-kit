#!/usr/bin/env python3
"""Validate generated knowledge core and platform bootstrap."""
import argparse
from pathlib import Path

REQUIRED = [
    "README.md", "CHANGELOG.md", "agent-rules/INDEX.md",
    "agent-rules/context-routing.md", "agent-rules/project-specific.md",
    "agent-rules/source-management.md", "agent-rules/changelog-policy.md",
    "agent-rules/storage-rules.md", "agent-rules/documentation-style.md",
    "sources/overview.md",
]
BOOTSTRAPS = ("PROJECT_INSTRUCTIONS.md", "AGENTS.md", "CLAUDE.md", "GEMINI.md")

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("directory", type=Path)
    p.add_argument("--runtime-ready", action="store_true")
    a = p.parse_args()
    root = a.directory
    errors = [f"missing {s}" for s in REQUIRED if not (root / s).is_file()]
    present = [s for s in BOOTSTRAPS if (root / s).is_file()]
    if len(present) != 1:
        errors.append(f"expected one platform bootstrap, found {present}")
    if a.runtime_ready and root.exists():
        for f in root.rglob("*.md"):
            value = f.read_text(encoding="utf-8")
            if "{{" in value or "}}" in value:
                errors.append(f"unresolved placeholder in {f.relative_to(root)}")
        config = root / "agent-rules" / "project-specific.md"
        if config.exists() and "UNCONFIGURED" in config.read_text(encoding="utf-8"):
            errors.append("storage root unconfigured")
    if errors:
        raise SystemExit("VALIDATION FAILED:\n" + "\n".join(errors))
    print("LOCAL STRUCTURE VALID; remote settings and source access require independent verification")

if __name__ == "__main__":
    main()
