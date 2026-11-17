# 🗺️ Diagram Catalogue

The original logical illustrations below are based on the repository's declared Excel → Power Query → Power BI → DAX → report workflow. They are not reverse-engineered PBIX diagrams.

## 1. System architecture
```mermaid
flowchart TB
  X["📄 Excel workbook"] --> Q["⚙️ Power Query"]
  Q --> M["🧱 Semantic model"]
  M --> D["🧮 DAX"]
  D --> R["📊 Dashboard"]
  R --> U["👤 Analyst"]
```

## 2. Analysis workflow
```mermaid
flowchart TD
  A["Open report"] --> B["Review date/filter context"]
  B --> C["Inspect KPI summary"]
  C --> D["Compare monthly performance"]
  D --> E["Explore store and category"]
  E --> F["Review product ranking"]
  F --> G["Inspect day-hour demand"]
  G --> H["Record finding and validate"]
```

## 3. Refresh sequence
```mermaid
sequenceDiagram
  actor User
  participant PBI as Power BI Desktop
  participant PQ as Power Query
  participant XLS as Excel workbook
  participant Model as Model
  User->>PBI: Refresh
  PBI->>PQ: Run queries
  PQ->>XLS: Read workbook
  XLS-->>PQ: Source rows
  PQ->>Model: Load transformed data
  Model-->>PBI: Evaluate measures
  PBI-->>User: Updated visuals
```

## 4. Report quality state
```mermaid
stateDiagram-v2
  [*] --> Draft
  Draft --> SourceChecked
  SourceChecked --> ModelChecked
  ModelChecked --> MeasuresChecked
  MeasuresChecked --> VisualsChecked
  VisualsChecked --> Reviewed
  VisualsChecked --> Draft: Defect found
  ModelChecked --> Draft: Reconciliation failed
  Reviewed --> [*]
```

## 5. Conceptual ER diagram
A verified ER diagram cannot be produced until the workbook and PBIX model are inspected. Do not infer table names, keys, or relationships from the project title. Capture the actual schema in [semantic-model.md](semantic-model.md), then add its Mermaid ER diagram here.
