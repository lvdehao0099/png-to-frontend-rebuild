# Asset Planning

Use this reference before implementation. The goal is to prevent lazy CSS approximations for artwork while avoiding unnecessary generated images for normal UI. Treat asset planning as a hard gate: high-fidelity rebuilds require independent visual assets, not CSS stand-ins for artwork.

## Standard Asset Table

Use this table shape:

| assetId | sourcePage | visualRole | strategy | reason | promptNeeded | outputPath | status | risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Field meanings:

- `assetId`: stable lowercase id, e.g. `bg-main`, `nav-home`, `product-card-1`.
- `sourcePage`: page or `all`.
- `visualRole`: background, logo, nav-icon, product, illustration, CTA-skin, QR, chart, table, card-style, etc.
- `strategy`: `image-model-required`, `extract-user-asset`, `css-dom`, or `hybrid`.
- `reason`: why this strategy is correct.
- `promptNeeded`: `yes` for image generation; `no` for CSS/extract; `maybe` when user approval is needed.
- `outputPath`: final asset path or component/class name.
- `status`: planned, generated, extracted, implemented, placeholder, blocked.
- `risk`: low, medium, high.

## Strategy Rules

## Mandatory Asset Inventory

For every source screen, scan the image and list all visually important non-standard assets before writing frontend code. The inventory must be general-purpose and source-driven, not project-specific.

Default these categories into the asset table:

- Scene or atmospheric backgrounds, including rooms, landscapes, venues, dashboards with decorative backdrop art, game scenes, product hero environments, and blurred or obscured visual fields.
- Custom icon families, including menu icons, nav icons, category icons, toolbar icons, badges, status glyphs, stickers, and repeated pictograms whose style is part of the design.
- Micro icon/art systems, including header action icons, avatars, membership level badges, rank gems, coupon/crown/shield/cube pictograms, service-card objects, bottom navigation icons, notification badges, and any small glossy/neon/material glyph.
- Characters, mascots, people, avatars, player cards, product photos, food/drink/object thumbnails, vehicles, devices, apparel, collectibles, or any subject-matter image.
- Illustrations, decorative objects, flags, ribbons, medals, awards, crowns, tickets, stamps, ornaments, textures, patterned materials, special CTA/button skins, and stylized card art.
- Exact data or identity assets such as QR codes, barcodes, maps, charts, official logos, legal marks, real people, and user-owned brand marks.

For each item, choose:

- `image-model-required` for approximate but high-fidelity artwork the model can generate.
- `extract-user-asset` for exact, identity-sensitive, legal, data-bearing, or user-owned assets.
- `hybrid` when an art layer is generated/extracted but text, controls, or state remain live DOM.
- `css-dom` only for normal interface construction and genuinely simple geometric controls.

Do not collapse many different visual objects into a vague row such as "icons" unless they will be generated as a deliberate coherent icon set. If grouped, the row must name the whole set, count or list members, and define a shared style prompt.

If a source contains a custom icon family or decorative object set, CSS reproduction is not acceptable for high fidelity unless an existing icon library is demonstrably close in silhouette, material, perspective, line weight, and color treatment. Otherwise classify it as `image-model-required`.

If the user asks for Image-2/model-drawn assets, source-image cropping is not a substitute. Do not crop screenshot icons and call them "redrawn" or "generated." Screenshot crops are `extract-user-asset` only and must be labeled as such.

Prefer `image-model-required` for:

- Complex or obscured backgrounds.
- Custom icon families where standard icon libraries visibly change the style.
- Product, food, drink, object, fashion, vehicle, device, or environment images.
- Illustrations, characters, scenes, decorative textures, patterns, ornaments.
- Special CTA/button skins where shape, lighting, material, or glow is artwork.
- Brand hero compositions when exact official assets are not required.
- Any custom visual asset whose style would materially change if replaced by CSS, emoji, Unicode symbols, generic SVGs, or off-the-shelf icons.

Prefer Image-2 when available. If Image-2 is unavailable, use the best available image generation/editing model. If no suitable model is available, mark the row blocked or placeholder; do not silently replace it with CSS.

When the user provides Image-2 or another image model configuration, and the table contains any `image-model-required` rows, run at least one generation pass before claiming high fidelity. If generation fails, record the error/blocker in the table and final response.

When the user provides Image-2 or another image model configuration, each `image-model-required` icon/art group must have a real generated output, not merely a CSS approximation or one sample generation. For example, a mobile membership screen usually needs separate generated rows for:

- background/hero environment
- hero product/device
- product thumbnails
- benefit strip icons
- function grid icons
- header action icons and avatar
- membership badge/rank gem
- bottom navigation icons
- service-card objects

## Generated Icon Rules

For high-fidelity UI icon work:

