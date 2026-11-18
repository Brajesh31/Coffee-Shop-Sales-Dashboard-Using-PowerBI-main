# 🔐 Security and Best Practices

## Purpose
Protect the workbook, PBIX, repository permissions, workflow tokens, screenshots, and any optional Service sharing configuration.

## Current project context
No custom authentication service or application authorization layer is present. Power BI source credentials, if any, belong in approved credential settings. Public repository visibility makes source-data classification especially important.

## Recommended workflow
Classify workbook contents before public release; minimize sensitive fields; avoid embedding credentials; restrict workflow permissions; review third-party actions; keep vulnerability reports private; and check sharing permissions before Service publication.

## Evidence and verification
A slicer is not a security control. RLS and Service permissions must be documented only if configured and tested. See access-control.md and secret-management.md.

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
