# 🧰 Repository Validation Scripts

## validate_docs.py
Runs repository-level documentation checks. It verifies required files, detects broken local Markdown links, checks basic Markdown fence balance, and parses SVG assets as XML.

Run locally with Python 3.10 or newer:

    python scripts/validate_docs.py

The documentation workflow currently configures Python 3.12.

## Interpreting results
A passing result means only that text documentation and SVG assets passed checks implemented at that commit. It does not mean the PBIX was opened, the workbook refreshed, DAX results reconciled, report interactions tested, or accessibility certified. Those activities require Power BI Desktop and recorded test evidence.
