#!/usr/bin/env python3
"""Search Pixabay's free music library and download a genre-matched track.

Pixabay music is FREE for commercial use, no attribution required. No payment ever.
Get a free API key at https://pixabay.com/api/docs/  (no credit card required).

Tracks are saved to <book_folder>/music/<genre_slug>_pixabay.mp3 so they're
reused across all slideshows for that book — gives the account a consistent
sonic identity.

Usage:
    python3 download_pixabay_music.py --genre dark_romance --out /path/to/book/music
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import config

# Pixabay search keywords per genre — designed to match the vibe of each romance/genre niche
GENRE_QUERIES = {
    "dark_romance": "dark cinematic piano",
    "dark_mm": "dark cinematic piano",
    "dark_mm_romance": "dark cinematic piano",
    "monster_romance": "epic orchestral fantasy",
    "paranormal_romance": "gothic moonlight strings",
    "romantic_suspense": "tense thriller noir",
    "thriller": "tense thriller noir",
    "spicy_romcom": "playful indie pop romance",
    "clean_romcom": "soft acoustic indie folk",
    "cozy_mystery": "quirky cozy jazz",
    "dark_stays": "dark ambient horror minimal",
    "psychological_horror": "dark ambient horror minimal",
    "sci_fi": "synthwave atmospheric futuristic",
    "cozy_fantasy": "cozy acoustic warm fantasy",
    "litrpg": "cozy acoustic warm fantasy",
    "vigilante_thriller": "tense brooding electronic",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--genre", required=True, help="Genre slug from genre-hook-styles (e.g., dark_mm_romance)")
    ap.add_argument("--out", required=True, help="Output folder (e.g., /path/to/book/music)")
    ap.add_argument("--query", default="", help="Override the auto-search query")
    ap.add_argument("--min-duration", type=int, default=15, help="Minimum track length in seconds (default 15)")
    args = ap.parse_args()

    cfg = config.load()
    api_key = cfg.get("pixabay_api_key", "").strip()
    if not api_key:
        print(
            "ERROR: No Pixabay API key configured.\n"
            "Get a free one (no credit card) at https://pixabay.com/api/docs/\n"
            "Then run /scroll-stopper-setup and paste the key, or edit ~/.scroll-stopper/config.json.",
            file=sys.stderr,
        )
        return 2

    query = args.query or GENRE_QUERIES.get(args.genre, "cinematic instrumental")
    print(f"Searching Pixabay Music for: {query}")

    # Pixabay music API endpoint
    api_url = (
        "https://pixabay.com/api/?"
        + urllib.parse.urlencode({
            "key": api_key,
            "q": query,
            "media_type": "music",
            "per_page": 10,
            "safesearch": "true",
        })
    )

    try:
        with urllib.request.urlopen(api_url, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"ERROR querying Pixabay: {e}", file=sys.stderr)
        print("If you see 401/403, your API key is invalid. Regenerate at https://pixabay.com/api/docs/", file=sys.stderr)
        return 3

    hits = data.get("hits", []) or []
    # Filter by min duration
    suitable = [h for h in hits if h.get("duration", 0) >= args.min_duration]
    if not suitable:
        suitable = hits  # fall back to anything if nothing meets duration threshold

    if not suitable:
        print(f"No Pixabay music results for '{query}'. Try a different query with --query.", file=sys.stderr)
        return 4

    # Pick the first result (Pixabay sorts by popularity)
    pick = suitable[0]
    audio_url = pick.get("audio_url") or pick.get("audio") or pick.get("file")
    if not audio_url:
        # Older API shape — try previewURL
        audio_url = pick.get("previewURL")
    if not audio_url:
        print(f"ERROR: Pixabay result didn't include an audio URL. Raw: {pick}", file=sys.stderr)
        return 5

    out_dir = Path(args.out).expanduser()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{args.genre}_pixabay.mp3"

    print(f"Downloading: {pick.get('title', '<no title>')} by {pick.get('user', '<unknown>')}")
    print(f"  -> {out_path}")

    try:
        urllib.request.urlretrieve(audio_url, str(out_path))
    except Exception as e:
        print(f"ERROR downloading: {e}", file=sys.stderr)
        return 6

    print(f"\nDone. Track saved.")
    print(f"License: Pixabay Music — free for commercial use, no attribution required.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
