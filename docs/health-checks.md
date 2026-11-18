# ❤️ Report Health Checks

## Purpose
A report health check is a release-time review, not an HTTP health endpoint. There is no web service to expose a /health route.

## Current project context
Check that the PBIX opens, expected workbook is available, refresh completes, model has no critical errors, key KPIs reconcile, core visuals render, filters behave, and no sensitive data is unintentionally exposed.

## Practical process
Record each result as pass, fail, blocked, or not run. Include source/report version and evidence. Recheck after source schema changes, Desktop upgrades, or report edits.

## Verification and boundaries
Do not create an application health endpoint or claim continuously monitored health.

## Related documentation
See the [documentation index](README.md), [project scope](scope-and-limitations.md), and [QA guide](qa.md).
