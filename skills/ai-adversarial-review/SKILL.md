---
name: ai-adversarial-review
description: Conduct a principal-engineer adversarial review of a local codebase or GitHub pull request, using independent research agents to find correctness and completeness defects, remediate local findings, validate the result, or submit concise inline PR comments. Use when asked to review code, assess a pull request, find logic bugs, check edge cases, or perform an adversarial code review.
---

# AI Adversarial Review

Review only correctness and completeness. Verify behavior against the stated intent, surrounding code, contracts, and realistic edge cases. Do not turn this into a style, naming, or preference review.

Read `rules/ai-adversarial-review.md` from the target repository when it exists. Follow repository instructions, including its validation commands and contribution rules.

## Set the review scope

1. Determine whether the target is local code or a GitHub pull request. Ask only if this cannot be inferred.
2. Establish the intended behavior from the request, issue, PR description, tests, API contracts, and nearby code. Record unknown requirements as uncertainty, not as findings.
3. When a diff exists, inspect it, impacted call paths, relevant tests, and the baseline implementation before judging the changed lines. For an unchanged codebase, establish the target entry points, call paths, contracts, and relevant tests before judging current behavior.
4. Run the project's existing validation commands before remediation when practical. Preserve and report pre-existing failures separately.

## Use independent research agents

Ask every research agent to look for defects of any severity. Do not give an agent a target severity. Triage severity after collecting evidence.

Start two independent agents for an ordinary, scoped change:

1. **Logic and state:** trace control flow, state transitions, data transformations, invariants, and failure propagation.
2. **Completeness and edges:** test contracts at boundaries, empty and malformed inputs, optional values, ordering, retries, partial failures, compatibility, and missing test coverage.

Add one agent when a change affects a public API, persistence, concurrency, authorization, cross-service contracts, or more than roughly 250 changed lines:

3. **Integration and regression:** trace callers and consumers, compare changed and previous behavior, and identify regressions across component boundaries.

Add a fourth agent when two or more of those conditions apply or the blast radius is high:

4. **Adversarial tests:** derive concrete counterexamples and determine whether the tests prove the intended behavior.

Give each agent the relevant raw artifacts: requirement or PR description, affected source and tests, and applicable contracts. Include the exact diff and baseline implementation when changed code is under review. For an unchanged codebase, include the target entry points and call paths instead. Require each finding to include a file and line, triggering input or sequence, observed consequence, and evidence. Agents must report no finding when they cannot substantiate one.

## Triage findings

Deduplicate findings and verify each one locally. Apply these levels consistently:

| Level | Threshold | Review outcome |
| --- | --- | --- |
| Blocker | Prevents a safe merge or release, such as an unrecoverable correctness failure in the primary path or an implementation that cannot meet its required contract. | Resolve locally or request changes on a PR. |
| Critical | Causes a clear, high-impact defect in a supported or common path, with concrete evidence of corruption, loss, incorrect authorization, outage, or material contract failure. | Resolve locally or request changes on a PR. |
| Major | Causes a concrete correctness defect in a realistic but narrower supported path, including a missing required edge case. | Recommend a targeted change. |
| Medium | Has a credible correctness or completeness risk, but impact, reachability, or intended behavior is limited or uncertain. | Recommend a focused check, test, or change. |

Do not escalate from intuition. Do not label missing tests as a finding unless they leave a realistic behavior unverified. Do not block for Major or Medium findings. Reclassify or omit findings disproved by the code, tests, or requirements.

## Review local code

1. Run the research agents, consolidate their evidence, and verify findings against the local codebase.
2. Remediate every substantiated finding in scope. Keep fixes small, preserve established patterns, and add or update regression tests for each fixed behavior.
3. Reinspect the changed paths and rerun the relevant research lens after remediation.
4. Run the repository's formatter, linter, type checks, targeted tests, and full test suite when available. Use the documented commands rather than inventing replacements.
5. Call the review complete only after the remediation is present and all applicable local validation passes. State any unavailable validation or pre-existing failure plainly.

## Review a GitHub pull request

1. Obtain the remote PR description, changed files, diff, base commit, and head SHA. Research the remote diff at that fixed head SHA.
2. Check out the exact researched head SHA locally in a separate worktree or another isolated checkout. Do not modify the author's branch, push fixes, or change the PR unless separately asked.
3. Have the reviewer reconcile the research evidence with the local source, dependencies, tests, and exact diff. Remove duplicates and unproven concerns.
4. Submit every finding as a GitHub line comment anchored to the changed line that best explains it. Use `RIGHT` for additions or context and `LEFT` for deletions. Use a review event of `REQUEST_CHANGES` only when at least one Blocker or Critical finding remains. Otherwise submit a `COMMENT` review with the inline recommendations.
5. Include a concise, nonempty review body of one sentence at most, as required by GitHub's REST create-review endpoint for both review events. Put findings in inline comments, not in a summary or a separate issue.

When using the GitHub API, submit one review with `commit_id` set to the inspected head SHA and provide each finding in the review's `comments` array with `path`, `line`, `side`, and `body`. Set `side: "RIGHT"` for added or context lines and `side: "LEFT"` for deleted lines. Do not comment on unchanged lines when an adjacent changed line can anchor the explanation.

## Write the review

Write like a collaborative principal engineer: concise, evidence-led, and specific about the consequence. Use a constructive, suggestive tone for recommendations. Never use an em dash.

Use this shape for an inline comment:

```text
[Severity] This can [consequence] when [trigger], because [mechanism]. Consider [specific remedy or test].
```

Do not include praise, a recap of the implementation, speculative hypotheticals, style nits, or duplicate comments. When no Blocker or Critical finding remains, do not describe the review as nonblocking.
