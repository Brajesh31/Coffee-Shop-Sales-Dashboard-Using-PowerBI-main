# 🔎 Observability and Diagnostics

## Purpose
Observability for this file-based project means traceable source versions, refresh evidence, KPI reconciliation, performance measurements, issue history, and artifact hashes.

## Current project context
The project does not emit custom logs, metrics, or distributed traces. Power BI Desktop diagnostics and GitHub Actions logs are the relevant existing evidence sources.

## Practical process
For incidents, capture the report/workbook version, environment, operation, query or measure, filter context, duration, sanitized error, and reproduction. For each release, keep commit and file hashes plus test report.

## Verification and boundaries
Do not create observability badges or imply live instrumentation that is not present.

## Related documentation
See the [documentation index](README.md), [project scope](scope-and-limitations.md), and [QA guide](qa.md).
