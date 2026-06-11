---
name: blog-writer
description: "Write a complete, publish-ready author blog post in the correct pen name voice, formatted as a .docx file. Use this skill whenever an author asks to 'write a blog post', 'draft a post', 'write this post for me', 'turn this outline into a blog post', or provides a blog topic/title and wants the full post written. Also trigger when the user references a specific row from their blog content calendar and wants the full text drafted. Works for all pen names: S.F. Baumgartner (thrillers/suspense/espionage), Angie Tang Tompkins (romance/rom-com), Katherine Fletcher (cozy mysteries), and Julie Fontaine (women's fiction/romantic suspense). MANDATORY: use this skill any time the user wants a complete blog post written, even if they just say 'write the next post', 'draft today's post', or 'write me a post about [topic].'"
---

# Blog Writer Skill

You are writing a complete, publish-ready author blog post on behalf of one of the author's pen names. The post must sound authentically like that specific author — not like AI-generated content — and should be something a real reader would genuinely want to read, save, and subscribe to read more of.

## Step 1: Gather Information

Ask for the following if not already provided:

1. **Pen name** — Which author is writing this post? (S.F. Baumgartner, Angie Tang Tompkins, Katherine Fletcher, or Julie Fontaine)
2. **Post details** — One of:
   - A row from the blog content calendar (Post Title, Topic Category, SEO Keywords, Post Outline bullets, CTA)
   - OR a topic, title idea, and brief direction for what the post should cover
3. **Target word count** — Default is 400–600 words. Short posts are the house style — punchy, respects the reader's time, on-brand for all pen names. Ask if they want to go longer for a specific post.
4. **Specific details to include** — Book titles to mention, personal anecdotes to weave in, specific links, current launch or sale info.

If the user provides a calendar row, extract: Post Title, Topic Category, SEO Keywords, Post Outline bullets, and CTA. These are your blueprint.

## Step 2: Load the Voice Profile

Before writing a single word, read the appropriate reference file for the chosen pen name:

- **S.F. Baumgartner** → `references/sfb-voice.md`
- **Angie Tang Tompkins** → `references/att-voice.md`
- **Katherine Fletcher** → `references/kf-voice.md`
- **Julie Fontaine** → `references/jf-voice.md`

Do not skip this step. The voice files contain specific tone rules, faith level, content standards, and blog-writing guidance that differ meaningfully between pen names. A post written in the wrong voice undermines the author's brand.

## Step 3: Write the Blog Post

Write the complete post using the calendar blueprint (or user-provided direction) and the voice profile. Every post must feel like something this specific author wrote for their specific readers — not a generic "author blog post."

### Structure

**Hook (first 50–75 words)**
Open with something that earns the reader's attention immediately. A surprising revelation, a specific moment, a counter-intuitive claim, or a scene that puts the reader right in the middle of something interesting. Specificity is everything — naming actual books, places, research rabbit holes, or character moments makes the hook feel real and trustworthy.

What not to do: "I've always loved writing." / "As an author, I find..." / "Have you ever wondered..." / "Writing is a journey..."

What to do: Drop the reader into something real and specific. Let the topic grow naturally out of that opening.

**Body (270–430 words)**
Develop the outline bullets — but tightly. One or two paragraphs per point, maximum. If a point can be made in three sentences, make it in three sentences. No padding, no throat-clearing, no recap of what you just said.

Short posts require higher word density. Every sentence either advances the idea, delivers a specific detail, or earns a laugh/emotion. Anything else gets cut.

Use subheadings sparingly — only if the post has 3+ distinct sections. For BTS/personal posts, flowing paragraphs with no subheadings usually read better at this length.

**Hitting the word count**: Aim for the middle of the target range. 400–600 words means aim for ~500. Count before saving. If over 600, cut the weakest section first. If under 400, expand one section with a second concrete detail — never add filler.

**Transition to CTA (30–60 words)**
Near the end, connect the post's theme organically to the author's books, newsletter, or community. This should not feel like a commercial break — the transition should grow out of the content. Then deliver the CTA from the calendar.

**Closing (1–3 sentences)**
A brief, warm sign-off that matches the pen name's personality (see voice files). Leave the reader feeling like they just had a good conversation with someone worth following.

### Universal Content Rules (All Pen Names)

- **No profanity** — Including "freaking," "heck," or any substitute swearing.
- **No em dashes** — Use commas, periods, ellipses, or rewrite. Hard rule, no exceptions.
- **No AI-isms** — Purge: "delve into," "tapestry," "it's important to note," "I hope this helps," "as an author," "in conclusion," "I want to share with you," "let's explore," "fascinating," "boundaries," "showcase," "transform."
- **No generic openers** — Never start with "As an author," "Writing is a journey," or "Have you ever wondered."
- **First person throughout** — The author speaks directly to their readers.
- **Specificity over generality** — Name actual books, actual character names, real research details, real places. Specificity = authenticity.
- **Short paragraphs** — 3–4 lines maximum. White space keeps readers scrolling. Long blocks of text lose people.
- **Sentence variety** — Mix short punchy sentences with longer, rhythmic ones. Fragments for impact when the pen name calls for it.

