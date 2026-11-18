# 🏗️ Build and Packaging Guide

## Purpose
A PBIX is authored and saved in Power BI Desktop. The repository does not contain a conventional compiler or build script that produces the report file from text source.

## Current project context
The maintainer's release preparation process is to open the PBIX, validate source connectivity, refresh, inspect the report, save a versioned PBIX, and keep it paired with the source workbook. If an export or packaged handoff is required, document the exact Power BI workflow and target format.

## Practical process
Record Desktop version, file hashes, workbook version, refresh result, QA result, and output file names. A successful GitHub workflow cannot build the PBIX.

## Verification and boundaries
Do not add a CI job that claims to compile or build a PBIX without a supported and tested build mechanism.

## Related documentation
See the [documentation index](README.md), [project scope](scope-and-limitations.md), and [QA guide](qa.md).
