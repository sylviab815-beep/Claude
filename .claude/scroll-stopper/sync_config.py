#!/usr/bin/env python3
"""Scroll Stopper config persistence bridge for Claude Code on the web.

The container is ephemeral, so ~/.scroll-stopper/config.json does not survive a
session. This bridges the repo-tracked non-secret config with environment-held
secrets.

  init  : repo config.json  ->  ~/.scroll-stopper/config.json, overlaying secrets
          from environment variables. Runs from a SessionStart hook.
  save  : ~/.scroll-stopper/config.json  ->  repo config.json, with ALL secret
          fields blanked, so user settings made via /scroll-stopper-setup persist
          without committing API keys. Run this, then commit, after setup.

Secret env vars -> config keys:
  PIXABAY_API_KEY    -> pixabay_api_key
  ELEVENLABS_API_KEY -> elevenlabs_api_key (also sets has_elevenlabs=true)
  DROPBOX_TOKEN      -> dropbox_token
(FAL_KEY and OPENAI_API_KEY are read directly from the environment by the
generation scripts, so they never touch config.json.)
"""
from __future__ import annotations
import json, os, sys
from pathlib import Path

SECRET_FIELDS = ["pixabay_api_key", "elevenlabs_api_key", "dropbox_token"]
ENV_TO_FIELD = {
    "PIXABAY_API_KEY": "pixabay_api_key",
    "ELEVENLABS_API_KEY": "elevenlabs_api_key",
    "DROPBOX_TOKEN": "dropbox_token",
}

REPO_CONFIG = Path(__file__).resolve().parent / "config.json"
HOME_DIR = Path.home() / ".scroll-stopper"
HOME_CONFIG = HOME_DIR / "config.json"


def _expand(cfg: dict) -> dict:
    for k in ("output_folder", "csv_log_path", "library_folder", "scheduler_csv_path"):
        v = cfg.get(k)
        if isinstance(v, str) and v.startswith("~"):
            cfg[k] = str(Path(v).expanduser())
    return cfg


def init() -> None:
    base = json.loads(REPO_CONFIG.read_text()) if REPO_CONFIG.exists() else {}
    # Preserve any in-session edits already in the home file.
    if HOME_CONFIG.exists():
        try:
            base.update({k: v for k, v in json.loads(HOME_CONFIG.read_text()).items() if v not in ("", None)})
        except json.JSONDecodeError:
            pass
    # Overlay secrets from the environment (authoritative for secret fields).
    for env, field in ENV_TO_FIELD.items():
        val = os.environ.get(env, "").strip()
        if val:
            base[field] = val
            if field == "elevenlabs_api_key":
                base["has_elevenlabs"] = True
    base = _expand(base)
    HOME_DIR.mkdir(parents=True, exist_ok=True)
    HOME_CONFIG.write_text(json.dumps(base, indent=2))
    present = [e for e in ENV_TO_FIELD if os.environ.get(e, "").strip()]
    for e in ("FAL_KEY", "OPENAI_API_KEY"):
        if os.environ.get(e, "").strip():
            present.append(e)
    print(f"[scroll-stopper] config -> {HOME_CONFIG}; secrets from env: {present or 'none'}")


def save() -> None:
    if not HOME_CONFIG.exists():
        print("[scroll-stopper] no ~/.scroll-stopper/config.json to save", file=sys.stderr)
        sys.exit(1)
    cfg = json.loads(HOME_CONFIG.read_text())
    for f in SECRET_FIELDS:           # never commit secrets
        cfg[f] = ""
    REPO_CONFIG.write_text(json.dumps(cfg, indent=2) + "\n")
    print(f"[scroll-stopper] saved settings to {REPO_CONFIG} (secrets stripped). Commit to persist.")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "init"
    (save if mode == "save" else init)()
