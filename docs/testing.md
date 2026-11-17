# 🧪 Testing and QA Strategy

## Test layers

### 1. Source-data tests
- Workbook opens.
- Expected sheets/tables exist.
- Data types are correct.
- Key uniqueness and null rules are checked.
- Date range and numeric domains are plausible.

### 2. Power Query tests
- Each query refreshes.
- Applied steps do not unexpectedly remove records.
- Source-to-output counts are reconciled.
- Errors and type conversion failures are reviewed.

### 3. Model tests
- Relationships use correct keys.
- Filter propagation is intended.
- Date relationships and time calculations are correct.
- No unexpected ambiguous paths exist.

### 4. KPI tests
- Sales reconciles to an independent sum.
- Orders use the documented transaction definition.
- Quantity uses the intended unit and treatment of returns.
- MoM values are tested for first month, missing month, and zero prior value.
- Daily average denominator is verified.
- Top-ten ranking is tested under slicers and ties.

### 5. Visual and interaction tests
- Titles and units are clear.
- Filters and cross-highlighting behave correctly.
- Matrix values and labels are legible.
- Tooltips and drill actions work if present.
- No visual shows an unexplained blank or error.

## ✅ Test case template
| ID | Scenario | Steps | Expected | Actual | Result |
|---|---|---|---|---|---|
| DATA-01 | Workbook accessible | Open source query | Source resolves | To be run | Not run |
| KPI-01 | Sales reconciliation | Apply known scope | Matches independent sum | To be run | Not run |
| KPI-02 | Order definition | Compare transaction IDs | Matches agreed definition | To be run | Not run |
| TIME-01 | Month comparison | Select current/prior month | Correct variance | To be run | Not run |
| VIS-01 | Store filter | Select one location | Relevant visuals update | To be run | Not run |

No test is marked passed by documentation creation alone.

## 🔎 Release gate
A report change is not release-ready until it opens, refreshes, reconciles important KPIs, and passes interaction checks.
