# 🗓️ Test Plan

## Purpose
The minimum regression set should cover workbook availability, PBIX open, refresh, total sales, total orders, quantity, month-over-month edge cases, filters, product ranking, weekday/weekend comparison, and the day-hour matrix.

## Current project context
Each case must record PBIX version, workbook version, environment, filter context, expected result, actual result, status, evidence path, tester, and date.

## Recommended workflow
Never pre-fill actual values without running the test. Add targeted tests for changed areas and retain core KPI checks as regression coverage. Use the QA test-case and test-report templates.

## Evidence and verification
If the environment is unavailable, mark a test blocked or not run rather than passing it by assumption.

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
