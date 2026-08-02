---
name: helm-documentation
description: Document Helm charts, templates, values.yaml files, and values schemas as stable consumer-facing configuration contracts. Use when creating or revising Helm chart documentation, values comments, README configuration references, or chart metadata.
---

# Helm Documentation

Treat chart metadata and values as a versioned interface for chart consumers.
Document current behavior and compatibility, never the history of a patch.

## Workflow

1. Read `Chart.yaml`, `values.yaml`, templates, `values.schema.json`,
   README files, and existing examples. Identify values referenced through
   `.Values` and any documented override paths.
2. Update chart-facing documentation:
   - Keep `Chart.yaml` metadata accurate and concise.
   - Document install, dependency, security, upgrade, and operational
     requirements in the README when applicable.
   - Keep schema descriptions, defaults, and constraints in sync with
     `values.yaml`.
3. Document each public or non-obvious value directly above its key. Explain
   its purpose, expected form, default, and constraints; describe migration
   only when compatibility requires it.
   - When the chart uses a compatible generator, group settings with
     `## @section`, describe value paths with `## @param`, and use
     `## @extra` for complex objects. Preserve the repository's established
     annotation syntax rather than introducing unconfigured tags.
4. Use lower camel case keys, favor flat values, quote strings to avoid YAML
   coercion, and keep secret material out of defaults and examples.
5. Comment templates only for non-obvious Kubernetes or rendering constraints.
   Do not narrate template syntax, previous behavior, or implementation deltas.
6. Validate with `helm lint` and render representative defaults and override
   files with `helm template --debug` when Helm is available.

## Values Pattern

```yaml
# Service port exposed by the Kubernetes Service.
servicePort: 8080

# Domain name accepted by the ingress controller.
ingressHost: "service.example.com"
```
