# Editorial Pipeline — Edit-As-You-Go + End-of-Book

The Codex to Manuscript skill runs two editorial loops:

1. **Edit-As-You-Go** — a fast per-chapter pass that runs immediately after each chapter is drafted. Catches AI tells, voice drift, and rhythm issues before they compound across a 50-80k-word manuscript.
2. **End-of-Book Pipeline** — the full five-pass editorial sweep, run once the whole manuscript is drafted.

Skipping the per-chapter pass is faster but consistently produces lower-quality output. Default is to run both.

---

## Loop 1: Edit-As-You-Go (per chapter)

**Purpose:** speed + voice lock. Not a comprehensive edit — a fast scan that catches the three things that must not calcify across the whole book.

### Per-chapter steps (run after every chapter is drafted)

**Step 1 — AI-ism scan (2-3 minutes)**

Read the chapter searching for every banned phrase in `ai_ism_scrub.md`. For each hit, revise the sentence. Common offenders:

- "a shiver ran down [their] spine"
- "the weight of the world"
- "she couldn't shake the feeling"
- "little did [they] know"
- "in that moment"
- "the silence was deafening"
- Any sentence starting with "It was as if…"
- Any "navigated the [emotion/situation]" construction
- Em-dash overload (more than 3 em-dashes per page)

**Step 2 — Genre guardrail sweep (3-5 minutes)**

Read the chapter through the lens of the genre's specific guardrail (from `genre_guardrails.md`). Flag any paragraph that violates a rule. Revise. For example:

- Paranormal Romance: did this chapter maintain the otherness rule? Did the magical bond escalate or stagnate?
- Romcom: did the comedy disappear? Are running gags being tracked?
- Dark Romance: did the narrator moralize? Did a redemption beat land too early?

**Step 3 — Voice/style sweep (2-3 minutes)**

If the user provided a writing sample for voice matching, hold the sample's fingerprints in mind and flag any paragraphs that diverge:

- Sentence rhythm (short/long balance)
- Adjective density
- Metaphor register
- Dialogue tag style (terse "said" vs. variant tags)

If the user did not provide a sample, apply the genre default voice register implied by the codex's tone.

**Step 4 — Rhythm pass (2-3 minutes)**

Scan for:

- Paragraphs with 4+ sentences in a row of similar length. Vary.
- Adjective stacks (any noun with 3+ adjectives). Cut to 1-2.
- Dialogue tags with adverbs ("said curiously," "whispered angrily"). Delete the adverb; let the line carry it.
- Chapter-opening exposition. The opening should hit a sensory detail, not a context dump.
- Body language clichés ("his jaw clenched," "she rolled her eyes").

**Step 5 — Log to Edit Log**

Append to `[Book Title] - Edit Log.md`:

```
## Chapter N — [Chapter Title]
Edit-as-you-go pass: [date]
Word count before: X / after: Y
Key fixes:
- [fix 1]
- [fix 2]
Voice notes: [any drift patterns noticed]
Guardrail check: [any rule violations caught]
```

**Step 6 — Move on**

Don't rewrite paragraphs you already edited. The end-of-book pipeline catches anything missed.

---

## Loop 2: End-of-Book Pipeline (run once after all chapters drafted)

The full five-pass editorial sweep. This is where the manuscript becomes publish-ready.

### Pass 1 — AI-ism Deep Scrub

Same banned-phrase list as Loop 1, but exhaustive. Use grep-style thoroughness over the whole manuscript. Flag every instance. Rewrite every flagged sentence.

### Pass 2 — Developmental Edit

Structural read. Focus areas:

- **Plot structure.** Are all the codex's mandatories hit? Are subplots resolved? Does the climax land?
- **Character arcs.** Does each character undergo the arc the codex specified?
- **Pacing.** Are there sagging middle chapters? Is the climax sequence in the right order?
- **Thread tracking.** Are all promised threads from the codex paid off?
- **POV integrity.** Is the alternation pattern (if specified) consistent? Any head-hops?
- **Genre guardrail alignment.** Does the whole book pass each rule of the routed guardrail?

