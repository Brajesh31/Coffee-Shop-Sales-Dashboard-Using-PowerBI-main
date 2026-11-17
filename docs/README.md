# 📚 Project Documentation

Welcome to the Coffee Shop Sales Dashboard documentation. These guides explain the business purpose, report usage, data workflow, Power BI model discovery, quality checks, and repository maintenance.

## 🧭 Start here
| Need | Guide |
|---|---|
| Understand the project | [Product overview](product-overview.md) |
| Open the PBIX | [Getting started](getting-started.md) |
| Explore business views | [Report usage](report-usage.md) |
| Understand system flow | [Architecture](architecture.md) |
| Inspect source fields | [Data dictionary](data-dictionary.md) |
| Understand transformations | [Data preparation](data-preparation.md) |
| Record model relationships | [Semantic model](semantic-model.md) |
| Define analytical calculations | [DAX measures](dax-measures.md) |
| Design and accessibility | [Visual design](visual-design.md) |
| Refresh data | [Data refresh](data-refresh.md) |
| Validate changes | [Testing](testing.md) |
| Publish or hand off | [Deployment](deployment.md) |
| Fix common issues | [Troubleshooting](troubleshooting.md) |
| Understand evidence gaps | [Limitations](limitations.md) |

## 🏛️ Technical and governance guides
- [System design](system-design.md)
- [Project structure](project-structure.md)
- [Data flow](data-flow.md)
- [Data quality](data-quality.md)
- [Privacy](privacy.md)
- [Security architecture](security-architecture.md)
- [Threat model](threat-model.md)
- [Operations and maintenance](operations.md)
- [Glossary](glossary.md)
- [FAQ](faq.md)
- [Diagram index](diagrams.md)

## 🧩 Templates
See [templates/README.md](templates/README.md) for architecture, KPI, data-quality, QA, incident, and release templates.

## 🖼️ Visual assets
Diagrams and original SVG illustrations are in [assets/](assets/). Real report screenshots belong in [assets/screenshots/](assets/screenshots/) and should only be added after capture from Power BI Desktop.

## ⚠️ Accuracy standard
This repository stores PBIX and XLSX binary files. Their internal metadata has not been extracted by GitHub's text-file interface. Field names, table names, formulas, data ranges, visual names, report-page names, and deployment settings must be confirmed in the actual files before being treated as facts.

## 🔄 Maintenance
When the report changes, update relevant model, KPI, visual, data, and QA guides in the same change. Run `python scripts/validate_docs.py` before submitting.
