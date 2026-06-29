#!/usr/bin/env python3
"""Append a row to the Scroll Stopper CSV log.

Usage:
    python3 log_run.py <plan.json> [--post-date YYYY-MM-DD] [--status posted|scheduled|draft]
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import config


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("plan", help="Path to slideshow plan JSON")
    ap.add_argument("--post-date", default="", help="Date you plan to post (YYYY-MM-DD)")
    ap.add_argument("--status", default="generated", help="generated|scheduled|posted")
    ap.add_argument("--dropbox-url", default="", help="Metricool-ready Dropbox URL for the rendered MP4")
    args = ap.parse_args()

    cfg = config.load()
    plan = json.loads(Path(args.plan).read_text())
    csv_path = Path(cfg["csv_log_path"]).expanduser()
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    columns = cfg["csv_columns"]
    new_file = not csv_path.exists()

    hooks = [s.get("hook", "") for s in plan.get("slides", [])]
    hook_summary = " | ".join(hooks[:3]) + (" ..." if len(hooks) > 3 else "")

    row_data = {
        "date_generated": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "pen_name": plan.get("author", ""),
        "book_title": plan.get("book_title", ""),
        "genre": plan.get("genre", ""),
        "slideshow_number": plan.get("slideshow_number", ""),
        "slide_count": len(plan.get("slides", [])),
        "mode": plan.get("mode", "ai"),
        "platforms": ", ".join(cfg.get("platforms", [])),
        "output_path": plan.get("output_folder", ""),
        "post_date": args.post_date,
        "status": args.status,
        "hook_summary": hook_summary,
        "dropbox_url": args.dropbox_url,
    }

    with csv_path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns, extrasaction="ignore")
        if new_file:
            writer.writeheader()
        writer.writerow(row_data)

    print(f"Logged to {csv_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
