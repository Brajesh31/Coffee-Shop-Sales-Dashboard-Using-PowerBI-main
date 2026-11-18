# 📘 Developer Guide

## Purpose
Contributors should understand row grain, source queries, model relationships, DAX, filter context, and visual behavior before editing the report.

## Current project context
The PBIX is the report development environment. GitHub contains binary report/source artifacts and supporting text documentation. No conventional source-code build command exists for the PBIX.

## Recommended workflow
Read README and project scope; open the PBIX; trace one KPI from source to visual; inspect relationships and filters; make one focused change; independently calculate expected values; and update related guide and QA evidence.

## Evidence and verification
Run python scripts/validate_docs.py for repository documentation checks only. Do not describe it as a Power BI test.

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
