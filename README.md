# Project Knowledge Kit

Reusable, **AI-platform-independent** project knowledge management.

The architecture separates three concerns:

- **Core** (`core/templates/project/`): source of truth, routing, changelog, documentation and knowledge structure.
- **AI platform adapters** (`platforms/`): OpenAI ChatGPT/Codex, Anthropic Claude/Claude Code and Google Gemini/Gemini CLI bootstrap instructions.
- **Installer** (`skills/project-knowledge-installer/SKILL.md`, `scripts/`): select an AI runtime and an independent storage provider, scaffold files, publish, configure and verify.

## Quick start

```sh
python3 scripts/install.py --name "Payment Platform" --slug payment-platform \
  --platform anthropic/claude-code --storage-provider github --output ./out
python3 scripts/validate.py ./out/payment-platform
```

Alternative AI platforms: `openai/chatgpt-project`, `openai/codex`, `anthropic/claude-project`, `anthropic/claude-code`, `google/gemini-app`, `google/gemini-cli`.

Storage providers: `github`, `google-drive`, `local`, `other`.

The generated bootstrap will be `AGENTS.md` (Codex), `CLAUDE.md` (Claude Code), `GEMINI.md` (Gemini CLI) or `PROJECT_INSTRUCTIONS.md` (hosted projects/apps). Read `docs/installation.md`.

**Scaffold ≠ published files ≠ applied instructions.** The local CLI does not change remote settings or upload files. Apply through authorized tools, otherwise use the documented manual flow and verify each step.

This is a public generic framework, not a copy of private NIAP documentation. MIT licensed.
