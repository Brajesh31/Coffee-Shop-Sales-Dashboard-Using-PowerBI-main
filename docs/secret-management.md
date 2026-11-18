# 🗝️ Secret and Credential Management

## Purpose
No .env contract is visible. Power BI source credentials, if required, should be managed by Power BI credential settings. GitHub workflow credentials should be provided by protected GitHub token/secret mechanisms.

## Current project context
Before sharing a PBIX, inspect source settings, parameters, M expressions, and embedded connection metadata. Before publishing screenshots, remove tenant IDs, private URLs, account names, and credential dialogs.

## Recommended workflow
If a secret is exposed, revoke or rotate it, assess scope, inspect workflow logs and repository history, and document the incident privately. Removing a secret from the latest commit does not invalidate it.

## Evidence and verification
Never store passwords, tokens, or connection secrets in Markdown, Power Query examples, screenshots, or committed environment files.

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
