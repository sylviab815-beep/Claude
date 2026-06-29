#!/usr/bin/env python3
"""Build an AuthorScale-style 9:16 slideshow from a plan JSON.

Reads slideshow_plan.json, calls DALL-E 3 for each slide, overlays the hook
text per the genre's text_style profile, and writes slide_NN.jpg files to the
output folder.

Usage:
    python3 build_slideshow.py slideshow_plan.json [--only 1,3,5] [--dry-run]
"""
from __future__ import annotations

import argparse
import io
import json
import os
import sys
import time
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

CANVAS_W, CANVAS_H = 1024, 1792
PADDING = 64
MAX_TEXT_W = CANVAS_W - 2 * PADDING
TOP_BASELINE_Y = 320
BOTTOM_BASELINE_Y = 1472
MAX_LINES = 3
FONT_MIN = 72
FONT_MAX = 140

# Style profiles — font names are searched on the system; fallbacks kick in.
STYLE_PROFILES = {
    "dark_romance": {
        "font_candidates": ["Playfair Display Black", "Playfair-Display-Black", "PlayfairDisplay-Black", "Cormorant Garamond Bold", "Georgia Bold"],
        "fill": (255, 255, 255),
        "stroke": (0, 0, 0),
        "stroke_w": 4,
        "shadow": (0, 0, 0, 230),
        "italic": False,
        "default_plate": False,
    },
    "monster_romance": {
        "font_candidates": ["Cinzel Black", "Cinzel-Black", "Cinzel Bold", "UnifrakturCook Bold", "Georgia Bold"],
        "fill": (245, 233, 200),
        "stroke": (43, 26, 15),
        "stroke_w": 3,
        "shadow": None,
        "italic": False,
        "default_plate": False,
    },
    "paranormal_romance": {
        "font_candidates": ["Italiana", "Great Vibes", "Georgia Italic"],
        "fill": (232, 220, 196),
        "stroke": (26, 26, 46),
        "stroke_w": 2,
        "shadow": (80, 60, 140, 140),
        "italic": True,
        "default_plate": False,
    },
    "romantic_suspense": {
        "font_candidates": ["Oswald Bold", "Bebas Neue", "Impact"],
        "fill": (255, 255, 255),
        "stroke": (0, 0, 0),
        "stroke_w": 4,
        "shadow": (0, 0, 0, 220),
        "italic": False,
        "default_plate": False,
    },
    "spicy_romcom": {
        "font_candidates": ["Caveat Bold", "Playfair Display Bold", "Georgia Bold"],
        "fill": (255, 248, 240),
        "stroke": (201, 123, 99),
        "stroke_w": 2,
        "shadow": (100, 60, 40, 120),
        "italic": False,
        "default_plate": False,
    },
    "clean_romcom": {
        "font_candidates": ["Quicksand Bold", "Nunito Bold", "Helvetica Bold"],
        "fill": (58, 46, 42),
        "stroke": (255, 255, 255),
        "stroke_w": 2,
        "shadow": None,
        "italic": False,
        "default_plate": False,
    },
    "cozy_mystery": {
        "font_candidates": ["Libre Baskerville Bold", "Baskerville Bold", "Georgia Bold"],
        "fill": (58, 46, 42),
        "stroke": (255, 248, 231),
        "stroke_w": 2,
        "shadow": None,
        "italic": False,
        "default_plate": False,
    },
    "dark_stays": {
        "font_candidates": ["EB Garamond Italic", "Garamond Italic", "Georgia Italic"],
        "fill": (232, 226, 212),
        "stroke": (10, 10, 10),
        "stroke_w": 2,
        "shadow": (0, 0, 0, 220),
        "italic": True,
        "default_plate": False,
    },
    "sci_fi": {
        "font_candidates": ["Orbitron Bold", "Space Mono Bold", "Courier Bold"],
        "fill": (0, 229, 255),
        "stroke": (10, 10, 15),
        "stroke_w": 2,
        "shadow": (0, 180, 255, 160),
        "italic": False,
        "default_plate": False,
    },
    "thriller": {
        "font_candidates": ["Anton", "Bebas Neue", "Impact"],
        "fill": (255, 255, 255),
        "stroke": (0, 0, 0),
        "stroke_w": 4,
        "shadow": (0, 0, 0, 220),
        "italic": False,
        "default_plate": False,
    },
}

