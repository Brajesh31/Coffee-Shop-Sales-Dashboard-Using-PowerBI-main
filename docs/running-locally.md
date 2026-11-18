# ▶️ Running the Report Locally

## Purpose
The local run experience is to open the PBIX in Power BI Desktop. There is no application process or HTTP port to start.

## Current project context
Keep the PBIX and workbook in a known directory. Open the PBIX. If a source path is broken, inspect Transform data and update the source step. Apply changes, refresh, and check for query or visual errors. Save a working copy rather than overwriting the original.

## Practical process
Record environment details and the exact source file used. Re-run critical KPI checks after refresh. For an error, follow debugging.md and troubleshooting.md.

## Verification and boundaries
Do not invent a localhost address, runtime command, or web route for this report.

## Related documentation
See the [documentation index](README.md), [project scope](scope-and-limitations.md), and [QA guide](qa.md).
