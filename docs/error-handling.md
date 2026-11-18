# 🧯 Error Handling and Recovery

## Purpose
Potential failure classes include a missing workbook path, unsupported file version, query conversion error, missing source column, invalid relationship key, blank measure, divide-by-zero result, inaccessible report file, or broken documentation link.

## Current project context
These are failure scenarios to guard against, not a claim that each defect currently exists.

## Recommended workflow
Preserve the failing copy, record exact sanitized error text and reproduction steps, check source availability and schema, review recent query/model changes, and validate against a known-good workbook/PBIX. Avoid blanket error suppression unless a business rule justifies it.

## Evidence and verification
Do not include credentials or confidential values in logs. For repository failures, run the documentation validator and inspect the reported path.

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
