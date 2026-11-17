# 🔏 Privacy and Data Handling

Before distributing the Excel workbook or PBIX, identify whether the source contains personal, customer, employee, payment, or commercially confidential information. A public repository does not make every data field safe to publish.

## ✅ Handling rules
- Minimize fields stored in public files.
- Remove or anonymize direct identifiers when not required.
- Avoid publishing customer-level records and confidential business details.
- Do not place credentials or tokens in Power Query parameters, PBIX metadata, screenshots, or documentation.
- Restrict Power BI Service access to intended audiences.
- Review exported CSV/XLSX/PDF files before committing.
- Document retention and deletion expectations for externally sourced data.

## ⚠️ Current evidence gap
The workbook contents have not been profiled in this update. This document does not assert that the workbook is anonymized or privacy-compliant. Inspect it before further public distribution.

Related: [Security policy](../SECURITY.md) · [Threat model](threat-model.md) · [Data quality](data-quality.md)
