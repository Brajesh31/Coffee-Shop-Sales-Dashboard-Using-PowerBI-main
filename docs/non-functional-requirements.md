# ⚙️ Non-functional Requirements

## Purpose
Reliability means the PBIX opens and refreshes from the intended workbook. Accuracy means measures reconcile to independent source calculations. Usability means titles, labels, units, and date context are understandable. Maintainability means transformations and measures can be traced. Security means sensitive data and credentials are not exposed. Accessibility means colour is not the only way to interpret values.

## Current project context
Performance targets must be measured on representative hardware and data volume. The repository does not publish a verified refresh-time or rendering-time baseline. Compatibility must state the tested Desktop and Excel versions.

## Recommended workflow
For each release, record environment, source size, selected filters, measured open/refresh/render times, QA results, and unresolved risks. Review security and accessibility after material changes.

## Evidence and verification
Do not publish arbitrary targets as achieved results. See performance, accessibility, and security guidance.

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
