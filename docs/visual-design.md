# 🎨 Visual Design and UX Guidelines

## ☕ Design intent
The project has a coffee-shop subject and includes a background image asset. The actual PBIX theme, exact palette, typography, page dimensions, and visual arrangement should be confirmed from the report rather than inferred from the background file.

## 📊 Visual selection guidance
| Question | Suitable visual | Review point |
|---|---|---|
| Trend over time | Line chart | Continuous date axis and clear period granularity |
| Compare stores | Bar/column chart | Consistent scale and readable labels |
| Compare categories | Bar or composition chart | Avoid misleading area comparisons |
| Rank products | Sorted bar chart or table | State the ranking metric |
| Compare day and hour | Matrix/heatmap | Include readable labels and accessible color cues |
| Highlight KPIs | Card | Include units and time context |

These are recommendations, not an inventory of confirmed existing visual types except where the project overview explicitly describes a line chart, ranked list, and matrix.

## ♿ Accessibility checklist
- Use meaningful titles that state the business question.
- Provide alt text for meaningful visuals.
- Maintain readable font sizes and sufficient contrast.
- Do not use color as the only indicator of magnitude.
- Use clear units and date formats.
- Keep tab order logical where supported.
- Test report navigation with keyboard interaction.
- Explain color scales and conditional formatting.

## 📱 Layout review
Power BI reports are canvas-based. Check actual page size, fit-to-page behavior, browser viewing, and phone layout if provided. Do not claim a responsive website implementation.

## 🖼️ Screenshots
Add only screenshots captured from the actual PBIX. Place them under `docs/assets/screenshots/`, use descriptive filenames, remove sensitive values, and add useful alt text. No dashboard screenshot is fabricated by this documentation package.
