# Scroll Stopper — User Guide

Everything you need to install Scroll Stopper and start generating reels. **Allow about 30 minutes for your first full run.** After that, you'll fly.

---

## PART 1 — INSTALL (one time, ~10 minutes)

### Step 1. Install Claude Code

Free from Anthropic. https://claude.com/claude-code

After install, open Terminal (Mac) or PowerShell (Windows) and type:

```
claude
```

If a Claude prompt appears, you're good. Type `/exit` to close.

---

### Step 2. Install the Python helpers

In Terminal, paste this and hit enter:

```bash
pip3 install fal-client Pillow python-docx ebooklib pypdf imageio-ffmpeg dropbox
```

If you see "command not found: pip3", install Python 3.9+ first from https://python.org.

---

### Step 3. Get a fal.ai API key

This is what generates your AI images. You pay fal.ai directly — about $0.05 per image, $1-2 per finished video. **Skip this step if you only plan to use cover-mode** (no AI images).

1. Go to https://fal.ai → sign up (free account)
2. Dashboard → **API Keys** → **Create Key** → copy the whole thing (looks like `keyid:secret`)
3. In Terminal, run:

   ```bash
   echo 'export FAL_KEY=PASTE_YOUR_KEY_HERE' >> ~/.zshrc
   source ~/.zshrc
   ```

   Replace `PASTE_YOUR_KEY_HERE` with the key you copied.

4. Test it: `echo $FAL_KEY` — your key should print.

---

### Step 4. (Optional) Get a Dropbox token

Skip this if you'll upload videos to your scheduler manually. Do it if you'll use **Metricool** or any tool that needs direct video URLs.

1. Go to https://www.dropbox.com/developers/apps
2. Click **Create app**
3. Pick **Scoped access** → **Full Dropbox** → name it `Scroll Stopper` → Create
4. **Permissions tab** → check these four boxes, click **Submit**:
   - `files.content.write`
   - `files.content.read`
   - `sharing.write`
   - `sharing.read`
5. **Settings tab** → scroll to **Generated access token** → expiration = **No expiration** → click **Generate**
6. Copy the token. You'll paste it during setup (Part 2).

This token only allows Scroll Stopper to write files into a `/Scroll-Stopper/` folder in your Dropbox. It can't read anything else.

---

### Step 5. Install the plugin itself

1. Download `scroll-stopper.zip` from the Skool classroom (Plugin Download section)
2. Unzip it (double-click the zip on Mac; right-click → Extract All on Windows)
3. Inside the unzipped folder you'll see two installers:

   ```
   Install-Scroll-Stopper.command   ← Mac
   Install-Scroll-Stopper.bat       ← Windows
   scroll-stopper/                  ← the plugin
   ```

4. **Mac:** double-click `Install-Scroll-Stopper.command`. If you see "can't be opened — unidentified developer", right-click the file → **Open** → click **Open** in the dialog. Mac remembers next time.

5. **Windows:** double-click `Install-Scroll-Stopper.bat`. If you see "Windows protected your PC", click **More info** → **Run anyway**.

6. Wait for "Done. Scroll Stopper is installed." Press any key to close the window.

---

### Step 6. Verify in Claude Code

Open Claude Code, type:

```
/plugins
```

You should see **scroll-stopper** in the list. If you don't, restart Claude Code.

---

## PART 2 — FIRST-TIME SETUP (one time, ~5 minutes)

In Claude Code, type:

```
/scroll-stopper-setup
```

It walks you through 8 questions. Answer each, hit enter:

| # | Question | What to answer |
|---|---|---|
| 1 | Where to save slideshows | Pick a folder — Dropbox, Google Drive, iCloud, or local. Default is `~/ScrollStopper`. |
| 2 | Books library folder | Where your manuscripts/epubs live. Optional — leave blank if you upload books one at a time. |
| 3 | Default mode | `ai` (premium AI images), `cover` (book cover only — free per slide), or `hybrid` (cover slide 1 + AI for the rest). |
| 4 | Platforms you post to | Comma-separated. Just for logging — `TikTok, Instagram, YouTube Shorts`. |
| 5 | Font preference | Use the genre-recommended fonts, or pick one font for everything (e.g. `Bebas Neue`). |
| 6 | Music default for videos | `silent` (let TikTok do the audio), `auto` (AI-generated track), `byo` (your own mp3), or `ask` (ask each time). |
| 7 | Dropbox token | Paste the token from Install Step 4, or `skip` for now. |
| 8 | Auto-write captions | `yes` = Scroll Stopper writes platform-specific captions (TikTok, IG, YouTube, FB, Pinterest) with hashtags + your buy link, drops them into a Metricool-ready CSV. `no` = skip. |
| 8a | Buy link template | e.g., `https://geni.us/{slug}` — the format your books usually follow. Or skip if every book has a unique URL. |
| 8b | Default CTA | e.g., `Out now in Kindle Unlimited`, `1-click your copy` |
| 8c | Social handles per platform | `@yourhandle` for tag-aware platforms |
| 8d | Scheduler | `metricool`, `later`, or `buffer` — Scroll Stopper formats the CSV columns to match. |
| 9 | CSV log columns | Press enter to keep all defaults. Or paste a custom comma-separated list. |

