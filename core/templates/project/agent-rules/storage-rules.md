# Storage Rules

Verify read/list/write permissions for required resources. On missing access, stop and name the precise inaccessible resource.

Read current remote content before editing; preserve stable file identity where possible. Do not overwrite canonical files from stale copies.

Prefer Markdown for source/rule files. After writes, re-fetch and verify changed content, references and changelog.

Document real provider specifics (GitHub/Drive/local) only after confirming the provider and available actions. Do not publish secrets, private project information or sensitive links in public repositories.
