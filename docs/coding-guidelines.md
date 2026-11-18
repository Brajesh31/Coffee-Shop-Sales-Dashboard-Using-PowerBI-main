# 🧭 Coding and Modeling Guidelines

## Purpose
For DAX, use explicit measure names, consistent naming, readable indentation, and clear denominator behavior. For Power Query, keep transformations traceable and avoid hidden magic constants. For SVG, provide a title and description. For Python validation, keep checks deterministic and fail clearly.

## Current project context
A measure should have a documented business definition, grain, aggregation, filter behavior, units, blank/zero behavior, and reconciliation example. A query should have documented source, applied steps, output schema, and refresh assumptions.

## Practical process
Review changes in context: a measure may be numerically valid but semantically misleading when applied to the wrong grain or date context. Do not rename source columns without assessing downstream dependencies.

## Verification and boundaries
These guidelines are recommendations for future edits, not an assertion that the original PBIX uses these conventions.

## Related documentation
See the [documentation index](README.md), [project scope](scope-and-limitations.md), and [QA guide](qa.md).
