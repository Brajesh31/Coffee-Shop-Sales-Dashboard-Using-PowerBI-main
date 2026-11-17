# 🗺️ Project Roadmap

This roadmap separates completed repository documentation work from proposed report-analysis work. A task is not complete until its evidence is reviewed.

## 🔎 Discovery and reproducibility

- [ ] Inspect workbook sheet names, columns, types, row counts, date range, and quality profile.
- [ ] Inspect PBIX report pages, visuals, filters, bookmarks, and interactions.
- [ ] Record all model tables, relationships, keys, and storage modes.
- [ ] Inventory DAX measures and calculated columns.
- [ ] Document actual Power Query source and transformation steps.
- [ ] Verify refresh after moving the source workbook to a clean local path.

## 📊 Analytical quality

- [ ] Define the grain and business definition of each KPI.
- [ ] Validate total sales, orders, and quantity against the source workbook.
- [ ] Validate month-over-month comparisons and missing-period behavior.
- [ ] Validate the ranking measure used by the top-ten product view.
- [ ] Check weekday/weekend classification and day-hour aggregation.
- [ ] Review currency, date, number, and percentage formatting.

## 🎨 Report usability

- [ ] Capture real screenshots for each report page.
- [ ] Review readability at common desktop and smaller window sizes.
- [ ] Verify keyboard and screen-reader considerations supported by Power BI.
- [ ] Review contrast, color dependence, titles, labels, and tooltip clarity.

## 🚀 Sharing and operations

- [ ] Document an intentional Power BI Service publishing path if used.
- [ ] Confirm data classification before publishing or sharing.
- [ ] Document gateway and scheduled refresh only if configured.
- [ ] Add a verified public report link only if one is approved for public access.

## ✅ Completion rule

Do not mark a task complete based only on documentation being written. Attach a result, screenshot, formula review, or reproducible validation outcome.
