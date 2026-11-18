# 🔑 Access Control and Sharing

## Purpose
The GitHub repository is public. A local PBIX does not expose a custom login system. If published to Power BI Service, workspace/report permissions and configured row-level security become relevant.

## Current project context
Service roles, access groups, report sharing, export settings, and RLS are not established by the current repository files.

## Recommended workflow
Review who can read, write, administer, download, and redistribute every artifact. Before publishing, identify the audience, review workspace roles, test as a normal viewer, and document export/share settings.

## Evidence and verification
A visual filter is not row-level security. Record RLS role definitions and test identities only after inspecting the PBIX.

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
