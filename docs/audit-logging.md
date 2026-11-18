# 📜 Audit Logging

## Purpose
The repository does not implement its own application audit trail. Git history records repository content changes; GitHub Actions provides workflow run records. Optional Power BI Service administration/audit capabilities depend on tenant configuration.

## Current project context
For a controlled report release, retain commit SHA, artifact hashes, reviewer, release date, test evidence, and any approved publication event.

## Practical process
If Service is used, document which administrative and activity logs are available, who can access them, retention, and how an incident investigation requests them. Do not include sensitive audit data in public documentation.

## Verification and boundaries
Do not claim complete access or data-export auditing from Git commit history.

## Related documentation
See the [documentation index](README.md), [project scope](scope-and-limitations.md), and [QA guide](qa.md).
