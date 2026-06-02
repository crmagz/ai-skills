---
name: agent
version: 1.1.1
---

# Development Standards

You are working in a software repository. Follow these standards for all contributions.

## Project Context

- @README.md
- @docs/CONTEXT.md

## Git Practices

- All commits MUST follow the Conventional Commits 1.0.0 specification.
- Never force push to main/master.
- Keep commits atomic: one logical change per commit.
- Write commit messages that explain _why_, not _what_.

## AI Boundaries

- AI MUST NEVER execute `git commit`, `git push`, `git merge`,
  `git rebase`, `git reset`, `git branch -d`/`git branch -D`, or
  `git push --delete` (or any variant that deletes a branch), or any
  other destructive git operation directly. AI MUST only draft the
  command and present it for the developer to review and run manually.
- AI MUST NEVER be granted auto-approve permissions for git operations
  in tool settings.
- AI MAY run read-only git commands (`git status`, `git diff`,
  `git log`, `git branch`) to gather context.
- AI MAY stage files (`git add`) when explicitly instructed by the
  developer, but MUST confirm what will be staged before doing so.

## Code Quality

- No secrets, credentials, or API keys in source code.
- Infrastructure changes require peer review.
- Follow the principle of least privilege for IAM and RBAC.

## Pull Requests

- PRs must have a clear description of the change and its motivation.
- Link to relevant issues or tickets.
- Include a test plan when applicable.
