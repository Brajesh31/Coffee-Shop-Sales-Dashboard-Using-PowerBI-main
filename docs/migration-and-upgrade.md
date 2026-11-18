# 🔄 Migration and Upgrade Guide

## Purpose
Possible upgrades include a new workbook schema, moved source path, changed table grain, Desktop version change, custom visual update, or report theme revision.

## Current project context
Back up the matched PBIX/XLSX pair and record baseline KPIs. Apply the upgrade to a working copy. Compare schema, query output, relationships, measures, visual rendering, refresh, compatibility, and accessibility.

## Recommended workflow
Do not replace source artifacts in place without rollback. Document downstream query, measure, and visual impacts for removed or renamed fields.

## Evidence and verification
Use the migration template and update versioning.md.

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
