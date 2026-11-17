# 🔄 Data Refresh and Source Paths

The PBIX is accompanied by an Excel workbook. When the repository is cloned to another folder, a local source path saved in the PBIX may no longer resolve.

## 🪜 Reconnect the workbook
1. Download both project files into a stable local folder.
2. Open the PBIX in Power BI Desktop.
3. Open **Transform data**.
4. Select each source query and inspect its source step.
5. Update the file path to the local workbook.
6. Check credentials and privacy-level prompts.
7. Apply query changes.
8. Refresh the model.
9. Review query errors, loaded row counts, and visuals.
10. Save a new PBIX copy and document the source-path strategy.

## 🧪 Refresh verification
Record refresh timestamp, source file name, source modified date, query errors, loaded row counts, and warnings. A successful refresh alone does not prove that the correct workbook or expected period was loaded.

## ☁️ Power BI Service
Publishing, gateway configuration, scheduled refresh, credentials, and workspace permissions are not confirmed by the repository files. If the report is published, document the actual workspace, credentials process, refresh schedule, gateway dependency, and access policy without exposing secrets.
