# 🗑️ Deprecation Policy

## Purpose
This policy applies to report pages, visuals, measures, source fields, query outputs, documentation links, and reusable templates.

## Current project context
Before removing or renaming an object, identify downstream dependencies in queries, relationships, DAX measures, visuals, filters, exports, and existing user guidance.

## Practical process
Give contributors notice in a changelog or migration note, provide a replacement or rationale, update affected docs, and test the report after removal. Remove an obsolete KPI only after confirming it is not relied upon.

## Verification and boundaries
Do not delete source columns or measures based only on apparent unused status; verify dependencies inside the PBIX.

## Related documentation
See the [documentation index](README.md), [project scope](scope-and-limitations.md), and [QA guide](qa.md).
