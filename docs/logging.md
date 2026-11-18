# 🪵 Logging and Diagnostics

## Purpose
There is no custom application logging subsystem in the repository. Diagnostics come from Power BI Desktop refresh/query error details, Query Diagnostics where appropriate, Performance Analyzer, and GitHub Actions logs.

## Current project context
Capture timestamp, artifact version, affected query/measure/page, sanitized error text, operation, filter context, environment, and reproduction steps. Avoid recording customer-level data, credential values, private workspace URLs, or tenant secrets.

## Practical process
Use logs to support diagnosis, not as a substitute for root-cause analysis. Retain only the detail needed to reproduce the defect and follow the data owner's retention rules. If Service is later used, document the available refresh history and audit facilities separately.

## Verification and boundaries
Do not create fake application log files or health telemetry that the report does not emit.

## Related documentation
See the [documentation index](README.md), [project scope](scope-and-limitations.md), and [QA guide](qa.md).
