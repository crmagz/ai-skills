# AI Adversarial Review Standard

Review code for correctness and completeness, including edge cases. Exclude style, naming, and preference feedback unless they cause a concrete behavioral defect.

Use independent research lenses for logic and state, plus completeness and edge cases. Add integration and regression research for public APIs, persistence, concurrency, authorization, cross-service contracts, or large changes. Add adversarial test research when multiple high-risk conditions or high blast radius apply. Agents investigate all severities. Severity is assigned only after evidence is verified.

| Level | Meaning | PR action |
| --- | --- | --- |
| Blocker | A safe merge or release is not possible. | Request changes. |
| Critical | A clear, high-impact defect affects a supported or common path. | Request changes. |
| Major | A concrete defect affects a realistic but narrower supported path. | Recommend a targeted change. |
| Medium | A credible correctness or completeness risk has limited or uncertain impact. | Recommend a focused check, test, or change. |

For local code, remediate substantiated findings, add regression coverage where needed, and complete only after the formatter, linter, type checks, and applicable tests pass. Keep pre-existing failures separate.

For pull requests, research the remote diff at a fixed head SHA, verify that exact SHA in an isolated local checkout, then submit findings as GitHub inline comments on changed lines. Anchor added or context lines on `RIGHT` and deleted lines on `LEFT`. Use `REQUEST_CHANGES` only for Blocker or Critical findings. Otherwise submit a `COMMENT` review. Include a concise nonempty review body of one sentence at most when using GitHub's REST create-review endpoint.

Write concise, evidence-led comments in a collaborative principal-engineer voice. State the trigger, mechanism, consequence, and suggested remedy. Never use em dashes. Do not call a review nonblocking, do not add vague concerns, and do not duplicate findings.