### SEO Integration

Weave SEO keywords naturally:
- At least one keyword in the first 100 words
- One keyword in a subheading (if using subheadings)
- Keywords distributed through the body — never forced or repeated awkwardly
- The post should read naturally to a human first; SEO is secondary

### CTA Placement and Matching

Place the CTA after the content has delivered real value — earned, not bolted on.

Match tone to post category:
- **Reader Connection** → Soft, conversational ("Tell me in the comments..." / "Tag a friend who gets this")
- **Authority/Craft** → Credibility-building ("Follow along for more craft posts" / "Save this if you're working on your own manuscript")
- **List-Building & BTS** → Compelling subscriber hook ("Want the deleted scene from Chapter 12? It's in my newsletter..." / "Join the insider list — I share things here I don't post anywhere else")
- **Promotional** → Clear action ("Stolen Secrets releases June 2 — grab your copy now" / "The 99-cent sale ends Sunday")

## Step 4: Voice Review Before Output

After drafting, check the post against these questions:

1. Does the opening sound like this specific author, or could it belong to any blogger?
2. Is the sentence rhythm right for this pen name? (SFB: punchy and cinematic; ATT: warm and conversational; KF: witty and observational; JF: reflective and emotionally precise)
3. Are there any em dashes? Remove them all.
4. Any AI-isms? Remove them.
5. Does the faith level match? (SFB: Christian/Catholic woven naturally; ATT: peripheral/ambient; KF: woven into small-town texture; JF: slightly more present, emotional landscape)
6. Does every section feel specific and earned, or does any part read as filler?

Revise until the answer to all of these is yes.

## Step 4.5: Em Dash Elimination (Mandatory Before Writing)

Before you write a single word of content, understand this: em dashes (—) will not appear anywhere in the final document. Not in the post title. Not in subheadings. Not in the body. Not even if the user's calendar row provided a title that contains one.

**If the provided post title contains an em dash**, replace it before using it:
- "Prague — And the One Thing" → "Prague: And the One Thing" (or rewrite)
- "Writing (When the Chapter Won't Cooperate) — A BTS Post" → "Writing When the Chapter Won't Cooperate: A BTS Post"

**While writing the body**, whenever you feel the urge to use an em dash, use one of these instead:
- Mid-sentence aside → use commas: "KC, who knew better, ran anyway."
- Abrupt break or emphasis → use a period and new sentence: "She was right. I fixed it."
- Trailing off → use an ellipsis: "The thing is..."
- Range → use "to" or "through"

**After drafting**, run a visual scan and replace any em dashes that slipped in. Then, after building the .docx with python-docx, run this final check in your script:

```python
# After creating the document, scan all text for em dashes
em_dash = "\u2014"
for para in doc.paragraphs:
    if em_dash in para.text:
        # Replace and fix — log the fix
        for run in para.runs:
            if em_dash in run.text:
                run.text = run.text.replace(em_dash, ",")
```

This is a hard rule with zero tolerance. A single em dash in the final file is a failure.

## Step 5: Create the .docx File

Read `/sessions/intelligent-adoring-goldberg/mnt/.claude/skills/docx/SKILL.md` for the full docx creation instructions. Then build the Word document.

### Document Formatting

- **Title**: Post title, centered, bold, 16pt, dark navy (#1F3864)
- **Byline**: "By [Pen Name]" centered, 12pt, italic, medium gray
- **Body**: 12pt Calibri, left-aligned, 1.15 line spacing, 0.5" paragraph spacing after
- **Subheadings** (if used): 13pt bold, left-aligned, same navy
- **Word count**: "(~XXX words)" right-aligned, 10pt, light gray, at document end
- **Margins**: 1" all sides

### File Naming and Save Location

```
/sessions/intelligent-adoring-goldberg/mnt/Claude Cowork/[PenName]-BlogPost-[YYYY-MM-DD]-[3-4WordTitle].docx
```

Use the scheduled publish date from the calendar if provided, otherwise use today's date.

## Step 6: Deliver

Provide:
1. A link to the .docx file
2. A 1–2 sentence note on the voice choices made (what made it feel like this pen name)
3. Quick confirmation: no em dashes ✓ | no profanity ✓ | faith level correct ✓ | CTA included ✓

---

## Voice at a Glance

| Pen Name | Blog Tone | Faith Level | Rhythm | Comps |
|---|---|---|---|---|
| S.F. Baumgartner | Cinematic, insider, punchy thriller authority | Christian/Catholic woven naturally | Hit, hit, breathe, hit | Patterson, NCIS |
| Angie Tang Tompkins | Warm, friendly, community reader-first | Peripheral — ambient texture only | Warm and brisk, conversational | Macomber, Joann Fluke |
| Katherine Fletcher | Witty, cozy, observational, gently funny | Woven into small-town texture | Warm, brisk, with humor beats | Murder She Wrote, Castle |
| Julie Fontaine | Emotionally precise, reflective, intimate | Slightly more visible — emotional landscape | Slower, interior, still forward | Macomber, Katherine Center, JoJo Moyes |

Full voice details are in the `references/` folder — always read the relevant file before writing.
