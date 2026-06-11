---
name: booktok-content-engine
description: >
  Generate 30 days of viral BookTok, Instagram Reels, YouTube Shorts, and Facebook content from any
  finished manuscript. Reads the book, extracts 50-100 emotionally compelling scenes, generates 120+
  scroll-stopping hooks in proven viral formats, and outputs a complete content calendar with image
  prompts, hashtag sets, and posting schedule. MANDATORY TRIGGERS: "booktok content", "content engine",
  "generate booktok", "tiktok content", "book content calendar", "viral book content", "booktok hooks",
  "social media content from book", "manuscript to content", "booktok factory", "content from my book",
  "reels content", "shorts content", "book marketing content", "generate hooks", "30 day content",
  "content calendar from book", "booktok slideshow", "slideshow content", or any mention of generating
  TikTok/BookTok/Reels/Shorts content from a manuscript. Use this skill even if the user just says
  "make content" or "create posts" when a manuscript is available.
---

# BookTok Content Engine

## Overview

The BookTok Content Engine transforms a finished manuscript into 30 days of platform-ready social media content. It reads the entire book, understands the narrative arc, extracts the most emotionally compelling moments, and generates scroll-stopping hooks in formats proven to go viral on BookTok, Instagram Reels, YouTube Shorts, and Facebook.

**What makes this different from generic content tools:** This engine reads YOUR actual manuscript. Every hook, every caption, every visual direction comes from what happens in YOUR story. Not templates. Not generic prompts. Content built from your characters, your scenes, your tropes.

## Requirements

- A finished manuscript in DOCX, PDF, or EPUB format
- That's it.

## Outputs (4 Documents Per Book)

1. **Content Calendar (XLSX)** — 120 content pieces (4/day x 30 days) with hooks, captions, image prompts, hashtag sets, platform tags, and optimal posting times
2. **Hook Bank (DOCX)** — All extracted scenes + 3-5 hook variations per scene, organized by hook type and emotional category
3. **Visual Direction Guide (DOCX)** — Detailed image/video prompts for every content piece, with mood boards, color palettes, and aesthetic direction matched to genre
4. **Platform Strategy Brief (DOCX)** — Genre-specific BookTok/Reels/Shorts strategy with trending formats, recommended posting cadence, hashtag rotation plan, and growth tactics

---

## PHASE 1: MANUSCRIPT ANALYSIS

### Step 1: Ingest the Manuscript

Read the uploaded manuscript file. Accept DOCX, PDF, or EPUB formats.

- For DOCX: Use `pandoc` to extract text
- For PDF: Use the Read tool with page ranges
- For EPUB: Use `pandoc` or unzip and read the HTML content files

### Step 2: Build the Book Profile

After reading the manuscript, build a comprehensive Book Profile. Present this to the user for confirmation before proceeding.

**Book Profile includes:**
- **Title and author** (from manuscript metadata or first pages)
- **Genre and subgenre** (detected from content: romance, cozy mystery, thriller, fantasy, LitRPG, literary fiction, nonfiction, etc.)
- **Heat level** (sweet/clean, mild, moderate, spicy, scorching) — this determines content boundaries
- **Target reader demographic** (age range, reading preferences, BookTok community alignment)
- **Core tropes** (enemies-to-lovers, found family, locked room mystery, chosen one, etc.)
- **Main characters** (names, key traits, relationships, physical descriptions for visual content)
- **Setting** (time period, location, atmosphere, aesthetic keywords)
- **Emotional tone** (humorous, dark, cozy, suspenseful, romantic, bittersweet)
- **Series status** (standalone, book in series, series position)
- **Comparable titles** (2-3 well-known books in the same space for hashtag targeting)

**IMPORTANT:** Present the Book Profile to the user and ask them to confirm or adjust before moving to Phase 2. Getting the genre and heat level right is critical — it determines everything downstream.

---

## PHASE 2: SCENE EXTRACTION

### Step 3: Extract Viral-Worthy Scenes

Scan the full manuscript and identify 50-100 scenes with high viral potential. A "viral-worthy scene" is any moment that would make a reader:
- Gasp, laugh, cry, or say "OH NO"
- Immediately want to text a friend about it
- Screenshot it and post it
- Reread it multiple times
- Argue about it in the comments

**Scene categories to extract (aim for variety across all categories):**

#### Emotional Gut-Punches (target: 10-15 scenes)
- Heartbreak moments, betrayals, devastating reveals
- Reunion scenes, reconciliation, forgiveness
- Sacrifice and selfless acts
- Loss, grief, letting go
- "I didn't sign up for these feelings" moments

