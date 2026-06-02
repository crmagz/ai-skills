---
description: ProjectEnvironment type extension pattern and environment configuration
alwaysApply: true
version: 1.0.0
---

# CDK Environment Configuration

NEVER declare environment configuration directly in stacks. Always source from `ProjectEnvironment` defined in `src/types/` and configured in `bin/environments.ts`.

## ProjectEnvironment Type

Extend `EnvironmentConfig` from `@your-org/cdk` with project-specific properties:

```typescript
// src/types/project.ts
import {EnvironmentConfig} from '@your-org/cdk';

export type ProjectEnvironment = EnvironmentConfig & {
    azure: AzureConfig;
};

type AzureConfig = {
    clientId: string;
    tenantId: string;
    objectId?: string;
    applicationName?: string;
};
```

## Environment Array

Configure per-environment values in `bin/environments.ts`:

```typescript
import {ProjectAccount, ProjectEnvironmentName, ProjectRegion} from '@your-org/cdk';
import {ProjectEnvironment} from '../src/types/project';

export const environment: ProjectEnvironment[] = [
    {
        env: {
            name: ProjectEnvironmentName.DEV,
            region: ProjectRegion.USE1,
            account: ProjectAccount.NONPROD,
            team: ProjectDevelopmentTeam.ADSRE,
            application: 'secret-service-infra',
        },
        azure: {
            clientId: AzureClientId.DEV_CLIENT_ID,
            tenantId: AzureTenantId.DEV_TENANT_ID,
        },
    },
    // ... additional environments (staging, prod)
];
```

## Extending ProjectEnvironment

1. Add new properties to the type in `src/types/`
2. Add corresponding values for each environment in `bin/environments.ts`
3. Use the extended properties in stacks and constructs via `props`

Use enums (in `src/enums/`) for type-safe constants like account IDs, client IDs, and application names.
