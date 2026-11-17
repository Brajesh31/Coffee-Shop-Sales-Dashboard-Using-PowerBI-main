# 🧰 Repository Scripts

## validate_docs.py
Checks required documentation files and local Markdown links. Returns a non-zero exit code when any required file or relative link is missing.

Run:
```bash
python scripts/validate_docs.py
```

This validator does not inspect PBIX or XLSX internals. Those require Power BI Desktop or spreadsheet tooling.
