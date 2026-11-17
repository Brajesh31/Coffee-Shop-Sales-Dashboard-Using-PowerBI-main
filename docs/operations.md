# ⚙️ Operations and Maintenance

## Routine maintenance

### When source data changes
- Confirm workbook schema compatibility.
- Refresh all queries.
- Reconcile key totals.
- Review categories and date coverage.
- Update data dictionary and lineage docs when columns change.

### When DAX changes
- Document business definition and formula.
- Test edge cases and filter context.
- Reconcile against source data.
- Update KPI catalogue and test cases.

### When visuals change
- Capture a real screenshot.
- Review titles, labels, units, contrast, and interactions.
- Update report usage and visual design docs.

### When automation changes
- Review GitHub Actions and Python tooling.
- Run documentation validation.
- Review workflow permissions and action versions.

## 🧯 Backup and recovery
Keep a known-good PBIX and workbook copy before major changes. Store backups in an approved location with appropriate access controls. Do not commit private credentials or sensitive production exports as backups.

## 🗓️ Maintenance cadence
Review documentation whenever the report, data schema, calculations, or refresh process changes. Review external workflow actions and security policy periodically.
