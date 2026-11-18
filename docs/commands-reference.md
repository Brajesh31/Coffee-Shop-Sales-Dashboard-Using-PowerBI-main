# ⌨️ Commands Reference

## Purpose
The repository's current executable command is the Python documentation validator. No application start, test, lint, or build command exists for the PBIX itself.

## Current project context
Run the repository check from the repository root using Python 3.10 or newer: python scripts/validate_docs.py. The GitHub documentation workflow configures Python 3.12 and runs the same script.

## Practical process
The script checks required documentation paths, local Markdown links, code-fence balance, and SVG XML. Interpret a pass as documentation/asset validation only. It does not refresh data, execute DAX, or inspect report visuals.

## Verification and boundaries
Do not add commands to this guide until an actual script or supported Power BI process exists.

## Related documentation
See the [documentation index](README.md), [project scope](scope-and-limitations.md), and [QA guide](qa.md).
