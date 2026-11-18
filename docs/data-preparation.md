# 🧹 Data Preparation and Power Query

## Purpose
The README identifies Power Query as the preparation technology. Exact query names, applied steps, M expressions, source navigation, dependencies, and load settings require Power BI Desktop inspection.

## Current project context
For each query, record its source, applied steps, changed types, filtered rows, renamed columns, merges/appends, custom columns, error handling, load destination, and refresh behavior.

## Recommended workflow
Validate source row counts against loaded output, inspect conversion errors, check nulls and duplicates, and test schema drift. Store safe M-expression excerpts only when they do not expose credentials or private paths.

## Evidence and verification
Do not describe a transformation that has not been observed in the PBIX.

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
