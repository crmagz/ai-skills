---
name: ai-plan
description: Create risk-scaled, durable implementation plans for features, fixes, refactors, migrations, infrastructure, workflow, or shared-contract changes. Use when a user asks to plan work, requests $ai-plan, needs a persisted plan before implementation, or wants an existing plan revised.
---

# AI Plan

Plan deliberately before implementation. Use this skill for planning only: do not edit application, test, configuration, or infrastructure files until the user explicitly confirms the plan.

## Workflow

1. Clarify an outcome that does not name a concrete behavior, system, or expected result. Do not fabricate requirements.
2. Inspect repository instructions, the current branch/status, build configuration, relevant source and tests, supplied requirements, and any named repositories. Treat an unsafe branch as a warning for inline plans and as an implementation blocker for durable plans.
3. Capture existing patterns for naming, errors, logging, persistence, tests, and validation. For IaC or GitOps, use the alternative pattern table in `references/risk-triggers.md`.
4. Establish a non-mutating validation baseline when practical. Record pre-existing failures rather than hiding them.
5. Classify risk. Before classifying infrastructure, deployment, or multi-repository work, read `references/risk-triggers.md` and quote every matched trigger exactly. Choose the highest matched tier; only de-escalate infrastructure when the reference's Observed-evidence gate is satisfied.
6. Label every meaningful repository claim as **Observed**, **Assumed**, **Proposed**, or **Unknown**. Cite a path and line, command output, verification path, or validation approach. Do not present speculation as fact.
7. Select output:
   - **Small**: inline plan with one validation check.
   - **Medium**: inline plan plus compact test checklist; create a durable file only for durable-review signals.
   - **Large**: durable plan with Plan, Test Matrix, and Specification.
   - **High-risk**: add a change-specific Review Checklist.
8. For a durable plan, resolve its location with `scripts/resolve-plan-path.mjs`; never hand-build the path or write a plan into the target repository. Read an existing matching plan and update it surgically instead of overwriting it.
9. End the response and every durable plan with the implementation gate below, then wait. On `adjust`, revise only affected sections, reclassify if scope changed, record the revision, and re-emit the gate.

## Durable Plan Contents

Use the templates in `references/` only as required by the chosen tier:

- `plan-template.md` for independently reviewable phases and conventional-commit boundaries.
- `test-matrix-template.md` for executable behavior coverage.
- `spec-template.md` for requirements, contracts, failure modes, and acceptance criteria.
- `review-checklist-template.md` for security, state, data-mutation, or other high-risk review checks.
- `multi-repo.md` before planning work across repositories.
- `plan-storage.md` for path rules and environment overrides.

## Implementation Gate

End with exactly this decision boundary, adapted only to name the work:

---

## Implementation Gate

**Status**: Awaiting user confirmation.

No application code changes will be made until you confirm.

- **proceed** — implement as planned (or `implement phase 1` for phased work)
- **adjust [feedback]** — revise the plan with your feedback
- **stop** — abandon this approach

## Guardrails

- Do not use an ephemeral task plan as a substitute for a requested durable plan.
- Do not create PRDs, tickets, ADRs, or requirement documents unless asked; treat them as inputs.
- Do not delegate planning by default. Keep inspection, classification, and plan authorship with the primary agent.
- If reality diverges during implementation, update the remaining durable plan before continuing.