- Prefer individual transparent assets, or generate sprite sheets on a flat chroma-key background and then split/remove the background locally.
- After splitting a sheet, crop each icon to transparent content bounds. Do not leave cell gutters or unused canvas that makes icons render tiny.
- Validate the icon assets inside the actual UI at final display size. If the icon is too small, boxed, blurry, or stylistically inconsistent, regenerate with explicit constraints about cell fill percentage and no frames.
- Never ship visible square cell backgrounds, dark boxes, frames, labels, or sheet gutters unless the source design has those boxes.
- Keep text labels and numeric state live DOM. If the generated icon accidentally bakes text or numbers that should be live, regenerate or remove them.

Prefer `extract-user-asset` for:

- QR codes, barcodes, maps, charts with exact data.
- Official logos and legal/brand-sensitive marks.
- Exact supplied product photos.
- User-owned brand assets.
- Real people or identity-sensitive images.

Prefer `css-dom` for:

- Regular editable text.
- Inputs, forms, normal buttons, tabs, badges, cards, lists, tables, simple nav bars.
- Borders, shadows, blur, simple gradients, dividers, spacing.
- Icons when a project library already matches the source style.

Do not use `css-dom` for:

- Custom menu/nav/category icon sets.
- Background scenes or environmental art.
- Stylized medals, crowns, tickets, flags, ribbons, stickers, trophies, or decorative objects.
- Product/character/person/object imagery.
- Complex material effects whose visual identity depends on lighting, texture, perspective, or painterly/3D treatment.

These must be `image-model-required`, `extract-user-asset`, or `hybrid`.

Use `hybrid` for:

- Generated button/card skin plus live label and click target.
- Generated logo mark plus live tagline.
- Generated chart background plus live data labels.
- Decorative image layer behind live controls.

If an item is visually important and hard to reproduce with code, classify it as `image-model-required`. Time saving is not a valid reason to downgrade a required visual asset.

## Fidelity Gate

Before implementation begins, the asset table must have no silent gaps:

- Every mandatory asset is listed.
- Every `image-model-required` row is `planned`, `generated`, `placeholder`, or `blocked`.
- Every high-fidelity deliverable has generated/extracted assets staged before final screenshot calibration.
- Any CSS fallback for a required asset is labeled `placeholder`, not `implemented`.

If required assets are still placeholders or blocked, finish as prototype fidelity unless the user explicitly accepts the gap.

## Copyright And Brand Rules

- Do not invent exact third-party logos or trademarked packaging.
- Do not generate readable brand text unless the user supplies/approves that asset and has rights to use it.
- For QR codes, barcodes, official logos, maps, legal marks, and exact product photos, request or extract the real user asset.
- For placeholder product art, avoid readable real brand labels and mark it as placeholder if it is not final.
- Keep original source images local and project-owned; do not scrape third-party targets.

## Prompt Patterns

Small UI icons:

```text
Use case: mobile/web UI icon
Asset type: single transparent-ready glyph
Primary request: <semantic object>, <style>, minimal detail, crisp at <target px>, simple silhouette
Composition: centered with padding, no text, no background panel
Avoid: app icon, 3D poster object, thick glossy render, extra symbols, watermark
```

Transparent/chroma-key icon sheet:

```text
Use case: mobile UI icon sprite sheet
Asset type: transparent-ready icon set
Primary request: <N> icons: <ordered list>
Style: match the source's material/glow/line weight
Composition: each icon centered and filling <70-85>% of its cell
Background: perfectly flat solid #00ff00 chroma-key green
Avoid: square cell backgrounds, frames, cards, labels, UI panels, text, watermark
Post-process: split sheet, remove chroma key, crop transparent bounds
```

Backgrounds:

```text
Use case: app/page background
Asset type: full composition without UI
Primary request: <scene/style>, important visual interest near edges, clean negative space behind UI
Lighting/mood: <mood>
Avoid: buttons, panels, QR codes, readable UI text, watermark
```

Product/object thumbnails:

```text
Use case: product/list/card thumbnail
Asset type: <square/rectangle> product image
Primary request: <object>, centered, readable at small UI size, consistent margins
Lighting/mood: <mood>
Avoid: people, hands, readable brand text, white background unless source requires it, watermark
```

Special button skins:

```text
Use case: UI button skin
Asset type: transparent-ready decorative button background
Primary request: <shape/material/glow>, no text, fits <width>x<height>
Composition: centered button skin with padding
Avoid: baked text, icons unless requested, watermark
```

## Asset Validation

Validate generated assets inside the real UI, at final display size. If the asset looks too detailed, too heavy, too realistic, too soft, or mismatched after downscaling, regenerate with constraints about final pixel size, visual weight, and role.

Keep old attempts only as alternates. Update frontend references to the best asset and screenshot-check the result.
