# Agent Rules Index — {{PROJECT_NAME}}

This is the canonical entrypoint for project operating rules. Do not duplicate detailed rules here.

## Startup
1. Read this index completely.
2. Read [context-routing.md](context-routing.md).
3. Determine the applicable rules below and read all of them before relevant operations.
4. Retrieve only the smallest needed source set.
5. Fail closed if any mandatory source/rule is inaccessible.

## Rule routing
| Task | Rules |
|---|---|
| Any project work | [project-specific.md](project-specific.md) |
| Navigation/context lookup | [context-routing.md](context-routing.md) |
| Storage access | [storage-rules.md](storage-rules.md) |
| Source create/change/move/delete | [source-management.md](source-management.md), [changelog-policy.md](changelog-policy.md) |
| Documentation style/structure | [documentation-style.md](documentation-style.md) |

## Priority
Platform/system restrictions → explicit user instructions → project-specific rules → task rules → this index. Escalate unresolved conflicts.

## Completion
Verify all relevant changed files, changelog entries, indexes and references; an incomplete gate means the task is incomplete.
