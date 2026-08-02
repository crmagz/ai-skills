---
name: python-documentation
description: Document Python modules and public APIs with concise Google-style docstrings and maintainable code comments. Use when adding or revising Python docstrings, API documentation, module documentation, or explanatory comments.
---

# Python Documentation

Document the current public contract without narrating the change that led to
it.

## Workflow

1. Read repository instructions, `pyproject.toml`, existing docstrings, and
   nearby public APIs. Follow the repository's formatter and docstring
   configuration when it differs from this skill.
2. Identify the public surface: exported modules, classes, functions, public
   methods, CLI entry points, and exceptions. Do not add boilerplate to
   private helpers whose name, signature, and local context are clear.
3. Write Google-style docstrings:
   - Begin with an imperative, current-behavior summary.
   - Use `Args:`, `Returns:`, `Yields:`, `Raises:`, and
     `Attributes:` only when they add information beyond type annotations.
   - Explain semantics, units, defaults, ownership, side effects, caller
     obligations, and failure conditions—not the implementation line by line.
4. Add code comments only for non-obvious invariants, external constraints,
   security rationale, or deliberate tradeoffs. Never write comments about
   prior behavior, implementation deltas, or the act of changing the code.
5. Validate with the repository's documentation and lint commands. When Ruff
   docstring rules are configured, run `ruff check` for the affected paths.

## Pattern

```python
def publish_report(report: Report, client: ApiClient) -> Publication:
    """Publish a report to the configured API.

    Args:
        report: Fully validated report to publish.
        client: Authenticated client for the target API.

    Returns:
        Publication metadata returned by the API.

    Raises:
        ApiError: If the API rejects or cannot accept the report.
    """
```

Use the repository's type annotations rather than duplicating them in prose.
Document nested data or opaque values only when their public meaning is not
clear from the declared type.
