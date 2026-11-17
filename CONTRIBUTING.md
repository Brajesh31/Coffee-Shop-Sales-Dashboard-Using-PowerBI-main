# 🧑‍💻 Contributing Guide

Thank you for helping improve the Coffee Shop Sales Dashboard. Contributions should make the report more accurate, understandable, accessible, reproducible, or easier to maintain.

## 🎯 Useful contributions

- Clarifying KPI definitions and business interpretation.
- Improving Power Query data preparation.
- Reviewing or correcting DAX calculations.
- Improving chart choice, labeling, color contrast, or report navigation.
- Adding verified screenshots and documentation.
- Improving refresh and troubleshooting instructions.
- Adding automated documentation checks.

## 🧰 Before making a change

1. Read the [README](README.md) and [documentation index](docs/README.md).
2. Open the PBIX in Power BI Desktop before changing the report.
3. Keep an unchanged backup of the original PBIX and workbook.
4. Confirm that changes do not expose private or sensitive data.
5. Record the business question that the change is intended to answer.

## 🌿 Suggested workflow

1. Fork the repository.
2. Create a focused branch, for example `docs/clarify-kpi-definitions` or `fix/monthly-comparison`.
3. Make one coherent set of changes.
4. Update affected documentation and screenshots.
5. Validate the report and refresh behavior.
6. Run the documentation checks described in [Testing](docs/testing.md).
7. Open a pull request with evidence and a concise explanation.

## 📊 Power BI contribution standards

- Preserve source data meaning and document transformations.
- Use explicit, understandable measure names.
- Define the grain of every KPI.
- Make date and filter context assumptions clear.
- Handle blanks, zero denominators, and missing periods deliberately.
- Use consistent units, currency formatting, and decimal precision.
- Avoid misleading truncated axes and unsupported causal claims.
- Ensure colors are not the only way information is communicated.
- Verify cross-highlighting, slicers, tooltips, and interactions after edits.
- Do not claim the report was tested unless it was actually opened and checked.

## 🧪 Evidence expected in a pull request

Include as applicable:

| Change type | Evidence |
|---|---|
| DAX change | Formula, expected behavior, sample filter context, before/after result |
| Data preparation | Source fields, transformation steps, row counts or quality checks |
| Visual change | Screenshot, question answered, accessibility considerations |
| Model change | Relationship diagram and rationale |
| Documentation | Links checked and affected files listed |
| Deployment | Target workspace/process and refresh validation |

Screenshots must come from the real report. Do not generate mock dashboard screens and present them as real.

## 📝 Commit and review expectations

Use clear commit messages such as:

- `docs: explain monthly KPI definitions`
- `fix: handle blank prior-month sales`
- `feat: add product category comparison`
- `test: add report validation checklist`

Keep pull requests focused. Explain limitations and unresolved questions. A reviewer may request changes when a metric is ambiguous, a visual is misleading, or documentation is inconsistent with the actual PBIX.

## 🔒 Data and security

Never commit credentials, access tokens, private workspace links, customer-identifying information, or confidential source data. Review [SECURITY.md](SECURITY.md) before reporting vulnerabilities.

## 📚 Related guides

- [Getting started](docs/getting-started.md)
- [DAX measures](docs/dax-measures.md)
- [Data quality](docs/data-quality.md)
- [Testing](docs/testing.md)
- [Pull request template](.github/PULL_REQUEST_TEMPLATE.md)
