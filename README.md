<div align="center">

# PNG To Frontend Rebuild

**Turn AI-designed UI screenshots into real frontend code without flattening the hard parts.**

English | [简体中文](README.zh-CN.md)

</div>

Modern AI can create beautiful UI mockups: rich backgrounds, custom icons, badges, product scenes, soft glows, glass panels, illustrated controls. The hard part starts when you try to implement them in a frontend tool or coding agent. Cropping the screenshot gives you dead pixels. Rebuilding everything with CSS loses the visual quality. Ignoring the details makes the result feel wrong.

`png-to-frontend-rebuild` is a Codex skill for that gap. It teaches Codex to treat a PNG/JPG/WEBP mockup as a rebuild project: identify the visual assets, regenerate or extract the parts that cannot be faithfully coded, implement the interface as real DOM/components, then verify the result with screenshots and ruler comparison.

![Problem comparison](docs/assets/problem-comparison.svg)

## The Problem

Screenshot-to-code often fails in one of two ways:

- **It slices the mockup into images.** The page may look close, but text, layout, states, and components are not really editable.
- **It codes everything as generic CSS.** The structure is editable, but complex art, custom icons, background effects, and branded visual details disappear.

This skill is for the third path: real frontend code plus explicit handling for complex visual assets.

## What It Makes Codex Do

- Plan the rebuild before coding.
- List every important visual asset instead of hand-waving the hard parts away.
- Use image generation or extraction for assets that should not be approximated with CSS.
- Keep normal interface elements as editable frontend code.
- Avoid presenting cropped screenshot fragments as “redrawn” assets.
- Ignore device chrome such as mobile status bars unless the user explicitly asks for it.
- Compare the implementation against the source image before claiming high fidelity.

## Install

Clone the repository and copy the skill folder into your Codex skills directory:

```powershell
git clone https://github.com/lvdehao0099/png-to-frontend-rebuild.git
Copy-Item -Recurse .\png-to-frontend-rebuild\png-to-frontend-rebuild "$env:USERPROFILE\.codex\skills\png-to-frontend-rebuild"
```

Start a new Codex session after copying the skill.

## Use

```text
Use $png-to-frontend-rebuild to rebuild this screenshot into a frontend project:
C:\path\to\mockup.png

Make it high fidelity. Do not slice screenshot icons. Use generated or extracted assets for complex visuals, and give me a browser screenshot plus comparison image.
```

## Best For

- AI-generated app or web mockups with custom visual effects.
- Landing pages, dashboards, mobile screens, product pages, and internal tools.
- Designs where icons, illustrations, backgrounds, badges, textures, or product art matter.
- Rebuilds where the output must remain editable and maintainable.

## Not For

- One-click OCR or generic screenshot slicing.
- Copying proprietary logos, people, maps, QR codes, or exact product photos without permission.
- Replacing a proper design source file when Figma or original assets are already available.

## Included

- `SKILL.md`: the main Codex workflow.
- `references/`: deeper rules for asset planning, framework adaptation, calibration, and mobile rebuilds.
- `scripts/make_ruler_compare.py`: helper for source-vs-implementation comparison images.
- `assets/html-template/`: a small static HTML starting point.
