---
description: Generate 9:16 Scroll Stopper slideshows from a manuscript — AI images, your book cover, or hybrid mix — with genre-aware text hooks baked in.
argument-hint: [manuscript-file] [number-of-slideshows] [slides-per-slideshow] [--mode ai|cover|hybrid] [--cover path]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

Read the slideshow-generation skill at `${CLAUDE_PLUGIN_ROOT}/skills/slideshow-generation/SKILL.md` and follow its complete workflow.

The user's arguments: $ARGUMENTS

### Before anything else: load config

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/slideshow-generation/scripts/config.py show
```

If the config doesn't exist, tell the user to run `/scroll-stopper-setup` first. Don't proceed without config.

Use the config's `output_folder` as the destination root, `default_mode` as the mode unless overridden by `--mode`, and `font_override` / `use_genre_fonts` for typography.

### Mode handling

Three modes are supported. If the user didn't specify, use `default_mode` from config. Always confirm the mode with the user before generating:

- **`ai`** — every slide is a fal.ai Flux Pro image (~$0.05/slide). The original Scroll Stopper experience.
- **`cover`** — every slide uses the user's book cover, with a different hook overlaid each time. $0/slide. Need the cover path. If `--cover` not provided, ask: "Where's the cover image for this book?"
- **`hybrid`** — slide 1 = book cover, slides 2-N = AI. Need the cover path AND fal.ai will be called for the rest.

For cover/hybrid modes, in each slide's plan JSON set `"mode": "cover"` and `"cover_path": "<path>"`. For AI slides, set `"mode": "ai"` and `image_prompt`.

### Confirm with the user

- Author / pen name (extract from manuscript or ask)
- Book title (extract or ask)
- **Pairing for romance** (MM / FF / MF / RH / monster / etc.) — see Phase 1.5 in SKILL.md, this is required
- Number of slideshows (ask if not provided)
- Slides per slideshow (ask if not provided)
- Mode (use config default, confirm)
- Cover path if cover/hybrid (ask if not provided)
- **Buy link for this book** (if `auto_generate_captions` is true in config) — use `buy_link_template` from config to suggest format

### After hooks approved + plans built — generate captions

If `cfg["auto_generate_captions"]` is true:

1. Read `references/caption-templates.md`
2. For each (slideshow × platform in `cfg["platforms"]`), generate a caption matching that platform's format
3. Use the SHARPEST hook from the slideshow as the opening line
4. Inject the buy link, CTA, and matching social handle
5. Pull genre + platform-appropriate hashtags from `references/caption-templates.md`
6. **Match pronouns to the confirmed pairing**
7. Save to `/tmp/scroll_stopper_plans/<Author>_<Title>_NN_captions.json`
8. Show all platform captions to user, allow edits/swaps
9. After all slideshows have been rendered AND uploaded to Dropbox, run:

   ```bash
   python3 ${CLAUDE_PLUGIN_ROOT}/skills/slideshow-generation/scripts/export_scheduler.py \
     /tmp/scroll_stopper_plans/<Author>_<Title>_01.json \
     --captions /tmp/scroll_stopper_plans/<Author>_<Title>_01_captions.json \
     --media-url "<dropbox-url>"
   ```

   for each slideshow. The Metricool-ready CSV gets appended each time.

### After generation: log to CSV

Once the slideshows render successfully, log each one:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/slideshow-generation/scripts/log_run.py "<plan-path>"
```

Then tell the user the CSV path and that they can edit `post_date`/`status` columns as they schedule.

### Output path

Final output goes to: `<output_folder from config>/<Pen Name>/<Book Title>/Slideshow-NN/`. Each slideshow gets its own folder with its own hook set.
