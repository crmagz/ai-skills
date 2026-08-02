---
description: JSDoc standards for JavaScript, TypeScript, and Node.js public APIs
alwaysApply: true
version: 1.0.0
globs: "*.js,*.cjs,*.mjs,*.jsx,*.ts,*.tsx"
---

# JavaScript, TypeScript, and Node.js Documentation

## Public API JSDoc

Document exported functions, classes, interfaces, type aliases, callbacks, and
Node.js entry points when their contract is not clear from their name and type
signature.

- Start with a concise summary of current behavior.
- Use `@param` for every non-obvious request, options, callback, and
  dependency argument. Describe semantics, validation, defaults, ownership,
  and mutation behavior.
- Use `@returns` for meaningful synchronous and asynchronous results.
  Describe what callers receive or the fulfilled value, not merely
  `Promise<T>`.
- Use `@throws` for errors callers are expected to handle.
- Link related exported types with `{@link TypeName}` or a resolvable
  JSDoc namepath. Do not duplicate TypeScript annotations in prose.
- In JavaScript, include JSDoc type expressions when they provide type
  checking. In TypeScript, let declared types remain the type source of truth.

```ts
/**
 * Create a deployment from a validated request.
 *
 * @param request - Deployment inputs and target environment.
 * @param client - Authenticated API client used to create the deployment.
 * @returns The created {@link Deployment}, including its server-assigned ID.
 * @throws {DeploymentError} If the API rejects the request.
 */
export async function createDeployment(
  request: CreateDeploymentRequest,
  client: DeploymentsClient,
): Promise<Deployment> {
  // ...
}
```

## Comments

- Explain non-obvious invariants, runtime constraints, security decisions, or
  required ordering near the code that relies on them.
- Do not narrate syntax, restate type declarations, or write comments about
  previous code, migrations, diffs, or implementation changes.
- Prefer clear names, small helpers, types, and JSDoc over prose that repeats
  the code.
