# Project Knowledge Kit

Reusable, provider-agnostic AI project knowledge management: **rules index → context routing → minimum relevant source → verified change**.

## Components
- `templates/project/`: project scaffold, canonical agent rules, sources, changelog and ChatGPT Project Instructions.
- `skills/project-knowledge-installer/SKILL.md`: reusable installer workflow.
- `scripts/install.py`: safe local scaffold generator.
- `scripts/validate.py`: local structural checks.
- `docs/installation.md`: complete setup and limitations.

## Quick start
```sh
python3 scripts/install.py --name "Payment Platform" --slug payment-platform --output ./out
python3 scripts/validate.py ./out/payment-platform
```
Publish the generated project folder to GitHub or another accessible canonical storage provider. Replace the `{{RULES_INDEX_URL}}` token in `PROJECT_INSTRUCTIONS.md` with the real, verified URL to the installed `agent-rules/INDEX.md`. Apply that content to the target **ChatGPT Project → Project settings → Instructions** (or use an authorized supported settings integration) and verify read-back.

**Scaffolding is not project configuration.** The installer must report `INSTRUCTIONS_PENDING` until the instructions are actually applied and verified. The supplied CLI cannot change ChatGPT Project settings.

This repository is a reusable *public framework*, **not** the NIAP knowledge base. Never publish project-private sources, secrets or access URLs into a public template.

Licensed under MIT. See [LICENSE](LICENSE).
