#!/usr/bin/env python3
"""Generate a genre-matched instrumental track via fal.ai.

Uses the same FAL_KEY the plugin already uses for images — no extra account or
key needed. Produces a royalty-free, no-vocals background track sized for a
short reel. Tracks are cached to <book_folder>/music/<genre_slug>_fal.mp3 so
they're reused across all slideshows for that book (consistent sonic identity).

Usage:
    python3 fal_music.py --genre "horror fairy tale" --out /path/to/book/music/track.mp3
    python3 fal_music.py --genre dark_romance --out track.mp3 --duration 22 --force

Prints the final file path on the last stdout line on success.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
import urllib.request
from pathlib import Path

# Keyword → music prompt. The genre string is scanned for these keywords in
# order; first hit wins. Keeps free-text genres ("horror fairy tale") working
# alongside the plugin's style keys ("dark_romance").
GENRE_MUSIC_PROMPTS: list[tuple[str, str]] = [
    ("horror",      "dark ambient horror instrumental, eerie detuned music box, low cello drone, unsettling tension, sparse, cinematic, no vocals"),
    ("dark_stays",  "dark ambient horror instrumental, eerie detuned music box, low cello drone, unsettling tension, sparse, cinematic, no vocals"),
    ("monster",     "epic dramatic orchestral fantasy instrumental, sweeping strings, primal percussion, cinematic, no vocals"),
    ("paranormal",  "gothic moonlit strings instrumental, ethereal choir pads, mysterious, haunting, cinematic, no vocals"),
    ("suspense",    "tense thriller noir instrumental, pulsing low strings, ticking suspense, cinematic, no vocals"),
    ("thriller",    "tense thriller noir instrumental, pulsing low strings, ticking suspense, cinematic, no vocals"),
    ("mafia",       "dark brooding cinematic instrumental, low piano, ominous strings, slow tension, no vocals"),
    ("spicy",       "playful flirty indie pop instrumental, warm upbeat groove, sensual, no vocals"),
    ("romcom",      "light playful indie pop instrumental, sweet upbeat acoustic, cheerful, no vocals"),
    ("clean",       "soft acoustic indie folk instrumental, gentle guitar, sweet and light, no vocals"),
    ("cozy",        "quirky cozy jazz instrumental, light pizzicato strings, playful intrigue, no vocals"),
    ("mystery",     "quirky cozy jazz instrumental, light pizzicato strings, playful intrigue, no vocals"),
    ("sci",         "atmospheric synthwave instrumental, futuristic pads, pulsing arpeggio, cinematic, no vocals"),
    ("fantasy",     "epic dramatic orchestral fantasy instrumental, sweeping strings, cinematic, no vocals"),
    ("romance",     "emotional dark cinematic piano instrumental, brooding strings, slow tension, longing, no vocals"),
    ("dark",        "emotional dark cinematic piano instrumental, brooding strings, slow tension, no vocals"),
]
DEFAULT_PROMPT = "cinematic atmospheric instrumental, emotive, moody, no vocals"
DEFAULT_MODEL = "fal-ai/stable-audio"


def prompt_for_genre(genre: str) -> str:
    g = (genre or "").lower()
    for keyword, prompt in GENRE_MUSIC_PROMPTS:
        if keyword in g:
            return prompt
    return DEFAULT_PROMPT


def slugify(genre: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", (genre or "track").lower()).strip("_") or "track"


def generate_music(genre: str, out_path: Path, duration: float = 22.0,
                   model: str = DEFAULT_MODEL, force: bool = False) -> Path:
    """Generate (or reuse cached) a genre-matched instrumental. Returns the path.

    Raises RuntimeError on failure so callers can fall back to silent.
    """
    out_path = Path(out_path).expanduser()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if out_path.exists() and out_path.stat().st_size > 2000 and not force:
        print(f"Reusing cached track: {out_path}")
        print(out_path)
        return out_path

    if not os.environ.get("FAL_KEY"):
        raise RuntimeError("FAL_KEY not set. Export it: export FAL_KEY=keyid:secret")

    try:
        import fal_client
    except ImportError as e:
        raise RuntimeError("fal-client not installed. Run: pip3 install fal-client") from e

    prompt = prompt_for_genre(genre)
    # Models accept slightly different arg names for length; send what each wants.
    arguments: dict = {"prompt": prompt}
    if "stable-audio" in model:
        arguments.update({"seconds_total": int(max(8, duration)), "steps": 100})
    else:
        arguments.update({"duration": int(max(8, duration))})

    print(f"Generating music via {model}: {prompt[:70]}...")
    result = fal_client.subscribe(model, arguments=arguments, with_logs=False)

    url = _find_audio_url(result)
    if not url:
        raise RuntimeError(f"No audio URL in fal response: {str(result)[:200]}")
    urllib.request.urlretrieve(url, out_path)
    if out_path.stat().st_size < 2000:
        raise RuntimeError("Downloaded track is empty/too small")
    print(out_path)
    return out_path


def _find_audio_url(result) -> str | None:
    for key in ("audio_file", "audio", "output"):
        v = result.get(key) if isinstance(result, dict) else None
        if isinstance(v, dict) and v.get("url"):
            return v["url"]
        if isinstance(v, str) and v.startswith("http"):
            return v
    import json
    m = re.search(r'https?://[^\s"]+\.(?:mp3|wav|flac|m4a)', json.dumps(result))
    return m.group(0) if m else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--genre", required=True, help="Genre or style key (free text ok, e.g. 'horror fairy tale')")
    ap.add_argument("--out", required=True, help="Output mp3 path")
    ap.add_argument("--duration", type=float, default=22.0, help="Seconds of music (default 22)")
    ap.add_argument("--model", default=DEFAULT_MODEL, help=f"fal.ai audio model (default {DEFAULT_MODEL})")
    ap.add_argument("--force", action="store_true", help="Regenerate even if a cached track exists")
    args = ap.parse_args()
    try:
        generate_music(args.genre, Path(args.out), args.duration, args.model, args.force)
        return 0
    except Exception as e:
        print(f"Music generation failed: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
