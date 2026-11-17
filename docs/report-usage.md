# 📊 Report Usage Guide

## 🧭 Recommended analysis sequence

### 1. Start with overall performance
Review sales, orders, and quantity KPIs. Record the selected date range and all active filters before interpreting values.

### 2. Examine monthly movement
Compare the selected month with the previous month. Check both absolute and percentage change. Confirm how the model treats a first month, missing month, and prior month with zero sales.

### 3. Compare locations
Use the location view to identify relative contribution. A top-performing location is not automatically more profitable: the described report focuses on sales, not costs or margin.

### 4. Explore categories and products
Review category breakdown and the top-ten product list. Confirm whether ranking is based on sales value, quantity, or another measure before drawing conclusions.

### 5. Review time patterns
Compare weekdays and weekends, then inspect the day-hour matrix. Consider staffing and demand hypotheses, but validate with additional periods before changing schedules.

## 🔍 Interaction checklist
Confirm these behaviors in the PBIX:
- Date filters and slicers.
- Cross-filtering between charts.
- Visual highlighting behavior.
- Drill-down and drill-through if present.
- Tooltips and report-page navigation.
- Reset or clear-filter behavior.

## ⚠️ Interpretation guardrails
- Comparisons are valid only when filter context is understood.
- Sales value is not the same as profit.
- Product ranking can change when the selected measure changes.
- A heatmap describes historical concentration, not guaranteed future demand.
- Monthly percentages can mislead when the prior period is zero or very small.
- Do not infer customer preferences or demographics from undocumented fields.
