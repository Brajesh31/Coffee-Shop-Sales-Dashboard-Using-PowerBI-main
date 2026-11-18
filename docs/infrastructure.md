# 🏗️ Infrastructure Boundaries

## Purpose
No custom cloud resources, servers, database clusters, containers, network topology, or infrastructure-as-code files are visible in the repository.

## Current project context
The visible workflow is GitHub repository storage plus a maintainer workstation running Power BI Desktop. An optional Power BI Service tenant/workspace is not confirmed.

## Practical process
If hosted distribution is introduced, document workspace capacity, data gateway, network allowlists, storage sources, identity integration, environments, owners, and failure modes as applicable.

## Verification and boundaries
Do not add Terraform, Kubernetes, or Docker files without a real infrastructure requirement.

## Related documentation
See the [documentation index](README.md), [project scope](scope-and-limitations.md), and [QA guide](qa.md).
