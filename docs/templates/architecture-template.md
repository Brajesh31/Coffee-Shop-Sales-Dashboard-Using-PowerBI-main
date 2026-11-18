# 🏛️ Architecture Review Template

## Metadata
| Field | Value |
|---|---|
| ID / title | |
| Status | Proposed / Accepted / Superseded |
| Author / reviewer | |
| Date / last reviewed | |
| Related release / commit | |

## Context and business need
Describe the analytical question, existing report behavior, and reason for change.

## Current-state evidence
List inspected PBIX objects, workbook objects, query steps, model relationships, and genuine screenshots. Separate facts from assumptions.

## Proposed architecture
Describe source, preparation, model, calculation, presentation, and consumption layers. Add a Mermaid diagram if it clarifies a boundary.

## Alternatives
| Option | Benefits | Costs / risks | Decision |
|---|---|---|---|

## Data, security, and accessibility impact
Record grain, keys, filters, data classification, access changes, credential implications, and accessibility changes.

## Validation and acceptance
- [ ] Refresh succeeds.
- [ ] Critical KPIs reconcile.
- [ ] Relationships and filters are tested.
- [ ] Visuals and accessibility are reviewed.
- [ ] Documentation and rollback are updated.

## Consequences and follow-up
Record migration work, technical debt, owners, and evidence required for closure.
