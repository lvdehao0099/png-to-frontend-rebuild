# Framework Adapters

Use this reference when the user specifies a target stack or the workspace already contains an app.

## Stack Selection

Prefer the existing project stack and conventions. Inspect package files, source folders, routing, component libraries, CSS strategy, and asset handling before creating new files.

If no app exists, choose based on user request:

- Static HTML/CSS/JS for portable demos or handoff packages.
- React/Next.js for componentized web apps.
- Vue/Nuxt for Vue projects.
- Tailwind when already present or requested.
- shadcn/ui when already present or the target is a modern app interface.
- WeChat Mini Program or UniApp when the target is a mini-program/mobile Chinese app workflow.

Do not create a new framework app inside an existing project unless the user asks.

## Static HTML

Use when the user wants a self-contained preview or no framework exists.

Recommended structure:

```text
delivery/
  index.html
  page-a.html
  page-b.html
  common.css
  common.js
  assets/
```

Use CSS variables for tokens. Keep links relative and portable.

## React / Next.js

Use existing routing and components. Prefer:

- Shared shell/layout component.
- Asset imports or public assets according to project convention.
- CSS modules, Tailwind, or existing styling system.
- Real button/input/link components.
- Component props for repeated cards, nav items, product rows, stats, filters.

Avoid large absolute-positioned single-page replicas unless the task is explicit screenshot calibration.

## Vue / Nuxt

Use existing component and style conventions. Prefer:

- Page shell component.
- Reusable components for nav, cards, product rows, tabs, forms.
- Scoped styles only when local; shared tokens/styles in existing global CSS.
- Project asset convention for `public/` or imported assets.

## Tailwind

Use Tailwind if it is already configured. Extract repeated values into components or CSS variables when many elements share exact dimensions or colors.

Avoid huge unreadable class strings for calibrated screens; local CSS is acceptable for complex measured layouts.

## shadcn/ui

Use shadcn components for normal app controls when the source resembles an app/dashboard and the project already uses shadcn. Do not force shadcn onto highly visual landing pages or game-like/mobile art-heavy screens.

Generated artwork still belongs in assets; shadcn should not replace required visual assets.

## WeChat Mini Program / UniApp

Use when the source has mini-program chrome, bottom tabs, mobile safe areas, or the user requests it.

Plan:

- App/page shell and safe-area spacing.
- Shared bottom navigation.
- Fixed versus internal scroll per page.
- WXSS/utility tokens for colors, spacing, nav height, top safe area.
- Assets in a portable local folder.

Keep text and controls live. Use generated/extracted images for backgrounds, icons, logos, product shots, and special decorative art.

## Dashboard / Admin

For dense operational screens:

- Prioritize readable data density and alignment.
- Use native tables or grid components from the project.
- Rebuild charts with a chart library if data is known; use image only for decorative or unknown chart screenshots and mark as placeholder.
- Verify responsive overflow, sticky headers/sidebar, filters, empty/loading/error states when visible.

## Existing Design Systems

If the repo has a design system, use it first. Only add new styling when the screenshot requires a visual surface the system does not provide. Keep new tokens named clearly and scoped to the rebuilt feature when they are not globally useful.
