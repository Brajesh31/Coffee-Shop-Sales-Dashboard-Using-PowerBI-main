# 🧑‍💻 Local Development Guide

## Purpose
Local report development happens in Power BI Desktop. Documentation, diagrams, templates, and GitHub configuration are edited as repository text files.

## Current project context
Make a separate working copy of the PBIX and workbook. Open the PBIX, refresh, inspect queries/model/measures, and perform a single focused report change. Save a review copy, validate KPIs and visuals, then update the relevant documentation and evidence.

## Practical process
For text changes run the documentation validation command described in commands-reference.md. For report changes record source version, PBIX version, filters, and reconciliation results. Never edit the only copy of a binary artifact.

## Verification and boundaries
This project has no local web server, localhost URL, browser dev server, or hot-reload runtime.

## Related documentation
See the [documentation index](README.md), [project scope](scope-and-limitations.md), and [QA guide](qa.md).
