# 🐙 GitHub Actions

## Purpose
The visible workflow inventory includes docs-validation.yml and update-readme.yml. One validates documentation using Python; the other updates README timestamp metadata.

## Current project context
For each workflow document trigger, paths, runner, actions, permissions, concurrency, inputs, outputs, and failure behavior. Prefer read-only permissions for validation and write permissions only for actions that must commit files.

## Recommended workflow
Do not add CodeQL, package build, or test jobs that cannot operate on this actual stack. Review action versions and permissions during maintenance.

## Evidence and verification
Workflow descriptions should match the YAML that exists on main.

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
