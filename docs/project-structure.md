# 🗂️ Complete Project Structure

This inventory is generated from the repository tree on main plus the documentation files in the current update. PBIX/XLSX binary internals are not represented by the Git directory tree.

## Repository tree

.
├── .github/
│   ├── DISCUSSION_TEMPLATE/
│   │   ├── ideas.yml
│   │   └── questions.yml
│   ├── ISSUE_TEMPLATE/
│   │   ├── accessibility_report.yml
│   │   ├── bug_report.yml
│   │   ├── config.yml
│   │   ├── documentation.yml
│   │   ├── feature_request.yml
│   │   └── performance_issue.yml
│   ├── workflows/
│   │   ├── docs-validation.yml
│   │   └── update-readme.yml
│   ├── dependabot.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/
│   ├── assets/
│   │   ├── diagrams/
│   │   │   ├── analysis-workflow.svg
│   │   │   ├── data-governance.svg
│   │   │   ├── data-refresh.svg
│   │   │   ├── README.md
│   │   │   ├── report-lifecycle.svg
│   │   │   ├── security-boundaries.svg
│   │   │   ├── system-architecture.svg
│   │   │   └── user-journey.svg
│   │   ├── screenshots/
│   │   │   └── README.md
│   │   ├── logo.svg
│   │   ├── project-banner.svg
│   │   └── README.md
│   ├── templates/
│   │   ├── accessibility-audit-template.md
│   │   ├── adr-template.md
│   │   ├── architecture-template.md
│   │   ├── bug-report-template.md
│   │   ├── change-request-template.md
│   │   ├── code-review-template.md
│   │   ├── data-dictionary-template.md
│   │   ├── data-quality-template.md
│   │   ├── deployment-checklist.md
│   │   ├── feature-specification-template.md
│   │   ├── incident-report-template.md
│   │   ├── kpi-definition-template.md
│   │   ├── maintenance-checklist.md
│   │   ├── meeting-notes-template.md
│   │   ├── migration-template.md
│   │   ├── project-status-template.md
│   │   ├── qa-test-case-template.md
│   │   ├── README.md
│   │   ├── release-checklist.md
│   │   ├── report-qa-template.md
│   │   ├── risk-assessment-template.md
│   │   ├── rollback-checklist.md
│   │   ├── security-audit-template.md
│   │   ├── test-plan-template.md
│   │   ├── test-report-template.md
│   │   └── threat-assessment-template.md
│   ├── access-control.md
│   ├── accessibility-testing.md
│   ├── accessibility.md
│   ├── animation-guidelines.md
│   ├── api-and-database-boundaries.md
│   ├── application-lifecycle.md
│   ├── architecture-decisions.md
│   ├── architecture.md
│   ├── audit-logging.md
│   ├── authentication.md
│   ├── authorization.md
│   ├── backup-and-restore.md
│   ├── branding-guidelines.md
│   ├── bug-reporting.md
│   ├── building.md
│   ├── ci-cd.md
│   ├── code-standards.md
│   ├── coding-guidelines.md
│   ├── color-contrast.md
│   ├── color-system.md
│   ├── commands-reference.md
│   ├── compatibility.md
│   ├── component-architecture.md
│   ├── component-library.md
│   ├── configuration.md
│   ├── contributor-guide.md
│   ├── data-deletion.md
│   ├── data-dictionary.md
│   ├── data-flow.md
│   ├── data-preparation.md
│   ├── data-privacy-and-retention.md
│   ├── data-protection.md
│   ├── data-quality.md
│   ├── data-refresh.md
│   ├── data-validation.md
│   ├── dax-measures.md
│   ├── debugging.md
│   ├── decision-log.md
│   ├── dependencies.md
│   ├── dependency-security.md
│   ├── deployment.md
│   ├── deprecation-policy.md
│   ├── design-patterns.md
│   ├── design-system.md
│   ├── design-tokens.md
│   ├── developer-guide.md
│   ├── development-workflow.md
│   ├── devops.md
│   ├── diagrams.md
│   ├── disaster-recovery.md
│   ├── documentation-coverage-matrix.md
│   ├── encryption.md
│   ├── environment-variables.md
│   ├── error-handling.md
│   ├── faq.md
│   ├── features.md
│   ├── functional-requirements.md
│   ├── getting-started.md
│   ├── github-actions.md
│   ├── glossary.md
│   ├── health-checks.md
│   ├── hosting.md
│   ├── incident-response.md
│   ├── infrastructure.md
│   ├── installation.md
│   ├── integration-testing.md
│   ├── integrations.md
│   ├── keyboard-navigation.md
│   ├── known-issues.md
│   ├── limitations.md
│   ├── local-development.md
│   ├── logging.md
│   ├── maintainer-guide.md
│   ├── maintenance.md
│   ├── migration-and-upgrade.md
│   ├── module-documentation.md
│   ├── monitoring.md
│   ├── navigation-structure.md
│   ├── non-functional-requirements.md
│   ├── observability.md
│   ├── operations.md
│   ├── performance-testing.md
│   ├── performance.md
│   ├── privacy.md
│   ├── problem-statement.md
│   ├── product-overview.md
│   ├── production-setup.md
│   ├── project-background.md
│   ├── project-objectives.md
│   ├── project-status.md
│   ├── project-structure.md
│   ├── qa.md
│   ├── quality-gates.md
│   ├── README.md
│   ├── release-management.md
│   ├── report-page-documentation.md
│   ├── report-usage.md
│   ├── responsive-behavior.md
│   ├── risk-register.md
│   ├── rollback.md
│   ├── running-locally.md
│   ├── scalability.md
│   ├── scope-and-limitations.md
│   ├── screen-reader-support.md
│   ├── secret-management.md
│   ├── security-architecture.md
│   ├── security-risk-register.md
│   ├── security-testing.md
│   ├── security.md
│   ├── semantic-model.md
│   ├── solution-overview.md
│   ├── system-design.md
│   ├── technical-debt.md
│   ├── technical-overview.md
│   ├── technology-stack.md
│   ├── test-plan.md
│   ├── test-strategy.md
│   ├── testing.md
│   ├── threat-model.md
│   ├── troubleshooting.md
│   ├── typography.md
│   ├── ui-ux-guidelines.md
│   ├── upgrade-guide.md
│   ├── use-cases.md
│   ├── user-journeys.md
│   ├── user-personas.md
│   ├── versioning.md
│   ├── visual-design.md
│   ├── visual-regression-testing.md
│   ├── vulnerability-management.md
│   └── wcag-compliance.md
├── scripts/
│   ├── README.md
│   └── validate_docs.py
├── .editorconfig
├── .gitattributes
├── .gitignore
├── AUTHORS.md
├── Background image.png
├── CHANGELOG.md
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── CODEOWNERS
├── coffee shop sales.pbix
├── Coffee Shop Sales.xlsx
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── ROADMAP.md
├── SECURITY.md
└── SUPPORT.md

