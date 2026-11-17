# 🧮 DAX Measures and KPI Catalogue

## Evidence status
The project README names DAX and describes KPI outputs. Exact DAX expressions were not extracted from the PBIX. This catalogue defines what must be documented and tested; it does not claim a particular implementation.

## 📊 Required measure specification
| Attribute | Description |
|---|---|
| Display name | Exact name shown in the model |
| Business definition | Plain-language meaning |
| Formula | Full DAX expression |
| Aggregation grain | Transaction, line item, day, month, etc. |
| Filter behavior | Date, store, category, product filters |
| Format | Currency, integer, decimal, percentage |
| Blank/zero handling | Expected behavior |
| Validation | Source calculation or test case |

## KPI definitions to verify

### 💰 Total sales
Confirm the sales column and whether amounts include tax, discounts, refunds, or voids. Validate against a source-workbook calculation.

### 🧾 Total orders
Confirm whether the intended metric is row count, distinct transaction count, or another definition. Do not use row count as a proxy unless the data grain supports it.

### 📦 Total quantity
Confirm units and how returns or negative quantities are handled.

### 📅 Month-over-month variance
Document current-period value, prior-period value, absolute difference, and percentage difference. Define behavior when the prior period is missing or zero.

### 📈 Daily average
Document whether the average uses days with transactions only or all calendar days in the selected range.

### 🏆 Top-ten products
Document the ranked measure, tie behavior, blank-product handling, and whether ranking changes under slicers.

## 🧪 Validation protocol
For each KPI, choose a filter context that can be calculated independently from the workbook. Compare model output with the independent result and record filters, expected result, actual result, difference, tolerance, reviewer, and date.

Do not publish illustrative DAX as the current measure. Add exact formulas only after copying them from the model and validating their semantics.
