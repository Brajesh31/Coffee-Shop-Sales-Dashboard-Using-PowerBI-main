# 🧯 Disaster Recovery

## Purpose
The main recovery assets are the last known-good PBIX, matching source workbook, documentation, and repository history. There is no application server or database cluster to fail over.

## Current project context
Keep recoverable copies in approved access-controlled storage. Preserve the commit hash of each known-good release. Confirm a maintainer can retrieve the pair, open the report, reconnect the workbook, refresh, and reproduce critical KPIs.

## Recommended workflow
Set RPO/RTO targets only after the owner agrees on business criticality. A public GitHub repository is not automatically an approved backup for confidential source data.

## Evidence and verification
undefined

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
