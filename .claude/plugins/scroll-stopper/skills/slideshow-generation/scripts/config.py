#!/usr/bin/env python3
"""Scroll Stopper config helper.

Reads / writes ~/.scroll-stopper/config.json. The setup command writes here;
build_slideshow.py and slideshow_to_video.py read from here for output paths,
default mode, font overrides, and CSV log location/columns.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

CONFIG_DIR = Path.home() / ".scroll-stopper"
CONFIG_PATH = CONFIG_DIR / "config.json"

DEFAULTS = {
    "output_folder": str(Path.home() / "ScrollStopper"),
    "library_folder": "",
    "default_mode": "ai",
    "platforms": ["TikTok", "Instagram", "YouTube Shorts"],
    "csv_log_path": str(Path.home() / "ScrollStopper" / "scroll-stopper-log.csv"),
    "csv_columns": [
        "date_generated",
        "pen_name",
        "book_title",
        "genre",
        "slideshow_number",
        "slide_count",
        "mode",
        "platforms",
        "output_path",
        "post_date",
        "status",
        "hook_summary",
        "dropbox_url",
    ],
    "font_override": "",
    "use_genre_fonts": True,
    "music_default": "silent",
    "pixabay_api_key": "",
    "dropbox_token": "",
    "dropbox_folder": "/Scroll-Stopper/Videos",
    "default_cta": "Out now in Kindle Unlimited",
    "buy_link_template": "",
    "social_handles": {
        "TikTok": "",
        "Instagram": "",
        "Facebook": "",
        "YouTube Shorts": "",
        "Pinterest": "",
    },
    "auto_generate_captions": True,
    "default_scheduler": "metricool",
    "scheduler_csv_path": "",
    # Optional integrations (asked at setup, never required)
    "has_elevenlabs": False,
    "elevenlabs_api_key": "",
    "elevenlabs_voice_id": "XB0fDUnXU5powFXDhCwa",  # Charlotte — warm sultry female narration
    "has_metricool": True,
    "metricool_mcp": False,  # Metricool MCP connected in Claude → enables direct scheduling
}


def load() -> dict:
    if not CONFIG_PATH.exists():
        return dict(DEFAULTS)
    try:
        cfg = json.loads(CONFIG_PATH.read_text())
    except json.JSONDecodeError:
        return dict(DEFAULTS)
    merged = dict(DEFAULTS)
    merged.update(cfg)
    return merged


def save(cfg: dict) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_text(json.dumps(cfg, indent=2))


def is_configured() -> bool:
    return CONFIG_PATH.exists()


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "show":
        print(json.dumps(load(), indent=2))
    elif len(sys.argv) > 1 and sys.argv[1] == "path":
        print(CONFIG_PATH)
    else:
        print(f"Config path: {CONFIG_PATH}")
        print(f"Configured: {is_configured()}")
