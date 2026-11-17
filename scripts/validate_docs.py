#!/usr/bin/env python3
"""Validate required documentation files and local Markdown links.

This checks repository text structure only. It does not inspect PBIX/XLSX
internals or claim Power BI measures and visuals work.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "LICENSE", "CODE_OF_CONDUCT.md", "CONTRIBUTING.md",
    "SECURITY.md", "SUPPORT.md", "CHANGELOG.md", "ROADMAP.md",
    "CITATION.cff", "docs/README.md", "docs/project-structure.md",
    "docs/data-dictionary.md", "docs/architecture.md",
]
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
IGNORE_SCHEMES = ("http://", "https://", "mailto:", "tel:", "#")

def main() -> int:
    errors: list[str] = []
    for item in REQUIRED:
        if not (ROOT / item).is_file():
            errors.append(f"Missing required file: {item}")
    markdown_files = [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md"))]
    for md in markdown_files:
        if not md.exists():
            continue
        for target in LINK_RE.findall(md.read_text(encoding="utf-8")):
            target = target.strip()
            if not target or target.startswith(IGNORE_SCHEMES):
                continue
            target = target.split()[0].strip("<>")
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            candidate = (md.parent / target).resolve()
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                errors.append(f"{md.relative_to(ROOT)}: link escapes repository: {target}")
                continue
            if not candidate.exists():
                errors.append(f"{md.relative_to(ROOT)}: broken local link: {target}")
    if errors:
        print("Documentation validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1
    print(f"Documentation validation passed for {len(markdown_files)} Markdown files.")
    print("PBIX/XLSX internals and Power BI behavior require manual validation.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
