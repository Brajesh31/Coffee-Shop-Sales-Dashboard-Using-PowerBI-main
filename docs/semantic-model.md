# 🧱 Semantic Model

## Purpose
This guide records how to inspect and document the Power BI model. The model is inside the PBIX binary and was not decoded during this repository update.

## 📋 Table inventory
| Table | Grain | Primary key | Role | Source |
|---|---|---|---|---|
| To be inspected | To be inspected | To be inspected | Fact / dimension / bridge | To be inspected |

Do not treat the example header as evidence that a particular table exists.

## 🔗 Relationship inventory
For every relationship, record:
- From table and column.
- To table and column.
- Cardinality.
- Cross-filter direction.
- Active or inactive status.
- Referential integrity assumptions.
- Reason for any many-to-many relationship.

## 📅 Date model review
Confirm whether a dedicated calendar table exists, whether it is marked as a date table, and how it relates to transaction dates. Record fiscal/calendar definitions, week-start convention, month labels, and handling of missing dates.

## 🧭 Filter context
Document which report slicers filter which tables. Verify that store, category, product, and date selections affect all intended measures and visuals consistently.

## ✅ Model validation
- [ ] Every table has a documented purpose and grain.
- [ ] Keys are stable and correctly typed.
- [ ] Relationships match the business model.
- [ ] Ambiguous filter paths are reviewed.
- [ ] Date relationship is verified.
- [ ] Unused columns and tables are considered for removal.
- [ ] Measures are organized and named consistently.
- [ ] Totals reconcile to the source.
