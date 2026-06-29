#!/usr/bin/env python3
"""Upload a video (or any file) to Dropbox and return a Metricool-ready direct URL.

The URL has `?dl=1` appended so external services (Metricool, Buffer, Hootsuite,
Make, Zapier) can fetch the raw MP4 instead of Dropbox's preview page.

Reads the Dropbox access token from ~/.scroll-stopper/config.json (key: dropbox_token).

Usage:
    python3 upload_dropbox.py <local-file> [--dest /Scroll-Stopper/Videos/]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import config


def to_direct_url(shared_url: str) -> str:
    """Convert a Dropbox shared link into a fetchable direct URL.

    Dropbox returns links like:
        https://www.dropbox.com/scl/fi/abc/file.mp4?rlkey=xyz&dl=0
    Metricool/etc. need:
        https://www.dropbox.com/scl/fi/abc/file.mp4?rlkey=xyz&dl=1
    """
    if "dl=0" in shared_url:
        return shared_url.replace("dl=0", "dl=1")
    if "dl=" not in shared_url:
        sep = "&" if "?" in shared_url else "?"
        return f"{shared_url}{sep}dl=1"
    return shared_url


def upload(local_path: Path, dest_folder: str, token: str) -> str:
    try:
        import dropbox
        from dropbox.exceptions import ApiError
        from dropbox.files import WriteMode
        from dropbox.sharing import SharedLinkSettings, RequestedVisibility
    except ImportError:
        print("ERROR: dropbox SDK not installed. Run: pip3 install dropbox", file=sys.stderr)
        sys.exit(2)

    dbx = dropbox.Dropbox(token)
    dest = f"{dest_folder.rstrip('/')}/{local_path.name}"

    file_size = local_path.stat().st_size
    chunk_size = 4 * 1024 * 1024  # 4MB

    print(f"Uploading {local_path.name} ({file_size / 1024 / 1024:.1f} MB) to Dropbox: {dest}")

    with local_path.open("rb") as f:
        if file_size <= chunk_size:
            dbx.files_upload(f.read(), dest, mode=WriteMode("overwrite"))
        else:
            session = dbx.files_upload_session_start(f.read(chunk_size))
            cursor = dropbox.files.UploadSessionCursor(session_id=session.session_id, offset=f.tell())
            commit = dropbox.files.CommitInfo(path=dest, mode=WriteMode("overwrite"))
            while f.tell() < file_size:
                if (file_size - f.tell()) <= chunk_size:
                    dbx.files_upload_session_finish(f.read(chunk_size), cursor, commit)
                else:
                    dbx.files_upload_session_append_v2(f.read(chunk_size), cursor)
                    cursor.offset = f.tell()

    # Create or fetch shared link
    try:
        link = dbx.sharing_create_shared_link_with_settings(
            dest,
            settings=SharedLinkSettings(requested_visibility=RequestedVisibility.public),
        ).url
    except ApiError as e:
        # Already shared — list and use the existing one
        if "shared_link_already_exists" in str(e):
            links = dbx.sharing_list_shared_links(path=dest, direct_only=True).links
            if not links:
                print(f"ERROR: file uploaded but no shared link could be created/found: {e}", file=sys.stderr)
                sys.exit(3)
            link = links[0].url
        else:
            raise

    return to_direct_url(link)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("file", help="Local file path to upload (typically the .mp4)")
    ap.add_argument("--dest", default="/Scroll-Stopper/Videos", help="Dropbox destination folder")
    args = ap.parse_args()

    cfg = config.load()
    token = cfg.get("dropbox_token", "").strip()
    if not token:
        print(
            "ERROR: No Dropbox token configured.\n"
            "Run /scroll-stopper-setup and add your Dropbox access token, OR\n"
            "edit ~/.scroll-stopper/config.json and set 'dropbox_token'.\n"
            "How to generate a token: https://www.dropbox.com/developers/apps",
            file=sys.stderr,
        )
        return 2

    local = Path(args.file).expanduser().resolve()
    if not local.exists():
        print(f"ERROR: File not found: {local}", file=sys.stderr)
        return 2

    try:
        url = upload(local, args.dest, token)
    except Exception as e:
        print(f"ERROR uploading: {e}", file=sys.stderr)
        return 3

    print(f"\nMetricool-ready URL:\n{url}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
