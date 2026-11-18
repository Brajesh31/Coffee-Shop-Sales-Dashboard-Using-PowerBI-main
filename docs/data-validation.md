# ✅ Data Validation and Reconciliation

## Purpose
Validation should cover source completeness, data types, keys, date coverage, category consistency, negative values, model relationships, and KPI totals.

## Current project context
Map each rule to the actual workbook schema after inspection. The README's business categories do not prove exact field names or source grain.

## Recommended workflow
For every critical KPI, select a controlled date/store/category context, calculate an independent workbook result, compare the report output, and record expected, actual, variance, tolerance, source/report version, reviewer, and date.

## Evidence and verification
A successful refresh is not the same as a reconciled dataset. See data-quality.md and test-plan.md.

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
