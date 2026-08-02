---
name: agent
version: 1.1.0
---

# Open Source Development Standards

You are working in an open source repository. Follow these standards for all contributions.

## Project Context

- @README.md
- @docs/CONTEXT.md

## Git Practices

- All commits MUST follow the Conventional Commits 1.0.0 specification
- Keep commits atomic: one logical change per commit
- Write commit messages that explain _why_, not _what_
- ALWAYS create a new branch from the freshly fetched remote default
  (`git fetch origin && git switch -c <branch> origin/<default>`), NEVER
  from a stale local `master`/`main`
- Curate the branch as a clean, readable conventional-commit story —
  squash fixups, reorder, and reword as needed before review
- To bring a branch up to date, **fetch the default branch and rebase
  onto it** (`git fetch origin && git rebase origin/<default>`). NEVER
  merge the default branch back into a feature branch — that pollutes
  history and makes future rebases harder
- After a rebase, re-publish the feature branch with
  `git push --force-with-lease` (never a bare `--force`)
- Default branch (`master`/`main`) is reached ONLY through a reviewed
  pull request — never a direct push or merge

## AI Boundaries

The AI is trusted to manage the full feature-branch lifecycle. It MAY,
without per-command developer sign-off:

- Commit (`git commit`)
- Stage files (`git add`)
- Pull, fetch, and rebase a feature branch (`git pull`, `git fetch`,
  `git rebase`, including `--continue`/`--abort` and rebasing onto the
  default branch)
- Push a feature branch, including `git push --force-with-lease` after a
  rebase
- Open, update, and comment on pull requests via the `gh` CLI

The AI MUST ALWAYS:

- ALWAYS format every commit as `type(scope): description` or
  `type: description` per the Conventional Commits specification. Include
  an issue or ticket identifier only when the project, branch, PR template,
  or developer requires one; NEVER invent or fabricate identifiers
- ALWAYS confirm the working tree is safe to start development BEFORE
  making changes: the current branch MUST be a descriptive feature branch
  and MUST NOT be `master`/`main`. If it is not, create or check out a
  feature branch first

The AI MUST NEVER (these are non-negotiable; the `pre-push` hook is a
local guardrail that catches mistakes early, but the authoritative control
for default-branch protection is server-side GitHub branch protection):

- NEVER push directly to, or merge into, `master`/`main` — default-branch
  changes land only through a reviewed PR
- NEVER force-push a default branch, or force-push a shared branch that
  other developers are collaborating on, with `--force` or
  `--force-with-lease`
- NEVER merge or close another author's PR
- NEVER use a bare `git push --force`; always prefer `--force-with-lease`
- NEVER use `--no-verify`, `--no-gpg-sign`, or any flag that bypasses hooks
- NEVER run `git reset --hard`, `git clean -fdx`, delete branches, or
  rewrite already-pushed history on shared branches without explicit
  instruction
- NEVER add `Co-Authored-By` or any AI attribution to commits or PRs

When unsure whether an operation is safe — especially anything touching
the default branch or rewriting shared history — the AI MUST stop and ask
the developer.

## Code Quality

- No secrets, credentials, or API keys in source code
- All infrastructure changes require peer review
- Follow the principle of least privilege for IAM and RBAC

## Pull Requests

- PRs must have a clear description of the change and its motivation
- Link to relevant issues or tickets
- Include a test plan when applicable

**Version**: 1.1.0 | **Ratified**: 2026-08-02 | **Last Amended**: 2026-08-02

### Changelog

- **1.1.0** (2026-08-02): Adds the AI-managed feature-branch lifecycle policy while retaining conventional commits, optional issue identifiers, and default-branch protections.
- **1.0.0** (2026-08-02): Initial open source baseline for repository development standards.
