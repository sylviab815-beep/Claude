# Editorial Passes — Chapter-by-Chapter Edit

The eleven-pass pipeline run against every chapter. Each pass has a single job; together they catch what a careful copyedit catches, calibrated to the active voice profile.

Run the Chapter Quality Gate first, then run the eleven passes in order. Do not skip. If a pass finds nothing, say so explicitly in the output — silence implies the pass wasn't run.

---

## Chapter Quality Gate — pre-edit and post-edit

**What it does.** Confirms the chapter is ready to move forward as a chapter, not merely clean at the sentence level. This gate is adapted from the Edit Like a Boss quality-check workflow and should run before edits are applied and again after any cleaned replacement or marked-up rewrite is produced.

**Inputs.**
- Pen name, genre, subgenre, and heat/intensity level when available.
- Active voice profile.
- Chapter outline, beat sheet, or chapter prompt when available.
- The full chapter.

**Checks.**
1. **Natural prose.** Flag AI fingerprints, repeated phrases, overused adverbs, generic body cues, and banned-list violations.
2. **Tone match.** Confirm humor, intensity, sensuality, violence, warmth, and language fit the pen name and genre promise.
3. **Outline adherence.** If an outline/prompt exists, confirm the chapter sticks to this chapter's assigned beats only. Flag later-plot leakage, premature resolution, skipped required beats, or a chapter that speeds the book past its intended position.
4. **Arc consistency.** Confirm character, relationship, mystery, suspense, or emotional arcs move in the expected direction for this story position.
5. **Romantic/emotional progression.** For romance and relationship-heavy fiction, confirm the relationship or emotional tension advances appropriately without jumping levels. For other genres, apply this as emotional-stakes progression.
6. **Pacing and transitions.** Flag rushed scene moves, jarring cuts, dead recap, and transitions that need a cleaner bridge or a harder break.
7. **Show vs. tell.** Flag emotion labels, filter-word distancing, summary where the scene should play, and body cues that name a feeling without dramatizing it.
8. **Chapter ending.** Confirm the ending lands on the active story beat with forward momentum. Flag wrap-up, overexplained foreshadowing, post-beat denouement, and endings that deflate the next-page pull.
9. **POV confirmation.** Confirm single-POV integrity unless the profile permits a switch. Flag head-hopping, unlicensed interiority, and tense drift.
10. **Heat/intensity calibration.** Confirm heat, violence, language, fear, or emotional intensity matches the pen name and reader promise.
11. **Banned-list sweep.** Apply the profile's banned vocabulary and action list. If no profile list exists, use the universal AI-tell and body-cue defaults from this skill and `ai-tell-eliminator` when available.

**What to do with failures.**
- In a flagged report, list every failed check with location, reason, and suggested fix.
- In marked-up or cleaned replacement formats, fix every rule-driven failure that can be corrected without changing plot, meaning, canon, POV intent, or author choice.
- If a failure requires an author decision, do not silently fix it. Preserve the text and surface an author-decision flag.
- After applying fixes, run the gate again and include a compact PASS/FAIL summary. Any remaining FAIL must have a reason.

---

## Pass 1 — Voice integrity

**What it does.** Catches banned vocabulary, AI tells, and out-of-voice phrasing.

**Inputs.**
- Profile Section 6 (banned vocabulary, zero tolerance, plus borderline list)
- Profile Section 8 (AI-tell guardrails — categories opted into)
- `author-voice-lock/references/AI_TELL_LIBRARY.md` if the profile opted in
- Profile Section 13 (things the voice avoids)

**What to flag.**
- Every instance of a banned word or construction.
- Every AI tell from opted-in categories.
- Borderline words that exceed the profile's threshold (e.g., "somehow" appearing more than once per chapter).
- Phrasing that drifts toward the patterns in Section 13.

**What to suggest.**
- A specific rewrite per instance, calibrated to the voice (not a generic "remove this").
- Note the rule that was violated.
- If a banned word has an allowed exception (e.g., literal idiom uses), confirm the instance falls outside the exception before flagging.

**Pass 1 example flag.**

> **Line 47:** _The way the light caught his face was something she would remember._
> **Rule:** Banned simile construction ("the way [X] verbs"). Profile Section 6.
> **Suggestion:** _The light caught his face. She would remember it._

---

## Pass 2 — POV & tense consistency

**What it does.** Catches POV drift, head-hops, tense slips, and breaks in the established voice register.

**Inputs.**
- Profile Section 2 (POV, tense, POV switch rules)

**What to flag.**
- A sentence that reports interiority from a non-POV character (head-hop in close third or first).
- A tense slip — past to present, present to past — that isn't a deliberate craft choice.
- A POV switch mid-scene if the profile says "never switch."
- A second-person address (_you walked into the room_) inserted into first or close third.
- An omniscient aside inserted into a close POV.

**What to suggest.**
- Rewrite to stay in POV — render the non-POV character's interiority as observable behavior the POV character could see.
- Restore the established tense.
- Flag the switch and ask if it was intentional rather than silently fixing it.

