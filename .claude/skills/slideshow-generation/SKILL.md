---
name: slideshow-generation
description: >
  Use this skill whenever the user asks to "create a slideshow", "scroll stopper",
  "make a reel from my book", "9:16 slideshow", "vertical slideshow", "tiktok
  slideshow", "booktok content", "book promo reel", "cover slideshow", "hybrid slideshow",
  or any request to turn a manuscript (.docx, .epub, .pdf) into ready-to-post 9:16
  slideshow images (AI-generated, book-cover-based, or hybrid mix) with text hooks
  overlaid. Reads ~/.scroll-stopper/config.json for output paths, default mode, font, and CSV log.
version: 2.0.0
---

# Scroll Stopper — Slideshow Generation

Generate one or more Scroll Stopper 9:16 vertical slideshows from a book manuscript. Each slide is either:

- **AI-generated** — fal.ai Flux Pro image matched to the genre aesthetic
- **Cover-based** — the user's book cover with a different scroll-stopping hook overlaid
- **Hybrid** — slide 1 is the cover, slides 2-N are AI

Output saves to the path the user configured during `/scroll-stopper-setup`, organized as `<output_folder>/<Pen Name>/<Book Title>/Slideshow-NN/`.

## Phase 0: Preflight

### Verify config exists

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/slideshow-generation/scripts/config.py show
```

If config is missing or the output folder is empty/default, stop and tell the user: "Run `/scroll-stopper-setup` first to configure where slideshows save."

### Verify environment

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/slideshow-generation/scripts/preflight.py
```

This verifies `FAL_KEY` is set (only required for AI / hybrid modes) and required packages are installed. If missing:

```bash
pip3 install fal-client Pillow python-docx ebooklib pypdf
export FAL_KEY=keyid:secret
```

If the user's chosen mode is `cover` only, FAL_KEY is not required — proceed without it.

## Phase 1: Manuscript Intake

### Locate the manuscript

Search for the file the user referenced — accept `.docx`, `.epub`, `.pdf`. If `library_folder` is set in config, search there first.

