---
name: show-dont-tell-fiction
description: "Diagnostic and drafting tool for show-don't-tell across general fiction — thriller, mystery, literary, horror, sci-fi, fantasy, historical, and upmarket. Use whenever a fiction writer wants to fix telling in their prose, draft scenes that show instead of tell, or train their AI to stop summarizing and start rendering. Triggers on 'show don't tell,' 'my writing is too telling,' 'fix this passage,' 'rewrite with show not tell,' 'draft this scene showing,' 'the emotion isn't landing,' 'this reads like a summary,' or any request to diagnose or draft fiction that needs sensory grounding, character reaction, or subtext. Calibrates to genre — thriller dread, literary restraint, horror wrongness, sci-fi/fantasy world-through-character. Two modes — DIAGNOSTIC (writer pastes prose, AI flags telling) and DRAFTING (AI writes fresh with show-don't-tell baked in). Also use when a scene feels flat or a character feels distant."
---

# Show Don't Tell — General Fiction Edition

A working tool for fiction writers across genres who want their AI to stop narrating and start rendering. This skill operates in two modes and calibrates to genre.

---

## How to use this skill

**First, identify the mode the writer needs:**

- **DIAGNOSTIC MODE** — the writer pastes a passage and wants it fixed. Flag every instance of telling, explain why it's telling, and propose a showing swap.
- **DRAFTING MODE** — the writer wants a scene written from scratch with show-don't-tell baked in. Ask for the setup, then draft using the rendering rules below.

**Second, calibrate to genre.** A character feeling afraid lands differently in literary fiction, thriller, and horror. Same principle, different execution. Always ask the genre if it isn't clear.

**Third, don't over-correct.** Telling has a job. Use the override rules in the final section before turning every line into a sensory paragraph.

---

## What "telling" actually looks like in fiction

Writers tell in six specific ways. Scan for these patterns.

### 1. Emotion labels
The writer names the emotion instead of rendering it.
- "She was afraid."
- "He was furious."
- "He felt betrayed."
- "She was happy for the first time in years."

### 2. State-of-being verbs doing the heavy lifting
*Was, were, felt, seemed, appeared, looked.* Not banned — but when they're carrying the emotional or atmospheric weight of the sentence, the writer is summarizing.
- "The house was creepy."
- "He was exhausted."
- "The meeting felt tense."

### 3. Summary narration
The writer compresses a scene that should be experienced.
- "They argued for an hour."
- "She spent the week trying to forget him."
- "The interrogation went on past midnight."

### 4. Internal labeling
The POV character diagnoses their own feelings or thoughts in a way that flattens them.
- "He realized he'd been wrong his whole life."
- "She knew she couldn't trust him."
- "He understood now what his father had meant."

### 5. Character description by adjective
Telling the reader who a character is instead of showing them acting like it.
- "He was a ruthless man."
- "She was kind but guarded."
- "He was the smartest person in the room."

### 6. Worldbuilding by exposition (sci-fi, fantasy, historical)
Dumping information instead of threading it through character experience.
- "The kingdom had been at war for a hundred years."
- "The colony ships had left Earth in 2247."
- "In Regency England, women could not inherit property."

---

## Diagnostic mode — how to run it

When a writer pastes a passage:

1. **Read the whole passage first.** Don't flag line-by-line on first read.
2. **Identify the emotional or atmospheric beats** the scene is trying to land.
3. **Tag each instance of telling** using the six categories above.
4. **For each tag, propose one showing swap** calibrated to the writer's genre and voice.
5. **Flag any sentences where telling is actually correct** (see override rules) so the writer doesn't over-correct.

**Output format:**

```
ORIGINAL: [quoted sentence]
TAG: [which of the 6 patterns]
WHY: [one sentence on what's being summarized]
SWAP: [rewritten sentence]
```

Keep the feedback specific. Don't say "this is telling" and move on — name the pattern and show the fix.

---

## Drafting mode — how to run it

When a writer asks for a scene drafted fresh:

**Before drafting, confirm:**
- Genre and subgenre (literary, commercial thriller, cozy mystery, cosmic horror, epic fantasy, etc.)
- POV character and POV type (first, close third, omniscient)
- What the scene needs to accomplish (suspense? revelation? rupture? quiet dread?)
- Setting and any physical stakes
- Tone and voice notes

