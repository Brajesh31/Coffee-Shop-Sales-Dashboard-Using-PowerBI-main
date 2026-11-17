# 🚀 Getting Started

## 🧰 Requirements
- Windows environment supported by Microsoft Power BI Desktop.
- A local copy of `coffee shop sales.pbix`.
- A local copy of `Coffee Shop Sales.xlsx`.
- Sufficient memory and disk space for the workbook and model.

Power BI Desktop installation guidance: https://learn.microsoft.com/power-bi/fundamentals/desktop-get-the-desktop

## 📥 Download
```bash
git clone https://github.com/Brajesh31/Coffee-Shop-Sales-Dashboard-Using-PowerBI-main.git
cd Coffee-Shop-Sales-Dashboard-Using-PowerBI-main
```

Or download a ZIP from GitHub. The repository includes a multi-megabyte Excel workbook and PBIX file.

## ▶️ Open the report
1. Launch Power BI Desktop.
2. Select **File → Open**.
3. Open `coffee shop sales.pbix`.
4. Review any source credential or path prompt.
5. If the Excel source is missing, inspect Power Query's source step.
6. Point the query to the local `Coffee Shop Sales.xlsx` copy.
7. Apply changes and refresh.
8. Check all report pages, filters, and visuals.
9. Save a separate working copy before editing.

## 🔄 First-refresh checklist
- [ ] Workbook exists locally.
- [ ] Source path points to intended workbook.
- [ ] No unexpected credential prompts remain.
- [ ] Queries complete without errors.
- [ ] Expected tables load.
- [ ] Date fields have intended data types.
- [ ] KPI values are not blank because of a broken relationship.
- [ ] Visuals render without missing-field warnings.

## 💾 Work safely
Treat the supplied PBIX as the baseline. Save experiments under a separate filename. Avoid overwriting the original until changes have been reviewed and validated.

See [Data refresh](data-refresh.md), [Troubleshooting](troubleshooting.md), and [Testing](testing.md).
