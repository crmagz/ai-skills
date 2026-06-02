---
description: Enforces Conventional Commits 1.0.0 format for all git commit messages
alwaysApply: true
version: 1.1.0
---

# Git Conventional Commits

All commit messages MUST follow the [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) specification.

## Format

```
<type>(<JIRA-ID>): <description>
```

All commits are **title-only** — no body, no footer. The title is the entire message.

The JIRA issue ID (e.g. `BATMAN-8413`) is **REQUIRED** in the scope position.
It is used by change management automation to track work. Every commit MUST
map to exactly one JIRA issue. If the issue ID is unknown, ask the developer
before proceeding — never assume or reuse an ID from a previous commit.

## Allowed Types

| Type       | Purpose                                                 |
| ---------- | ------------------------------------------------------- |
| `feat`     | New feature or capability                               |
| `fix`      | Bug fix                                                 |
| `docs`     | Documentation only                                      |
| `style`    | Formatting, semicolons, etc. (no logic change)          |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `perf`     | Performance improvement                                 |
| `test`     | Adding or correcting tests                              |
| `build`    | Build system or external dependency changes             |
| `ci`       | CI configuration and scripts                            |
| `chore`    | Maintenance tasks (no src/test change)                  |
| `revert`   | Reverts a previous commit                               |

## Rules

- The type, JIRA issue ID, and description are REQUIRED
- The JIRA issue ID MUST appear in the scope position: `type(JIRA-1234): description`
- Never assume a JIRA ID from prior commits — each commit is atomic and maps to one issue
- If the developer has not provided a JIRA ID, ask for it before drafting the message
- Description MUST be lowercase, imperative mood, no period at the end
- The **entire title** (type + scope + description) MUST NOT exceed 72 characters. This matches [GitHub's truncation point](https://cbea.ms/git-commit/#limit-50) in commit list views
- **Always title-only** — no body, no footer, regardless of diff size
- Breaking changes MUST be indicated by appending `!` immediately before the colon: `type(JIRA-ID)!:`
- NEVER add `Co-Authored-By` or any AI attribution to commit messages

## Output Format

When presenting a commit command, always use a **single-line** format:

```
git commit -m "type(JIRA-ID): description"
```

NEVER use HEREDOC/EOF syntax, multi-line commit commands, or `cat <<EOF` blocks.
These do not copy reliably from terminal UIs.

## References

- [Conventional Commits 1.0.0 Specification](https://www.conventionalcommits.org/en/v1.0.0/#specification)
- [How to Write a Git Commit Message](https://cbea.ms/git-commit/#limit-50) — origin of the 72-character convention

## Examples

Good:

```
feat(BATMAN-8413): add SAML SSO support for enterprise accounts
```

```
fix(PLAT-2201): prevent race condition in concurrent webhook delivery
```

```
chore(INFRA-440): update terraform provider versions
```

```
feat(UI-971)!: redesign navigation to sidebar layout
```

Bad:

```
Updated stuff                    # No type, no JIRA ID, vague
feat: Added new feature.         # Missing JIRA ID, capitalized, period
feat(auth): add login            # Missing JIRA ID — use feat(PROJ-123)
Fix bug                          # No type prefix, no JIRA ID
FEAT: add login                  # Type must be lowercase, no JIRA ID
```