**Then draft using these rules:**

1. **Name the body, not the feeling.** A swallow, a hand that won't stay still, a stomach that registers the room before the brain does.
2. **Use the five senses unevenly.** Pick the two that matter for this scene. Thrillers often live in sight and sound. Horror lives in smell and touch (wrongness is tactile). Literary fiction lives in the unexpected sense — the one that surprises the reader.
3. **Let dialogue carry subtext.** What the character doesn't say is often the showing. The pause before an answer does more than the answer.
4. **Anchor internal reaction to a specific trigger.** Not "he was suspicious" but "he noticed she hadn't asked how he got the number."
5. **Worldbuild through friction.** A character bumping into a rule of the world shows the world. A paragraph explaining the rule tells it.
6. **Stay in real time for beats that matter.** If the scene is doing real work — emotional, tonal, atmospheric — don't compress it.

---

## The swap library — by beat and genre

Before/after pairs organized by the emotional or atmospheric work the scene is doing.

### Fear / dread

**TELL:** She was afraid of what was upstairs.

**SHOW (thriller):** She stood at the bottom of the stairs with her hand on the light switch. She didn't flip it.

**SHOW (cosmic horror):** The stairs looked the same. They were not the same. She could not have said how she knew.

**SHOW (literary):** She had been climbing these stairs since she was four years old. Tonight she counted them.

---

### Anger

**TELL:** He was furious.

**SHOW (thriller):** He set the glass down on the bar. The bartender, who had been about to say something, did not say it.

**SHOW (literary):** He folded the letter back into its envelope. He folded the envelope in half. He did this slowly, with great attention, as though it were a task he had been assigned.

---

### Suspicion

**TELL:** She didn't trust him.

**SHOW:** He'd said his mother was from Tulsa. In the kitchen, he'd said Tulsa was where his sister lived. She filed it.

---

### Grief

**TELL:** She was devastated by her father's death.

**SHOW (literary):** She made the phone calls. She ordered the flowers. She stood in the funeral home and shook the hands of men she had not seen since she was a child. At home, alone, she could not remember if she had eaten.

**SHOW (upmarket):** The grocery store was impossible now. The cereal aisle especially. He had been the one who ate cereal.

---

### Exhaustion

**TELL:** He was exhausted.

**SHOW:** He'd been reading the same paragraph for six minutes. He didn't notice until he did.

---

### A character's nature (instead of adjective)

**TELL:** She was the kindest person he'd ever known.

**SHOW:** She'd stopped the car three times on the drive up. Once for a turtle. Once for a man whose tire had gone flat. Once for no reason he could identify, just because she needed a minute.

---

**TELL:** He was a ruthless man.

**SHOW:** He waited until she was crying before he named his price.

---

### Atmospheric wrongness (horror)

**TELL:** The house felt wrong.

**SHOW:** The hallway was longer than it had been that morning. He counted the doors. There were seven. There had been six.

---

**TELL:** The town was unsettling.

**SHOW:** No one in the diner was eating. They had plates in front of them. The plates had food on them. The forks stayed on the table.

---

### Suspense / building tension (thriller)

**TELL:** She knew something was about to go wrong.

**SHOW:** The car behind her had followed her through three turns. The fourth turn was into her own driveway. She kept driving.

---

### Worldbuilding through character (sci-fi / fantasy)

**TELL:** In this world, magic was outlawed and carried a death sentence.

**SHOW:** She waited until the lamp was out and the door was locked before she let the flame curl up between her fingers. Even then, only for a second. Even then, only because her hands wouldn't stop shaking.

---

**TELL:** The colony had been on the planet for three generations and had lost most of its technology.

**SHOW:** The radio in the mayor's office had been his grandfather's. No one alive knew how to fix it. It still worked, though, on the good days.

---

### Revelation / understanding

**TELL:** He realized he'd been lied to his whole life.

**SHOW:** He read the letter twice. Then he sat down at the kitchen table and looked at his hands for a while. He did not get up when the kettle started.

---

### Intimacy between non-romantic characters (friendship, family)

**TELL:** She loved her sister more than anyone.

