# 🐛 Debugging Guide

## Purpose
Debugging should identify which layer failed: source workbook, Power Query, semantic model, DAX calculation, report visual, or repository automation.

## Current project context
For source errors inspect file path, workbook availability, sheet/table selection, and schema changes. For query errors inspect Applied Steps and conversion errors. For model issues inspect relationship keys, cardinality, and filter direction. For measure issues simplify the DAX expression and record filter context. For visual issues inspect filters, sort, field assignments, and blank handling.

## Practical process
Preserve the failing copy and sanitized error details. Change one factor at a time. Confirm the fix with a reproducible test and a known-good comparison. For repository docs, use the validator output to locate missing links or malformed SVGs.

## Verification and boundaries
Do not suppress query or measure errors without understanding the business meaning of the affected records.

## Related documentation
See the [documentation index](README.md), [project scope](scope-and-limitations.md), and [QA guide](qa.md).
