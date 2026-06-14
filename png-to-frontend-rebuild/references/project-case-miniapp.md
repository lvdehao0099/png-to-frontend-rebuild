# Case Reference: Multi-Page Mobile App

Read this only for tasks resembling a mobile app or mini-program with multiple pages, fixed bottom navigation, generated icon assets, and shared visual systems.

## Lessons

The project pattern:

- Multiple AI-generated PNG pages.
- A shared mobile width and safe top area.
- A shared background/atmosphere.
- Custom bottom navigation icons.
- Some pages fixed to one viewport, others scroll.
- Product/list imagery and decorative artwork generated as independent assets.
- Common CSS/JS or shared components used to prevent page drift.
- System status bars and home indicators in screenshots are usually capture chrome, not app UI, and should be omitted unless explicitly requested.

These lessons generalize to apps such as ordering, events, membership, booking, entertainment, ecommerce, community, and service workflows.

## Multi-Page Rules

- Select one canonical source image per page before coding.
- Centralize background, top bar, bottom nav, card style, typography, buttons, tags, and spacing tokens.
- Use one coherent icon family for bottom nav.
- Treat top-right action icons, avatars, membership badges, level gems, service-card icons, benefit-strip icons, and bottom navigation icons as required visual assets when their styling is custom.
- Generate custom icon families with the configured image model when available. Do not replace them with screenshot crops or CSS stand-ins for high fidelity.
- Use transparent/no-frame icon assets. If generating sprite sheets, use a removable chroma-key background, split the sheet, remove the background, crop transparent bounds, and inspect a contact sheet before wiring icons into the UI.
- Keep labels, badge counts, and dynamic numbers as live DOM layered over/near generated icons.
- Keep page links and asset paths portable inside the delivery folder/app.
- Decide each page's scroll model before implementation:
  - fixed canvas for screenshot-like landing/booking pages;
  - internal scroll for product/menu/list panels with fixed cart/nav;
  - full-page scroll for profile, invitation, coupon, settings, or content-heavy pages.
- Capture both initial and scrolled screenshots for scroll-heavy pages.

## Common Asset Types

- Shared background: usually image-model-required.
- Brand/logo: extract-user-asset when exact; image-model-required when stylized but approximate is acceptable.
- Bottom nav icons: image-model-required when custom; CSS/icon library only when style matches.
- Header action icons, avatars, membership ranks, benefit icons, and service-card objects: image-model-required when custom; do not omit because they are small.
- Product/object thumbnails: image-model-required or extract-user-asset.
- QR code: extract-user-asset only.
- Decorative card ornaments or special buttons: image-model-required or hybrid.

## Delivery Shape

For static handoff:

```text
delivery/
  common.css
  common.js
  page-a.html
  page-b.html
  assets/
  output/screenshots/
```

For framework apps, map the same ideas to shared shell/components and route pages.

## Quality Checks

- Active nav state is visible and correct per page.
- Bottom nav stays fixed when expected.
- Device OS status bar/home indicator is omitted unless intentionally included.
- Generated icons have no visible square cell backgrounds, frames, labels, or sheet gutters.
- Product/list pages do not hide controls behind nav/cart.
- Text remains live and editable.
- Image assets are visually consistent at final size.
- Shared background/card/nav styles make the pages feel like one product, not separate mockups.
