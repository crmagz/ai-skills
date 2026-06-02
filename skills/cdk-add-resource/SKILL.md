---
name: cdk-add-resource
description: Interactive workflow for adding new infrastructure resources to a CDK repository. Guides developers through extending types, configuring environments, and wiring into the stack.
version: 1.1.1
---

# Add CDK Resource

Step-by-step interactive workflow for adding a new infrastructure resource to a CDK repository.

## Workflow

### Step 1: Determine the Resource Type and Check Package Registry

Ask the developer what resource they are adding (Lambda, DynamoDB table, S3 bucket, OpenSearch cluster, etc.).

**Then, check the organization or project package registry before proceeding:**

| Package | AWS Service |
| --- | --- |
| `@your-org/cdk` or equivalent shared CDK package | Base CDK utilities, types, and enums |
| `@your-org/api-gateway` | API Gateway + Lambda constructs |
| `@your-org/aurora` | Aurora (RDS) clusters |
| `@your-org/bedrock` | Bedrock AI/ML resources |
| `@your-org/cloudfront` | CloudFront distributions |
| `@your-org/cloudwatch` | CloudWatch alarms, dashboards, logs |
| `@your-org/eks` | EKS clusters |
| `@your-org/elasticache` | ElastiCache (Redis/Memcached) |
| `@your-org/opensearch` | OpenSearch domains |
| `@your-org/s3` | S3 buckets |
| `@your-org/sqs` | SQS queues |
| `@your-org/waf` | WAF web ACLs and rules |

**Validation workflow:**

1. Identify the AWS service the resource belongs to
2. Check if a matching shared package exists in the table above
3. Query CodeArtifact to verify the package exists and check available versions:
   ```bash
   # List available shared packages
   npm search @your-org --registry <registry-url>

   # Get latest version info for a specific package
   npm view @your-org/<package-name> versions --json --registry <registry-url>
   ```
   If authentication fails, ask the engineer to authenticate to the package registry using the project-specific workflow.
4. If a package exists:
   - Check if the package is already installed in the project's `package.json`
   - If not installed, install it: `npm install @your-org/<package>` or the package manager command used by the repository
   - Inspect the package's exported functions and types (read `node_modules/@your-org/<package>/dist/index.d.ts` or source) to verify the specific construct is available
   - Follow the **Package-Provided** path (preferred)
5. If no matching package exists — follow the **Custom Construct** path

**Do NOT create custom constructs when an approved shared package already provides the resource.**

### Step 2: Extend ProjectEnvironment

Open `src/types/environment-type.ts` and add the new resource property to `ProjectEnvironment`:

```typescript
import {OrgPythonLambdaProps} from '@your-org/api-gateway';
import {EnvironmentConfig} from '@your-org/cdk';

export type ProjectEnvironment = EnvironmentConfig & {
    // existing properties...
    newResource: NewResourcePropsType;
};
```

Use the props type from the package when available. Otherwise, define a new type in `src/types/`.

### Step 3: Configure Environments

Open `bin/environments.ts` and add environment-specific values for each deployment target (dev, staging, prod):

- Use enums from `src/enums/` for type-safe constants
- Use helper functions like `getAbsoluteLambdaPath()` where available
- Follow the `cdk-resource-naming` rule for all resource names: `resource-name-${props.env.name}-${props.env.region}`

### Step 4: Wire into the Stack

**Package-Provided path** — call the package function directly in `lib/project-stack.ts`:

```typescript
import {createPythonLambda} from '@your-org/api-gateway';

// Inside the stack constructor
createPythonLambda(
    this,
    props.newResource.functionName,
    props.newResource.absPathToEntryFile,
    props.env.name,
    props.env.region,
    props.newResource
);
```

**Custom Construct path** — create a construct in `src/constructs/`, then call it from the stack:

```typescript
import {createMyConstruct} from '../src/constructs/create-my-construct';

// Inside the stack constructor
createMyConstruct(this, props);
```

Custom constructs should use arrow functions with explicit return types and accept `(scope: Construct, props: ProjectEnvironment)`.

### Step 5: Lambda Handlers (if applicable)

If the resource includes a Lambda function:

1. Create the handler in `src/lambda/{lambda-name}/`
   - Python: `lambda_function.py` with `lambda_handler` function
   - Node.js: `index.ts` with `handler` function
2. Configure in environments with: function name, VPC, subnets, memory, timeout, environment variables, IAM policy statements
3. Use `getAbsoluteLambdaPath('lambda-name', 'src/lambda')` for the path

### Step 6: Services (if applicable)

If the resource needs runtime service logic, follow the `cdk-service-pattern` rule:

1. Define interface in `src/interfaces/`
2. Implement in `src/services/` with a factory function export

### Step 7: Documentation

- Update README.md with a high-level summary if the resource is user-facing
- Add detailed documentation to `/docs` per the `cdk-documentation` rule

## Related Rules

- `cdk-directory-structure` — where files belong
- `cdk-stack-pattern` — stack implementation patterns
- `cdk-environment-config` — ProjectEnvironment extension
- `cdk-resource-naming` — naming conventions
- `cdk-code-style` — imports and TypeScript conventions
- `cdk-service-pattern` — interface-first services
- `cdk-documentation` — documentation standards
