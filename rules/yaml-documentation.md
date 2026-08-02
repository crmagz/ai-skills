---
description: Documentation and portability standards for YAML configuration files
alwaysApply: true
version: 1.0.0
globs: "*.yaml,*.yml"
---

# YAML Documentation

## Configuration Contract

- Treat each YAML file as a consumer-facing data contract. Read the schema,
  parser, and deployment tool before documenting or changing keys.
- Place concise comments immediately above public or non-obvious settings.
  Explain purpose, accepted shape, units, defaults, constraints, or security
  implications—not YAML syntax or change history.
- Keep comments accurate to the current file. Do not describe prior values,
  migrations, diffs, or implementation deltas.
- Keep related schemas, examples, and reference documentation aligned with the
  keys and defaults that consumers receive.

## Portable YAML

- Follow the repository's existing indentation and formatting conventions;
  otherwise use two-space indentation and avoid tabs.
- Quote strings that could be parsed as booleans, nulls, dates, version
  numbers, identifiers with leading zeroes, or numbers that must remain
  strings. Keep true booleans and numeric values unquoted.
- Use block scalars intentionally: `|-` preserves line breaks and removes
  the final newline; `>-` folds prose and removes the final newline.
- Avoid anchors, aliases, and custom tags in public configuration unless the
  consuming tool explicitly supports them and the reuse materially improves
  correctness.
- Use placeholders or secret references in examples. Never place credentials,
  tokens, keys, or private endpoints in YAML defaults or comments.

```yaml
# Duration before the worker gives up waiting for the upstream service.
requestTimeoutSeconds: 30

# Identifier used by the deployment platform; preserve as a string.
releaseId: "00142"
```
