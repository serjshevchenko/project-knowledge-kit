# Framework Changelog

## 2026-11-01

- Refactored into provider-neutral `core/` and `platforms/` for OpenAI, Anthropic and Google runtimes.
- Added independent AI platform and storage provider selection to installer.
- Moved shared templates to `core/templates/project/`; retired the previous `templates/project/` location.
- Clarified local versus remote configuration verification.
- Initial framework scaffold, installer Skill, CLI and documentation.
