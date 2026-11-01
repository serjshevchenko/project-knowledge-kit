---
name: project-knowledge-installer
description: Initialize, configure, validate and upgrade provider-neutral AI project knowledge with platform and storage adapters.
---

# Project Knowledge Installer

Use the version-controlled `core/templates/project/` and `platforms/` in this repository, not recollection.

## Independent dimensions

**AI platform** selects how the agent receives bootstrap instructions: OpenAI ChatGPT Project, OpenAI Codex, Anthropic Claude Project, Anthropic Claude Code, Google Gemini app, or Google Gemini CLI.

**Storage provider** selects where canonical project files are published: GitHub, Google Drive, local, or other. Never conflate AI runtime with storage. The same canonical core should work across runtimes.

## Initialize

1. Identify project name, slug, AI platform, storage provider and destination. Never invent external URLs.
2. Inspect destination and permissions before writes; preserve existing files.
3. Scaffold using `python3 scripts/install.py --name ... --slug ... --platform ... --storage-provider ...` or reproduce the exact template rendering using authorized tools.
4. Publish the generated files to the selected storage provider using available authorized APIs. Verify by read-back, not presumed success.
5. Determine a real, accessible canonical URL for the published `agent-rules/INDEX.md`, then render the chosen platform bootstrap with it.
6. Apply the bootstrap using the relevant `platforms/` adapter. Use a documented settings API only when available and authorized; otherwise hand over the exact rendered content and manual target instructions.
7. Verify the target runtime loads the bootstrap and can read the canonical index and routed rules. If no read-back is possible, request explicit user confirmation and do not claim verified installation.

## Storage operations

GitHub: use an authorized connector to create files/commits or a PR; do not assume direct CLI access.
Google Drive: use authorized Drive operations to create Markdown files and folders; check actual source URLs and access.
Local: write only if filesystem access exists; local paths are not automatically reachable by hosted agents.

## Status

Report independently: `SCAFFOLDED`, `FILES_PUBLISHED`, `BOOTSTRAP_PENDING`, `BOOTSTRAP_APPLIED`, `VERIFIED`. State the exact blocker if the target settings cannot be written or inspected.

## Upgrade

Read current project-specific sources and rules, compare against core/adapter versions, preserve local modifications, update changelog and references and verify all changes. Never silently overwrite canonical sources.