## Key artifact responsibilities

| Path | Responsibility | Notes |
|---|---|---|
| coffee shop sales.pbix | Power BI report and semantic model | Internal pages, measures, relationships, queries, and theme require Desktop inspection |
| Coffee Shop Sales.xlsx | Source-data workbook | Sheet names, columns, grain, and quality profile require workbook inspection |
| Background image.png | Existing background asset | Not a dashboard screenshot |
| README.md | Repository landing page | Links to the documentation catalogue |
| LICENSE | MIT license | Existing repository license |
| CODEOWNERS | Review ownership | Maps repository paths to the maintainer |
| .github/ | Issue forms, discussions, workflows | No application deployment pipeline is implied |
| docs/ | Product, technical, data, design, security, testing, delivery, and operations guides | Indexed from docs/README.md |
| docs/assets/ | Logo, banner, SVG diagrams, screenshot policy | Illustrations are not PBIX captures |
| docs/templates/ | Reusable change and QA templates | Indexed from docs/templates/README.md |
| scripts/ | Repository documentation validation | Not part of report runtime |

## Architectural boundaries

No frontend application, backend service, API implementation, database migration, container definition, or server deployment configuration is visible in the repository. The PBIX contains report-specific model and visual information that is not represented by this file tree.

## Maintenance
Update this page from the actual Git tree when files move. Do not list planned files as existing or describe internal PBIX objects as repository folders.
