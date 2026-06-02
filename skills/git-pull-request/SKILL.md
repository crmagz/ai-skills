---
name: git-pull-request
description: Interactive workflow for creating pull requests following project standards.
version: 1.0.0
invocation: /pr
---

# Create Pull Request

## Prerequisites

Before running this skill, validate the following:

### 1. GitHub CLI Installation

Check if `gh` is installed:

```bash
command -v gh
```

If not installed, provide platform-specific instructions:

- **macOS**: `brew install gh`
- **Ubuntu/Debian**: `sudo apt install gh`
- **Fedora**: `sudo dnf install gh`
- **Arch**: `sudo pacman -S github-cli`

### 2. GitHub Authentication

Check authentication status:

```bash
gh auth status
```

If not authenticated:

```bash
gh auth login
```

### 3. Git Status

Verify clean working state and correct branch:

```bash
git status
git branch --show-current
```

## Workflow

### Step 1: Validate Environment

Run these checks before proceeding:

1. **gh CLI**: `command -v gh` must succeed
2. **gh auth**: `gh auth status` must show authenticated
3. **Git repo**: Must be in a git repository
4. **Branch**: Should NOT be on `master` or `main`
5. **Clean state**: No uncommitted changes (warn if present)

If any check fails, stop and provide remediation steps.

### Step 2: Analyze Changes

Gather information about the PR:

```bash
# Get current branch
BRANCH=$(git branch --show-current)

# Get commits since diverging from master
git log master..HEAD --oneline

# Get changed files
git diff --name-only master...HEAD
```

### Step 3: Validate Test Coverage

Check if changes require tests:

```bash
# List changed source files
git diff --name-only master...HEAD | grep -E '^src/'
```

If source files changed, verify test updates:

```bash
# List changed test files
git diff --name-only master...HEAD | grep -E '^tests/'
```

**Validation Rules**:
- If `src/**` files changed AND no `tests/**` files changed:
  - WARN: "Source files modified but no tests added/updated"
  - ASK: "Is this intentional? (docs-only, config, trivial change)"

### Step 4: Validate Documentation

Check if changes require documentation:

```bash
# List changed doc files
git diff --name-only master...HEAD | grep -E '^docs/'
```

**Validation Rules**:
- If `feat` or breaking change AND no `docs/**` files changed:
  - WARN: "New feature but no documentation added"
  - ASK: "Should documentation be added before creating PR?"

### Step 5: Extract JIRA ID

Extract JIRA ID from branch name or commits:

```bash
# From branch name (e.g., feat/FALCON9-123-description)
echo "$BRANCH" | grep -oE '[A-Z]+-[0-9]+'

# From commit messages
git log master..HEAD --format=%s | grep -oE '[A-Z]+-[0-9]+' | head -1
```

If no JIRA ID found:
- ASK: "What is the JIRA issue ID for this PR?"

### Step 6: Determine PR Type

Analyze commits to suggest PR type:

```bash
git log master..HEAD --format=%s
```

- Look for conventional commit prefixes (feat, fix, etc.)
- Suggest the most common type found
- ASK user to confirm or change

### Step 7: Generate PR Title

Format: `<type>(JIRA-ID): <description>`

- Use the determined type and JIRA ID
- Generate description from branch name or ask user
- Validate: lowercase, no period, max 72 chars

### Step 8: Generate PR Body

Use the PR template format:

```markdown
## JIRA Issue

[JIRA-ID](https://your-domain.atlassian.net/browse/JIRA-ID)

Resolves: [JIRA-ID]

## Type of Change

- [ ] Feature (new functionality)
- [ ] Bug fix (non-breaking fix)
- [ ] Refactor (no functional change)
- [ ] Performance improvement
- [ ] Documentation update
- [ ] Infrastructure / CI / Build
- [ ] Breaking change

## Summary

[What problem does this solve? What's the motivation?]

## What Changed

[What did you change and why this approach? What alternatives did you consider?]

## How You Tested

[Unit tests? Integration tests? Manual validation? Include commands or steps]

- [x/space] Tests added/updated in `/tests`
- [x] All tests pass locally

## Checklist

- [x] PR title follows conventional commit format
- [x] Self-reviewed my own code
- [x/space] Docs updated (if behavior changed)
- [x] No new warnings generated
```

### Step 9: Run Pre-PR Checks

Execute validation commands based on the project type:

**Node.js projects:**
```bash
npm run test
npm run lint
npm run build
```

**Python projects:**
```bash
uv run test
uv run lint
```

**Java projects:**
```bash
./gradlew test
./gradlew check
./gradlew build
```

Detect project type by checking for:
- `package.json` → Node.js
- `pyproject.toml` or `uv.lock` → Python
- `build.gradle` or `build.gradle.kts` → Java/Gradle

If any checks fail:
- STOP: "Pre-PR checks failed. Fix issues before creating PR."

### Step 10: Create PR

If all validations pass:

```bash
gh pr create \
  --title "<type>(JIRA-ID): <description>" \
  --body "<generated body>" \
  --base master
```

### Step 11: Output Result

Display:
- PR URL
- PR number
- Review link

## Error Handling

| Error | Resolution |
|-------|------------|
| gh not installed | Provide install instructions for detected platform |
| gh not authenticated | Run `gh auth login` |
| Not a git repo | Navigate to a git repository |
| On master/main | Create a feature branch first |
| Tests failing | Fix tests before creating PR |
| No JIRA ID | Require JIRA ID input |

## Example Usage

```
User: /pr
