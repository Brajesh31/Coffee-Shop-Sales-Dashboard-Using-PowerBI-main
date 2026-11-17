# 🏛️ Architecture Overview

## 🧩 Logical components
The repository describes a Power BI workflow centered on an Excel source workbook:

```mermaid
flowchart TB
  subgraph Source["📄 Source"]
    XLSX["Excel source workbook"]
  end
  subgraph BI["📊 Power BI"]
    PQ["Power Query transformations"]
    MODEL["Semantic model"]
    DAX["DAX calculations"]
    REPORT["Report visuals"]
  end
  USER["👤 Analyst / business user"]
  XLSX --> PQ --> MODEL --> DAX --> REPORT --> USER
```

## 🔎 Component responsibilities
| Component | Responsibility | Evidence status |
|---|---|---|
| Excel workbook | Source-data artifact | File exists in repository |
| Power Query | Data import and transformation | Named by README; exact steps uninspected |
| Semantic model | Tables and relationships | PBIX exists; model uninspected |
| DAX | KPI calculations | Named by README; formulas uninspected |
| Report visuals | Business-facing charts and matrices | Views described; individual visuals uninspected |
| User | Interacts with report | Intended report usage |

## 🔁 Refresh sequence
```mermaid
sequenceDiagram
  actor Analyst
  participant Desktop as Power BI Desktop
  participant Query as Power Query
  participant Workbook as Excel workbook
  participant Model as Semantic model
  participant Visuals as Report visuals
  Analyst->>Desktop: Open PBIX and request refresh
  Desktop->>Query: Evaluate source queries
  Query->>Workbook: Read workbook source
  Workbook-->>Query: Return source tables
  Query->>Model: Load transformed data
  Model->>Visuals: Evaluate model and measures
  Visuals-->>Analyst: Render report
```

This is conceptual. Query count, folding behavior, refresh mode, and storage configuration require inspection.

## 🚫 Not represented
No web server, application API, authentication service, online transaction processing, or external database appears in the visible repository file inventory.
