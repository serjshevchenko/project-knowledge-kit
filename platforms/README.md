# AI platform adapters

The platform adapter defines **how an AI runtime receives bootstrap instructions**; it does not own project rules. The provider-neutral canonical rules live under `core/templates/project/`.

Adapter IDs: `openai/chatgpt-project`, `openai/codex`, `anthropic/claude-code`, `anthropic/claude-project`, `google/gemini-cli`, `google/gemini-app`.

A CLI/file-based adapter may produce `AGENTS.md`, `CLAUDE.md` or `GEMINI.md`. Hosted chat experiences may require manual configuration and source attachment. Never assume a provider or product supports an undocumented settings API.

Storage location is independent: GitHub, Drive and local filesystem are storage choices, not AI platforms. Verify the runtime can actually read the canonical index URL.