#### Tension & Chemistry (target: 10-15 scenes)
- First meeting / meet-cute / meet-ugly
- Almost-kiss / interrupted moments
- Jealousy and possessiveness (calibrate to heat level)
- Forced proximity, one-bed, accidental touch
- The moment one character realizes their feelings
- Banter that crackles with subtext

#### Plot Bombs (target: 8-12 scenes)
- Major reveals and twists
- Cliffhanger moments (chapter endings that would make readers scream)
- Dramatic confrontations
- "I knew it!" and "I NEVER saw that coming" moments
- The darkest moment / all-is-lost beat

#### Humor & Charm (target: 8-12 scenes)
- Laugh-out-loud dialogue exchanges
- Awkward situations
- Running gags paying off
- Character quirks on full display
- Wholesome or cozy moments that feel like a warm hug

#### Aesthetic & Atmosphere (target: 5-10 scenes)
- Visually stunning settings or moments
- Sensory-rich passages (food, nature, architecture, weather)
- Magical or fantastical moments (for SFF)
- Cozy domestic scenes (for cozy/romance)
- Dark or atmospheric moments (for thriller/horror)

#### Character Moments (target: 5-10 scenes)
- Badass character moments
- Vulnerability and emotional openness
- Character growth milestones
- Found family bonding
- Internal monologue gems (one-liners that encapsulate a character)

### Step 4: Create the Scene Bank

For each extracted scene, record:
- **Scene ID** (numbered S001-S100)
- **Chapter and approximate location** (early, mid, late — NO specific page numbers to avoid spoiler complaints)
- **Category** (from the list above)
- **The actual excerpt** (2-5 key sentences that capture the moment — NOT the full scene)
- **Emotional core** (one sentence: what makes this scene hit)
- **Spoiler level** (safe / mild spoiler / major spoiler)
- **Visual mood** (dark, warm, chaotic, ethereal, cozy, etc.)

**CRITICAL RULE:** Mark spoiler levels carefully. Content from the first 30% of the book is generally safe. Major plot twists, the ending, and mystery solutions are MAJOR SPOILERS and should be flagged. These can still be used — but hooks must be crafted to tease without revealing.

---

## PHASE 3: HOOK GENERATION

### Step 5: Generate Hooks

For each scene in the Scene Bank, generate 3-5 hooks using the proven viral formats below. Read `references/hook-templates.md` for the full template library.

**Core Hook Formats (use ALL of these across the 30-day calendar):**

1. **POV Hooks** — "POV: you're reading a book where [scenario]"
2. **Reader Reaction Hooks** — "me after reading the chapter where [vague tease]"
3. **The Moment Hooks** — "the moment when [character] realizes [emotional beat]"
4. **Controversial Opinion Hooks** — "unpopular opinion: [character] was RIGHT to [action]"
5. **Book Boyfriend/Girlfriend Hooks** — "if [character] is not your book boyfriend, you're wrong"
6. **Trope Celebration Hooks** — "when the [trope] hits different because [reason]"
7. **Spicy Teaser Hooks** — "that scene in chapter [X]... you know the one" (calibrate to heat level)
8. **Emotional Damage Hooks** — "this book made me [extreme emotional reaction] at 3am"
9. **Quote Hooks** — Direct character quotes that hit hard, displayed as text overlays
10. **Recommendation Hooks** — "if you liked [comp title], you NEED this book"
11. **Slideshow Story Hooks** — Multi-slide narrative retelling (no spoilers) that builds tension
12. **Aesthetic Hooks** — Mood/vibe content with atmospheric visuals and minimal text
13. **Challenge/Trend Hooks** — Adaptations of current BookTok trends applied to the book

**Hook Quality Rules:**
- Every hook must create curiosity WITHOUT giving away the answer
- Spoiler-heavy scenes get hooks that tease the emotion, not the plot
- Hooks should make non-readers curious and existing readers feel seen
- Vary sentence length — short punchy hooks AND longer narrative hooks
- Include hooks that invite comments ("tell me I'm wrong", "who else felt this?")
- NEVER use the same hook format twice in a row on the content calendar

### Step 6: Generate Captions & Hashtags

For each hook, create:
- **Primary caption** (2-3 sentences expanding on the hook, with CTA)
- **Platform-specific adjustments:**
  - TikTok: 150 chars max for on-screen text, caption for description
  - Instagram Reels: Longer caption OK (up to 2200 chars), include book purchase link CTA
  - YouTube Shorts: Title-optimized (60 chars), description with keywords
  - Facebook: Conversational tone, question-based engagement
