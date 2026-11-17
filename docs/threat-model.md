# 🛡️ Threat Model

## Scope
This lightweight threat model covers repository artifacts, local report development, and the existing GitHub automation. A hosted environment is not assumed.

## Assets and threats
| Asset | Threat | Potential impact | Mitigation |
|---|---|---|---|
| XLSX workbook | Sensitive data committed | Data exposure | Classify, minimize, anonymize, review |
| PBIX file | Embedded credentials or sensitive model data | Data or access exposure | Inspect sources and report contents before sharing |
| GitHub workflow | Excessive permissions or compromised action | Unauthorized changes | Least privilege, action review, protected branches |
| External links | Malicious destination | Phishing or malware | Verify domains and use official documentation |
| KPI results | Incorrect formula or grain assumptions | Poor decisions | Independent reconciliation and explicit definitions |
| Public report sharing | Overly broad access | Unintended disclosure | Review workspace permissions and sharing settings |

## Trust boundaries
- GitHub repository and workflow execution.
- Maintainer workstation and local file system.
- External data source, if later configured.
- Power BI Service, only if publishing is implemented.

Rate risks using [risk-assessment-template.md](templates/risk-assessment-template.md). Revisit when data sources, workflows, or sharing modes change.
