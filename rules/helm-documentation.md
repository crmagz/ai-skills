---
description: Helm chart documentation standards for Chart.yaml, README files, values.yaml, and values schemas
alwaysApply: true
version: 1.0.0
globs: "**/Chart.yaml,**/values*.yaml,**/values.schema.json,**/templates/**/*.yaml,**/templates/**/*.yml,**/templates/**/*.tpl"
---

# Helm Documentation

## Chart Contract

- Keep `Chart.yaml` name, version, description, dependencies, and chart type
  accurate. Write the description for chart consumers, not implementation
  history.
- Document installation, upgrade constraints, dependencies, required
  permissions, and operational behavior in the chart README when the chart is
  user-facing.
- Keep `values.schema.json` descriptions and constraints aligned with public
  `values.yaml` keys when a schema is present.

## Values Files

Treat `values.yaml` as a user-facing configuration API.

- Use lower camel case for values keys. Prefer flat values; nest only coherent,
  related settings where at least one member is required.
- Precede public or non-obvious values with concise comments that state their
  purpose, accepted shape, default behavior, and important constraints.
- Quote strings, including string-form identifiers and large integers, to
  avoid YAML type coercion. Leave actual booleans and numbers unquoted.
- Provide safe, functional defaults or make required values explicit. Never
  commit real secrets, tokens, or private endpoints.
- Preserve override compatibility: do not rename, move, or change a value's
  type without documenting migration and compatibility implications.

```yaml
# Image reference used by the Deployment. Tag defaults to the chart appVersion.
image:
  repository: "example/service"
  tag: ""

# Number of ready replicas maintained by the Deployment.
replicaCount: 2
```

## Generated Values References

When the chart already uses a documentation generator that recognizes values
annotations, retain and extend its established annotation format:

- Use `## @section <name>` to group a coherent set of consumer settings.
- Use `## @param <value.path> <description>` for public value paths.
- Use `## @extra <value.path> <description>` for complex objects whose
  nested fields need contextual explanation.
- Keep annotations immediately before the value or group they document, and
  ensure every documented path exists and remains override-compatible.
- Do not introduce annotation syntax unless the repository's chart tooling
  already supports it.

```yaml
## @section Service
## @param service.port Port exposed by the Kubernetes Service.
##
service:
  port: 8080
```

## Template Comments

- Comment templates only to explain non-obvious rendering constraints,
  Kubernetes behavior, or security and compatibility decisions.
- Use helpers for repeated expressions instead of prose that restates
  templating syntax.
- Do not document change history, prior values, or patch deltas in templates
  or values files.
