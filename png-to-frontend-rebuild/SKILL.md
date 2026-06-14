---
name: png-to-frontend-rebuild
description: Codex workflow for rebuilding flat PNG UI designs, AI-generated mockups, app screenshots, or multi-page design sets into high-fidelity frontend projects with planned image-generation assets, real HTML/CSS/JS or framework code, shared components, and screenshot-based calibration. Use when the user asks Codex to convert one or more PNG/JPG/WEBP UI images into usable frontend, recreate a screenshot accurately, extract or regenerate missing visual assets, plan Image-2 or image-model asset generation, adapt the result to an existing stack, avoid screenshot slicing, or improve visual fidelity.
---

# PNG To Frontend Rebuild

## Contract

Use this skill as a Codex workspace workflow, not as a chat-only prompt. It assumes the agent can inspect local files, edit project code, stage assets, run a local page/app, capture browser screenshots, compare results, and generate or extract independent visual assets.

Do not slice the input image into static fragments. Rebuild it as:

- Generated or extracted assets for complex artwork.
- Live DOM/components for text, forms, controls, layout, and states.
- Shared tokens/components for repeated UI systems.
- Browser screenshots and calibration before claiming fidelity.

Prefer Image-2 when available for high-quality generated assets. If Image-2 is unavailable, use the best available image generation/editing model, but do not silently downgrade required visual assets to CSS or placeholders.

## Hard Lessons From Failed Rebuilds

These rules are mandatory for high-fidelity PNG-to-frontend work:

- Do not treat "small" as "simple." Header actions, avatars, membership badges, level gems, bottom-nav icons, service pictograms, coupons, crowns, shields, chat bubbles, and similar small visuals are required assets when their style is custom.
- Do not crop icons out of the source screenshot and call them "redrawn." Source extraction is allowed only when exact identity/data preservation is required or when explicitly labeled as extraction. If the user asks for Image-2/model-drawn icons, generate them with the image model.
- Do not replace custom icon families with CSS/SVG approximations for high fidelity unless the source icon style is genuinely simple and the asset table explains why.
- Do not use generated sprite sheets directly if cell backgrounds, frames, or gutters are visible. Produce transparent/no-frame assets, or remove a chroma-key background locally, crop transparent bounds, and validate in the real UI.
- Do not leave product/hero images as rectangular crops with background unless that rectangle is part of the source design. Use generated transparent-ready assets, extraction with masking, or an explicit hybrid art layer.
- For mobile app screenshots, do not recreate the phone OS status bar (time, cellular/Wi-Fi, battery, home indicator) unless the user explicitly asks for device chrome. Treat it as capture chrome, not product UI.
- Do not claim high fidelity until a side-by-side ruler comparison image or measured region table exists and has informed at least one calibration pass.

## Mandatory Visual Asset Contract

For every PNG/JPG/WEBP rebuild, assume the source contains visual assets that must be independently generated or extracted unless proven otherwise. This rule applies across all future projects, stacks, themes, and subject matter.

Before writing frontend code:

- Identify every visually important non-standard asset, including backgrounds, custom icon sets, mascots, characters, people, products, scene art, illustrations, ornaments, badges, medals, flags, stickers, maps, charts, textures, special controls, and brand-like compositions.
- Include micro-assets in that inventory: membership levels, rank gems, header action icons, avatars, notification/message icons, service cards, bottom navigation icons, status badges, coupon/crown/shield/cube icons, and any custom glyph whose glow/material is visible.
- Classify each such item as `image-model-required`, `extract-user-asset`, or `hybrid` in the asset table. Do not omit small repeated icons; grouped icon families still count as required assets.
- Use Image-2 or the configured image model for all `image-model-required` rows before replacing them with CSS. If the user provides Image-2/model configuration, use it for every `image-model-required` icon/artwork group, not just one sample. If generation is unavailable, mark the row `blocked` or `placeholder` and state the blocker.
- Use extraction only for exact user-provided assets, real people, legally sensitive marks, QR/barcodes, exact charts/maps, and assets that must preserve identity or data.
- Keep normal UI as live DOM/CSS: text, card boxes, borders, grids, tabs, buttons with editable labels, forms, and simple stateful controls.

CSS may reproduce an asset only when it is a standard geometric UI affordance or an already-installed icon library closely matches the source style. CSS must not be used as a substitute for custom artwork, custom icon families, scene backgrounds, decorative objects, or stylized material assets merely to save time.

