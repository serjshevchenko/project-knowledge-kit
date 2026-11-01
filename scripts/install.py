#!/usr/bin/env python3
"""Create a non-destructive Project Knowledge Kit scaffold."""
import argparse
from pathlib import Path
from datetime import date
import re

SOURCE = Path(__file__).resolve().parent.parent / "templates" / "project"

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--name", required=True)
    p.add_argument("--slug", required=True)
    p.add_argument("--output", default="./out")
    p.add_argument("--storage-root", default="UNCONFIGURED")
    a = p.parse_args()
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", a.slug):
        p.error("slug must use lowercase letters/digits and hyphens")
    dest = Path(a.output).resolve() / a.slug
    if dest.exists(): p.error(f"destination exists: {dest}")
    if not SOURCE.is_dir(): p.error("missing templates/project")
    replacements = {
      "{{PROJECT_NAME}}": a.name,
      "{{INSTALL_DATE}}": date.today().isoformat(),
      "{{STORAGE_ROOT}}": a.storage_root,
    }
    for f in sorted(SOURCE.rglob("*")):
        if not f.is_file(): continue
        txt = f.read_text(encoding="utf-8")
        for key, value in replacements.items():
            txt = txt.replace(key, value)
        target = dest / f.relative_to(SOURCE)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(txt, encoding="utf-8")
    print(f"SCAFFOLDED {dest}")
    print("NEXT: publish; resolve {{RULES_INDEX_URL}}; apply and verify Project Instructions")

if __name__ == "__main__": main()
