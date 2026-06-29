---
description: Turn a Scroll Stopper slideshow folder into a 9:16 TikTok-ready MP4 with Ken Burns zoom, crossfades, optional music (silent / auto-generated / your own track), and optional AI voiceover narration (ElevenLabs, if connected).
argument-hint: [slideshow-folder] [optional-music-file]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

The user wants to convert a slideshow folder (produced by `/create-slideshow`) into an MP4 video for TikTok / Reels / YouTube Shorts.

Arguments: $ARGUMENTS

### Workflow

1. **Load config** to get the output folder root and music default:

   ```bash
   python3 ${CLAUDE_PLUGIN_ROOT}/skills/slideshow-generation/scripts/config.py show
   ```

2. **Resolve the slideshow folder.** The user may give you a full path or a partial name like "Debt Marker Slideshow 1" — search under the configured `output_folder` for the matching folder.

3. **Decide music handling.** Read `music_default` from config:

   - **`silent`** — render without audio, no questions asked
   - **`free`** — search Pixabay Music for a genre-matched track and download it ($0, free for commercial use, no attribution). Save once per book at `<book-folder>/music/<genre_slug>_pixabay.mp3` and reuse across all slideshows for that book:

     ```bash
     python3 ${CLAUDE_PLUGIN_ROOT}/skills/slideshow-generation/scripts/download_pixabay_music.py --genre <genre_slug> --out "<book-folder>/music"
     ```

     If no `pixabay_api_key` is configured, prompt the user to add one (see `/scroll-stopper-setup`) or fall back to silent.

   - **`auto`** — generate a custom genre-matched instrumental via fal.ai (uses the same `FAL_KEY` as images, ~$0.04 per book). Just pass `--music auto` to the encoder (step 4): it auto-detects the book's genre from the slideshow's `hooks.json`, generates the track via `fal_music.py`, caches it once per book at `<book-folder>/music/<genre_slug>_fal.mp3`, reuses it across that book's slideshows, and falls back to silent if fal is unreachable.
   - **`byo`** — ask: "Point me at an mp3/wav/m4a for this video."
   - **`ask`** (or unset) — present all five options:

     > "How do you want to handle sound?
     > 1. **Silent MP4** — add trending audio inside TikTok after upload (best for algorithm)
     > 2. **Free Pixabay Music** — auto-search and download a genre-matched track from Pixabay's free library ($0, no attribution, commercial use OK)
     > 3. **Bring your own track** — point me at an mp3/wav/m4a
     > 4. **Auto-generate (paid)** — fal.ai writes a custom genre-matched instrumental (~$0.04, reused across this book's slideshows)
     > 5. **Royalty-free pull (manual)** — I'll recommend sources (YouTube Audio Library, TikTok's Commercial Music Library) for you to download yourself"

   For **Pixabay** (option 2 / `free`) use `download_pixabay_music.py` (above). For **auto-generate** (option 4 / `auto`) just pass `--music auto` to the encoder — no hand-written fal calls needed; `fal_music.py` owns the genre→prompt mapping (horror → dark ambient, romance → cinematic piano, cozy → quirky jazz, etc.) and accepts free-text genres.

3b. **Voiceover (optional — only offer if ElevenLabs is connected).** Read `has_elevenlabs` from config.

   - If `false` or unset → **skip silently**, don't mention voiceover.
   - If `true` → offer it:

     > "🎙️ You've got ElevenLabs connected — want an AI voiceover reading the hooks over this reel? Sound-on narration holds viewers longer on BookTok.
     > 1. **Yes** — narrate the hooks (auto-paced to the voice; music ducks underneath)
     > 2. **No** — text + music only"

   If **yes**, write a tight ~25–40s narration **script** from the slideshow's own hooks (the lines overlaid on the slides), smoothed into spoken flow and ending on the book title + CTA (e.g. "…out now."). Pass it to the encoder with `--vo-text "<script>"`. The voice defaults to the configured `elevenlabs_voice_id` (Charlotte); add `--voice-id <id>` to override. Keep it clean for TikTok — no explicit lines.

4. **Run the encoder:**

   ```bash
   python3 ${CLAUDE_PLUGIN_ROOT}/skills/slideshow-generation/scripts/slideshow_to_video.py "<folder>" [--music auto | --music "<track>"] [--vo-text "<narration script>"]
   ```

   `--music auto` generates a genre-matched fal.ai track automatically (see step 3); `--music "<file>"` uses a specific track; omit `--music` for silent.

   Default settings: 3 seconds per slide, 0.6s crossfade, 1080×1920, 30fps, H.264/AAC, alternating Ken Burns zoom-in / zoom-out per slide.
   **When `--vo-text` (or `--vo-audio`) is used:** the slideshow auto-paces so its length matches the narration (so `--duration` is ignored), background music is automatically ducked under the voice, and the final audio is loudness-normalized to ~-14 LUFS (TikTok standard). Voiceover needs ElevenLabs set up in `/scroll-stopper-setup`.

5. **Override timing if requested.** Add `--duration 2.5` for faster pacing or `--duration 4` for slower reads.

6. **Deliver.** The MP4 lands next to the slideshow folder. Open it for the user so they can preview before uploading.

### Royalty-free music sources (option 4)

- **Pixabay Music** (pixabay.com/music) — no attribution required, free commercial use
- **YouTube Audio Library** — free, attribution-optional
- **TikTok Commercial Music Library** — TikTok-safe (best if posting to TikTok anyway)
- **Epidemic Sound** — paid sub, TikTok-safe

### Edge cases

- **ffmpeg missing:** script uses `imageio-ffmpeg`'s bundled binary. If missing: `pip3 install imageio-ffmpeg`
- **Slideshow folder empty:** point the user at `/create-slideshow` first
- **One slide:** no crossfade needed; the script handles this case automatically
