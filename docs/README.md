# 📚 Coffee Shop Sales Dashboard Documentation

This documentation set is organized for a Power BI analytics project. It covers business purpose, report lifecycle, workbook-to-model lineage, report UX, quality, security, governance, and maintenance. It deliberately does not invent APIs, database tables, authentication modules, or report-page names that are not visible in the repository.

## 🚀 Start here

| Goal | Guide |
|---|---|
| Understand the project | [Product overview](product-overview.md) · [Project background](project-background.md) · [Scope](scope-and-limitations.md) |
| Open and refresh the report | [Getting started](getting-started.md) · [Data refresh](data-refresh.md) |
| Explore business views | [Features](features.md) · [Report usage](report-usage.md) · [Use cases](use-cases.md) |
| Trace data and KPIs | [Data dictionary](data-dictionary.md) · [Preparation](data-preparation.md) · [Semantic model](semantic-model.md) · [DAX](dax-measures.md) |
| Contribute safely | [Developer guide](developer-guide.md) · [Maintainer guide](maintainer-guide.md) · [Contributor guide](contributor-guide.md) |
| Validate a change | [QA](qa.md) · [Test strategy](test-strategy.md) · [Test plan](test-plan.md) · [Quality gates](quality-gates.md) |

## ☕ Product and requirements
- [Project Background](project-background.md)
- [Project Objectives](project-objectives.md)
- [Problem Statement](problem-statement.md)
- [Solution Overview](solution-overview.md)
- [Features and Analytical Capabilities](features.md)
- [Functional Requirements](functional-requirements.md)
- [Non-functional Requirements](non-functional-requirements.md)
- [User Personas](user-personas.md)
- [User Journeys](user-journeys.md)
- [Use Cases](use-cases.md)
- [Scope and Limitations](scope-and-limitations.md)

## 🏛️ Architecture and development
- [Technical Overview](technical-overview.md)
- [Report Lifecycle](application-lifecycle.md)
- [Component Architecture](component-architecture.md)
- [Module and Artifact Documentation](module-documentation.md)
- [Technology Stack](technology-stack.md)
- [Dependencies and External Services](dependencies.md)
- [Configuration Guide](configuration.md)
- [Environment Variables](environment-variables.md)
- [Development Workflow](development-workflow.md)
- [Developer Guide](developer-guide.md)
- [Maintainer Guide](maintainer-guide.md)
- [Error Handling and Recovery](error-handling.md)
- [Performance Considerations](performance.md)
- [Compatibility Matrix](compatibility.md)

## 📊 Data and Power BI
- [Data Dictionary and Source Profiling](data-dictionary.md)
- [Data Preparation and Power Query](data-preparation.md)
- [Data Validation and Reconciliation](data-validation.md)
- [Integrations and Data Connections](integrations.md)
- [API and Database Boundaries](api-and-database-boundaries.md)
- [Report UI and UX Guidelines](ui-ux-guidelines.md)
- [Data flow](data-flow.md)
- [Data quality](data-quality.md)
- [Data refresh](data-refresh.md)
- [Semantic model](semantic-model.md)
- [DAX measures](dax-measures.md)
- [Report usage](report-usage.md)

## 🎨 Report design and accessibility
- [Report Design System](design-system.md)
- [Responsive and Small-screen Behavior](responsive-behavior.md)
- [Report Navigation Structure](navigation-structure.md)
- [Report Page Documentation Standard](report-page-documentation.md)
- [Branding and Visual Asset Guidelines](branding-guidelines.md)
- [Visual design](visual-design.md)

## 🔐 Security and privacy
- [Security and Best Practices](security.md)
- [Access Control and Sharing](access-control.md)
- [Secret and Credential Management](secret-management.md)
- [Vulnerability Management](vulnerability-management.md)
- [Incident Response](incident-response.md)
- [Disaster Recovery](disaster-recovery.md)
- [Backup and Restore](backup-and-restore.md)
- [Security Risk Register](security-risk-register.md)
- [Privacy overview](privacy.md)
- [Security architecture](security-architecture.md)
- [Threat model](threat-model.md)

## 🧪 Testing and quality
- [Accessibility Guidelines](accessibility.md)
- [Accessibility Testing and Audit](accessibility-testing.md)
- [Quality Assurance](qa.md)
- [Test Strategy](test-strategy.md)
- [Test Plan](test-plan.md)
- [Integration Testing](integration-testing.md)
- [Performance Testing](performance-testing.md)
- [Visual Regression Testing](visual-regression-testing.md)
- [Bug Reporting](bug-reporting.md)
- [Quality Gates](quality-gates.md)
- [Existing testing guide](testing.md)

## 🚀 Delivery and maintenance
- [DevOps and Operations](devops.md)
- [CI/CD Pipeline](ci-cd.md)
- [GitHub Actions](github-actions.md)
- [Release Management](release-management.md)
- [Versioning Policy](versioning.md)
- [Rollback Procedure](rollback.md)
- [Data Privacy and Retention](data-privacy-and-retention.md)
- [Data Deletion](data-deletion.md)
- [Maintenance Plan](maintenance.md)
- [Known Issues and Evidence Gaps](known-issues.md)
- [Technical Debt Register](technical-debt.md)
- [Project Risk Register](risk-register.md)
- [Migration and Upgrade Guide](migration-and-upgrade.md)
- [Decision Log](decision-log.md)
- [Project Status](project-status.md)
- [Contributor Guide](contributor-guide.md)
- [Deployment](deployment.md)
- [Operations](operations.md)
- [Troubleshooting](troubleshooting.md)
- [Limitations](limitations.md)
- [Glossary](glossary.md)
- [FAQ](faq.md)

## 🧩 Templates and visual assets

- [Template catalogue](templates/README.md)
- [Visual asset catalogue](assets/README.md)
- [Diagram catalogue](diagrams.md)
- [Project structure](project-structure.md)
- [Screenshot policy](assets/screenshots/README.md)

## ⚖️ Evidence and maintenance standard

Every implementation claim must be supported by a checked repository file, PBIX inspection, workbook inspection, or reproducible test. Label uncertain details as unknown. Update affected guides in the same change as report, source, or workflow changes. Run python scripts/validate_docs.py before submitting.