Done. You're ready.

---

## PART 3 — DAILY WORKFLOW (every time you make videos)

Four commands in order. The first run feels slow — second run, you'll fly.

### Command 1 — Scan your library (optional, but recommended)

Detects every book in your library folder, auto-detects the genre, and finds matching covers.

```
/scan-library
```

You'll see a table. Confirm or correct:

```
| # | File              | Detected Title    | Genre              | Cover Found |
| 1 | Debt-Marker.epub  | Debt Marker       | dark_mm_romance    | ✓           |
| 2 | sweet-witch.docx  | The Sweet Witch   | paranormal_romance | —           |
```

Tell it which books to process (e.g. "do book 1, 3 slideshows × 7 slides each, hybrid mode").

Skip this if you only want to process one book — go straight to Command 2.

---

### Command 2 — Generate slideshows from one book

```
/create-slideshow path/to/your-book.epub 3 7
```

That's: 3 slideshows × 7 slides each.

It'll ask:

- **Pen name** — which name should this go under in the folder?
- **Pairing** (for romance) — MM, FF, MF, RH, monster pairing? **CONFIRM THIS.** AI defaults to MF if you don't, which is wrong for ~40% of romance subgenres.
- **Genre** — confirm the auto-detection
- **Mode** — confirm AI / cover / hybrid (uses your config default)
- **Cover path** (cover/hybrid mode only) — where's your cover image?
- **Hooks** — it generates ~50% more than needed. You approve, swap, edit before any image generation happens. **Iterate here, not after spending money on images.**

When you approve, images generate. Cost shows in the manifest (~$0.05 per AI image, $0 per cover slide).

Output goes to: `<your output folder>/<Pen Name>/<Book Title>/Slideshow-NN/`

---

### Command 3 — Render slideshows to MP4

```
/slideshow-to-video Slideshow-01
```

Or pass a partial name and Scroll Stopper finds it:

```
/slideshow-to-video "Debt Marker 01"
```

It asks about music (unless your config sets a default):

1. **Silent** — best for TikTok, swap audio in-app after upload
2. **Bring your own mp3/wav**
3. **Auto-generate genre track** — fal.ai writes a custom instrumental ($0.04, reused across all slideshows for that book)
4. **Royalty-free pull** — you grab from Pixabay/YouTube Audio Library

The MP4 lands next to the slideshow folder. Default: 3 sec per slide, 0.6 sec crossfade, 1080×1920, 30fps, Ken Burns zoom.

Repeat for each slideshow folder you generated.

---

### Command 4 — Upload to Dropbox for Metricool

