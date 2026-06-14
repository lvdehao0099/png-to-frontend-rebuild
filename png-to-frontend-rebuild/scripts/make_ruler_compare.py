#!/usr/bin/env python3
"""Create a side-by-side ruler comparison for PNG-to-frontend calibration."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, help="Source PNG design")
    parser.add_argument("--current", required=True, help="Current frontend screenshot")
    parser.add_argument("--out", required=True, help="Output comparison PNG")
    parser.add_argument("--width", type=int, default=430, help="Comparison width for each side")
    parser.add_argument("--step", type=int, default=25, help="Ruler line step in pixels")
    parser.add_argument(
        "--mark",
        action="append",
        default=[],
        help="Named horizontal marker as label:y, e.g. title:52. May be repeated.",
    )
    parser.add_argument(
        "--vmark",
        action="append",
        default=[],
        help="Named vertical marker as label:x, e.g. card-left:16. May be repeated.",
    )
    return parser.parse_args()


def scaled_to_width(image: Image.Image, width: int) -> Image.Image:
    height = round(image.height * width / image.width)
    return image.resize((width, height), Image.Resampling.LANCZOS)


def main() -> None:
    args = parse_args()
    source_path = Path(args.source)
    current_path = Path(args.current)
    out_path = Path(args.out)

    source = scaled_to_width(Image.open(source_path).convert("RGB"), args.width)
    current = Image.open(current_path).convert("RGB")
    if current.width != args.width:
        current = scaled_to_width(current, args.width)

    gutter = 34
    height = max(source.height, current.height)
    canvas = Image.new("RGB", (args.width * 2 + gutter, height), (18, 18, 20))
    canvas.paste(source, (0, 0))
    canvas.paste(current, (args.width + gutter, 0))

    draw = ImageDraw.Draw(canvas)
    for y in range(0, height, args.step):
        if y % 100 == 0:
            color = (255, 255, 255)
        elif y % 50 == 0:
            color = (160, 160, 160)
        else:
            color = (80, 80, 80)
        for x0 in (0, args.width + gutter):
            draw.line([(x0, y), (x0 + args.width, y)], fill=color, width=1)
        if y % 50 == 0:
            draw.text((args.width + 4, y + 2), str(y), fill=(255, 210, 90))

    draw.text((8, 8), f"source scaled {args.width}w", fill=(255, 255, 255))
    draw.text((args.width + gutter + 8, 8), "current", fill=(255, 255, 255))

    for raw in args.mark:
        label, y = parse_marker(raw)
        color = (255, 72, 72)
        for x0 in (0, args.width + gutter):
            draw.line([(x0, y), (x0 + args.width, y)], fill=color, width=2)
            draw.text((x0 + 4, y + 2), label, fill=(255, 190, 190))

    for raw in args.vmark:
        label, x = parse_marker(raw)
        color = (83, 215, 255)
        for x0 in (0, args.width + gutter):
            xx = x0 + x
            draw.line([(xx, 0), (xx, height)], fill=color, width=2)
            draw.text((xx + 3, 22), label, fill=(190, 235, 255))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out_path)
    print(f"saved {out_path} source={source.size} current={current.size} compare={canvas.size}")


def parse_marker(raw: str) -> tuple[str, int]:
    if ":" not in raw:
        raise SystemExit(f"marker must be label:value, got {raw!r}")
    label, value = raw.rsplit(":", 1)
    try:
        position = int(float(value))
    except ValueError as exc:
        raise SystemExit(f"marker value must be numeric, got {raw!r}") from exc
    return label, position


if __name__ == "__main__":
    main()
