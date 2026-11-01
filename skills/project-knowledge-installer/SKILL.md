---
name: project-knowledge-installer
description: Scaffold, configure, validate and upgrade an AI Project Knowledge Kit, including ChatGPT Project Instructions and lazy project context routing.
---

# Project Knowledge Installer

Use the version-controlled `templates/project/` files as source of truth, not memory.

## Initialize
1. Identify project name, slug, destination/provider and accessible canonical URL; do not invent values.
2. Inspect the target first. Never overwrite existing sources without an approved migration plan.
3. Run `python3 scripts/install.py --name ... --slug ... --output ...` or reproduce its behavior where shell access is unavailable.
4. Publish files to the approved provider with authorized write tools; verify by re-reading.
5. Resolve an actual accessible URL to the published `agent-rules/INDEX.md`.
6. Replace `{{RULES_INDEX_URL}}` in generated `PROJECT_INSTRUCTIONS.md` with that URL.

## Apply ChatGPT Project Instructions
- Inspect available authorized tools to identify a supported **target ChatGPT Project settings write** action.
- If available, apply instructions to the correct project and read them back.
- Otherwise, return the exact rendered text and guide the user to **Project settings → Instructions**. Request user confirmation/read-back.
- Never use undocumented private APIs, assume instructions are installed, or report success without evidence.
- If unavailable/unconfirmed, report `INSTRUCTIONS_PENDING`.

## Validate
Run `scripts/validate.py` to check local files. Verify live canonical links, routing, access, source version selection and actual project setting separately.

Statuses: `SCAFFOLDED`, `FILES_PUBLISHED`, `INSTRUCTIONS_PENDING`, `INSTRUCTIONS_APPLIED`, `VERIFIED`. Each status needs observable evidence; never equate a local scaffold with a configured project.

## Upgrade
Read existing sources, preserve project-specific changes, propose a diff, follow source-change/changelog rules and verify all writes. Avoid destructive copy-over upgrades.
