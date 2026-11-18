# ⚡ Performance Considerations

## Purpose
Report performance depends on workbook size, query transformations, model cardinality, relationship design, measure complexity, visual count, and filter context.

## Current project context
The repository does not publish a measured refresh or rendering baseline. No arbitrary performance target is treated as achieved.

## Recommended workflow
Use Power BI Performance Analyzer. Measure initial open, refresh, page load, and per-visual rendering separately. Record Desktop version, device, source size, filters, duration, and repeatability. Optimize only after profiling.

## Evidence and verification
Potential optimizations include removing unused columns, reducing unnecessary high-cardinality fields, simplifying expensive measures, and avoiding redundant visuals. Revalidate results after each optimization.

## Related documentation
Use the [documentation index](README.md) to find related data, architecture, security, QA, and operations guidance.