---

## Pass 3 — Sentence rhythm preservation

**What it does.** This is the "don't fix what's a feature" pass. Catches the editorial reflex to smooth, vary, and tighten signature moves.

**Inputs.**
- Profile Section 3 (sentence rhythm — fragments, em-dashes, colon-lists, same-starter parallels, three-beat closers, negation patterns)
- Profile Section 7 (preferred vocabulary and signature moves to preserve)

**What to flag.**
- A passage where the chapter does a signature move and previous editorial passes (or the original draft) "fixed" it. Restore.
- A passage where the chapter does NOT do a signature move at a moment that calls for one (e.g., a body/intimacy/action peak with no fragment run).

**What to suggest.**
- For the first case, restore the signature move. Explain the rule.
- For the second, flag for the author — "this peak might land harder with a fragment run; up to you" — rather than rewriting.

**Pass 3 example flag.**

> **Lines 112–115:** _I waited for him to answer. Then I noted his expression. Then I went into the kitchen._
> **Rule:** Same-starter parallels are signature in this voice (Profile Section 3). The "varied" version weakens the cadence.
> **Suggestion:** _I waited. I noted. I went in._

---

## Pass 4 — Dialogue mechanics

**What it does.** Tags, adverbs, action beats, character voice consistency.

**Inputs.**
- Profile Section 5 (dialogue mechanics)
- Profile Section 11 (character voice rules — protagonist, love interests, recurring secondaries)

**What to flag.**
- Tag conventions broken (e.g., profile says `said` only, chapter has `whispered`, `barked`, `hissed`).
- Adverb on a tag if profile bans them (_he said softly_).
- Tag where an action beat would do more work, or the reverse, depending on profile preference.
- A character speaking out of voice — flat dialogue in a character whose voice is signature, or a tic from one character bleeding into another.
- `said` used for a question, or `asked` used for a statement, if the profile distinguishes.

**What to suggest.**
- Replace with the convention the profile establishes.
- For voice drift, rewrite the line in the character's actual register if Section 11 has enough detail; otherwise flag with a question.

---

## Pass 5 — Filter words & show-don't-tell

**What it does.** Catches the filter words that distance the reader from the POV character's experience and the telling-instead-of-showing patterns that flatten prose.

**Inputs.**
- Universal filter-word list (below)
- Profile Section 7 (signature moves) — some voices use filter words deliberately; preserve those uses

