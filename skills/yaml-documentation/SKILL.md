---
name: yaml-documentation
description: Document YAML configuration files with concise contract comments, portable scalar handling, and schema-aligned examples. Use when creating or revising YAML configuration documentation, comments, examples, schemas, or values files outside Helm-specific workflows.
---

# YAML Documentation

Describe the configuration consumers use now. Keep comments factual, local,
and free of change narratives.

## Workflow

1. Identify the YAML consumer, schema, parser version, existing formatting,
   examples, and validation command. Do not assume all YAML consumers support
   the same features.
2. Document public and non-obvious keys directly above their definitions.
   Explain purpose, accepted value shape, units, default behavior, constraints,
   and security implications where relevant.
3. Preserve portable scalar intent:
   - Quote identifiers, versions, date-like values, boolean-like strings,
     null-like strings, leading-zero values, and numeric strings.
   - Keep actual booleans and numbers unquoted.
   - Use `|-` for literal multi-line content and `>-` for folded prose
     when their newline behavior is intentional.
4. Keep schemas, examples, and reference documentation synchronized with
   current keys and defaults. Use secret references or placeholders rather
   than real credentials.
5. Avoid comments that restate YAML syntax, narrate control flow, or describe
   previous implementations and patch deltas.
6. Run the repository's YAML parser, schema validation, formatter, and linter
   commands when available.

## Pattern

```yaml
# Comma-separated hosts accepted by the proxy.
allowedHosts: "api.example.com,admin.example.com"

# PEM certificate presented by the service.
tlsCertificate: |-
  -----BEGIN CERTIFICATE-----
  <certificate-data>
  -----END CERTIFICATE-----
```
