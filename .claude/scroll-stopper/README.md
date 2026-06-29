# Scroll Stopper — persistent config (Claude Code on the web)

This container is ephemeral, so `~/.scroll-stopper/config.json` does not survive a
session. This folder persists your settings via the repo and keeps secrets out of git.

## How it works
- `config.json` — your NON-SECRET settings, tracked in the repo (persists).
- `sync_config.py init` — runs from a SessionStart hook (`.claude/settings.json`).
  Writes `~/.scroll-stopper/config.json` from `config.json`, overlaying secrets
  from environment variables.
- `sync_config.py save` — after you run `/scroll-stopper-setup`, copies your new
  settings back to `config.json` with all API keys blanked, so they can be committed.

## Secrets = environment variables (set in your remote environment settings)
Set these in the Claude Code on the web environment (NOT in the repo):
- `FAL_KEY` — fal.ai / FLUX image generation
- `OPENAI_API_KEY` — DALL·E image generation (if used)
- `PIXABAY_API_KEY` — Pixabay music
- `ELEVENLABS_API_KEY` — ElevenLabs voiceover
- `DROPBOX_TOKEN` — Dropbox upload

The init hook injects PIXABAY/ELEVENLABS/DROPBOX values into the materialized
config each session; FAL_KEY and OPENAI_API_KEY are read straight from the env by
the generation scripts.

## After running /scroll-stopper-setup
```
python3 .claude/scroll-stopper/sync_config.py save
git add .claude/scroll-stopper/config.json && git commit -m "Update Scroll Stopper settings" && git push
```
(Ask me and I'll do this for you.)
