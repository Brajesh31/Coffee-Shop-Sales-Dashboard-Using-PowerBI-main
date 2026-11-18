# 🔄 Report Lifecycle

## Purpose
The lifecycle is maintain source workbook, preserve a known-good copy, inspect or update Power Query, refresh the model, validate relationships and measures, review visuals and filters, capture evidence, save a versioned PBIX, update documentation, and distribute the approved artifact.

## Current project context
This is a report lifecycle, not an application runtime. The report executes inside Power BI Desktop or an approved Power BI environment selected by the owner.

## Recommended workflow
Stop a release when source refresh fails, totals do not reconcile, a critical visual is blank, sensitive data is exposed, or documentation no longer matches the PBIX. Record the failure and recovery evidence.

## Evidence and verification
Do not describe a build server, web deployment, or automated PBIX compiler unless one is actually introduced.

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
