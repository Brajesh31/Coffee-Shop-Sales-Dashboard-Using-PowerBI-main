# 🚦 Quality Gates

## Purpose
Gate 1: source schema and refresh are clean. Gate 2: critical KPIs reconcile. Gate 3: filters and interactions behave as intended. Gate 4: no critical accessibility/security issue remains. Gate 5: docs links and SVG assets validate. Gate 6: rollback artifacts and release notes exist.

## Current project context
Automated checks cover repository text and SVG. PBIX refresh, DAX, visual, and accessibility checks require the actual report and a suitable Power BI environment.

## Recommended workflow
When a check cannot be run, mark it blocked or not run. A missing test result is not a pass. Record reviewer sign-off and unresolved risks.

## Evidence and verification
Do not equate a passing docs workflow with report QA approval.

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
