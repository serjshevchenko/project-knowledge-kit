# Install a project

1. Scaffold: `python3 scripts/install.py --name "Payment Platform" --slug payment-platform --output ./out`.
2. Check structure: `python3 scripts/validate.py ./out/payment-platform`.
3. Publish generated Markdown to an approved GitHub/Drive location accessible by the target agent.
4. Replace `{{RULES_INDEX_URL}}` in `PROJECT_INSTRUCTIONS.md` with a verified agent-readable link to **the new project's** `agent-rules/INDEX.md`.
5. Apply rendered text in **ChatGPT Project → Project settings → Instructions** or use a documented authorized settings-write integration. The CLI does **not** modify ChatGPT settings.
6. Confirm the target project instructions via readback/user confirmation, then test a fresh chat's ability to read the index, routing map and relevant rules.
7. Only after these checks report `VERIFIED`. Otherwise report `INSTRUCTIONS_PENDING` or the exact blocker.

Review all generated references before putting them in production. Never deploy a placeholder or private links that the agent cannot access.
