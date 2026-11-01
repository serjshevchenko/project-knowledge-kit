# Storage providers (independent of AI platforms)

- **GitHub**: use authorized repository operations to create branches, upload/write Markdown, and verify commits by read-back. Prefer PRs for existing projects.
- **Google Drive**: create the folder tree and upload source Markdown using authorized Drive operations. Verify every URL, access grant and content. Do not assume that copying Markdown to a native document preserves file identity.
- **Local**: write files in an authorized directory. A local path is not necessarily accessible to remote AI runtimes.

Storage only houses the knowledge. Each AI runtime needs its own bootstrap and a verified path to the same canonical source. The installer Skill routes the publication workflow based on the chosen storage provider; the local CLI only scaffolds.
