---
description: Python API documentation and comment standards using Google-style docstrings
alwaysApply: true
version: 1.0.0
globs: "*.py"
---

# Python Documentation

## Public API Docstrings

Use Google-style docstrings for public modules, classes, functions, methods,
and command-line entry points when callers need contract detail beyond the
name and type signature. Use `"""triple double quotes"""`.

- Start with one imperative summary sentence that describes current behavior.
- Add a blank line before multi-line detail.
- Document inputs, outputs, side effects, supported exceptions, and caller
  restrictions only when they are material to using the API.
- Use `Args:`, `Returns:`, `Yields:`, `Raises:`, and `Attributes:`
  only when applicable; do not add empty or redundant sections.
- Treat type annotations as the type source of truth. Describe meaning,
  units, ownership, constraints, defaults, and failure conditions instead of
  repeating annotations.
- Document command-line modules sufficiently for `--help` usage when the
  module is intended to be run directly.

```python
def load_release_config(path: Path, *, strict: bool = True) -> ReleaseConfig:
    """Load a release configuration from a YAML file.

    Args:
        path: YAML file to read.
        strict: Reject unknown configuration keys when true.

    Returns:
        Parsed configuration with defaults applied.

    Raises:
        ConfigError: If the file cannot be parsed or fails validation.
    """
```

## Comments

- Use comments for non-obvious invariants, external constraints, security
  rationale, or intentionally surprising behavior.
- Keep comments adjacent to the code they explain and remove comments that no
  longer match the code.
- Do not restate syntax, narrate control flow, or describe historical changes,
  diffs, migrations, or previous implementations.
- Prefer a clear name, type, helper, or docstring over a prose comment.
