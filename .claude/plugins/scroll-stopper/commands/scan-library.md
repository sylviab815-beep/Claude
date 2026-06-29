---
description: Scan the user's books library folder, detect each book's genre, and present a confirmable list before bulk slideshow generation.
argument-hint: [optional-folder-path]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

The user wants to scan their books library and see what's there with auto-detected genres. Optional argument: a folder path. Otherwise read the configured library folder.

### Workflow

1. **Load config** to get `library_folder`:

   ```bash
   python3 ${CLAUDE_PLUGIN_ROOT}/skills/slideshow-generation/scripts/config.py show
   ```

   If `library_folder` is empty AND no folder argument was passed, ask the user to point to a folder. If they want to permanently set it, suggest re-running `/scroll-stopper-setup`.

2. **Find every manuscript file** under that folder (recursive): `.docx`, `.epub`, `.pdf`.

   ```bash
   find "<library_folder>" -type f \( -name "*.docx" -o -name "*.epub" -o -name "*.pdf" \) | head -200
   ```

3. **For each book**, extract title + a genre signal from the first ~3000 words:

   ```bash
   python3 ${CLAUDE_PLUGIN_ROOT}/skills/slideshow-generation/scripts/extract_text.py "<path>" 2>/dev/null | head -c 12000
   ```

   Use the genre decision tree in `references/genre-hook-styles.md` to pick the most BookTok-marketable fit.

4. **Look for matching covers** — for each book, check the same folder for a `<title>.jpg`, `<title>.png`, `cover.jpg`, or any image file in the same dir. Note whether a cover was found.

5. **Present a table** to the user:

   ```
   | # | File | Detected Title | Detected Genre | Cover Found |
   |---|------|----------------|----------------|-------------|
   | 1 | Debt-Marker.epub | Debt Marker | dark_mm_romance | ✓ |
   | 2 | sweet-witch.docx | The Sweet Witch | paranormal_romance | — |
   ```

   Then ask:

   > "Anything to correct? You can:
   > - Confirm all (`yes` / `looks good`)
   > - Fix one: `2: cozy mystery, title is Brews and Broomsticks`
   > - Drop a row: `skip 3`
   >
   > Once confirmed, tell me which books to make slideshows for and how many slideshows × slides each."

6. **Wait for confirmation**, then run `/create-slideshow` for each selected book using the confirmed metadata. Pass the cover path along when found, so cover/hybrid modes can use it without re-prompting.

### Important

- Don't auto-generate. The user must approve genres + chosen books first.
- If you find more than 50 books, paginate or ask whether to scan everything.