SYSTEM_FONT_DIRS = [
    "/System/Library/Fonts",
    "/System/Library/Fonts/Supplemental",
    "/Library/Fonts",
    str(Path.home() / "Library/Fonts"),
    # Plugin-bundled fonts
    str(Path(__file__).resolve().parent.parent / "fonts"),
]

FALLBACK_FONTS = [
    "Georgia.ttf",
    "Georgia Bold.ttf",
    "HelveticaNeue.ttc",
    "Helvetica.ttc",
    "Arial.ttf",
    "Arial Bold.ttf",
]


def find_font_file(candidates: list[str]) -> str | None:
    """Search system font dirs for any of the candidate family names."""
    search_names = list(candidates) + FALLBACK_FONTS
    for directory in SYSTEM_FONT_DIRS:
        dpath = Path(directory)
        if not dpath.exists():
            continue
        # First try exact-ish matches by family
        for name in search_names:
            norm = name.lower().replace(" ", "").replace("-", "")
            for f in dpath.rglob("*"):
                if f.suffix.lower() not in (".ttf", ".otf", ".ttc"):
                    continue
                stem = f.stem.lower().replace(" ", "").replace("-", "")
                if norm in stem or stem in norm:
                    return str(f)
    return None


def load_font(style: dict, size: int, font_override: str = "") -> ImageFont.FreeTypeFont:
    candidates = [font_override] + style["font_candidates"] if font_override else style["font_candidates"]
    path = find_font_file(candidates)
    if path is None:
        # last-resort PIL default (not scalable) — wrap in truetype with DejaVu if present
        for common in ("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
                       "/Library/Fonts/Arial.ttf"):
            if Path(common).exists():
                return ImageFont.truetype(common, size)
        return ImageFont.load_default()
    return ImageFont.truetype(path, size)


def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_w: int, draw: ImageDraw.ImageDraw) -> list[str]:
    """Greedy word-wrap to fit within max_w."""
    words = text.split()
    lines: list[str] = []
    current: list[str] = []
    for w in words:
        trial = " ".join(current + [w])
        bbox = draw.textbbox((0, 0), trial, font=font)
        if bbox[2] - bbox[0] <= max_w:
            current.append(w)
        else:
            if current:
                lines.append(" ".join(current))
            current = [w]
    if current:
        lines.append(" ".join(current))
    return lines


def fit_font(text: str, style: dict, draw: ImageDraw.ImageDraw, font_override: str = "") -> tuple[ImageFont.FreeTypeFont, list[str]]:
    """Find the largest font size where the text wraps into <= MAX_LINES and fits width."""
    for size in range(FONT_MAX, FONT_MIN - 1, -4):
        font = load_font(style, size, font_override)
        lines = wrap_text(text, font, MAX_TEXT_W, draw)
        if len(lines) <= MAX_LINES:
            # All lines must also fit width (wrap_text guarantees this)
            return font, lines
    # Fall through to smallest
    font = load_font(style, FONT_MIN, font_override)
    lines = wrap_text(text, font, MAX_TEXT_W, draw)
    return font, lines[:MAX_LINES]


