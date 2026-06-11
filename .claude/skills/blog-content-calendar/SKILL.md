---
name: blog-content-calendar
description: "Generate a 30-day author blog content calendar as a formatted .xlsx spreadsheet, tailored to a specific pen name, genre, posting schedule, and upcoming releases. Use this skill whenever an author asks to 'create a blog content calendar', 'plan my blog posts', 'generate blog topics', 'what should I blog about', 'schedule blog content', 'blog post ideas for my pen name', 'content plan for my author blog', or anything involving planning, scheduling, or generating a batch of blog post ideas for an author website or platform. Also trigger when the user says 'blog calendar', 'content calendar', 'editorial calendar', 'blog schedule', or asks for help filling their author blog for a month. MANDATORY: use this skill even if the user just says 'blog ideas' or 'what should I write about on my blog' when they are an author."
---

# Blog Content Calendar Skill

You are creating a 30-day author blog content calendar — a strategic, genre-aware content plan that helps an author consistently publish blog posts that attract readers, build their platform, and support book sales.

## Step 1: Gather Information

Before generating anything, ask the user for the following if not already provided:

1. **Pen name** — Which author name is this calendar for?
2. **Genre/subgenre** — What do they write? (e.g., women's fiction, cozy mystery, contemporary romance, romantic suspense, crime thriller, espionage thriller)
3. **Content tone/values** — Any important content guidelines? (e.g., clean & wholesome, Christian-friendly, faith-based, sweet romance only, family-friendly, no profanity/violence). This shapes every post topic and CTA.
4. **Target reader** — Who is their ideal reader? (brief description: age range, what they love, etc.)
5. **Posting frequency** — How many posts per week? (Default: 3x/week. Ask which days work best, e.g., Mon/Wed/Fri or Tue/Thu/Sat)
6. **Upcoming releases or promotions** — Any books launching, pre-orders, sales, or events in the next 30 days? If so, what are the titles and dates?
7. **Existing series or backlist** — What books do they already have published? List titles specifically — these MUST be referenced by name in the calendar.
8. **Any topics to avoid or always include** — Optional. E.g., "always tie to faith themes", "no politics", "readers love recipes", etc.

If files are provided (outline, codex, character sheets), read them to inform post topics.

## Step 2: Plan the Content Mix

A strong author blog calendar is NOT all promotional. Use this content ratio as a guide:

- **~30% Reader Connection** — posts that feel personal, relatable, or entertaining for the target reader (e.g., "5 things every [genre] reader will understand", book recommendations in genre, trope love letters, reader Q&As). Keep these consistent with content tone/values.
- **~25% Authority/Craft** — posts that establish the author as a knowledgeable voice (e.g., research rabbit holes, "why I write [genre]", the books that inspired this story, writing craft insights)
- **~25% List-Building & Behind the Scenes** — posts designed to deepen reader connection AND convert visitors to subscribers. This is a priority for ALL pen names, not just new ones. Include a healthy mix of:
  - Writing day/process posts ("A day in my writing life", "How I write a chapter", "My writing routine")
  - Behind-the-scenes posts (research trips, inspiration boards, playlist reveals, drafting chaos)
  - Character spotlights (who is [character name], how they came to life, reader favorites)
  - Setting deep-dives (the real place that inspired the fictional town, mood boards, atmosphere posts)
  - "Get the bonus content" list-building hooks (deleted scenes, bonus epilogues, ARC team invites)
- **~20% Promotional** — posts directly tied to books (cover reveals, launch announcements, excerpt drops, sale alerts, countdown posts, series recaps before a new release)

This mix keeps readers coming back, builds a genuine connection, AND grows the email list — without feeling like a constant advertisement.

## Step 3: Generate the Calendar

Create 30 days of blog post entries at the requested posting frequency. Default is **3x per week**. If the user asks for 3x/week, generate 12-13 posts spread across the month on consistent days (e.g., Monday, Wednesday, Friday). Calculate actual calendar dates correctly for the requested month — verify each date falls on the correct day of the week before entering it.

**Date calculation rule**: If the month starts on, say, a Tuesday and the posting days are Mon/Wed/Fri, the first Monday in that month would be the closest upcoming Monday. Work this out carefully — do not guess. Use actual calendar logic.

For each post, generate:
- **Date** — actual publish date (format: Month DD, YYYY, e.g., May 5, 2026). Must fall on the requested day(s) of the week.
- **Post Title** — a compelling, specific headline (not generic; should feel like something a reader would actually click). Must align with the pen name's content tone/values.
- **Topic/Category** — one of: Reader Connection | Authority/Craft | List-Building & BTS | Promotional
- **SEO Keywords** — 3-5 target keywords or phrases (think: what would the reader Google?)
- **Post Outline** — 3-4 bullet points covering the key sections/beats of the post. Be specific — give the author a real head start, not a generic template.
- **CTA (Call to Action)** — what you want the reader to do at the end. Match the CTA to the post type:
  - Reader Connection → softer CTAs ("comment below", "share with a friend who needs this")
  - Authority/Craft → build credibility CTAs ("follow for more craft posts", "save this for your writing shelf")
  - List-Building & BTS → subscriber-focused CTAs ("join my list to get the deleted scene", "sign up for exclusive BTS content", "join my reader group")
  - Promotional → clear action CTAs ("grab it here before the sale ends", "pre-order now to save your spot", "add to your TBR today")

**IMPORTANT — Backlist & Series Integration**: When the user has provided backlist titles, those titles MUST appear by name in the spreadsheet — in post titles, outlines, or CTAs. Do not just write generically about "my books." Name the actual books. For example, if "Stolen Secrets" is a title, a post might say "Read Books 1-6 of the Mirror Estate Series Before You Read This: Here's Your Spoiler-Free Recap" or an outline bullet might say "Tease: Stolen Secrets picks up exactly where [previous book] left off..."

## Step 4: Build the .xlsx File

Use openpyxl to create a well-formatted, professional spreadsheet. Follow the xlsx skill guidelines.

### Sheet Structure

**Sheet 1: "30-Day Calendar"** — Main calendar with all posts

Columns (in order):
| # | Column | Width |
|---|--------|-------|
| A | Post # | 8 |
| B | Publish Date | 16 |
| C | Post Title | 42 |
| D | Topic Category | 22 |
| E | SEO Keywords | 35 |
| F | Post Outline | 55 |
| G | CTA | 32 |
| H | Status | 14 |

**Sheet 2: "Content Mix Summary"** — A quick-glance dashboard
- Count of posts per category
- Formula-driven percentage of each category
- Target vs. actual mix comparison

### Formatting Guidelines

- **Header row**: Bold, white text, dark navy background (hex: 1F3864)
- **Alternate row shading**: Very light gray (#F2F2F2) on every other data row
- **Row height**: 80px for content rows (outlines need space to breathe)
- **Wrap text**: ON for all content columns
- **Status column (H)**: Leave blank — the author fills this in as they write ("Draft", "Scheduled", "Published")
- **Font**: Calibri, size 10 for body, size 11 bold for headers
- **Freeze panes**: Freeze row 1 so headers stay visible while scrolling
- **Date format**: Stored as string "Month DD, YYYY" (e.g., May 5, 2026)

### Color-code rows by Topic Category (apply to entire row):
- Reader Connection → soft blue background: #DDEEFF
- Authority/Craft → soft green background: #E2F0D9
- List-Building & BTS → soft lavender background: #EAD1DC
- Promotional → soft peach/orange background: #FCE4D6

## Step 5: Recalculate and Verify

After creating the file:
1. Run `python /sessions/intelligent-adoring-goldberg/mnt/.claude/skills/xlsx/scripts/recalc.py <output_path>` to recalculate formulas
2. Verify zero formula errors
3. Confirm the Content Mix Summary sheet totals match Sheet 1
4. Spot-check 2-3 dates to confirm they land on the correct day of week

## Step 6: Save and Deliver

Save the final file to the user's workspace folder:
`/sessions/intelligent-adoring-goldberg/mnt/Claude Cowork/[PenName]-Blog-Calendar-[Month]-[Year].xlsx`

Then provide the user with:
- A link to the file
- A 2-3 sentence summary of the content mix, any launch/promo clusters, and list-building highlights

## Tone and Voice Notes

- Blog post titles should feel **specific and clickable** — not generic. Compare:
  - ❌ "My Writing Process"
  - ✅ "The 6 AM Writing Routine That Finally Worked (After I Stopped Fighting My Brain)"
  - ❌ "About My Books"
  - ✅ "Why I Set Stolen Secrets in Prague — And the One Thing I Got Wrong About the City"

- **Content tone/values matter throughout**: If the pen name writes clean & Christian content, every post should reflect that worldview — including craft posts ("how faith shapes my antagonist's redemption arc"), BTS posts ("the prayer that unlocked this chapter"), and reader connection posts ("books that strengthened my faith and my writing"). This is not just about avoiding certain content — it's about actively infusing the right values.

- Outlines should give the author a **real head start** — three specific bullets that say what each section actually covers, not "introduce topic, add examples, conclude."

- CTAs should match the post goal — don't slap "buy my book" on a reader-connection post. Use softer CTAs there. Save the direct buy CTAs for promotional posts.

- Tie promotional posts to genuine reader value — instead of "my book is out, buy it," frame it as "here's the scene I rewrote seven times — and why it changed the whole book."
