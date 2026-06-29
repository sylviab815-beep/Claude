---
description: Generate a single-row test CSV using your real config + a sample book, so you can validate the import flow in your scheduler BEFORE running 50+ rows.
argument-hint: (no arguments)
allowed-tools: Read, Write, Edit, Bash, Glob
---

The user wants to validate that their scheduler accepts the Scroll Stopper CSV format before running a real batch. Most refunds and "stuck" support questions come from people doing 50 rows of bad data because they didn't test 1 row first.

### Workflow

1. **Load config:**

   ```bash
   python3 ${CLAUDE_PLUGIN_ROOT}/skills/slideshow-generation/scripts/config.py show
   ```

   Confirm `default_scheduler`, `platforms`, `social_handles`, and `dropbox_token` (if set) are populated. If `default_scheduler` is empty, tell the user to run `/scroll-stopper-setup`.

2. **Generate a test plan + captions** using their real config but a fake demo book ("Test Book" by `<their pen name or "Test Author">`). Write to `/tmp/scroll_stopper_plans/_test_plan.json`:

   ```json
   {
     "book_title": "Test Book",
     "author": "<pen name from setup or 'Test Author'>",
     "genre": "dark_mm_romance",
     "pairing": "MM",
     "slideshow_number": 99,
     "mode": "ai",
     "output_folder": "/tmp/scroll_stopper_test",
     "slides": [
       {"slide_number": 1, "hook": "This is a Scroll Stopper import test."}
     ]
   }
   ```

   And `/tmp/scroll_stopper_plans/_test_captions.json` with one short caption per platform in the user's config — keep them genuinely brief and label them clearly so the user can spot them in their scheduler:

   ```json
   {
     "TikTok": "🧪 Scroll Stopper test post — please delete.\n\n#test #scrollstopper",
     "Instagram": "🧪 Scroll Stopper test post — please delete after verifying it appears here.\n\n#test #scrollstopper",
     "...": "..."
   }
   ```

3. **Try uploading a test video** to Dropbox if `dropbox_token` is set. If not, skip and use a public placeholder MP4 URL: `https://www.w3schools.com/html/mov_bbb.mp4`

   ```bash
   # If a real test MP4 exists locally, upload it. Otherwise skip and use placeholder.
   python3 ${CLAUDE_PLUGIN_ROOT}/skills/slideshow-generation/scripts/upload_dropbox.py /tmp/scroll_stopper_test/test.mp4 --dest "/Scroll-Stopper/_test"
   ```

   Capture the URL.

4. **Generate the test CSV** using the user's `default_scheduler`:

   ```bash
   python3 ${CLAUDE_PLUGIN_ROOT}/skills/slideshow-generation/scripts/export_scheduler.py \
     /tmp/scroll_stopper_plans/_test_plan.json \
     --captions /tmp/scroll_stopper_plans/_test_captions.json \
     --media-url "<dropbox-test-url-or-placeholder>" \
     --out /tmp/scroll-stopper-import-test.csv
   ```

5. **Open the CSV in the user's default app** so they can preview before importing:

   ```bash
   open /tmp/scroll-stopper-import-test.csv
   ```

6. **Walk the user through the import**, scheduler-specific:

   **For Metricool:**
   > "Open Metricool → Planning → Bulk Upload → drop the CSV. You should see 1 test post per platform you've configured. Date/time will be today at noon — change one row to a near-future time (5 minutes from now), keep it as a draft, and confirm:
   > 1. The caption renders correctly (no broken hashtags, no encoding glitches)
   > 2. The video preview shows up — Metricool may say 'attaching media' for a few seconds. If the preview never loads, your video URL didn't pass through. Check the Picture Url 1 column.
   > 3. The platform-specific options (Pinterest Board, YouTube category, etc.) populated as expected.
   >
   > If anything looks wrong — DON'T POST. Tell me what you see and I'll debug."

   **For Later:**
   > "Later → Schedule → Bulk Schedule → CSV Upload. Verify the caption + media preview, then schedule for a few minutes from now to a test draft (or skip Schedule and just validate the preview)."

   **For Buffer:**
   > "Buffer → Settings → Bulk Upload → CSV. Buffer auto-fills the queue. Pause the queue or move the test post to the bottom so it doesn't actually publish before you verify."

   **For Hootsuite:**
   > "Hootsuite → Publisher → Bulk Composer → Upload. Save as draft, don't publish. Verify the message + image URL render."

7. **After they confirm or report issues**, clean up:

   ```bash
   rm /tmp/scroll-stopper-import-test.csv
   rm /tmp/scroll_stopper_plans/_test_*.json
   ```

   And tell them: "Test draft posts in your scheduler should be deleted manually — they're not auto-cleared."

### Why this command exists

Scheduler bulk imports fail silently in three common ways:
1. **Video URL doesn't resolve** — Dropbox token expired, or `?dl=1` got stripped
2. **Caption encoding breaks** — emoji, em-dashes, or smart quotes get mangled
3. **Platform booleans wrong** — Metricool imports as TikTok-only when the user wanted IG-only

Catching this on 1 test row saves the user an hour of "why did 50 posts fail."
