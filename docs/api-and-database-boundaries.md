# 🚫 API and Database Boundaries

## Purpose
This is a Power BI dashboard repository. No REST/GraphQL API source, webhook receiver, application database schema, server-side authentication code, backend service, or web frontend is visible in the repository tree.

## Current project context
The analytical model is contained inside the PBIX and the source artifact is an Excel workbook. This is not an externally managed relational database schema.

## Recommended workflow
If an API or database is introduced later, add endpoint contracts, request/response schemas, auth rules, error codes, migrations, ER diagrams, monitoring, and security review before describing it as integrated.

## Evidence and verification
Do not create fake endpoints, database tables, or unused backend boilerplate merely to increase file count.

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
