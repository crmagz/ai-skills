---
name: session-handoff
description: Create, validate, list, assess, and resume durable session handoffs for long-running work. Use when a user requests a handoff, context save, resume, or pause; when a substantial milestone is complete; or when a fresh agent needs unambiguous continuation context.
---

# Session Handoff

Preserve the precise state another agent needs to continue safely. Store new handoffs in `.codex/handoffs/`; scripts also discover legacy `.claude/handoffs/` documents so existing history remains usable.

## Create

1. From the project root, create a scaffold:

   ```bash
   python /Users/bluewizard/.codex/skills/session-handoff/scripts/create_handoff.py <task-slug>
   ```

   For a continuation, pass `--continues-from <filename>`.
2. Complete every placeholder. Prioritize Current State Summary, Important Context, Decisions Made, Immediate Next Steps, critical files, branch/worktree state, validation, and known blockers.
3. Mention environment variable names only. Never include credentials, tokens, keys, connection strings, or secret values.
4. Validate before reporting completion:

   ```bash
   python /Users/bluewizard/.codex/skills/session-handoff/scripts/validate_handoff.py <handoff-file>
   ```

   Do not finalize if secrets are reported or the score is below 70.
5. Report the file path, validation result, concise captured state, and the first next action.

Use `references/handoff-template.md` to ensure the document is complete. Avoid a handoff for trivial, easily reconstructible work.

## Resume

1. List available handoffs:

   ```bash
   python /Users/bluewizard/.codex/skills/session-handoff/scripts/list_handoffs.py
   ```
2. Assess freshness before acting:

   ```bash
   python /Users/bluewizard/.codex/skills/session-handoff/scripts/check_staleness.py <handoff-file>
   ```
3. Read the entire selected handoff and any linked predecessor. Then follow `references/resume-checklist.md` before modifying files.
4. Start at Immediate Next Steps item 1 only after reconciling the handoff with current branch, worktree, repository, and environment state.

## Guardrails

- Describe facts, decisions, validation results, and unresolved risks concretely; cite paths and commit IDs where they matter.
- Treat a stale handoff as context, not authority. Re-check assumptions against the repository.
- Preserve predecessor links for a long-running effort; do not overwrite an existing handoff.