**SHOW:** She'd driven four hours to bring her soup. She pretended the soup was the reason.

---

### Quiet menace (villain POV or villain on-page)

**TELL:** He was dangerous.

**SHOW:** He asked about her daughter's school by name. She had not told him her daughter's name.

---

## Genre-level calibration rules

The principle is the same across genres. The execution is not.

**Thriller / suspense:**
- Showing lives in specific detail that carries implication.
- The reader should see the threat before the character fully registers it.
- Physical response is often delayed — the body reacts before the brain understands.
- Short sentences. Clean syntax. Let white space do work.

**Literary fiction:**
- Showing lives in restraint and the unexpected specific.
- The sense detail should surprise — the one the reader didn't expect.
- Subtext carries most of the emotional weight.
- Sentences can breathe longer. Syntax can do more work.

**Horror / dark fiction:**
- Showing lives in wrongness — something that should not be what it is.
- Smell and touch do more work than sight.
- The reader should feel dread before the character names it.
- Specificity is terrifying. Vagueness is not.

**Sci-fi / fantasy:**
- Showing worldbuilds through character friction with the world's rules.
- A character breaking a rule teaches the rule. A paragraph explaining it does not.
- The alien / magical thing should be rendered through the character's body, not through narration.

**Historical fiction:**
- Showing threads period detail through action, not exposition.
- The character should bump into the period — its constraints, its textures, its assumptions — not describe it.
- A woman who knows she cannot sign the document shows the period better than a paragraph about women's rights.

**Mystery / cozy:**
- Showing plants clues in the texture of the scene.
- The detective should notice specific, renderable things — not "something seemed off."
- Dialogue does heavy lifting for character and clue both.

---

## When telling is actually correct — the override rules

Don't over-correct. Telling has four legitimate jobs in fiction:

1. **Transitions and time skips.** "Three weeks passed." "They spent the winter underground." Compressing off-screen time is telling and that's fine.
2. **Low-stakes beats.** Not every sentence needs sensory grounding. "She made coffee" is fine if coffee isn't the point.
3. **Pacing control.** After a sensory-heavy scene, one or two lines of summary lets the reader breathe before the next beat lands.
4. **Voice and commentary.** In first-person or close third with a strong narrative voice, telling IS the voice. A narrator who says "He was the kind of man who had never been told no" is doing character work, not lazy writing.

**Rule of thumb:** If the scene is doing real work — emotional, atmospheric, tonal — show it. If the scene is moving characters from Point A to Point B, telling is fine.

---

## Common AI failures in fiction show-don't-tell

Flag these when you see them. They're the patterns that make AI-generated fiction feel flat.

1. **Universal body cues.** Pounding hearts, sweating palms, shaking hands. Specific body = specific character. Generic body = generic scene.
2. **Over-signaling atmosphere.** "A chill ran down her spine." "The hair on the back of his neck stood up." These are tells, not shows. Real unease is rendered in the specific — what the character notices but can't quite explain.
3. **Naming the emotion after showing it.** "Her hands trembled. She was afraid." The second sentence erases the first. Trust the reader.
4. **Weather as emotional shorthand.** Storms for conflict. Sunsets for hope. Fog for mystery. Lazy.
5. **Exposition dumps disguised as dialogue.** "As you know, Bob, our planet has been at war for fifty years." If a character is explaining something the other character already knows, the writer is telling the reader.
6. **Telling atmosphere with adjectives.** "The room was tense." "The silence was heavy." Render what makes it that way instead.

---

## Quick checklist for the writer

Before sending a scene out, scan for:

- [ ] Any sentence with "was/were/felt/seemed" that's carrying emotional or atmospheric weight
- [ ] Any named emotion (afraid, furious, devastated)
- [ ] Any adjective-as-character-description ("he was ruthless," "she was kind")
- [ ] Any compressed beat ("they argued," "she grieved")
- [ ] Any universal body cue (pounding heart, shaking hands, chill down the spine)
- [ ] Any sentence where the POV character diagnoses their own feelings or realizations
- [ ] Any worldbuilding paragraph that explains instead of renders

If any of these are in a scene doing real work, swap them. If they're in a transitional beat, leave them alone.
