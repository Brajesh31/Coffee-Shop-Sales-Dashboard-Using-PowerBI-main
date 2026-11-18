# 📦 Dependency Security

## Purpose
The visible repository has no application package manifest. Main operational dependencies are vendor desktop software, the Excel workbook, GitHub Actions, and any custom visual or connector embedded in the PBIX.

## Current project context
Review workflow action ownership and version, Power BI Desktop updates, Office security updates, and the source of any custom visual/connector discovered during PBIX inspection.

## Practical process
Record each dependency, version, permission scope, update path, license, risk, and review date. Run relevant scanners only against an actual dependency inventory and report the scope of each scan.

## Verification and boundaries
Do not show a package-audit badge where no package manager or dependency lockfile exists.

## Related documentation
See the [documentation index](README.md), [project scope](scope-and-limitations.md), and [QA guide](qa.md).
