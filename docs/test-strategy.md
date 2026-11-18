# 🧭 Test Strategy

## Purpose
The most useful test layers are source profiling, transformation checks, model integrity, independent measure reconciliation, visual/interaction review, accessibility review, and documentation validation.

## Current project context
There is no conventional application unit-test suite in the repository. Automate deterministic text and asset checks; perform PBIX-dependent checks in Power BI Desktop.

## Recommended workflow
Choose tests based on change risk. A schema change requires data/model regression tests; a DAX change requires independent calculations and edge cases; a visual change requires rendering and accessibility review.

## Evidence and verification
A green documentation workflow does not certify report calculations or visuals.

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
