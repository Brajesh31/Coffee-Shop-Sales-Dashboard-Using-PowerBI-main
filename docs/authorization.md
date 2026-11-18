# 🪪 Authorization Boundaries

## Purpose
There is no application-level role/permission engine in the visible source tree. GitHub permissions govern repository changes; optional Power BI workspace/report permissions govern hosted report access.

## Current project context
Row-level security may be configured inside a PBIX, but it has not been inspected or tested. Visual-level filtering is not an authorization boundary.

## Practical process
When reviewing a hosted report, map workspace roles, report sharing, export/download permissions, and any RLS roles. Test representative identities and document denied as well as permitted access.

## Verification and boundaries
Do not invent admin, manager, or viewer roles in the report model without evidence.

## Related documentation
See the [documentation index](README.md), [project scope](scope-and-limitations.md), and [QA guide](qa.md).
