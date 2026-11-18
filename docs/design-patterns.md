# 🧱 Analytics Design Patterns

## Purpose
Useful BI patterns include clear fact-table grain, descriptive dimensions, explicit date intelligence, reusable measures, star-schema evaluation where appropriate, and separation of source shaping from report presentation.

## Current project context
The current model has not been reverse-engineered. Do not state that it already follows a star schema, uses a date dimension, or implements a specific relationship pattern.

## Practical process
During model review, identify facts and dimensions, keys, relationships, role-playing dates, filter direction, and measure dependencies. Apply a star schema when the actual data and analytical requirements justify it. Document trade-offs and regression tests for each model change.

## Verification and boundaries
Do not create a database ER diagram for unverified model tables. Use a model diagram captured from the actual PBIX where available.

## Related documentation
See the [documentation index](README.md), [project scope](scope-and-limitations.md), and [QA guide](qa.md).
