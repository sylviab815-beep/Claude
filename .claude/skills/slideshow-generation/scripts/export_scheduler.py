#!/usr/bin/env python3
"""Write a scheduler-ready CSV from a slideshow plan + per-platform captions.

Supports three scheduler formats with their REAL bulk-import schemas:
  - metricool  (matches Metricool's official bulk calendar template)
  - later      (matches Later's CSV bulk schedule format)
  - buffer     (matches Buffer's bulk upload format: Text, Image URL, Tags, Posting Time, Board Name)

Each row in the output CSV = one scheduled post. To preserve platform-tuned
captions, the script writes one row per (slideshow × platform) — even for
Metricool (which CAN cross-post one row to multiple platforms via booleans),
we use one platform per row so each platform gets its own caption.

Usage:
    python3 export_scheduler.py <plan.json> --captions <captions.json> --media-url <url> [--format metricool|later|buffer]
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import config


# ---------------------------------------------------------------------------
# METRICOOL — matches the real Metricool calendar template
# ---------------------------------------------------------------------------
METRICOOL_COLUMNS = [
    "Text", "Date", "Time", "Draft",
    "Facebook", "Twitter/X", "LinkedIn", "GBP", "Instagram", "Pinterest", "TikTok", "Youtube", "Threads", "Bluesky",
    "Picture Url 1", "Picture Url 2", "Picture Url 3", "Picture Url 4", "Picture Url 5",
    "Picture Url 6", "Picture Url 7", "Picture Url 8", "Picture Url 9", "Picture Url 10",
    "Alt text picture 1", "Alt text picture 2", "Alt text picture 3", "Alt text picture 4", "Alt text picture 5",
    "Alt text picture 6", "Alt text picture 7", "Alt text picture 8", "Alt text picture 9", "Alt text picture 10",
    "Document title", "Shortener", "Video Thumbnail Url", "Video Cover Frame",
    "Twitter/X Can reply", "Twitter/X Type", "Twitter/X Poll Duration minutes",
    "Twitter/X Poll Option 1", "Twitter/X Poll Option 2", "Twitter/X Poll Option 3", "Twitter/X Poll Option 4",
    "Pinterest Board", "Pinterest Pin Title", "Pinterest Pin Link", "Pinterest Pin New Format",
    "Instagram Post Type", "Instagram Show Reel On Feed",
    "Youtube Video Title", "Youtube Video Type", "Youtube Video Privacy", "Youtube video for kids",
    "Youtube Video Category", "Youtube Video Tags", "Youtube playlist",
    "GBP Post Type",
    "Facebook Post Type", "Facebook Title",
    "First Comment Text",
    "TikTok Title", "TikTok disable comments", "TikTok disable duet", "TikTok disable stitch",
    "TikTok Post Privacy", "TikTok Branded Content", "TikTok Your Brand", "TikTok Auto Add Music",
    "TikTok Photo Cover Index",
    "TikTok musicId", "TikTok music title", "TikTok music author", "TikTok music previewUrl",
    "TikTok music thumbnailUrl", "TikTok music soundVolume", "TikTok music originalVolume",
    "TikTok music startMillis", "TikTok music endMillis", "TikTok Ai generated content",
    "LinkedIn Type", "LinkedIn Poll Question", "LinkedIn Poll Option 1", "LinkedIn Poll Option 2",
    "LinkedIn Poll Option 3", "LinkedIn Poll Option 4", "LinkedIn Poll Duration",
    "LinkedIn Show link preview", "LinkedIn Images as Carousel",
    "Threads Reply Control", "Threads Is Spoiler", "Threads Post Type",
    "Brand name",
]

METRICOOL_PLATFORM_COLUMN = {
    "TikTok": "TikTok",
    "Instagram": "Instagram",
    "Instagram Reels": "Instagram",
    "YouTube": "Youtube",
    "YouTube Shorts": "Youtube",
    "Facebook": "Facebook",
    "Facebook Reels": "Facebook",
    "Pinterest": "Pinterest",
    "Pinterest Idea Pins": "Pinterest",
    "Twitter": "Twitter/X",
    "X": "Twitter/X",
    "LinkedIn": "LinkedIn",
    "Threads": "Threads",
    "Bluesky": "Bluesky",
    "GBP": "GBP",
}

# All boolean platform columns Metricool expects
METRICOOL_BOOLEAN_COLS = ["Facebook", "Twitter/X", "LinkedIn", "GBP", "Instagram", "Pinterest", "TikTok", "Youtube", "Threads", "Bluesky"]


def metricool_row(*, plan, platform_label, caption, media_url, sid, handle):
    target_col = METRICOOL_PLATFORM_COLUMN.get(platform_label)
    if not target_col:
        return None  # skip platforms Metricool doesn't support

    row = {col: "" for col in METRICOOL_COLUMNS}
    now = datetime.now()
    row["Text"] = caption
    row["Date"] = now.strftime("%Y-%m-%d")
    row["Time"] = "12:00:00"
    row["Draft"] = "false"

    # All platforms false except the target
    for col in METRICOOL_BOOLEAN_COLS:
        row[col] = "true" if col == target_col else "false"

    # Media — for video, we put the direct MP4 URL in Picture Url 1.
    # Metricool will detect video by extension and route accordingly.
    row["Picture Url 1"] = media_url

    # Per-platform extras
    if target_col == "Pinterest":
        # Pinterest needs a board (customer fills in if blank) and pin title (use first line of caption)
        first_line = caption.split("\n", 1)[0][:100]
        row["Pinterest Board"] = ""  # leave blank — customer fills
        row["Pinterest Pin Title"] = first_line
        row["Pinterest Pin New Format"] = "false"
    elif target_col == "Instagram":
        row["Instagram Post Type"] = "REEL"
        row["Instagram Show Reel On Feed"] = "true"
    elif target_col == "Youtube":
        first_line = caption.split("\n", 1)[0][:100]
        row["Youtube Video Title"] = first_line
        row["Youtube Video Type"] = "SHORT"
        row["Youtube Video Privacy"] = "PUBLIC"
        row["Youtube video for kids"] = "false"
        row["Youtube Video Category"] = "PEOPLE_BLOGS"
    elif target_col == "Facebook":
        row["Facebook Post Type"] = "REEL"
    elif target_col == "TikTok":
        row["TikTok disable comments"] = "false"
        row["TikTok disable duet"] = "false"
        row["TikTok disable stitch"] = "false"
        row["TikTok Post Privacy"] = "PUBLIC_TO_EVERYONE"
        row["TikTok Branded Content"] = "false"
        row["TikTok Your Brand"] = "false"
        row["TikTok Auto Add Music"] = "false"
        row["TikTok Ai generated content"] = "false"

    return row


# ---------------------------------------------------------------------------
# BUFFER — matches Buffer's bulk upload format
# ---------------------------------------------------------------------------
# Columns per Buffer's bulk uploader: Text, Image URL, Tags, Posting Time, Board Name (Pinterest only)
BUFFER_COLUMNS = ["Text", "Image URL", "Tags", "Posting Time", "Board Name"]


def extract_hashtags(text: str) -> str:
    tags = re.findall(r"#\w+", text)
    # Strip # for Buffer's tag column (commas separated)
    return ", ".join(t.lstrip("#") for t in tags)


def extract_link_from_caption(text: str) -> str:
    m = re.search(r"https?://\S+", text)
    return m.group(0) if m else ""


def buffer_row(*, plan, platform_label, caption, media_url, sid, handle):
    return {
        "Text": caption,
        "Image URL": media_url,
        "Tags": extract_hashtags(caption),
        "Posting Time": "",  # leave blank — Buffer auto-schedules to next slot, or customer fills
        "Board Name": "" if platform_label not in ("Pinterest", "Pinterest Idea Pins") else "",
    }


# ---------------------------------------------------------------------------
# LATER — matches Later's bulk CSV schedule format
# ---------------------------------------------------------------------------
LATER_COLUMNS = ["Scheduled Time", "Caption", "Media URL", "Profile", "Label"]
LATER_PLATFORMS = {"TikTok", "Instagram", "Instagram Reels", "Facebook", "Facebook Reels", "Pinterest", "Pinterest Idea Pins", "YouTube", "YouTube Shorts"}


def later_row(*, plan, platform_label, caption, media_url, sid, handle):
    if platform_label not in LATER_PLATFORMS:
        return None
    now = datetime.now()
    return {
        "Scheduled Time": now.strftime("%Y-%m-%d %H:%M"),
        "Caption": caption,
        "Media URL": media_url,
        "Profile": handle or platform_label,
        "Label": sid,
    }


# ---------------------------------------------------------------------------
# HOOTSUITE — matches Hootsuite's bulk Composer CSV
# ---------------------------------------------------------------------------
# Hootsuite's bulk upload: Date (YYYY-MM-DD HH:MM, with optional tz), Message, Link URL
# Plus optional: Image URL (only via Hootsuite's image-supporting bulk template)
HOOTSUITE_COLUMNS = ["Date", "Message", "Link", "Image URL", "Profile"]
HOOTSUITE_PLATFORMS = {"TikTok", "Instagram", "Instagram Reels", "Facebook", "Facebook Reels", "YouTube", "YouTube Shorts", "Twitter", "X", "LinkedIn", "Pinterest", "Pinterest Idea Pins", "Threads"}


def hootsuite_row(*, plan, platform_label, caption, media_url, sid, handle):
    if platform_label not in HOOTSUITE_PLATFORMS:
        return None
    now = datetime.now()
    return {
        "Date": now.strftime("%Y-%m-%d %H:%M"),
        "Message": caption,
        "Link": extract_link_from_caption(caption),
        "Image URL": media_url,
        "Profile": handle or platform_label,
    }


# ---------------------------------------------------------------------------
# Schema registry
# ---------------------------------------------------------------------------
SCHEMAS = {
    "metricool": {
        "filename_default": "metricool-import.csv",
        "columns": METRICOOL_COLUMNS,
        "row_builder": metricool_row,
        "tip": "Metricool: Planning → Bulk Upload → drop the CSV. Edit Date/Time per row before importing. Verify the Picture Url 1 video resolves; Metricool may require uploading larger MP4s manually for some platforms.",
    },
    "later": {
        "filename_default": "later-import.csv",
        "columns": LATER_COLUMNS,
        "row_builder": later_row,
        "tip": "Later: Schedule → Bulk Schedule → CSV Upload. Edit Scheduled Time per row before uploading.",
    },
    "buffer": {
        "filename_default": "buffer-import.csv",
        "columns": BUFFER_COLUMNS,
        "row_builder": buffer_row,
        "tip": "Buffer: Settings → Bulk Upload → CSV. Tags are pulled from the caption hashtags. Posting Time blank = Buffer auto-schedules to your next slot.",
    },
    "hootsuite": {
        "filename_default": "hootsuite-import.csv",
        "columns": HOOTSUITE_COLUMNS,
        "row_builder": hootsuite_row,
        "tip": "Hootsuite: Publisher → Bulk Composer → Upload CSV. Hootsuite's image/video support varies by plan tier — verify with one row before bulk import.",
    },
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("plan", help="Path to slideshow plan JSON")
    ap.add_argument("--captions", required=True, help="Path to captions JSON ({platform: caption})")
    ap.add_argument("--media-url", default="", help="Direct media URL (Dropbox ?dl=1) for the rendered MP4")
    ap.add_argument("--format", choices=list(SCHEMAS.keys()), default=None, help="Scheduler format (default: from config)")
    ap.add_argument("--out", default="", help="Output CSV path (default: <output_folder>/<scheduler>-import.csv)")
    args = ap.parse_args()

    cfg = config.load()
    scheduler = (args.format or cfg.get("default_scheduler") or "metricool").lower()
    if scheduler not in SCHEMAS:
        print(f"ERROR: unknown scheduler '{scheduler}'. Choose: {list(SCHEMAS.keys())}", file=sys.stderr)
        return 2
    schema = SCHEMAS[scheduler]

    plan = json.loads(Path(args.plan).read_text())
    captions = json.loads(Path(args.captions).read_text())

    if args.out:
        out_csv = Path(args.out).expanduser()
    else:
        cfg_path = cfg.get("scheduler_csv_path", "").strip()
        out_csv = Path(cfg_path).expanduser() if cfg_path else Path(cfg["output_folder"]).expanduser() / schema["filename_default"]
    out_csv.parent.mkdir(parents=True, exist_ok=True)

    new_file = not out_csv.exists()

    sid = (
        f"{plan.get('author', 'unk')}__{plan.get('book_title', 'unk')}__"
        f"SS{plan.get('slideshow_number', 0):02d}"
    ).replace(" ", "_")
    handles = cfg.get("social_handles", {}) or {}

    rows = []
    for platform_label in cfg.get("platforms", []):
        if platform_label not in captions:
            continue
        row = schema["row_builder"](
            plan=plan,
            platform_label=platform_label,
            caption=captions[platform_label],
            media_url=args.media_url,
            sid=sid,
            handle=handles.get(platform_label, ""),
        )
        if row is None:
            print(f"  [skip] {scheduler} doesn't support '{platform_label}' — row skipped", file=sys.stderr)
            continue
        rows.append(row)

    with out_csv.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=schema["columns"], extrasaction="ignore")
        if new_file:
            w.writeheader()
        for r in rows:
            w.writerow(r)

    print(f"\nWrote {len(rows)} rows in {scheduler.upper()} format to:\n  {out_csv}")
    print(f"\n{schema['tip']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
