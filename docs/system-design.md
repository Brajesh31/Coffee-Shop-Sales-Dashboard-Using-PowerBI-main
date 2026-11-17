# 🧱 System Design

## Design objective
Keep the analytical flow understandable and reproducible: source workbook → preparation → model → measures → report.

## Logical layers
1. **Source:** the committed Excel workbook.
2. **Preparation:** Power Query import and transformation.
3. **Model:** tables, relationships, date semantics, and metadata in the PBIX.
4. **Calculation:** DAX measures and calculated objects.
5. **Presentation:** report pages, visuals, filters, and interactions.
6. **Consumption:** analyst interpretation and operational discussion.

## Design principles
- Keep transformation logic traceable.
- Prefer explicit measure definitions over ambiguous chart-only calculations.
- Define grain for every fact table and KPI.
- Use a consistent calendar definition for time comparisons.
- Avoid ambiguous many-to-many relationships unless justified.
- Keep display formatting separate from business logic where practical.
- Treat the Excel workbook as a versioned input.

## Model review questions
- What is the row grain of the main sales table?
- Is there a stable transaction or order identifier?
- Are products and stores represented by dimension tables?
- Is there a dedicated date table marked as a date table?
- What are the active and inactive relationships?
- Which measures rely on iterators or context transition?
- How are missing dates and zero denominators handled?

Answers must come from the actual PBIX model, not generic retail assumptions.