- **Hashtag set** (read `references/hashtag-database.md` for genre-specific sets)
  - 5-7 hashtags per post
  - Mix of high-volume (#BookTok, #romance) and niche (#enemiestolovers, #cozymystery)
  - Rotate hashtags across the 30 days (never use the same exact set twice)
- **Call-to-action** (varied: "link in bio", "comment your favorite trope", "follow for more", "save this for your TBR")

---

## PHASE 4: VISUAL DIRECTION

### Step 7: Create Visual Prompts

For each content piece on the calendar, generate a detailed image/visual prompt. Read `references/visual-styles.md` for genre-specific aesthetic direction.

**Each visual prompt includes:**
- **Image generation prompt** (ready to paste into Ideogram, Midjourney, or DALL-E)
- **Mood/aesthetic** (dark academia, cottagecore, romantasy, noir, cozy kitchen, etc.)
- **Color palette** (3-4 hex colors that match the scene mood)
- **Typography suggestion** (font style for text overlays: serif for literary, handwritten for romance, bold sans for thriller)
- **Slide count** (for slideshow content: typically 3-7 slides)
- **Text overlay placement** (where the hook text goes on each slide)
- **Transition style** (fade, cut, zoom — for video formats)
- **Background music mood** (dramatic, soft piano, lo-fi, upbeat indie — NOT specific song names due to licensing)

**Visual Style by Genre:**
- **Romance:** Soft lighting, warm tones, intimate close-ups, golden hour, candlelight, rain on windows
- **Cozy Mystery:** Autumn colors, cozy interiors, cats/animals, teacups, small-town charm, foggy mornings
- **Thriller/Suspense:** High contrast, shadows, rain, urban nightscapes, red accents, shattered glass
- **Fantasy/Sci-Fi:** Ethereal lighting, magical particles, dramatic landscapes, glowing elements, starscapes
- **Literary Fiction:** Muted tones, natural textures, minimalist composition, quiet beauty, contemplative spaces
- **Nonfiction:** Clean design, professional typography, concept visualization, data-beautiful aesthetics

---

## PHASE 5: CONTENT CALENDAR ASSEMBLY

### Step 8: Build the 30-Day Calendar

Read `references/calendar-strategy.md` for the posting schedule framework.

Assemble all content into a 30-day calendar with 4 posts per day (120 total pieces). The calendar follows a strategic content mix:

**Daily Content Mix (4 posts/day):**
- **Morning post (8-9am):** Engagement hook (question, opinion, trope celebration) — gets comments flowing
- **Midday post (12-1pm):** Visual/aesthetic content (slideshow, mood board, quote graphic) — gets saves and shares
- **Afternoon post (4-5pm):** Emotional/dramatic hook (tension, chemistry, gut-punch) — peak engagement window
- **Evening post (7-9pm):** Story/narrative content (multi-slide story, character spotlight) — lean-back viewing

**Weekly Content Rotation:**
- **Monday:** Character-focused content (introductions, thirst traps, character quotes)
- **Tuesday:** Trope celebration day (lean into the book's dominant tropes)
- **Wednesday:** Emotional content (gut-punches, "this book destroyed me")
- **Thursday:** Spicy/tension content (chemistry, almost-kisses, confrontations — calibrated to heat level)
- **Friday:** Fun/humor content (banter, awkward moments, reader reactions)
- **Saturday:** Aesthetic/vibe content (mood boards, settings, atmospheric scenes)
- **Sunday:** Community/engagement content (recommendations, reading lists, "tell me your favorite [trope]")

**Spoiler Management:**
- Weeks 1-2: Zero spoilers — hook readers who haven't read the book yet
- Weeks 3-4: Mild spoilers allowed (with warnings) — reward readers who HAVE read it and create FOMO for those who haven't

### Step 9: Generate the XLSX Content Calendar

Create the content calendar as an XLSX file using the xlsx skill patterns. Read the skill at `/sessions/dazzling-gracious-volta/mnt/.claude/skills/xlsx/SKILL.md` for Excel generation instructions.

**XLSX Structure:**

**Sheet 1: "30-Day Calendar"**
| Column | Content |
|--------|---------|
| Day | Day 1-30 |
| Date | (user fills in their start date) |
| Time Slot | Morning / Midday / Afternoon / Evening |
| Platform | TikTok / IG Reels / YouTube Shorts / Facebook |
| Content Type | Slideshow / Quote / Reaction / Story / Aesthetic / Engagement |
| Hook Format | POV / Reader Reaction / The Moment / etc. |
| Hook Text | The actual hook copy |
| Caption | Full caption with CTA |
| Hashtags | 5-7 hashtags |
| Scene Reference | Scene ID (links to Hook Bank) |
| Spoiler Level | Safe / Mild / Major |
| Image Prompt | Visual direction summary |
| Slides | Number of slides (for slideshows) |
| Music Mood | Background audio direction |
| Status | Blank (user tracks: Draft / Filmed / Posted) |

**Sheet 2: "Platform Distribution"**
Summary showing content distribution across platforms, content types, and hook formats to ensure variety.

**Sheet 3: "Hashtag Rotation"**
Full hashtag sets organized by week with rotation schedule.

**Sheet 4: "Quick Stats"**
- Total content pieces: 120
- By platform breakdown
- By content type breakdown
- Spoiler-safe vs. spoiler content ratio

### Step 10: Generate the Hook Bank (DOCX)

Create a comprehensive Hook Bank document organized by:
1. **By Scene** — All hooks grouped under their source scene, with the excerpt and emotional core
2. **By Hook Format** — All POV hooks together, all Reader Reaction hooks together, etc.
3. **By Emotional Category** — Tension, Humor, Romance, Drama, Cozy, etc.
4. **Bonus Hooks** — 20 additional "evergreen" hooks that don't reference specific scenes (general book/author/trope content)

Use the docx skill at `/sessions/dazzling-gracious-volta/mnt/.claude/skills/docx/SKILL.md` for document generation.

### Step 11: Generate the Visual Direction Guide (DOCX)

Create the visual guide organized by content type:
1. **Slideshow Templates** — 5 genre-matched slideshow layouts with slide-by-slide visual direction
2. **Quote Graphics** — Typography and layout specs for quote-style posts
3. **Aesthetic Mood Boards** — 4-6 mood board concepts with color palettes and image prompt sets
4. **Character Visual Profiles** — Image prompts for character portraits (based on manuscript descriptions)
5. **Scene Illustration Prompts** — Detailed prompts for key scene visuals
6. **Platform Specs** — Exact dimensions, safe zones, and format requirements per platform

### Step 12: Generate the Platform Strategy Brief (DOCX)

Create a strategy document covering:
1. **Genre-Specific BookTok Strategy** — What works for THIS genre on BookTok right now
2. **Platform Breakdown** — How to adapt content for TikTok vs. IG vs. YouTube vs. Facebook
3. **Posting Cadence** — Why 4x/day, optimal times, what to do if 4x is too much (priority ranking)
4. **Hashtag Strategy** — How to use the rotation plan, when to use trending vs. niche hashtags
5. **Engagement Tactics** — How to respond to comments, drive saves, create conversation
6. **Growth Playbook** — First 30 days strategy for building a BookTok presence from zero
7. **Content Repurposing** — How to turn 1 piece of content into 3-4 across platforms
8. **Trending Formats** — Current BookTok trends and how to adapt them to this book
9. **Series Strategy** — If the book is part of a series: how to promote read-through and upcoming releases

---

## PHASE 6: DELIVERY & REVIEW

### Step 13: Deliver All Documents

Save all four output files to the user's workspace:

```
BookTok Content Engine - [Book Title]/
├── [Book Title] - 30-Day Content Calendar.xlsx
├── [Book Title] - Hook Bank.docx
├── [Book Title] - Visual Direction Guide.docx
└── [Book Title] - Platform Strategy Brief.docx
```

### Step 14: Offer Next Steps

After delivery, offer:
- **Generate another 30 days** (months 2-3 content using remaining scenes from the bank)
- **Series content** (if they have multiple books — cross-promote and optimize for read-through)
- **Seasonal adaptation** (holiday, summer reading, back-to-school angles)
- **A/B test variants** (generate alternative hooks for their top-performing content)

---

## IMPORTANT GUIDELINES

### Content Quality Standards
- Every hook must be unique — no repeated structures, no copy-paste variations
- Captions should sound like a real BookTok creator, not a marketing robot
- Match the energy and vocabulary of the book's target audience
- Romance readers and thriller readers speak VERY differently on BookTok — know the difference
- When in doubt, lean into emotion over information

### Spoiler Ethics
- NEVER reveal the ending, the mystery solution, or major plot twists in "safe" content
- Teasing is an art — make readers desperate to know what happens WITHOUT telling them
- "That thing that happens in chapter 14" is a valid hook — you don't have to say what it is
- When using spoiler content (weeks 3-4), ALWAYS include a spoiler warning in the caption

### Platform Awareness
- TikTok: Hook in first 1-2 seconds, text overlays essential, trending sounds boost reach
- Instagram Reels: Higher production value expected, hashtags in caption not on screen, cover image matters
- YouTube Shorts: Title and description are searchable (SEO matters), thumbnail important
- Facebook: Native video performs better than links, longer captions OK, share-friendly content

### Heat Level Calibration
- **Sweet/Clean:** Focus on emotional tension, longing glances, almost-touches, romantic gestures
- **Mild/Moderate:** Can reference "that scene" and "the tension," light innuendo OK
- **Spicy/Scorching:** Lean into it — BookTok loves spice content. "If you know, you know" hooks, spice ratings, "I need to go touch grass after that chapter"
- NEVER include explicit content in hooks regardless of heat level — tease, don't show
