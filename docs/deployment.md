# 🚀 Deployment and Handoff

## 🖥️ Desktop handoff
The current repository supports downloading and opening a PBIX file in Power BI Desktop. This is the only deployment mode directly inferable from the visible artifacts.

- Confirm PBIX opens in the intended Desktop version.
- Confirm workbook source path and refresh.
- Confirm visuals render.
- Remove development-only filters and sensitive fields.
- Save the final reviewed PBIX.
- Provide the workbook or an approved refresh source.
- Document ownership and future update process.

## ☁️ Optional Power BI Service publishing
If publishing is chosen:
1. Confirm data classification and sharing authorization.
2. Publish to an approved workspace.
3. Configure source credentials securely.
4. Configure a gateway only if required.
5. Configure scheduled refresh only after testing.
6. Apply workspace and report access permissions.
7. Test as a normal viewer.
8. Document refresh ownership and failure handling.

Publishing and public embed links can expose data. Do not add a public link until access scope is reviewed.

## 🔁 Release checklist
- PBIX version identified.
- Workbook version identified.
- Refresh tested.
- KPI reconciliation recorded.
- Screenshots captured from the release.
- Documentation updated.
- Sensitive data and credentials reviewed.
- Rollback copy retained.
