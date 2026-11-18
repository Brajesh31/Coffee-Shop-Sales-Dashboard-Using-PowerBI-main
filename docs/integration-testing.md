# 🔗 Integration Testing

## Purpose
The key integration chain is Excel source to Power Query to semantic model to DAX to report visuals. No separate API/database integration suite is applicable to the visible repository.

## Current project context
Test that the expected workbook object is read, transformations produce the expected schema, relationships propagate filters, measures evaluate in intended context, and visuals show results without errors.

## Recommended workflow
Record source version, query status, row-count comparison, relationship checks, KPI reconciliation, filter behavior, and visual result. Extend this guide if an external connector is added.

## Evidence and verification
A successful query refresh does not establish that a measure or visual is correct.

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
