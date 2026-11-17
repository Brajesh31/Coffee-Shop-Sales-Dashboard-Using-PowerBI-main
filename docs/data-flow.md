# 🔀 Data Flow

## End-to-end logical flow
```mermaid
flowchart LR
  A["📁 Workbook"] --> B["📥 Source query"]
  B --> C["🧹 Data shaping"]
  C --> D["🧱 Model tables"]
  D --> E["🔗 Relationships"]
  E --> F["🧮 DAX evaluation"]
  F --> G["📊 Charts and matrices"]
  G --> H["👤 Analyst interpretation"]
```

## Flow boundaries
- The workbook is the visible data artifact.
- Power Query is identified as the transformation technology in the existing project overview.
- The PBIX stores the report and model artifact.
- The report description identifies its analytical output areas.
- No separate data API or hosted database is documented.

## Data lineage record
For each displayed KPI, trace the lineage from source column through Power Query transformations and model relationships to the DAX measure and visual. Complete this using Power BI Desktop inspection.

## Validation points
1. Source file and source object are correct.
2. Transformation output matches expected row counts and types.
3. Model relationships preserve intended grain.
4. Measure results reconcile to a known source calculation.
5. Visuals respond correctly to the intended filter context.
