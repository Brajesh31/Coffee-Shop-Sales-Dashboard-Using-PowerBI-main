# 🛠️ Troubleshooting

| Symptom | Likely area | What to check |
|---|---|---|
| PBIX cannot open | Desktop version or corrupt download | Re-download and use a supported Power BI Desktop release |
| Excel source not found | Saved local path | Update source step in Power Query |
| Credentials prompt | Source authentication | Review source type and credential settings |
| Refresh error | Query step or source schema | Inspect first failing query and changed headers/types |
| Blank KPI | Filter context, relationship, or measure logic | Clear filters and inspect model relationships |
| Month comparison blank | Date model or prior period | Check calendar coverage and prior-period logic |
| Unexpected order count | Transaction grain | Compare row count with distinct order identifiers |
| Heatmap values inconsistent | Day/hour derivation or aggregation | Validate date/time fields and filter context |
| Visual missing fields | Model schema changed | Rebind fields and update documentation |
| Workbook repair warning | File integrity | Use a verified copy and preserve the original |

Include sanitized error text, Desktop version, affected page/visual/measure, filters, reproduction steps, expected and actual value, and refresh status in bug reports. Never post confidential rows, credentials, or private workspace details.