**Filter words to flag (default list).**
- _watched_ (when the POV character is watching something happen — usually rewrite to render the thing directly)
- _noticed_
- _saw_ (in the sense of perception, not visual detail)
- _heard_
- _felt_ (when used to introduce an emotion the prose could render)
- _realized_
- _seemed_ / _seemed to_
- _started to_ / _began to_ (almost always a tell — either the action happened or it didn't)
- _decided to_
- _thought_ (in close POV, often unnecessary)
- _wondered_

**What to flag.**
- Every filter-word instance, in context, with a rewrite suggestion.

**What to suggest.**
- Rewrite to render the perception directly. _She watched him cross the room_ → _He crossed the room_ (the POV is hers; we know she's seeing it).
- For _started to / began to_: just do the action. _He started to stand_ → _He stood_.
- For _felt_: render the body data. _She felt anxious_ → render the anxiety as physical observation.

---

## Pass 6 — Tone consistency

**What it does.** Catches tonal slips — passages that read in a register inconsistent with the profile and the rest of the chapter.

**Inputs.**
- Profile Section 1 (one-sentence voice summary)
- Profile Section 9 (genre and trope guardrails)
- Profile Section 13 (things the voice avoids)

**What to flag.**
- A passage that slips into therapy-speak when the voice doesn't use it (_she was processing the loss_).
- A passage that slips into romance-novel cadence beats when the voice avoids them (_her heart pounded as he stepped closer_).
- A passage that slips into clinical detachment when the voice runs warm.
- A passage that slips into authorial commentary or genre-aware winking.
- A passage that slips into adjective-stack overwriting (_the cold, dark, oppressive house_).
- A modern-sense word in a historical voice, or vice versa.

**What to suggest.**
- Rewrite the passage in the established register.
- If the slip is short (a phrase or sentence), surgical fix.
- If the slip is paragraph-length, flag and rewrite, noting which voice rule was violated.

---

## Pass 7 — Repetition & tic words

**What it does.** Catches words and phrases used more times than the chapter's length warrants, including unconscious tic words.

**Inputs.**
- Universal echo-flag thresholds (below)
- Profile Section 6 borderline list (some words have explicit per-chapter limits)

**Default thresholds (profile can override).**
- A distinctive content word (any noun, verb, or adjective that isn't a function word) appearing 3+ times in the same paragraph: flag.
- A distinctive content word appearing 5+ times in a 1,000-word chapter span: flag.
- Profile-listed borderline words (_somehow_, _almost_, _moment_, etc.) exceeding their per-chapter limit: flag.
- Common physical-action words used as tics (_nodded_, _smiled_, _shrugged_, _looked_) appearing more than once per page on average: flag.

**What to flag.**
- Each instance, with line numbers, and a count.
- Whether the repetition is rhythmic (signature) or unconscious (tic).

**What to suggest.**
- For tics, vary the action or cut.
- For signature repetition (a refrain), confirm the author intended it before "fixing."
- For body-language tics, often the right fix is to delete the action altogether — the line of dialogue carries.

---

## Pass 8 — Continuity (within chapter)

**What it does.** Catches contradictions inside this chapter. Cross-chapter continuity is out of scope (use a series-keyed editing skill or whole-manuscript polish for that).

**Inputs.**
- The chapter itself

**What to flag.**
- Names spelled differently (e.g., _Caitlin_ in paragraph 4 and _Kaitlyn_ in paragraph 9).
- Age, height, hair color, eye color contradictions.
- Timeline contradictions (_an hour later_ followed by _it had been twenty minutes_).
- Physical position contradictions (a character described as sitting, then standing without the move being narrated).
- Object contradictions (a glass empty, then full, with no refill).
- Weather or time-of-day contradictions inside the same scene.
- Established facts contradicted later in the chapter.

**What to suggest.**
- Identify which version is correct (or flag both as needing the author's call).
- Suggest the minimal fix.

---

## Pass 9 — Structure & shape

**What it does.** Asks whether the chapter does what a chapter should do.

**Inputs.**
- Profile Section 9 (genre — different genres have different chapter expectations)
- The chapter itself

**What to flag.**
- A chapter with no clear opening hook, escalation, and button.
- A chapter that's all one beat with no movement.
- A chapter that ends mid-conversation in a way that reads as accidental rather than crafted.
- A chapter so long it's actually three chapters and should split.
- A chapter so short it's actually a scene and should merge.
- Pacing problems — too much exposition front-loaded, climax buried, etc.

**What to suggest.**
- Specific structural notes ("scene 2 could move to chapter 4 — it doesn't escalate from scene 1," "consider closing on the dialogue exchange in line 312 — the two paragraphs after it are denouement that belongs to chapter 6").
- Don't rewrite chapter structure. Flag and let the author decide.

---

## Pass 10 — Opening & closer audit

**What it does.** Looks closely at the first and last paragraphs.

**Inputs.**
- Profile Section 1 (voice summary — opening should sound like this voice immediately)
- Profile Section 12 (things the voice does)

**What to flag in the opening.**
- A weak hook — first sentence is generic, weather, or scene-setting that could open any chapter.
- A long expository ramp before the chapter actually starts.
- An opening that introduces a character or place without the voice signature being evident.
- An opening that telegraphs the chapter's plot in the first line.

**What to flag in the closer.**
- A limp button — the chapter trails off rather than landing.
- A button that overstates ("and that was when she realized everything had changed").
- A closer that resolves a tension the chapter just opened.
- A closer that doesn't propel the reader to the next chapter.

**What to suggest.**
- Specific rewrite candidates for openings and closers, calibrated to the voice's signature moves (e.g., a three-beat closer if the profile uses them; a withheld noun if the voice withholds; a single short sentence if the voice favors them).

---

## Pass 11 — Worldbuilding canon

**What it does.** Enforces the capitalization and lowercase rules from the profile.

**Inputs.**
- Profile Section 10 (worldbuilding hooks — capitalize/lowercase lists, recurring proper nouns, recurring motifs)

**What to flag.**
- A common noun the profile says stay lowercase but the chapter capitalized (_The Binding_ when canon is _the binding_).
- A proper noun the profile says capitalize but the chapter lowercased (_the hollow_ when canon is _the Hollow_).
- A new proper noun the chapter introduces that isn't in the profile — flag for the author with the question of canon vs. invention.
- Inconsistent spelling of profile-listed proper nouns (e.g., _Vauclain_ vs. _Vauclair_).

**What to suggest.**
- Direct fix per the canon list.
- For new proper nouns, ask before assuming.

---

## When a pass needs profile content the profile lacks

Some profiles are skeleton-thin. If a pass needs Section X and the profile left it blank, run the pass at universal default and note in the delivery that the pass was constrained.

Example: if Profile Section 11 (character voice rules) is empty, Pass 4 (dialogue) still runs against universal dialogue mechanics from Section 5, but it can't flag character-voice-drift specifically. Note this in the output.

---

## Pass output summary

Every pass produces a section in the chosen output format. The summary at the end of every chapter delivery should include:

- Chapter Quality Gate results, including any checks constrained by missing outline, profile, or heat calibration.
- Total issues flagged per pass.
- Any pass that was constrained or skipped (and why).
- Top three highest-priority issues across all passes.
- A confidence note if any flag is uncertain.

The author can then choose to apply, ignore, or push back on each flag.
