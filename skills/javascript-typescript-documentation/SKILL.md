---
name: javascript-typescript-documentation
description: Document public JavaScript, TypeScript, and Node.js APIs with JSDoc, including request parameters, results, errors, and linked types. Use when adding or revising JSDoc, exported API documentation, or explanatory code comments.
---

# JavaScript, TypeScript, and Node.js Documentation

Document the API that callers use today. Do not use documentation to narrate
the patch or a previous implementation.

## Workflow

1. Read repository instructions, compiler or JSDoc configuration, exports,
   call sites, and neighboring public APIs.
2. Document exported functions, classes, types, callbacks, and Node.js entry
   points when names and declarations do not fully express their contract.
3. Write concise JSDoc:
   - Use `@param` for request objects, options, callbacks, and dependencies;
     document nested request fields only when their meaning is unclear.
   - Use `@returns` for result or response semantics, including the resolved
     value of an async API.
   - Use `@throws` for handled failure modes and `{@link TypeName}` for
     related exported types.
   - In TypeScript, do not repeat declared types in tags. In JavaScript, add
     JSDoc type expressions when they support editor and type-checker tooling.
4. Keep implementation comments for invariants, interoperability constraints,
   security decisions, and intentionally surprising behavior only. Never
   comment on code deltas or historical behavior.
5. Run the repository's type check, lint, documentation, and test commands.

## Pattern

```ts
/**
 * Submit an order to the payment provider.
 *
 * @param request - Customer, line-item, and payment inputs.
 * @returns A {@link PaymentReceipt} for the accepted order.
 * @throws {PaymentError} If the provider declines the payment.
 */
export async function submitOrder(
  request: SubmitOrderRequest,
): Promise<PaymentReceipt> {
  // ...
}
```
