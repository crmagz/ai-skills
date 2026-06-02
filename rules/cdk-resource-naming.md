---
description: Collision-safe kebab-case resource naming conventions for CDK
alwaysApply: true
version: 1.0.0
---

# CDK Resource Naming Conventions

## Naming Format

All resources must follow this collision-safe pattern:

```typescript
`resource-name-${props.env.name}-${props.env.region}`
```

Examples:

```typescript
`secret-service-kms-${props.env.name}`
`secret-metadata-inventory-${props.env.name}`
`secret-create-lambda-${props.env.name}`
`secret-create-rule-${props.env.name}`
`secret-create-lambda-role-${props.env.name}`
```

## Kebab-Case Standard

Use kebab-case (lowercase with dashes) for all resource names:

```
app-apollo-api-dev          # correct
app-sigma-tests-prod        # correct
secret-create-lambda-dev    # correct
```

Do NOT use camelCase (`appApolloAPIDev`), snake_case (`app_apollo_api_dev`), or mixed case (`App-Apollo-API-Dev`).

## No Redundant Type Suffixes

Do NOT append the resource type to the name. The resource type is already known from the SDK/construct context.

```
app-sigma-tests-prod              # correct
app-sigma-tests-prod-secret       # incorrect — redundant suffix
app-sigma-tests-prod-bucket       # incorrect — redundant suffix
```
