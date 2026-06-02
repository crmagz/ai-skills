---
name: git-commit
description: Create a git commit following the Conventional Commits specification. Use when the user wants to commit staged changes or asks for help writing a commit message.
version: 1.1.0
---

# Conventional Commit Skill

Guide the user through creating a well-formed conventional commit.

## Workflow

1. Run `git status` and `git diff --cached` to inspect staged changes
2. If nothing is staged, inform the user and ask if they want to stage files
3. **Ask the developer for the JIRA issue ID** if not already provided.
   Never assume or reuse a JIRA ID from a previous commit — each commit
   MUST map to exactly one JIRA issue. This is critical for change
   management automation.
4. Analyze the staged changes to determine:
   - The appropriate **type** (feat, fix, docs, refactor, etc.)
   - Whether this is a **breaking change**
5. If multiple logical changes are staged, suggest splitting into
   separate commits — each with its own JIRA ID
6. Draft a **title-only** commit message:
   ```
   <type>(<JIRA-ID>): <description>
   ```
7. Present the draft to the user for review
8. Output the commit command as a **single-line** `git commit -m "..."`.
   NEVER use HEREDOC/EOF syntax — it does not copy reliably from terminal UIs.
   NEVER execute `git commit` directly.

### Output Format

Always output exactly this — one line, easy to copy:

```
git commit -m "type(JIRA-ID): description"
```

NEVER output multi-line commit commands, HEREDOC syntax, or `cat <<EOF` blocks.

## AI Boundaries — Strict

- NEVER execute `git commit`, `git push`, `git merge`, or any destructive
  git operation. Only draft the command and present it for the developer
  to review and run manually.
- NEVER use `--no-verify`, `--no-gpg-sign`, or any flag that bypasses hooks.
- NEVER amend a previous commit unless the developer explicitly requests it.
- NEVER force push to any branch.
- NEVER add `Co-Authored-By` or any AI attribution footer to commit messages.
- AI MAY run read-only git commands (`git status`, `git diff`, `git log`,
  `git branch`) to gather context.
- AI MAY stage files (`git add`) only when explicitly instructed by the
  developer, and MUST confirm what will be staged before doing so.

These boundaries are non-negotiable. Even if the developer approves a
commit message, the developer MUST execute the commit themselves.

## Commit Message Guidelines

- JIRA issue ID is REQUIRED in the scope: `type(JIRA-1234): description`
- Description: lowercase, imperative mood, no period
- The **entire title** (type + scope + description) MUST NOT exceed 72 characters
- **Always title-only** — no body, no footer, regardless of diff size
- Indicate breaking changes with `!` after the type/scope: `feat(JIRA-1234)!: description`

## Type Selection Logic

- New functionality added? use `feat`
- Bug corrected? use `fix`
- Only documentation changed? use `docs`
- Code restructured without behavior change? use `refactor`
- Performance improved? use `perf`
- Tests added or updated? use `test`
- Build/dependency changes? use `build`
- CI pipeline changes? use `ci`
- Formatting/whitespace only? use `style`
- Everything else (configs, tooling)? use `chore`
