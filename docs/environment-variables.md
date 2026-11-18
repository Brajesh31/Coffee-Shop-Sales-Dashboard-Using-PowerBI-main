# 🔐 Environment Variables

## Purpose
No application runtime or environment-variable contract is visible. An environment file is not required by the documented process for opening the PBIX. Power BI source credentials, if required, belong in Power BI credential settings.

## Current project context
Do not create example secrets or pretend that a .env file is part of the dashboard. If future automation introduces environment variables, document exact name, purpose, required status, format, secret classification, and configuration location.

## Recommended workflow
Never commit passwords, access tokens, tenant secrets, GitHub tokens, or private workspace identifiers. Secret handling guidance belongs in secret-management.md.

## Evidence and verification
No .env.example file is created because there is no verified environment-variable contract in the current project.

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
