# Global Plan Storage — Path Rules

Durable plans are stored outside the target repo:

```text
~/.codex/plans/<baseRepo>/<kebab-case-name>.plan.md
```

Path rules:

- Resolve durable plan paths with
  `source/skills/ai-plan/scripts/resolve-plan-path.mjs` when the
  script is available. Do not hand-build the path.
- Use `$AI_PLAN_HOME` as the plan root if it is set.
- Otherwise use `~/.codex`.
- Set `$AI_PLAN_HOME` to override the plan root.
- Store plans under `plans/<baseRepo>/`.
- Derive `<baseRepo>` from the primary repo root and sanitize its
  directory basename to kebab-case. A repo root like
  `/Users/cristian/ihm/nodejs/devkit` must produce `devkit`, not the full
  path.
- Derive `<kebab-case-name>` from the JIRA-ID plus a short request title
  when available, for example `falcon9-1234-payment-retry`; otherwise use
  a concise kebab-case title from the request.
- Create the parent directory if needed.
- Include plan path, primary repo, all related repos, branch context,
  source of request, and creation date in the plan file header.
- Do not create repo-local planning files.

Example:

```bash
node source/skills/ai-plan/scripts/resolve-plan-path.mjs \
  --repo-root /Users/cristian/ihm/nodejs/devkit \
  --jira FALCON9-1234 \
  --title "Payment retry"
```

This resolves under `~/.codex/plans/devkit/` by default.