Output: a developmental notes list keyed to chapter. Apply the most actionable.

### Pass 3 — Beta Read

Simulate a target-audience reader for the codex's genre. Focus:

- Did the genre promises pay off?
- Did the relationship/mystery/threat land?
- Were any emotional beats under- or over-played?

Output: a beta-reader-style review with 3-5 concrete suggestions. Implement the clearest ones.

### Pass 4 — Line Edit

Sentence-level polish:

- Repeated words within paragraphs (not intentional repetition).
- Filter words: started, began, seemed, felt, noticed, watched. Cut where they distance the reader.
- Passive voice sweeps where active is stronger.
- Dialogue tag variety check: 95%+ should be "said" or no tag. Variant tags only when the line truly demands it.
- Specificity pass: replace generic nouns with specific ones.

### Pass 5 — Proofread

Final pass:

- Spelling.
- Punctuation (especially comma splices, em-dash use, semicolons).
- Quotation mark consistency (smart quotes, not straight).
- Em-dashes spaced consistently (— with no spaces, or — with thin spaces — pick one and stick with it).
- Number/quantity consistency (was it "twelve" in chapter 3 and "12" in chapter 14?).
- Name/place consistency (this catches typos in renames).

### Pass 6 — Holistic Manuscript Polish

The final whole-manuscript pass. Treats the manuscript as a single cohesive arc and revises for whole-book flow, consistency, and authenticity. Works at a different level than the previous passes — Passes 1-5 each operate at a specific scope (sentence, scene, structure); Pass 6 operates at the level of the entire book.

**Critical rule: preserve chapter length and narrative weight.** Do not shorten or compress scenes during this pass. Honor the codex's word count target.

The five workstreams of Pass 6 (apply all five end-to-end):

1. **Structure, pacing, and flow** — strip artificial chapter endings (philosophical wrap-ups, forced cliffhangers, manufactured mic-drops, end-of-chapter moralizing), replace with mid-scene cuts and forward momentum, improve transitions so the book reads as one arc.
2. **AI artifact removal** — eliminate direct AI references, leftover prompt language ("Write a scene where…"), meta-commentary, POV breaks, generic transitional phrases ("Additionally," "Furthermore," "It's worth noting"), clinical emotion descriptions, artificial precision, and AI-style emotional labeling ("she felt something that could only be described as…").
3. **Dialogue and character voice** — replace stiff/formal dialogue with authentic speech, reduce surname overuse where first names fit the relationship, break repetitive call-and-response patterns, add interruptions and conversational messiness, ensure each character maintains a distinct consistent voice across the whole manuscript.
4. **Narrative authenticity and immersion** — replace forced metaphors and overwriting, simplify inflated sentence structures, remove author-as-character observations, cut filler connectors ("Suddenly," "Just then," "Finally"), keep all sensory detail strictly grounded in the active POV character's awareness and limitations.
5. **Verification** — confirm word count is at or above target, no chapter ends on cliché, no AI artifacts remain, voices are distinct, POV is locked. Append 3-5 before/after examples to the Edit Log.

Full reference: `manuscript_polish.md` in this same folder. Read it before running Pass 6.

---

## ECIS Override (only when the codex specifies open-door / explicit / scorching heat)

The Explicit Content Integrity System runs as part of every editorial pass when applicable:

- **No fade-to-black on scenes the codex marks intimate.** If the chapter outline says "Intimate Beat: Yes" or specifies an explicit scene, write it fully on-page.
- **Anatomical specificity matches the heat level.**
- **Emotional context per scene.** Every explicit scene must serve the emotional arc, not just satisfy a beat count.
- **Consent integration.** Show consent through dialogue, body language, and pacing — not as a checkbox.

If the codex specifies sweet / closed-door, ECIS does not apply — fade-to-black is correct.
