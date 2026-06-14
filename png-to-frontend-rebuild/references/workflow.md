# Workflow

Use this reference for the overall PNG/screenshot-to-frontend workflow.

## Input Routing

First identify the task route:

- **Single-page rebuild:** One UI image becomes one frontend page.
- **Multi-page product rebuild:** Several related images become a small app/site with shared systems.
- **Design-system extraction:** The user wants reusable tokens/components from one or more images.
- **Legacy UI recreation or refresh:** The source is an existing app screenshot, often with a requested modernization.
- **Marketing/landing page rebuild:** The source is a page mockup or screenshot with hero/media/sections.
- **Dashboard/admin rebuild:** The source has dense tables, filters, charts, sidebars, or operational panels.
- **Mobile app/mini-program rebuild:** The source has mobile safe areas, fixed navigation, scroll regions, and app-like controls.
- **Calibration pass:** The frontend already exists and the user wants proportions, details, or fidelity improved.

Choose the smallest route that satisfies the request. For multi-page, dashboard, mobile, or high-fidelity routes, complete the planning gate before coding.

## Planning Gate

Before implementation, produce:

- Source inventory: image path, page name, dimensions, likely viewport, version/finality.
- Target stack: existing project stack first; user-requested stack second; static HTML only when no app stack exists or user requests it.
- Fidelity tier: prototype, high fidelity, or calibration.
- Canvas strategy: fixed canvas, responsive adaptation, internal scroll, full-page scroll, or dashboard fluid layout.
- Shared systems: typography, colors, spacing, background, nav/sidebar, cards, buttons, forms, data rows, charts.
- Asset decision table from `asset-planning.md`.
- Mandatory asset groups: backgrounds, custom icon sets, subject-matter imagery, decorative objects, brand-sensitive/exact assets, and hybrid art layers.
- Image generation/extraction plan: model/tool, target dimensions, prompt scope, output paths, and fallback/blocker handling.
- Mobile/device chrome policy: omit OS status bars, browser chrome, camera notches, and home indicators unless the user explicitly asks to reproduce the device frame.
- Verification plan: preview command/server, screenshot sizes, compare method.

If the user requests speed, reduce fidelity explicitly instead of skipping hidden steps.

Do not begin frontend implementation for high-fidelity or calibration work until mandatory assets have been generated, extracted, staged, or explicitly marked blocked/placeholders in the table. For custom icon families, generated assets must be usable icon files, not visible sprite cells with backgrounds.

## Fidelity Tiers

**Prototype fidelity**

- Output: runnable page/app and at least one screenshot.
- Goal: recognizable layout, theme, and main interactions.
- Generated assets may be rough or placeholders if marked.

**High fidelity**

- Output: asset decision table, independent assets, runnable page/app, screenshot(s), and gap notes.
- Goal: main regions align, important artwork is generated/extracted, controls are live, obvious states work.
- Requirement: `image-model-required` and `extract-user-asset` rows are present as real files or are explicitly blocked. CSS stand-ins for these rows downgrade the result to prototype fidelity unless the user accepts them.
- Use screenshot comparison at target viewport(s).

**Calibration fidelity**

- Output: high-fidelity outputs plus ruler compare images or measured region notes.
- Goal: measured alignment of major regions, typography, asset placement, and scroll behavior.
- Iterate: CSS/assets -> screenshot -> compare -> measured fix.

## Implementation Flow

1. Inspect source images and existing project files.
2. Select canonical images; for versioned sets, prefer final/latest sources and use older variants only for recovery or intent.
3. Read `asset-planning.md` and complete the standard asset table.
4. Read `framework-adapters.md` if a stack exists or is requested.
5. Generate/extract required assets for the selected fidelity tier, including coherent icon sets, backgrounds, subject imagery, decorative objects, and hybrid art layers.
6. For generated icon sheets, split them, remove chroma-key/backgrounds if needed, crop transparent bounds, and create a contact sheet for visual inspection.
7. Place generated/extracted assets in the project, validate they render at intended size, and update the asset table statuses.
8. Implement shared tokens/components before per-page polish.
9. Implement real interaction states: active nav, tabs, selection, buttons, quantity, filters, drawer/modal when visible.
10. Run locally and capture screenshots.
11. Create a side-by-side ruler comparison for high-fidelity work and use it to calibrate at least the major regions.
12. Compare against the source; fix large regions before micro details.
13. Report what is done, what differs, and why.

## Failure Handling

Stop and tell the user when a required step is blocked:

- Image generation/model access is unavailable for required assets.
- The agent has no callable image-generation path despite the user expecting generated assets.
- The source image is too low-resolution or cropped to infer important content.
- The project stack cannot run locally.
- A supplied exact asset is missing: QR code, official logo, product photo, legal/brand mark.
- Browser screenshots cannot be captured.
- A required framework dependency cannot be installed or used.

Do not fake completion with silent placeholders. Mark each placeholder in the asset table and final response.

Do not replace a blocked required asset with CSS and still call the output high fidelity. Either generate/extract it, get user approval for a lower tier, or report the blocker.

## Verification

Use real browser screenshots. For mobile work, common viewport sizes include `375x812`, `390x844`, `414x896`, `430x764`, and `430x932`, but prefer the source aspect ratio or user-specified device.

For mobile screenshots, verify that OS/device chrome has not been recreated by default. Text such as `9:41`, carrier/wifi/battery indicators, and bottom home indicators should be absent unless they are part of the requested product UI.

For multi-page work, capture each initial viewport and at least one scrolled state for scroll-heavy pages.

For dashboard/admin work, verify dense content: table row height, sidebar width, header controls, empty/loading/error states if implemented, and horizontal overflow.

For high-fidelity work, use `scripts/make_ruler_compare.py` or measured region notes before final reporting. Measure large regions first: header/sidebar/nav, hero/content blocks, primary artwork, major cards/tables, CTA/footer/nav.

## Reporting

Final response should include:

- Preview URL/path.
- Changed files.
- Generated/extracted asset files.
- Required asset rows that were generated, extracted, placeholder, or blocked.
- Screenshot files.
- Fidelity tier reached.
- Remaining gaps grouped as layout, asset fidelity, text/font, interaction, responsiveness, source ambiguity, or model/tooling blocker.