def draw_plate(img: Image.Image, position: str) -> Image.Image:
    """Add a soft dark gradient plate to improve text legibility."""
    plate = Image.new("RGBA", (CANVAS_W, CANVAS_H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(plate)
    if position == "top":
        for y in range(int(CANVAS_H * 0.25)):
            frac = 1 - (y / (CANVAS_H * 0.25))
            alpha = int(115 * frac)
            draw.rectangle([(0, y), (CANVAS_W, y + 1)], fill=(0, 0, 0, alpha))
    else:
        start = int(CANVAS_H * 0.75)
        for y in range(start, CANVAS_H):
            frac = (y - start) / (CANVAS_H - start)
            alpha = int(115 * frac)
            draw.rectangle([(0, y), (CANVAS_W, y + 1)], fill=(0, 0, 0, alpha))
    return Image.alpha_composite(img.convert("RGBA"), plate)


def render_text(img: Image.Image, text: str, style_key: str, position: str, force_plate: bool | None, font_override: str = "") -> Image.Image:
    style = STYLE_PROFILES.get(style_key, STYLE_PROFILES["dark_romance"])
    use_plate = style["default_plate"] if force_plate is None else force_plate

    if use_plate:
        img = draw_plate(img, position).convert("RGBA")
    else:
        img = img.convert("RGBA")

    draw = ImageDraw.Draw(img)
    font, lines = fit_font(text, style, draw, font_override)

    # Compute total block height
    line_heights = []
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        line_heights.append(bbox[3] - bbox[1])
    line_spacing = int(font.size * 0.18)
    total_h = sum(line_heights) + line_spacing * max(0, len(lines) - 1)

    center_y = TOP_BASELINE_Y if position == "top" else BOTTOM_BASELINE_Y
    start_y = center_y - total_h // 2

    # Soft shadow (optional)
    if style["shadow"] is not None:
        shadow_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
        sdraw = ImageDraw.Draw(shadow_layer)
        y = start_y
        for line, lh in zip(lines, line_heights):
            bbox = sdraw.textbbox((0, 0), line, font=font)
            w = bbox[2] - bbox[0]
            x = (CANVAS_W - w) // 2
            sdraw.text((x + 4, y + 6), line, font=font, fill=style["shadow"])
            y += lh + line_spacing
        shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=14))
        img = Image.alpha_composite(img, shadow_layer)
        draw = ImageDraw.Draw(img)

    # Text with stroke
    y = start_y
    for line, lh in zip(lines, line_heights):
        bbox = draw.textbbox((0, 0), line, font=font)
        w = bbox[2] - bbox[0]
        x = (CANVAS_W - w) // 2
        draw.text(
            (x, y),
            line,
            font=font,
            fill=style["fill"],
            stroke_width=style["stroke_w"],
            stroke_fill=style["stroke"],
        )
        y += lh + line_spacing

    return img.convert("RGB")


def generate_fal_image(prompt: str, model: str = "fal-ai/flux-pro/v1.1") -> bytes:
    """Call fal.ai Flux and return the downloaded image bytes. Requires FAL_KEY env var."""
    import fal_client
    result = fal_client.subscribe(
        model,
        arguments={
            "prompt": prompt,
            "image_size": "portrait_16_9",
            "num_inference_steps": 28,
            "guidance_scale": 3.5,
            "num_images": 1,
            "enable_safety_checker": True,
            "safety_tolerance": "5",
            "output_format": "jpeg",
        },
        with_logs=False,
    )
    url = result["images"][0]["url"]
    with urllib.request.urlopen(url) as r:
        return r.read()


def generate_dalle_image(prompt: str, api_key: str) -> bytes:
    """Call DALL-E 3 and return the downloaded image bytes."""
    from openai import OpenAI
    client = OpenAI(api_key=api_key)
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1792",
        quality="standard",
        n=1,
        response_format="url",
    )
    url = response.data[0].url
    with urllib.request.urlopen(url) as r:
        return r.read()


def load_cover_image(cover_path: str) -> Image.Image:
    """Load a book cover and resize/crop to 1024x1792 9:16 canvas."""
    img = Image.open(cover_path).convert("RGB")
    src_w, src_h = img.size
    src_ratio = src_w / src_h
    dst_ratio = CANVAS_W / CANVAS_H
    if src_ratio > dst_ratio:
        new_h = src_h
        new_w = int(src_h * dst_ratio)
        left = (src_w - new_w) // 2
        img = img.crop((left, 0, left + new_w, new_h))
    elif src_ratio < dst_ratio:
        new_w = src_w
        new_h = int(src_w / dst_ratio)
        top = (src_h - new_h) // 2
        img = img.crop((0, top, new_w, top + new_h))
    return img.resize((CANVAS_W, CANVAS_H), Image.LANCZOS)


