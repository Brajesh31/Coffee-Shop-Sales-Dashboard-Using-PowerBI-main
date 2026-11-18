# ↩️ Rollback Procedure

## Purpose
Rollback targets include the previous PBIX/workbook pair, documentation commit, and workflow configuration.

## Current project context
Identify the failing release, stop further distribution, restore the matching known-good pair, correct approved local paths, refresh, reconcile key KPIs, and review interactions. Revert related documentation/workflow changes where necessary.

## Recommended workflow
Record rollback commit, source/report hashes, approver, reason, validation evidence, and follow-up work.

## Evidence and verification
Rotate exposed credentials separately; reverting a file does not revoke a secret.

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