### Extract text

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/slideshow-generation/scripts/extract_text.py "<path>" > /tmp/scroll_stopper_manuscript.txt
```

Read the first ~8000 words — enough for genre detection and hook pulls.

### Confirm pen name + title

Extract the title from the manuscript or filename. **Always ask the user for the pen name** — many authors publish under multiple names.

> "What pen name should I file this under? I'll save the slideshows to `<output_folder>/<Pen Name>/<Title>/`. The title I extracted is: `<title>` — let me know if that needs correcting."

### Confirm slideshow counts

If the user's command didn't specify, ASK:

> "How many slideshows do you want from this book, and how many slides per slideshow? Typical: 3 slideshows × 7 slides each."

Never proceed without explicit numbers for both.

### Confirm mode

Read `default_mode` from config. Confirm with the user:

> "Mode: **<default_mode>** (from your config). Want to override?
> - `ai` — every slide is an AI image (~$0.05/slide)
> - `cover` — every slide is your book cover with a different hook (free)
> - `hybrid` — slide 1 is your cover, slides 2-N are AI"

If `cover` or `hybrid`, ask for the cover image path if not already known. If a `<title>.jpg/.png` exists in the manuscript folder, suggest that as the default.

## Phase 1.5: Pairing Detection (Romance Only — REQUIRED)

If the genre is any flavor of romance, **you must detect and confirm the pairing before generating hooks or images.** Image generators default to MF (male/female) when not told otherwise. For any MM, FF, RH, why-choose, polyamory, or monster/human book this produces wrong-content reels — which is a refund risk.

### How to detect

Read the first ~5000 words of the manuscript focusing on intimate / POV scenes. Count pronouns referring to romantic leads:

- Heavy "he/him + he/him" pairing → **MM**
- Heavy "she/her + she/her" pairing → **FF**
- "she/her" + multiple distinct men named → **reverse harem** (RH / why-choose)
- "he/him" + "she/her" → **MF**
- Non-human partner cues (claws, fangs, horns, scales, monster name) + gender of human → **monster pairing** (specify both genders + species)

### How to confirm

Always ask the user, even when detection is confident:

> "Reading this as **<detected pairing>** — for example, MM dark romance with two men, or RH with one woman and three men. Should I generate hooks and images with that pairing? Type the correct pairing if I'm wrong (MM / FF / MF / RH / MMF / monster-MF / monster-MM / etc.)."

Wait for the user's answer. Save the confirmed pairing into the plan JSON as `"pairing": "MM"` (or the correct code).

### How to use it

- **In every image prompt:** prepend pairing tokens from `references/dalle-prompt-templates.md` (e.g., "two men, M/M couple, ..." for MM)
- **In every hook:** use pronouns matching the pairing — never say "she's his" for an MM book
- **Solo character hooks/images:** still specify gender clearly so Flux doesn't default to a stock female model when the lead is male

### Critical

Do not skip this phase. Do not assume "romance = MF." This is the single most common point of failure in batch reel generation for indie romance authors.

---

## Phase 2: Genre Detection

Detect the genre from the manuscript using `references/genre-hook-styles.md`:

1. Dark romance / dark MM
2. Monster romance
3. Paranormal romance
4. Romantic suspense
5. Romcom (spicy or clean)
6. Cozy mystery
7. Psychological horror / Dark Stays
8. Sci-fi (non-romance)
9. Cozy fantasy / LitRPG
10. Thriller / suspense

Confirm the detected genre with the user before generating hooks. The genre drives hook voice, image aesthetic, and text style.

## Phase 3: Hook Generation

Read `references/genre-hook-styles.md` for per-genre voice.

Generate enough unique hooks for **all requested slideshows combined**:

- **Total hooks needed** = (number_of_slideshows × slides_per_slideshow) + buffer
- Generate ~50% more candidates so the user has room to swap

### Hook rules

- Under 12 words
- Genre-voice match
- Drawn from actual story content (no generic stock)
- Scroll-stopping (POV, taboo reveal, promise, question)
- Vary the angle across candidates

### Variety across slideshows

Each slideshow should have a distinct theme/arc. Group hooks into thematic clusters before assigning. Present grouped candidates to the user and ask for approval / swaps before any spending.

## Phase 4: Plan JSONs

For each slideshow, write a plan JSON to `/tmp/scroll_stopper_plans/<Author>_<Title>_<NN>.json`:

```json
{
  "book_title": "Debt Marker",
  "author": "Dana Sacco",
  "genre": "dark_mm_romance",
  "pairing": "MM",
  "slideshow_number": 1,
  "mode": "hybrid",
  "output_folder": "<output_folder from config>/Dana Sacco/Debt Marker/Slideshow-01",
  "font_override": "<font_override from config, or empty>",
  "use_genre_fonts": true,
  "slides": [
    {
      "slide_number": 1,
      "mode": "cover",
      "cover_path": "/path/to/debt-marker-cover.jpg",
      "hook": "He's my rival. He's my enemy. He's mine.",
      "text_position": "bottom",
      "text_style": "dark_romance"
    },
    {
      "slide_number": 2,
      "mode": "ai",
      "image_prompt": "Cinematic moody photograph...",
      "hook": "Two scars. One name. Mine.",
      "text_position": "top",
      "text_style": "dark_romance"
    }
  ]
}
```

Per-slide rules:
- For `mode: "cover"` → set `cover_path`, skip `image_prompt`
- For `mode: "ai"` → set `image_prompt`, no `cover_path`
- Alternate `text_position` between top/bottom
- Match `text_style` to genre per `references/text-overlay-styles.md`

For AI prompts, reference `references/dalle-prompt-templates.md`. Flux rules:
- Subject in clear composition with obvious text negative space
- No text in the prompt — Pillow renders the hook on top
- Reference cinematography (anamorphic, Kodak, A24, film grain)
- Avoid faces — prefer silhouettes, hands, objects, environment

## Phase 5: Build

Run the builder once per slideshow:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/slideshow-generation/scripts/build_slideshow.py /tmp/scroll_stopper_plans/<Author>_<Title>_01.json --provider fal
```

The builder respects each slide's `mode`. If a slide fails, re-run with `--only 3,7` after editing the prompt or cover path.

## Phase 6: Log to CSV

