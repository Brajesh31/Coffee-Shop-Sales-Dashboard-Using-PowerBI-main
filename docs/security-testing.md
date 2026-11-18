# 🧪 Security Testing

## Purpose
Security review covers workbook sensitivity, PBIX source settings, committed secrets, GitHub workflow permissions, action integrity, and optional Power BI sharing/access controls.

## Current project context
There is no application authentication or API security test suite in this repository.

## Practical process
Check public files and screenshots for sensitive values, review M expressions/parameters, inspect GitHub Actions token permissions, test private vulnerability reporting, and verify Service audience and RLS only if deployed. Record tools, scope, date, findings, and retest.

## Verification and boundaries
A clean documentation validator does not mean security tests passed.

## Related documentation
See the [documentation index](README.md), [project scope](scope-and-limitations.md), and [QA guide](qa.md).
