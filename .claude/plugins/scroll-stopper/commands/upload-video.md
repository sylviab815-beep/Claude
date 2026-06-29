---
description: Upload a Scroll Stopper MP4 (or a whole book's slideshows) to Dropbox and get back Metricool-ready direct URLs to paste into your bulk scheduling CSV — or, if the Metricool MCP is connected, schedule them straight to your calendar.
argument-hint: [mp4-file or slideshow-folder or book-folder]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

The user wants to upload one or more rendered MP4s to Dropbox so they can drop the URLs into Metricool's bulk CSV. Google Drive links don't work with Metricool — Dropbox does, when the URL ends in `?dl=1` (handled automatically here).

Arguments: $ARGUMENTS

### Workflow

1. **Load config and verify Dropbox token:**

   ```bash
   python3 ${CLAUDE_PLUGIN_ROOT}/skills/slideshow-generation/scripts/config.py show
   ```

   If `dropbox_token` is empty, tell the user to run `/scroll-stopper-setup` again (or paste their token directly into `~/.scroll-stopper/config.json`). Walk them to https://www.dropbox.com/developers/apps if they need to generate one — see INSTALL.md for the step-by-step.

2. **Resolve what they want to upload:**

   - **A single MP4 file** → upload that one
   - **A `Slideshow-NN/` folder** → find any `.mp4` inside and upload it
   - **A book folder** (e.g., `<output_folder>/Pen Name/Book Title/`) → upload every `.mp4` under it

   Use the `output_folder` from config as the search root if the user gave a partial name.

3. **Verify the dropbox SDK is installed:**

   ```bash
   python3 -c "import dropbox" 2>/dev/null || pip3 install dropbox
   ```

4. **For each MP4, upload and capture the URL:**

   ```bash
   python3 ${CLAUDE_PLUGIN_ROOT}/skills/slideshow-generation/scripts/upload_dropbox.py "<path-to-file>.mp4" --dest "/Scroll-Stopper/<Pen Name>/<Book Title>"
   ```

   The script prints the Metricool-ready URL (with `?dl=1`) on the last line. Capture each one.

5. **Update the CSV log** for each uploaded video. Use the `dropbox_url` column (add it to `csv_columns` if missing — read the config, append to the list, save). For each row already logged for that slideshow, fill in the `dropbox_url`. If you need to re-log because there's no matching row yet, run:

   ```bash
   python3 ${CLAUDE_PLUGIN_ROOT}/skills/slideshow-generation/scripts/log_run.py "<plan.json>" --dropbox-url "<url>"
   ```

5b. **Direct scheduling (optional — only if the Metricool MCP is connected).** Read `metricool_mcp` from config.

   - If `false` → skip; the Dropbox URLs + CSV are the delivery (existing flow).
   - If `true` → **verify the MCP is actually reachable before offering it** (the flag could be stale if the connector was removed since setup). Do a quick `getBrandSettings` probe; if the tools are missing or the call errors, don't promise direct scheduling — tell the user the Metricool MCP looks disconnected, fall back to the Dropbox URLs + CSV, and suggest re-running `/scroll-stopper-setup`. If the probe succeeds, offer it:

     > "🚀 You've got the Metricool MCP connected — want me to schedule these straight to your Metricool calendar instead of importing the CSV by hand?
     > 1. **Yes, schedule them** — pick the pen name + I'll queue each reel
     > 2. **No, just give me the URLs/CSV**"

   If **yes**, use the Metricool MCP directly (the buyer's Claude has the tools — search them if needed):
   1. `getBrandSettings` → list brands; match the pen name to its `blogId`.
   2. For slots: ask the user for date/times, or call `getBestTimeToPostByNetwork` and propose the top slots (prefer ~1/day cadence over hoarding the single peak).
   3. For each reel, `createScheduledPost` with:
      - `media`: the **Dropbox `?dl=1` URL** from step 4 (already public — no Drive-sharing issue).
      - `text`: the caption Scroll Stopper generated for that platform (hook → `<Title> by <Author> — available on Amazon.` → hashtags; no links).
      - `providers`: the brand's networks (e.g. `[{"network":"tiktok"}]`), `publicationDate` with the brand timezone, and `tiktokData`/etc.
   4. **Verify** each created post's returned `media` URL ends in **`.mp4`** (not `.html`) and status is `PENDING`, then report the planner link.

   Still also fill in the CSV (step 5) as a backup record.

6. **Show the user a clean table of results:**

   | # | Slideshow | Dropbox URL |
   |---|---|---|
   | 1 | Debt Marker - Slideshow-01 | https://www.dropbox.com/.../...?dl=1 |
   | 2 | Debt Marker - Slideshow-02 | https://www.dropbox.com/.../...?dl=1 |

   Then tell them: "Paste these URLs into the `Media URL` column of your Metricool CSV. The CSV log at `<csv_log_path>` already has these recorded for you."

### Edge cases

- **File too large** (Dropbox free is 50GB total / single file 50GB) — unlikely for a 16-second 9:16 reel (~5-15MB) but flag if the file is over 1GB.
- **Auth error** — token likely expired or scoped wrong. Tell the user to regenerate at https://www.dropbox.com/developers/apps and update config.
- **Same filename uploaded twice** — Dropbox API uses `WriteMode.overwrite` so it replaces in-place. The shared link should still work; the script handles `shared_link_already_exists` automatically.
