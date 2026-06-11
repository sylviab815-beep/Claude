# Workflow Steps

Detailed instructions for each phase of the romantic suspense outlining process. Complete each step fully, present the output, then pause and wait for user input before proceeding.

## IMPORTANT: Names & Places to Avoid

At the very start of the workflow (before generating any content), read the bundled file `references/ai-names-avoidance.md`. It contains lists of overused AI-generated character names, place names, business names, title words, and descriptive clichés.

**This list must be respected throughout the ENTIRE workflow.** Every name, place, title, and business generated at any step must be checked against it. This applies to:
- Story idea titles (Step 3)
- Character names — first and last names (Steps 4, 5, 6)
- Place names, business names, street names (Step 9)
- Any other named elements throughout

Follow the "Alternative Approaches" guidance in that document for generating fresh, non-cliché names. No "Blackwood" estates. No "Sarah/Jack" generic thriller names. No "The [Dark Adjective] [Noun]" titles.

---

## Step 0: K-Lytics Market Data Setup

Before starting, check whether the user has a K-Lytics genre report for romantic suspense (or an adjacent genre like contemporary romance or thriller).

Use AskUserQuestion to ask:

**Question**: "Do you have a K-Lytics genre report you'd like me to use? These reports give us real market data on what's selling — tropes, reader expectations, heat levels, and length trends. They're especially useful for romantic suspense, which sits at the intersection of romance and thriller markets."

**Options**:
- **Yes, I have one** — "I'll upload my K-Lytics report"
- **No, I don't have one** — "Proceed without market data"
- **What's K-Lytics?** — "Tell me more"

### If yes:
Ask them to upload the report. Once uploaded, extract:
- Top-selling tropes and romantic suspense subgenre trends
- Reader expectations for heat level and relationship pacing
- Marketable threat/danger types that pair well with romance
- Length and series vs. standalone trends

Store these findings to inform Steps 2 and 3.

### If no:
Respond warmly: "No problem — I'll use my own knowledge of what romantic suspense readers are buying right now. If you ever want to grab a K-Lytics report, you can find them at https://k-lytics.com/dap/a/?a=24047. Let's get started!"

### If what's K-Lytics?:
Explain briefly:

"K-Lytics produces market research reports for book genres — breaking down what's selling, which tropes are trending, reader expectations, pricing, and more.

You can browse their genre reports here: https://k-lytics.com/dap/a/?a=24047

But they're totally optional for this process! Would you like to proceed without one?"

---

## Step 1: Genre Setup

Use AskUserQuestion to gather three things:

**Question 1 — Romantic Suspense Flavor**:

Romantic suspense has distinct flavors that set the tone of both the danger and the romance. Which best fits the story you want to tell?

Options (up to 4 at a time — present first group, then ask if they want more options):

**Group 1**:
- **Small-Town Romantic Suspense** — Danger arrives in a tight-knit community where everyone knows everyone. Secrets are harder to keep AND harder to escape.
- **Domestic Suspense with Romance** — The threat lives close — in the home, the neighborhood, the workplace. The protagonist can't tell who to trust, including possibly herself.
- **Cozy Romantic Suspense** — Lighter stakes, amateur sleuth energy, warm community. The danger is real but the tone is warmer — think mystery-lover romance.
- **Other / I'll describe it** — Custom subgenre

If they ask for more options, present:
- **Military / Security Romance** — Hero has a protective role (former military, bodyguard, law enforcement). The romance and the danger both run through his presence.
- **Spy / Espionage Romance** — High-stakes international or organizational threat. The danger is sophisticated, the settings are varied, and the trust issues run deep.
- **Psychological Romantic Suspense** — The threat is partly internal or gaslighting — the protagonist isn't sure what's real. The romance may be part of the uncertainty.
- **Romantic Thriller** — Thriller-paced danger with romance as a co-equal A-plot. Plot-driven, action-forward, both arcs at full intensity.

**Question 2 — Heat Level**:
- Sweet/Clean (closed door — romantic tension only; physical affection stops at kissing)
- Moderate (fade to black)
- Steamy (open door)