def build_slide(slide: dict, provider: str, out_path: Path, dry_run: bool, font_override: str = "") -> None:
    mode = slide.get("mode", "ai")  # "ai" | "cover"

    if dry_run:
        img = Image.new("RGB", (CANVAS_W, CANVAS_H), (30, 30, 40))
        for y in range(CANVAS_H):
            c = int(30 + (y / CANVAS_H) * 60)
            ImageDraw.Draw(img).rectangle([(0, y), (CANVAS_W, y + 1)], fill=(c, c - 10, c + 10))
    elif mode == "cover":
        cover_path = slide.get("cover_path")
        if not cover_path or not Path(cover_path).exists():
            raise FileNotFoundError(f"cover_path missing or not found: {cover_path}")
        img = load_cover_image(cover_path)
    else:
        prompt = slide.get("image_prompt") or slide.get("dalle_prompt")
        if provider == "fal":
            img_bytes = generate_fal_image(prompt)
        else:
            img_bytes = generate_dalle_image(prompt, os.environ["OPENAI_API_KEY"])
        img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
        # Normalize to exact 1024x1792 (flux portrait_16_9 returns ~1088x1920)
        if img.size != (CANVAS_W, CANVAS_H):
            img = img.resize((CANVAS_W, CANVAS_H), Image.LANCZOS)

    # Cover slides default to plate ON for legibility unless overridden
    plate_default = True if mode == "cover" else slide.get("text_plate")
    overlaid = render_text(
        img,
        slide["hook"],
        slide.get("text_style", "dark_romance"),
        slide.get("text_position", "bottom"),
        plate_default,
        font_override,
    )
    overlaid.save(out_path, "JPEG", quality=92)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("plan", help="Path to slideshow_plan.json")
    parser.add_argument("--only", help="Comma-separated slide numbers to (re)build", default=None)
    parser.add_argument("--dry-run", action="store_true", help="Skip image API, use a placeholder image")
    parser.add_argument("--provider", choices=["fal", "openai"], default="fal", help="Image generation provider (default: fal)")
    args = parser.parse_args()

    plan_path = Path(args.plan).expanduser().resolve()
    if not plan_path.exists():
        print(f"Plan not found: {plan_path}", file=sys.stderr)
        return 2
    plan = json.loads(plan_path.read_text())

    needs_api = any(s.get("mode", "ai") == "ai" for s in plan.get("slides", []))
    if not args.dry_run and needs_api:
        if args.provider == "fal" and not os.environ.get("FAL_KEY"):
            print("FAL_KEY not set. Export it: export FAL_KEY=keyid:secret", file=sys.stderr)
            return 2
        if args.provider == "openai" and not os.environ.get("OPENAI_API_KEY"):
            print("OPENAI_API_KEY not set.", file=sys.stderr)
            return 2

    out_folder_str = plan.get("output_folder", "slideshow_out")
    out_dir = Path(out_folder_str).expanduser()
    if not out_dir.is_absolute():
        out_dir = plan_path.parent / out_folder_str
    out_dir.mkdir(parents=True, exist_ok=True)
    font_override = plan.get("font_override", "")

    only: set[int] | None = None
    if args.only:
        only = {int(x) for x in args.only.split(",") if x.strip()}

    slides = plan["slides"]
    failed: list[int] = []

    for slide in slides:
        n = slide["slide_number"]
        if only is not None and n not in only:
            continue
        out_path = out_dir / f"slide_{n:02d}.jpg"
        print(f"[{n}/{len(slides)}] Generating: {slide['hook'][:60]}")
        try:
            build_slide(slide, args.provider, out_path, args.dry_run, font_override)
            print(f"  -> {out_path}")
        except Exception as e:
            print(f"  FAILED: {e}", file=sys.stderr)
            failed.append(n)
            continue
        # Rate-limit politeness
        time.sleep(1)

    # Write manifest
    manifest_path = out_dir / "manifest.txt"
    ai_count = sum(1 for s in slides if s.get("mode", "ai") == "ai")
    cover_count = len(slides) - ai_count
    manifest_lines = [
        f"Book: {plan.get('book_title', '')}",
        f"Author: {plan.get('author', '')}",
        f"Genre: {plan.get('genre', '')}",
        f"Slides: {len(slides)} ({ai_count} AI, {cover_count} cover)",
        f"Cost estimate: ${ai_count * 0.05:.2f}",
        "",
        "HOOKS:",
    ]
    for s in slides:
        manifest_lines.append(f"  {s['slide_number']:02d}. {s['hook']}")
    manifest_path.write_text("\n".join(manifest_lines))

    hooks_path = out_dir / "hooks.json"
    hooks_path.write_text(json.dumps(plan, indent=2))

    if failed:
        print(f"\nFailed slides: {failed}. Edit prompts and re-run with --only {','.join(map(str, failed))}", file=sys.stderr)
        return 1

    print(f"\nDone. Output: {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
