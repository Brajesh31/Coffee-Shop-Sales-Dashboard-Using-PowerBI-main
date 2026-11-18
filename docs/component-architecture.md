# 🧩 Component Architecture

## Purpose
Logical layers: source workbook; Power Query preparation; PBIX semantic model; DAX calculations; report pages and visuals; analyst consumption; GitHub repository and documentation automation.

## Current project context
The boundaries are conceptual. Internal query names, model object names, relationships, and visual configurations are uninspected. No API, database, authentication service, or microservice boundary is visible.

## Recommended workflow
For every discovered component, record its inputs, outputs, owner, dependencies, failure modes, security implications, and verification method. Update diagrams only when the real design changes.

## Evidence and verification
Use an ER diagram only for a verified relational schema. The PBIX model is not automatically equivalent to an external database schema.

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
