#!/usr/bin/env python3
"""Validate required docs, local Markdown links, code fences, and SVG XML.

This repository-text validator does not inspect PBIX/XLSX internals, execute
DAX, refresh Power BI queries, or certify report UX.
"""
from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "LICENSE", "CODE_OF_CONDUCT.md", "CONTRIBUTING.md",
    "SECURITY.md", "SUPPORT.md", "CHANGELOG.md", "ROADMAP.md",
    "CITATION.cff", "CODEOWNERS", "docs/README.md",
    "docs/project-structure.md", "docs/product-overview.md",
    "docs/project-background.md", "docs/project-objectives.md",
    "docs/functional-requirements.md", "docs/user-journeys.md",
    "docs/architecture.md", "docs/technical-overview.md",
    "docs/data-dictionary.md", "docs/data-preparation.md",
    "docs/data-validation.md", "docs/semantic-model.md",
    "docs/dax-measures.md", "docs/report-page-documentation.md",
    "docs/security.md", "docs/accessibility.md", "docs/qa.md",
    "docs/test-plan.md", "docs/devops.md", "docs/maintenance.md",
    "docs/templates/README.md", "docs/assets/README.md",
    "docs/assets/diagrams/README.md", "docs/assets/logo.svg",
    "docs/assets/project-banner.svg", "scripts/README.md",
]
FENCE_CHAR = chr(96)

def check_markdown(path: Path, errors: list[str]) -> None:
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"{path.relative_to(ROOT)}: not valid UTF-8")
        return

    fence_count = 0
    for line in content.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(FENCE_CHAR * 3) or stripped.startswith("~~~"):
            fence_count += 1
    if fence_count % 2:
        errors.append(f"{path.relative_to(ROOT)}: unbalanced Markdown code fences")

    link_pattern = re.compile(r"!?\[[^\]]+\]\(([^)]+)\)")
    for raw in link_pattern.findall(content):
        target = raw.strip().split()[0].strip("<>")
        if not target:
            continue
        parsed = urlparse(target)
        if parsed.scheme.lower() in {"http", "https", "mailto", "tel", "data"}:
            continue
        if target.startswith("#"):
            continue
        local_target = unquote(parsed.path)
        if not local_target:
            continue
        candidate = (path.parent / local_target).resolve()
        try:
            candidate.relative_to(ROOT)
        except ValueError:
            errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {target}")
            continue
        if not candidate.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken local link: {target}")

def main() -> int:
    errors: list[str] = []
    for item in REQUIRED:
        if not (ROOT / item).is_file():
            errors.append(f"Missing required file: {item}")

    markdown_files = sorted(set([
        ROOT / "README.md",
        *ROOT.joinpath("docs").rglob("*.md"),
        *ROOT.joinpath(".github").rglob("*.md"),
    ]))
    for path in markdown_files:
        if path.is_file():
            check_markdown(path, errors)
            if path.stat().st_size < 120:
                errors.append(f"{path.relative_to(ROOT)}: suspiciously short documentation file")

    svg_files = sorted(ROOT.rglob("*.svg"))
    for path in svg_files:
        try:
            root = ET.parse(path).getroot()
            if not root.tag.endswith("svg"):
                errors.append(f"{path.relative_to(ROOT)}: root element is not SVG")
        except (ET.ParseError, OSError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid SVG XML: {exc}")

    if errors:
        print("Documentation validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(
        f"Documentation validation passed: {len(markdown_files)} Markdown files, "
        f"{len(svg_files)} SVG files, and {len(REQUIRED)} required paths checked."
    )
    print(
        "PBIX/XLSX internals, DAX results, refresh behavior, report interactions, "
        "and accessibility still require manual Power BI validation."
    )
    return 0

if __name__ == "__main__":
    sys.exit(main())