After each slideshow renders successfully, log it:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/slideshow-generation/scripts/log_run.py /tmp/scroll_stopper_plans/<Author>_<Title>_01.json
```

The CSV path and columns come from the user's config. Tell the user the CSV path and that they can update `post_date` / `status` columns as they schedule posts.

## Phase 6.5: Caption Generation + Scheduler CSV (REQUIRED if auto_generate_captions is true)

Captions matter as much as the image. Each platform gets its own caption — read `references/caption-templates.md` for the per-platform format and per-genre hashtag pools.

### Collect per-book metadata

Before generating captions, ensure you have:
- **Buy link** for this book — ask the user if not already captured. Suggest the format from `cfg["buy_link_template"]` (e.g., `https://geni.us/<slug>` or `https://amazon.com/dp/<asin>`)
- **CTA** — use `cfg["default_cta"]` or ask
- **Pen name handles per platform** — read from `cfg["social_handles"]`. If empty for a platform, skip the @ tag.

### Generate one caption per (slideshow × platform)

For each slideshow plan and each platform in `cfg["platforms"]`, write a caption matching that platform's format (per `references/caption-templates.md`). Use the SHARPEST hook from the slideshow as the opening line. Pull 4-15 hashtags from the genre pool sized to the platform.

Save to `/tmp/scroll_stopper_plans/<Author>_<Title>_NN_captions.json`:

```json
{
  "TikTok": "He's mine. He's mine. He's mine.\n\n1-click → geni.us/debt-marker\n\n#booktok #darkmmromance #mmromance #morallygreyheroes #spicybooks #possessivehero",
  "Instagram": "He's mine. He's mine. He's mine.\n\nTwo enemies. One name carved into both their skin. Neither walking away whole.\n\n1-click in stories →\n\n.\n.\n.\n#booktok #darkmmromance #mmromance #morallygreyheroes #darkromance #spicybooks #romancereads #booktokmademereadit #mmreaders #obsessivelove",
  "YouTube Shorts": "Dark MM romance — enemies to lovers — possessive antihero. Out now: geni.us/debt-marker\n\n#shorts #darkromance #mmromance #booktok",
  "Facebook": "He's mine. He's mine. He's mine.\n\nTwo enemies. Two scars. One name they refuse to give up.\n\nDebt Marker — out now in Kindle Unlimited → geni.us/debt-marker\n\n#booktok #darkmmromance #mmromance",
  "Pinterest": "Debt Marker — Dark MM enemies-to-lovers romance with a morally grey antihero. #darkmmromance #darkromancebooks #mmromance"
}
```

### Confirm with user before exporting

Show all platform captions to the user. Let them edit/swap/regenerate before any CSV is written.

### Export to scheduler CSV

For each slideshow that's been rendered to MP4 AND uploaded to Dropbox (so we have a media URL), append rows to the scheduler CSV:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/slideshow-generation/scripts/export_scheduler.py \
  /tmp/scroll_stopper_plans/<Author>_<Title>_01.json \
  --captions /tmp/scroll_stopper_plans/<Author>_<Title>_01_captions.json \
  --media-url "<dropbox-direct-url>" \
  --format <metricool|later|buffer>
```

The `--format` flag is optional — defaults to `cfg["default_scheduler"]`. The script writes a CSV in the format that scheduler expects:

- **metricool** → `date, time, network, text, media_url, scroll_stopper_id` → `metricool-import.csv`
- **later** → `scheduled_at, caption, media_url, profile, label` → `later-import.csv`
- **buffer** → `date, time, text, link, image_url, profile` (with link auto-extracted from caption) → `buffer-import.csv`

The customer edits `date` and `time` per row before importing into Metricool.

### Critical rule

Captions for romance MUST match the confirmed pairing's pronouns (Phase 1.5). An MM book with "she/her" caption text is the #1 refund driver.

---

## Phase 7: Delivery

Show the user:
- The output folder path with all slideshows
- Total cost (only AI slides × $0.05)
- The final hook list per slideshow
- Suggest running `/slideshow-to-video <folder>` to render to MP4
- The CSV log path

## Critical rules

- **Always read config first** — never hardcode paths
- **Always confirm pairing before generating** — MM ≠ MF ≠ FF ≠ RH; the wrong pairing in images is a refund risk
- **Captions follow the same pairing rule** — pronouns in captions must match the confirmed pairing
- **Hook approval before spend** — iterate on hooks before any image gen
- **One folder per slideshow** — `Slideshow-01`, `Slideshow-02`, zero-padded
- **Never embed text in the Flux prompt** — Pillow overlays all text
- **9:16 only** (`portrait_16_9`)
- **Confirm mode before building** — cover/hybrid need a cover path
- **Log every run to CSV** — that's the user's content tracker
