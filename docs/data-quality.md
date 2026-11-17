# ✅ Data Quality and Validation

## Quality dimensions
| Dimension | Question | Suggested check |
|---|---|---|
| Completeness | Are required values present? | Null/blank counts for dates, sales, quantity, keys |
| Validity | Are values in expected domains? | Date, numeric, category, currency checks |
| Uniqueness | Are identifiers unique at intended grain? | Duplicate key counts |
| Consistency | Are categories and units standardized? | Distinct-value and spelling review |
| Integrity | Do dimension references resolve? | Unmatched key checks |
| Accuracy | Do totals match the source? | Independent aggregation |
| Timeliness | Is the workbook current? | Source date and refresh record |

## 🧪 Reconciliation protocol
1. Choose a known period and filter context.
2. Calculate totals independently from the workbook.
3. Apply the same filters in Power BI.
4. Compare sales, order count, and quantity.
5. Investigate every variance beyond documented tolerance.
6. Record whether differences are caused by filters, duplicates, blank handling, returns, date boundaries, or transformations.

## ⚠️ Known unknowns
The workbook and PBIX internals were not text-extracted in this pass. No row counts, date range, null rates, duplicate rate, or KPI reconciliation result is claimed.

Use [data-quality-template.md](templates/data-quality-template.md) for repeatable profiling and sign-off.
