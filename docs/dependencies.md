# 🔗 Dependencies and External Services

## Purpose
Operational dependencies include Power BI Desktop, access to the source workbook, compatible Excel/workbook handling, and Python 3.12 for the current docs-validation workflow.

## Current project context
The PBIX may contain connectors, M expressions, custom visuals, fonts, or other dependencies not visible through text-file inspection. No application package manifest is present.

## Recommended workflow
For each discovered dependency record name, version, source, license, update cadence, access requirement, security impact, and fallback. Review custom visuals and connectors before distribution.

## Evidence and verification
Do not claim a clean dependency scan or add npm/package badges when no such dependency manifest exists.

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