**Question 3 — Series or Standalone**:
- Standalone
- Book 1 of a planned series
- Interconnected standalone (same world, new couple each book)
- Continuing a series (I'll upload previous books)

If they choose interconnected standalone or continuing: ask them to upload any existing world bible, series notes, or previous books so you can maintain continuity.

---

## Step 2: Market Snapshot

### If K-Lytics data was provided:
Briefly summarize the market findings relevant to their chosen flavor and heat level (3-5 bullet points). Then move on.

### If no K-Lytics data:
Share 3-5 bullet points from your own knowledge:
- What's trending in this flavor of romantic suspense right now
- Which romance tropes pair best with this type of danger
- Reader expectations for their chosen heat level
- Series vs. standalone patterns in this space

Keep this concise — it's context for the story ideas, not a lecture.

---

## Step 3: Generate 5 Story Ideas

Generate 5 distinct, compelling story ideas for their chosen flavor. Each idea must:

- Include **at least 3 romance tropes** that pair naturally with this type of danger
- Have a clear **romance hook** (what pulls these two people together) AND a clear **suspense hook** (what the external threat is)
- Show how the two hooks are structurally connected — not just co-existing but intensifying each other
- Have a **working title** that avoids all overused title words from the avoidance list
- Include a 2-3 sentence premise

Make the ideas diverse — vary the protagonist type, the nature of the threat, the relationship starting point, and the tone. At least one idea should make the love interest a source of suspense as well as attraction.

**CRITICAL**: No names from the avoidance list. Every title must be fresh and specific.

**Present all 5 and ask: "Which story speaks to you? You can pick one, ask for changes, or request 5 new ideas."**

---

## Step 4: Hook and Pitch

Once the user selects an idea, generate:

- **Hook**: A single grabby sentence that captures both the romance AND the danger in one breath. Weave in the tropes. Think: what would a reader see on the first line of the back-cover copy?
- **Pitch**: A 150-250 word pitch that introduces the protagonist, the love interest, the threat, ALL confirmed tropes, and the central tension that makes this story impossible to put down. The romance and the danger should both be irresistible in this pitch.

Present and wait for feedback. Revise if asked.

---

## Step 5: Protagonist Bio

Generate a detailed bio using the format from SKILL.md. Key things to get right:

- **The Wound and the Lie must serve both arcs simultaneously.** The wound that makes her resist the romance should also be the wound that makes her vulnerable to the threat (or that caused the situation she's in). This is what braiding looks like at the character level.
- **Her connection to the threat must be specific.** "She's a witness" is thin. Why her, why now, what did she see or know or inherit or do?
- **Her skill set must be real and earned**, not vague competence. What can she actually do, and what can't she do? The limitation is as important as the skill.

**CRITICAL**: No names from the avoidance list. Draw from specific cultural backgrounds, regional naming patterns, or historical names.

**Present the bio and ask for changes. The user may have specific details they want built in.**

---

## Step 6: Love Interest Bio

Generate a detailed bio using the Love Interest format from SKILL.md.

The love interest's most important characteristic in romantic suspense is **ambiguity about his trustworthiness.** He should be genuinely helpful AND genuinely suspicious at the same time — not because the author is playing games, but because the circumstances are genuinely complicated. Design him so that a smart reader could believe either interpretation.

Key things to get right:
- His connection to the threat must create legitimate suspicion, not just narrative convenience
- His "why he's wrong for her" should feel as real as his "why he's right for her"
- His internal conflict should be independent and interesting — not just reactive to her

**Same naming rules apply.**

**Present and wait for feedback.**

---

## Step 7: Antagonist / Threat Architecture

This is the suspense spine. Use the Antagonist/Threat Architecture format from SKILL.md.

The antagonist needs the same depth the protagonist gets. Generic villainy (greed, power, revenge-as-motive) produces generic suspense. A specific, layered antagonist — someone whose logic makes sense even if their methods are monstrous — creates the kind of dread that doesn't let readers put the book down.

Work through these questions and then produce the full architecture:

1. **What type of threat is this?** A specific person? A conspiracy? A secret from the past with present-day consequences? A pattern of events?
2. **What do they want, specifically?** Not just "to get away with it" — why this, why now, why this protagonist?
3. **What do they know that the protagonist doesn't?** This is their power. The outline must track this information asymmetry.
4. **How does their goal intersect with the love interest?** The most powerful romantic suspense antagonists are connected to BOTH leads — not just the protagonist.
5. **What's the reveal schedule?** Map out when the reader learns each layer: first suspicion, first hard evidence, the misdirection (if any), the real reveal.

**Present the full threat architecture and ask for revisions.**

---

## Step 8: Suspense Arc and Information Schedule

Now map the suspense arc as a standalone story engine — before worrying about how it braids with the romance.

### The Suspense Arc Spine

Produce these beats for the suspense track:

- **Inciting Threat**: How does the danger enter the protagonist's life? What's the first signal that something is wrong?
- **Escalation 1**: The threat becomes undeniable. What happens that raises the stakes?
- **False Lead / Misdirection** (if any): What does the protagonist (and reader) believe is true that turns out to be wrong or incomplete?
- **Midpoint Revelation**: Something the protagonist learns that reframes the danger — now she knows more, but it makes things worse
- **Escalation 2**: The threat gets personal. It's not just danger — it's aimed at her specifically, or at someone she loves
- **Maximum Danger**: The worst moment of the external threat — the protagonist is most vulnerable, most isolated, most outmatched
- **The Turn**: How she gets the advantage — using what she's learned, what she's built, who she trusts
- **Resolution**: The external threat is neutralized — but at what cost?

### The Information Release Schedule

Build the table (see format in SKILL.md):

| Chapter | Reader Learns | Still Hidden | Reader Believes (possibly false) |

Map every clue, every misdirection, every revelation. The reader should be able to re-read and say "of course" at every reveal.

**Present and confirm before proceeding.**

---

## Step 9: Romance Arc

Now map the romance arc as a standalone love story — then you'll braid the two together.

Produce these beats using the Nine Romance Arc Beats from SKILL.md:

1. Meet / Alliance
2. Forced Cooperation
3. First Real Connection
4. Deepening Stakes
5. The Almost
6. Trust Break / Misunderstanding
7. Black Moment
8. The Turn
9. HEA / HFN

For each beat: describe what happens, what emotional ground is covered, and what the romantic stakes are.

**Heat level note**: If sweet/clean was chosen, make sure the romantic tension is real and often intense — the heat comes from charged awareness, near-misses, unspoken feelings, and the specific weight of proximity under pressure, not from explicit content. Clean doesn't mean flat.

**Present and wait for feedback.**

---

## Step 10: Braid Map

This is the distinctive step that makes a romantic suspense outline different from either a romance outline or a thriller outline.

Identify 5-8 key braid points — moments where the two arcs directly intersect and change each other. For each:

Use the Braid Map format from SKILL.md.

**What to look for in a strong braid point:**
- Danger creates forced proximity → romance accelerates whether they want it to or not
- Intimacy creates a new vulnerability → the antagonist targets the love interest, or the protagonist realizes how much she has to lose
- A romance revelation changes how the protagonist reads the threat (or vice versa)
- The black moment: the relationship breaks because of something in the suspense arc — not a misunderstanding invented for drama, but a genuine complication from the external threat

**The test for a braid point**: If you could remove the romance from this moment and the danger scene would be unchanged, it's not a braid point. And if you could remove the danger and the romance beat would be unchanged, it's not a braid point either. A true braid point changes *both* tracks.

**Present the braid map and ask for feedback.**

---

## Step 11: Supporting Character Bios

Generate short bios for all supporting characters using the Supporting Character format from SKILL.md.

Romantic suspense has specific supporting character needs:

- **The person who's too helpful** — someone who assists the protagonist but whom the reader (rightly or wrongly) suspects
- **The reliable ally** — someone who's trustworthy and provides information, cover, or support in both arcs
- **The person who holds a key piece of information** — they may not know they have it; the outline should track what they know and when it matters
- **The antagonist's connection** — someone in the protagonist's orbit who (knowingly or not) has ties to the threat

Give each supporting character both a romance-arc purpose and a suspense-arc purpose where possible. Avoid the "pure comic relief" or "pure exposition" character — everyone should earn their place in both storylines.

**Same naming rules apply. No sassy best friend archetypes. Specific, layered personalities.**

**Present and ask if the user wants to add, remove, or change anyone.**

---

## Step 12: Settings List

Create a settings list. For each location include:
- **Name / Location**
- **Description** (2-3 sentences — atmosphere and sensory detail)
- **Romance Scenes likely set here**
- **Suspense Scenes likely set here**
- **Mood / Tone contribution** (what does this place feel like — safe, watched, charged, claustrophobic, deceptively warm?)

**CRITICAL naming rules**: No Maplewood. No Main Street Diner. No "old Victorian with wraparound porch." No Blackwood, Thornfield, or gothic modifier estates. Settings should feel specific to the geography, culture, and demographic of the story world.

Note: in romantic suspense, settings often do double duty — the same place can feel safe in the romance context and menacing in the suspense context. Design with that in mind.

**Present and wait for feedback.**

---

## Step 13: Chapter Outline

This is the main event. Before generating, ask:
- How many chapters? (Remind them: novels typically 25-40 chapters; novellas 15-25)
- Any chapter count or length preferences?

Then generate the full chapter outline using the Chapter Outline Format from SKILL.md. **Every chapter must include every field — both tracks, the braid point, tension level, information tracking, and romance beat.**

**Critical: weave in the braid map.** Every braid point identified in Step 10 must have a corresponding chapter. Don't let the braiding live only in the braid map — it must show up in the chapter entries.

**Information control is law.** The information release schedule from Step 8 dictates when every reveal happens. Do not invent additional reveals, advance the timing, or add clues that weren't planned. The outline's job is to honor the architecture — the writer's job is to execute it.

**Tension never flatlines.** Every chapter either escalates the threat, provides a brief relief valve (which plants a seed for the next escalation), or delivers a revelation. No neutral chapters. Even the tender romance scenes should carry an undercurrent of danger — a feeling that this peace is borrowed.

**The romance arc beats from SKILL.md must all appear.** Account for every beat, distributed appropriately across the chapter structure.

**If the outline is too long to fit in one response**: stop at a natural break point, tell the user what's covered, and offer a "continue" command to keep going. Never truncate chapter entries. Every chapter gets the full treatment.

**Once the full outline is presented, ask for feedback and revisions.**

---

## Step 14: HEA / Aftermath

Generate **at least 3 epilogue / HEA scene options**. Each should:
- Show a different time-jump or vantage point
- Confirm the HEA for the couple — the romance arc needs its landing
- Acknowledge the aftermath of the suspense arc (the danger is gone, but what changed? What was lost? What was built?)
- Vary in approach — e.g., one quiet domestic moment, one with community/secondary characters, one more explicit about the future

**Present options and let the user choose or combine.**

---

## Step 15: Final Delivery

Compile everything into a single .docx document:
- Story idea with hook and pitch
- Protagonist bio
- Love interest bio
- Antagonist / Threat Architecture
- Suspense arc and information release schedule
- Romance arc beats
- Braid map
- Supporting character bios
- Settings list
- Full chapter outline
- Selected HEA / epilogue

Save as `[Title] - Romantic Suspense Outline.docx` and deliver to the user's workspace folder.

---

## Step 16: Would You Like This Story Written?

After delivering the outline, offer:

"Your outline is complete — with both the romance arc and the suspense arc fully mapped and braided together. This outline is ready to hand off to the Romantic Suspense Writer skill, which will turn it into a full manuscript matching your voice.

Would you like this written into a full book?"

Use AskUserQuestion:

**Options**:
- **Yes, and I have a writing sample** — "I'll upload a writing sample so you can match my style"
- **Yes, but no writing sample** — "Write it in a style that fits the genre"
- **Not right now** — "Just the outline for now"

### If yes with writing sample:
Ask them to upload their writing sample. Analyze the style briefly (sentence rhythm, POV depth, tension style, dialogue patterns, pacing, romantic tension approach) and present a summary for their confirmation. Then let them know the Romantic Suspense Writer skill will handle the manuscript.

### If yes without writing sample:
Let them know the Romantic Suspense Writer skill will handle the manuscript, writing in a style that fits their chosen flavor and heat level.

### If not right now:
"Your outline is ready to go. When you're ready to write, just come back and say 'write my romantic suspense' — I'll pick right up from here. Happy writing!"
