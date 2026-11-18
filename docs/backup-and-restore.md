# 💾 Backup and Restore

## Purpose
Git history records repository changes but does not replace an encrypted, access-controlled backup for sensitive source data.

## Current project context
Before editing, make a timestamped working copy. At release, retain the approved PBIX and matching workbook, record hashes and source versions, and store copies in approved backup storage.

## Recommended workflow
Restore the matching pair, correct only approved local paths, refresh, and reconcile critical KPIs. Never commit confidential backups to a public repository. Verify report open, refresh, filters, and visuals after restore.

## Evidence and verification
A successful Git checkout alone is not proof that a report can be refreshed or restored.

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
