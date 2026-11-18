# 🔁 CI/CD Pipeline

## Purpose
The repository currently has documentation-validation automation. PBIX refresh and full visual validation are not run in GitHub Actions.

## Current project context
The pipeline is therefore a repository quality pipeline, not a full Power BI build/deployment system.

## Recommended workflow
Automate Markdown link checks, required-file checks, SVG validation, and workflow linting when reliable. Keep Desktop-only tests in a release checklist. Use read-only permissions for validation jobs and scoped triggers.

## Evidence and verification
A green documentation workflow does not certify report correctness.

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