(Skip this if you don't use Metricool or another bulk scheduler.)

```
/upload-video <book-folder>
```

For example:

```
/upload-video "Dana Sacco/Debt Marker"
```

Scroll Stopper:
- Finds every MP4 under that folder
- Uploads each to your Dropbox `/Scroll-Stopper/<Pen Name>/<Book Title>/`
- Creates a shared link with `?dl=1` (Metricool-fetchable)
- Writes the URL into your CSV log

Then opens Finder/Explorer to your CSV. Paste the rows into Metricool's bulk scheduler. Schedule the whole batch.

---

### What ships in your scheduler CSV (when auto-captions is on)

You get a second file alongside your tracking log, formatted for the scheduler you picked during setup:

- `metricool-import.csv` — for Metricool
- `later-import.csv` — for Later
- `buffer-import.csv` — for Buffer

**One row per (slideshow × platform).** So if you generated 3 slideshows and post to TikTok + Instagram + YouTube + Facebook + Pinterest = **15 rows**, all pre-written.

| date | time | network | text | media_url | scroll_stopper_id |
|---|---|---|---|---|---|
| 2026-05-15 | 12:00 | TIKTOK | He's mine. He's mine. He's mine.\n\n1-click → geni.us/debt-marker\n\n#booktok #darkmmromance #mmromance #morallygreyheroes #spicybooks | https://www.dropbox.com/.../...?dl=1 | DanaSacco__DebtMarker__SS01 |
| 2026-05-15 | 12:00 | INSTAGRAM | He's mine. He's mine. He's mine.\n\nTwo enemies. One name carved into both their skin... | https://www.dropbox.com/.../...?dl=1 | DanaSacco__DebtMarker__SS01 |
| 2026-05-15 | 12:00 | YOUTUBE | Dark MM romance — enemies to lovers... | https://www.dropbox.com/.../...?dl=1 | DanaSacco__DebtMarker__SS01 |

Captions are platform-tuned:
- **TikTok** — punchy, 4-6 hashtags, link line
- **Instagram** — emotional middle paragraph, 8-15 hashtags hidden after dots
- **YouTube Shorts** — keyword-heavy for SEO
- **Facebook** — longer storytelling
- **Pinterest** — descriptive title format, evergreen keywords

**You only need to fill in `date` and `time` per row** before importing into Metricool. Scroll Stopper picks today as a placeholder so you can see the format.

The captions are also genre + pairing aware:
- MM book → "He's mine" not "She's his"
- Cozy mystery → "Who killed the baker? You'll never guess." not romantic phrasing
- Dark romance hashtags ≠ romcom hashtags

---

## YOUR CSV LOG

Lives at the path you set during setup (default: `<output folder>/scroll-stopper-log.csv`).

Default columns:

| Column | What it is |
|---|---|
| `date_generated` | When you made it |
| `pen_name` | Which pen name |
| `book_title` | Which book |
| `genre` | Auto-detected genre |
| `slideshow_number` | Slideshow 01, 02, 03... |
| `slide_count` | How many slides |
| `mode` | ai / cover / hybrid |
| `platforms` | Where it's going |
| `output_path` | Local folder path |
| `post_date` | YOU fill this in as you schedule |
| `status` | generated / scheduled / posted |
| `hook_summary` | First 3 hooks for quick scanning |
| `dropbox_url` | Auto-filled when you run `/upload-video` |

Open the CSV in Numbers or Excel any time to see what's been made and where it was posted.

---

## TROUBLESHOOTING

**Plugin doesn't show up in /plugins** — restart Claude Code.

**`ModuleNotFoundError: No module named 'fal_client'` (or similar)** — re-run the pip3 install command from Step 2.

**`FAL_KEY not set`** — restart Terminal, or run `source ~/.zshrc` again. Verify with `echo $FAL_KEY`.

**Mac installer won't open** — right-click → Open. Don't double-click.

**Windows installer says "protected your PC"** — click "More info" → "Run anyway".

**Installer says "scroll-stopper folder not found"** — you double-clicked before unzipping. Unzip the download fully, then double-click the installer from inside the unzipped folder.

**Wrong pronouns / wrong gender pairing in hooks or images** — you skipped or rushed the pairing-confirmation step. Re-run `/create-slideshow` and pay close attention when it asks "MM / FF / MF / RH / monster?". Also: re-edit the plan JSON in `/tmp/scroll_stopper_plans/` and re-run with `--only N` to fix individual slides.

**Image looks generic / not matching the genre** — the manuscript was too short to give the genre detector enough cues. Either confirm genre manually when prompted, or use cover mode for that book.

**Dropbox upload fails** — token expired or wrong scopes. Regenerate at https://www.dropbox.com/developers/apps with the four scopes listed in Step 4, paste into `~/.scroll-stopper/config.json`.

**Metricool says "couldn't fetch media"** — your Dropbox URL doesn't end in `?dl=1`. Open the CSV, check the `dropbox_url` column. If you uploaded outside `/upload-video`, fix the URL manually.

---

## TIPS FROM DANA

- **Confirm the pairing every single time.** Don't trust auto-detection blindly. The wrong pronouns ruin a slideshow.
- **Iterate on hooks before letting images generate.** Hook approval is free. Image regen costs $0.05 per slide.
- **Use cover mode for backlist books**, AI mode for new releases. Saves money where you can, looks premium where it matters.
- **One music track per book**, generated once, reused across that book's slideshows. Sonic identity = stronger brand on TikTok.
- **Schedule in batches of 30-60 reels at a time.** Metricool handles it; your account looks consistent.
- **Update your CSV `post_date` as you schedule.** Future-you needs to know what's already in the queue.

---

## STUCK?

Post in the **Q&A thread** inside the Skool classroom. Dana checks it daily. Tag @Dana with a screenshot if it's a bug.
