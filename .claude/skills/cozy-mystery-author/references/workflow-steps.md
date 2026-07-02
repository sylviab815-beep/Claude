# Cozy Mystery Author — Workflow

Six phases, executed in order. Apply the Cozy Equilibrium System (`cozy-equilibrium-system.md`) after every chapter and the prose rules (`prose-craft.md`) while drafting.

---

## Phase 1: Get & Verify the Outline

1. Ask the user to paste or share their completed outline from the **Cozy Mystery Outline Builder**.
2. Verify it contains:
   - All chapters with summaries and mystery beats
   - The **suspect roster** (3-5 suspects with motive/means/opportunity) and the designated **killer**
   - The **Clue Ledger** (clues planted → paid off, with red-herring assignments)
   - The **community map** (shop/job, best friend, recurring townsfolk, law-enforcement foil)
   - Paranormal notes (ability, familiar, magic rules) IF paranormal mode
3. If anything critical is missing, ask the user to return to the Outline Builder (or offer to reconstruct the missing piece with them before writing).
4. Confirm the length tier (novella / standard / cozy novel).

---

## Phase 2: Interactive Setup (8 questions via AskUserQuestion)

Ask one at a time; document each answer.

1. **Paranormal mode?** — confirm grounded vs. paranormal (activates Rule 6 and the familiar/magic handling). Should match the outline.
2. **Tone slider** — warm-and-witty ←→ gentle-and-heartfelt.
3. **Heat level** — confirm sweet/clean, closed-door (the cozy default).
4. **POV** — first or third person; single (sleuth) or limited multi.
5. **Tense** — past or present.
6. **Length confirmation** — novella / standard / cozy novel (match the outline).
7. **Author name** — exactly as it should appear on the title page and KDP. (Never assume or hard-code a name — always ask.)
8. **Style sample (optional)** — invite the user to paste a sample of their own prose to match their voice. If none, use the cozy default voice.

Use the answers to calibrate voice, pacing, and emphasis.

---

## Phase 3: Pre-Writing Prep

1. **Load the embedded Names Avoidance List** (`references/names-avoidance.md`). Cross-reference every character, town, business, pet, and familiar name in the outline against it. Replace matches with fresh alternatives and note the swaps for the user.
2. **Build tracking tables** in your working notes:
   - **Clue tracker** — from the outline's Clue Ledger: each clue, plant chapter, payoff chapter, what it points to. Tick off plants and payoffs as you write (Rule 1).
   - **Suspect tracker** — each suspect's viability, last on-page appearance, and red-herring clue status (Rule 4).
   - **Community tracker** — last appearance of the shop, the best friend, and the most recent comfort beat (Rule 5).
   - **[Paranormal] Magic-rules tracker** — the stated rules/limits, so nothing gets shortcut (Rule 6).
3. **Set the output folder** to the user's working folder. Create a clearly named subfolder for this book (title + date). Do not use any private or hard-coded path.
4. **Confirm** the prose rules and the Cozy Equilibrium System are loaded.

---

## Phase 4: Manuscript Writing

For each chapter in the outline:

1. Write the chapter in full prose from the outline's beat, applying `prose-craft.md` as you go.
2. Target word count for the tier:
   - **Novella:** 1,000-2,500 words/chapter
   - **Standard / cozy novel:** 2,200-3,500 words/chapter
3. **Immediately after the chapter, run the Cozy Equilibrium System checks:**
   - Rule 1 — any clue used traces to an earlier plant; log new plants in the clue tracker
   - Rule 2 — violence off-page; warmth present; the ending isn't bleak
   - Rule 3 — the sleuth behaves plausibly; any danger has a safety net; law enforcement is competent
   - Rule 4 — suspect viability is intact; red herrings carry real evidence
   - Rule 5 — the everyday world is present; check the community tracker
   - Rule 6 *(paranormal)* — magic respects its rules; the familiar's info is filtered through animal limits
   - Log any intervention and fix before moving on.
4. Update the trackers. Move to the next chapter.

**Completeness:** every chapter is fully written. No placeholders, no summaries. If context runs short, write in chunks (chapters 1-8, then 9-16, etc.) — never summarize later chapters. Use Task subagents for chunks when helpful, and give each subagent the outline, the CES rules, the prose rules, and the trackers.

**Mystery-craft reminders:** the body is discovered by ~Chapter 2-3 (death off-page); the midpoint recontextualizes a clue; the dark moment is genuine (not "the sleuth feels sad for a page"); the reveal converges 3+ planted clues; the aftermath gets a full chapter (don't compress trial/community reaction); the ending restores the community.

---

## Phase 5: Editorial Pipeline (5 stages)

Execute all five stages from `revision-guide.md` in order:

1. **AI-ism Revision** — strip universal + cozy-specific AI crutches; regenerate affected chapters
2. **Cozy Equilibrium Audit** — re-run all six rules across the full manuscript; fix any chapter that fails
3. **Developmental Edit** — structure, pacing, character, mystery fairness, cozy-tone maintenance; apply the top fixes
4. **Beta Read** — simulate a dedicated cozy reader; honest star rating, the good, the bad, ranked suggestions
5. **Targeted Revision** — apply the top 3 structural fixes; verify continuity; regenerate the .docx

Log all changes per stage.

---

## Phase 6: KDP Metadata & Delivery

1. Generate Amazon metadata (see `kdp-template.md`): title/subtitle, author name, ≤4000-char blurb, 7 keywords, 3 BISAC categories, price point, series info, 3 comp titles, audience profile, cover prompt.
2. Create two files:
   - `[Book Title].docx` — the formatted manuscript (`docx-template.md`)
   - `[Book Title] - KDP Metadata.docx`
3. Save both to the user's working subfolder.
4. Give the user a short delivery summary: word count, chapters, which chapters triggered CES interventions, the names you swapped, and a quick KDP-upload checklist.
