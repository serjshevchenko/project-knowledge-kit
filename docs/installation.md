# Install Project Knowledge Kit

## Choose dimensions separately

- `--platform`: AI runtime: OpenAI ChatGPT Project/Codex; Anthropic Claude Project/Claude Code; Google Gemini app/Gemini CLI.
- `--storage-provider`: GitHub, Google Drive, local, other.

## Scaffold

```sh
python3 scripts/install.py \
  --name "Payment Platform" --slug payment-platform \
  --platform openai/chatgpt-project \
  --storage-provider google-drive --output ./out
python3 scripts/validate.py ./out/payment-platform
```

No existing destination is overwritten. Optional `--storage-root` and `--rules-index-url` set known, verified values. Without them, unresolved placeholders explicitly remain.

## Publish

Commit/upload the generated core Markdown files to the selected canonical provider using authorized GitHub/Google Drive/local operations. Confirm the remote paths and permissions by reading files back. A local scaffold alone is not remotely accessible.

## Apply runtime bootstrap

Provide a verified, accessible URL to the new project's `agent-rules/INDEX.md` in the generated bootstrap. Supported target files are `PROJECT_INSTRUCTIONS.md` (ChatGPT/Claude Project or Gemini app guidance), `AGENTS.md` (Codex), `CLAUDE.md` (Claude Code) and `GEMINI.md` (Gemini CLI).

Follow the corresponding `platforms/` adapter. Hosted apps can require manual setting; do not assume programmatic settings access or persistence. Applying a file to a repository does not configure a hosted AI app automatically.

## Validate

`python3 scripts/validate.py ./out/payment-platform --runtime-ready` detects unresolved placeholders. It **does not** prove remote source accessibility or runtime configuration.

Start a fresh session in the target runtime; verify discovery of bootstrap, read access to index/map/rules and correct fail-closed behavior. Record `VERIFIED` only after this succeeds. Otherwise report precise pending work.