When the user provides Image-2 or another image-model configuration, and the source contains any `image-model-required` assets, at least one generation pass for those assets is mandatory before implementation can be called high fidelity. A runnable page with CSS stand-ins is at most prototype fidelity unless all required generated/extracted assets are present or explicitly blocked.

For generated UI icons, prefer one of these two delivery patterns:

- Individual transparent PNG/WebP assets.
- Sprite sheets generated on a flat chroma-key background, then split, background-removed, transparent-bounds-cropped, and validated at final display size.

Never ship sprite cells with visible square backgrounds, frames, labels, or gutters unless the source design visibly has those boxes.

## Required References

Read the relevant reference files before acting:

- `references/workflow.md`: Always read. Covers input routing, planning gate, delivery flow, fidelity tiers, failure handling, and verification.
- `references/asset-planning.md`: Read before implementation. Covers the asset decision table, image-model rules, copyright/brand constraints, and prompt patterns.
- `references/framework-adapters.md`: Read when working inside an existing app or when the user specifies React, Vue, Next.js, Tailwind, shadcn/ui, static HTML, WeChat Mini Program, UniApp, or another target stack.
- `references/calibration.md`: Read for high-fidelity or calibration work.
- `references/project-case-miniapp.md`: Read only when a task resembles a multi-page mobile mini-program/app with shared bottom navigation, generated icon assets, or mobile screenshot delivery.

## Non-Negotiable Planning Gate

Before writing frontend code, produce a short execution plan and an asset decision table. Skip this only when the user explicitly requests a rough throwaway prototype.

The plan must include:

- Input type and task route.
- Target page(s), canonical source image(s), and target viewport(s).
- Target stack and how existing project conventions will be used.
- Fidelity tier and acceptance outputs.
- Shared systems to centralize.
- Standard asset decision table.
- Explicit list of mandatory generated/extracted asset groups and which model/tool will produce them.
- Screenshot/verification plan.

Use this standard asset table:

| assetId | sourcePage | visualRole | strategy | reason | promptNeeded | outputPath | status | risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bg-main | all | background | image-model-required | complex hidden atmosphere | yes | assets/bg-main.png | planned | medium |
| qr-invite | invite | QR code | extract-user-asset | must be exact | no | assets/qr-invite.png | needed | high |
| primary-button | all | normal CTA | css-dom | editable text and state | no | component | planned | low |

Allowed `strategy` values:

- `image-model-required`: Use Image-2 or best available image model for complex backgrounds, stylized icons, product art, special button skins, illustrations, ornaments, textures, and visual assets that CSS cannot match.
- `extract-user-asset`: Use supplied/extracted exact assets for QR codes, official logos, legally sensitive marks, exact product photos, and user-provided brand assets.
- `css-dom`: Use code for text, forms, standard buttons, cards, tabs, badges, borders, simple gradients, layout, and stateful controls.
- `hybrid`: Use an image skin/art layer with live DOM text/control.

If a visually important item is hard to reproduce with code, classify it as `image-model-required`. Do not classify it as CSS merely to save time.

## Execution Summary

1. Inspect source images and project context.
2. Route the task using `references/workflow.md`.
3. Complete the planning gate and asset table.
4. Generate, extract, or stage all `image-model-required`, `extract-user-asset`, and `hybrid` art-layer items needed for the target fidelity before substituting CSS or coding around them.
5. Implement using the existing project stack or the requested target stack.
6. Run the page/app locally.
7. Capture screenshots at target viewport(s).
8. Compare with source images; for high fidelity, use ruler calibration.
9. Iterate assets and code until the selected fidelity tier is satisfied or blockers are explicit.
10. Report changed files, preview URL/path, screenshots, generated assets, and remaining gaps.

## Completion Checklist

- Source images inspected and canonical sources selected.
- Planning gate completed unless explicitly skipped by the user.
- Asset decision table uses the standard fields.
- Required generated/extracted assets exist or are listed as unfinished blockers.
- Image-model-required assets were actually generated with Image-2/best available model, unless marked blocked with a concrete reason.
- CSS was not used as a fallback for custom artwork or icon families.
- Regular UI is live code, not baked text/images.
- Complex artwork uses generated/extracted assets where appropriate.
- Existing project framework and design conventions are respected.
- Multi-page work centralizes shared tokens/components/navigation.
- Local preview runs.
- Browser screenshots are captured.
- High-fidelity work includes ruler comparison or measured region notes.
- Final response names remaining gaps by category: layout, asset fidelity, text/font, interaction, responsiveness, source ambiguity, model/tooling blocker.
