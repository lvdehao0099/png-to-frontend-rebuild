# Ruler Calibration Guide

Use this guide when the user asks for higher fidelity, says proportions are wrong, or asks to continue restoring the design.

## Normalize The Comparison

1. Scale the source PNG to the target viewport width.
2. Capture the current frontend at the same width.
3. Place both images side by side with horizontal ruler lines.
4. Compare regions by y-coordinate and bounding boxes.

For high-fidelity work, create this comparison artifact before final reporting. Do not rely on visual memory or a screenshot shown in isolation.

The source image's scaled height may differ from the browser screenshot height. Do not stretch everything to fit. Decide whether the task needs:

- **Design canvas lock:** preserve the original design aspect ratio and allow extra browser height outside the design canvas.
- **Responsive adaptation:** preserve relative composition but fill the viewport, accepting measured differences.

For high-fidelity visual reconstruction, prefer design canvas lock first.

## Regions To Measure

Record approximate top/bottom y-coordinates after source scaling:

- Page title or app header.
- Info summary block.
- Tab/time selector strip.
- Main card outer bounds.
- Section title and ornament group.
- Primary artwork/table/product bounds.
- Count/status line.
- CTA button.
- Warning/notice text.
- Bottom navigation.
- Custom icon groups and generated-art asset boxes.
- Mobile device chrome exclusion: verify OS status bars and home indicators are omitted unless requested.

Use a table like this during calibration:

| Region | Source x/y/w/h | Current x/y/w/h | Difference | Fix |
| --- | --- | --- | --- | --- |
| Title |  |  |  |  |
| Info block |  |  |  |  |
| Tabs |  |  |  |  |
| Main card |  |  |  |  |
| Section title |  |  |  |  |
| Primary asset |  |  |  |  |
| CTA |  |  |  |  |
| Bottom nav |  |  |  |  |

Measure x-coordinates for:

- Card left/right edges.
- Tab strip left/right edges.
- Section title center and ornament groups.
- Primary asset width.
- Button width.
- Nav item centers.

## Adjustment Order

1. Canvas/aspect strategy.
2. Top-level vertical sections.
3. Major containers: card, tab strip, nav.
4. Primary generated assets.
5. Typography: size, weight, line-height, letter spacing.
6. Micro-ornaments: dots, dividers, glows.
7. Interaction states.

For generated icons and other small assets, check asset source, cleanliness, and display size before tweaking layout:

- **Asset source:** Is this actually generated/extracted according to the asset table, or did CSS/source-crop sneak in?
- **Asset cleanliness:** Does it have visible square backgrounds, frames, labels, or unused sprite gutters?
- **Display size:** Does transparent-bound cropping make it readable at final UI size?

Do not start with micro-ornaments if the large regions are still off.

## Common Fixes

- If everything feels too tall or too spread out, lock the design canvas to the source aspect ratio instead of filling a taller viewport.
- If the background feels too large, generate a more zoomed-out background asset before distorting CSS background size.
- If a regular button looks soft or pasted in, rebuild it with CSS instead of using a generated image.
- If icons look inconsistent, regenerate each icon independently with identical prompt constraints.
- If generated icon sprite cells show boxes or dark backgrounds, regenerate on a flat chroma-key background or remove the background locally; do not hide the issue with CSS blend modes.
- If generated icons render too small, crop transparent bounds before changing layout.
- If text looks wrong, adjust live text font-size, font-weight, line-height, and container position; do not bake text into images.

## Reporting

When finishing a calibration pass, report:

- Which screenshot version was produced.
- Which compare/ruler image was produced.
- What was aligned.
- What remains visibly different and why.
- Which generated asset groups were validated clean/no-frame at final display size.

## Acceptance Notes

For generated assets, separate two questions:

- **Placement fidelity:** Does the asset occupy the same box as the source?
- **Asset fidelity:** Does the generated asset itself look like the source?

Fix placement with CSS. Fix asset fidelity with a new image prompt or a different asset strategy. Do not compensate for a bad asset by distorting layout.
