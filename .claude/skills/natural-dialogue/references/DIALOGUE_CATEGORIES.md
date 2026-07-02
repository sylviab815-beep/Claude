# Dialogue Audit Categories

The 14-category framework. Run each in order on the prose. Skip a category in your written audit if it's clean — don't pad with "looks fine" notes. Every category here exists because it has stripped a manuscript of voice when missed.

---

## Table of contents

1. Bare confirmations
2. Filler exchanges
3. Acknowledgment fluff
4. On-the-nose emotional naming
5. Therapy-speak slipping in
6. Excessive politeness
7. Generic tic openers
8. Tag-as-meaning
9. Adverbs on tags
10. Speaker-voice collapse
11. Explainer dialogue
12. Question-then-answer-the-same-question
13. Trailing dot-dot-dot fluency
14. Same-character lexical repetition

---

## 1. Bare confirmations

**What to flag:** Lines of dialogue that consist only of *"Yes."* / *"No."* / *"Okay."* / *"Sure."* / *"Right."* / *"Uh-huh."* / *"Mm-hmm."* / *"I see."* / *"Got it."* / *"Of course."* (when generic).

**Why it matters:** Bare confirmations strip the speaker of voice. They confirm but reveal nothing. A character who says only *"Yes"* could be anyone.

**Allowed exception:** When the bareness IS the characterization — a character stonewalling, refusing to engage, performing flatness as a defense. Flag for author review; never deploy as a default.

**Fix patterns:** Replace with one of —
- **Voice tic** — character's signature register doing its thing
- **Plot information** — specifics about what was heard
- **Reframe** — refuses the assumption embedded in the asker's wording
- **Question back** — turns the exchange around
- **Echo a detail** — signals careful listening

**Examples:**
- ❌ *"You're new?" / "Yes."* → ✓ *"You're new?" / "Showing already?"* (deflection)
- ❌ *"Don't be late." / "Yes."* → ✓ *"Don't be late." / "Five and eight."* (echo, signals attention)
- ❌ *"Mr. Smith?" / "Yes."* → ✓ *"Mr. Smith?" / "Mostly."* (voice tic)

**Grep:** `grep -nE '"\s*(Yes|No|Okay|Sure|Right|Uh-?huh|Mm-?hmm|I see|Got it|Of course)\.?\s*"'`

---

## 2. Filler exchanges

**What to flag:** Greeting/parting/social-script exchanges that mirror real life but produce nothing on the page.

- *"Hi." / "Hi."*
- *"How are you?" / "Good, you?" / "Good."*
- *"Thanks." / "No problem."*
- *"Have a good one." / "You too."*

**Why it matters:** Real conversation is full of these. Fiction skips them. They're the conversational equivalent of describing a character pouring coffee — neutral filler that lowers the page's voltage.

**Allowed exception:** When the filler IS the characterization — e.g., a character who can't move past social scripts because their mind is elsewhere; or a deliberately flat exchange between strangers that's contrasted with a charged exchange a paragraph later. Flag for author review.

**Fix patterns:**
- Cut entirely; jump to the next charged beat
- Replace with action — characters gesture, hand off objects, make eye contact instead of greeting
- Compress — *"They greeted each other."* / *"He nodded; she nodded back."*

**Example:**
- ❌ *"Hi, Sara." / "Hi, Mark." / "How was the drive?" / "Long. Yours?" / "Same."*
- ✓ *He met her at the gate. They didn't greet each other. The drive had been long for both of them and neither needed the small talk.*

---

## 3. Acknowledgment fluff

**What to flag:** Lines that do the work of *Yes* but with more syllables.

- *"I see."*
- *"I understand."*
- *"Of course."*
- *"Got it."*
- *"That makes sense."*
- *"Fair enough."*
- *"Mm."*

**Why it matters:** Same problem as bare confirmations, but harder to grep because the phrases vary. The character is acknowledging without revealing.

**Fix:** Same patterns as Category 1.

**Allowed exception:** As a character voice tic when consistently used by ONE character (e.g., a clinical-detached character whose *"I see"* is signature). Document the tic; ban the same phrase from other characters.

---

## 4. On-the-nose emotional naming

**What to flag:** Characters who name their own emotions directly in dialogue.

- *"I'm angry."*
- *"That makes me sad."*
- *"I'm scared."*
- *"I love you. So much."* (when not earned by buildup)
- *"I'm overwhelmed right now."*

**Why it matters:** Subtext is the medium. Characters who narrate their own feelings strip the reader of the work of inference. Most emotional revelations should land through body, action, what's NOT said, or what's said with deliberate inadequacy.

**Allowed exception:** A character whose voice register IS direct emotional naming (some YA voices, some literary fiction). Document; verify it's a deliberate choice, not drift.

**Fix patterns:**
- Show through body — *Her hands had stopped on the bowl.*
- Show through action — *He left the room.*
- Show through indirection — *"Don't ask me right now," she said.*
- Show through deliberate inadequacy — *"I'm fine," he said. He was not fine.*

---

## 5. Therapy-speak slipping in

**What to flag:** Modern self-help / clinical / therapy-language vocabulary appearing in dialogue where it shouldn't.

- *processing*
- *holding space*
- *boundaries* (modern usage; the literal word is fine)
- *that's valid*
- *let me sit with that*
- *trauma response*
- *triggered* (when not literal)
- *checking in*

**Why it matters:** This vocabulary belongs to a specific cultural-historical moment and a specific register. It's instant anachronism in any setting that isn't contemporary American urban-professional. Even in contemporary fiction, it's overused enough to flatten character.

**Allowed exception:** A specific contemporary-set character who explicitly speaks this register (a therapist, a wellness influencer, a college student in a contemporary novel). Document; restrict to that character.

**Fix:** Translate to the character's actual register. *"That's valid"* → *"You're not wrong."* / *"I hear you."* / silence + a body beat.

---

## 6. Excessive politeness

**What to flag:** *please / thank you / sorry / pardon / excuse me* density inappropriate for the character's register or the situation's intensity.

**Why it matters:** Default LLM dialogue (and tired-author dialogue) leans polite. Most characters under stress, in genre fiction, in working-class registers, in family conflict, etc. don't say *please.* Politeness is data — when overused, it becomes anti-data.

**Audit:** Count *please / thank you / sorry / pardon* per chapter. Flag if density seems wrong for the speaker (a hardened detective shouldn't be saying *thank you* every other line).

**Fix:** Cut. Replace with action, terser phrasing, or silence.

---

## 7. Generic tic openers

**What to flag:** Lines that begin with default LLM/default-fiction tic phrases.

- *"Look,"*
- *"Listen,"*
- *"I mean,"*
- *"Well,"*
- *"So,"*
- *"Right, so…"*
- *"Honestly,"*

**Why it matters:** When every character opens lines this way, the prose loses speaker-voice differentiation. These openers are also LLM defaults — they're the prose-tic of someone trying to sound conversational.

**Allowed exception:** As a single-character voice tic, deployed consistently and flagged. Document.

**Fix:** Cut the opener. Start the line with the substance.

**Example:**
- ❌ *"Look, I just don't think we should…"*
- ✓ *"I don't think we should…"*

---

## 8. Tag-as-meaning

**What to flag:** Tags that do the emotional work the line should have done.

- *"That's enough," she said angrily.*
- *"I love you," he said tenderly.*
- *"Please don't," she begged desperately.*

**Why it matters:** If the line had the right rhythm and word choice, the tag wouldn't need the adverb. The tag-as-meaning move is a confession that the line itself is flat.

**Fix:** Strengthen the line; cut the adverb.

**Example:**
- ❌ *"That's enough," she said angrily.*
- ✓ *"That's enough."* Or: *"That's enough." Her hand had closed on the table edge.*

---

## 9. Adverbs on tags (general)

**What to flag:** Any *-ly* adverb modifying a dialogue tag.

- *softly, gently, sharply, coldly, quietly, harshly, evenly, tenderly, eagerly, reluctantly*

**Why it matters:** Most adverbs on tags are flag-of-flatness (see Category 8). A small number — *evenly, quietly* — can be load-bearing when the data IS the manner of speech (a character speaking *evenly* when reader expects upset). Most are deletable.

**Fix:** Flag every instance. Review case-by-case.
- If the adverb names data the line couldn't carry alone (and stripping the line would be flat) → keep, sparingly
- If the adverb is doing tag-as-meaning work → cut, rewrite the line

**Grep:** `grep -nE 'said [a-z]+ly\b'` plus `grep -nE 'asked [a-z]+ly\b'`

---

## 10. Speaker-voice collapse

**What to flag:** Passages where dialogue could be reassigned between two characters without confusion.

**Why it matters:** Each character should have a register the reader could pick blind. When two characters speak interchangeably, one of them isn't a character.

**Audit:** Take a passage. Strip all tags and attributions. Read. Can you tell who said what? If not, voice collapse.

**Fix patterns:**
- Identify the character with the weaker voice; consult voice profile (if loaded) for that character's specific tics
- Sharpen with: distinct vocabulary, distinct rhythm, distinct pause mechanics, distinct emotional register
- If profile-aware: pull the per-character voice rules; rewrite the weaker character's lines to fit

---

## 11. Explainer dialogue

**What to flag:** Characters telling each other things both already know, for the reader's benefit.

- *"As you know, the Council was formed three centuries ago…"*
- *"Remember when we first met at the lake?"*
- *"Your father, Harold, who was the village blacksmith…"*

**Why it matters:** Insults the reader. Strips the conversation of stakes. Worldbuilding info-dump in costume.

**Fix patterns:**
- Cut the explainer entirely; trust the reader to absorb later
- Move the information to narration where appropriate
- Reframe so one character genuinely doesn't know — e.g., the protagonist is new to the setting, an outsider character is being briefed
- Show through scene — let the reader see the Council's behavior; trust them to infer

---

## 12. Question-then-answer-the-same-question

**What to flag:** Q-and-A exchanges where the response confirms the question without complication.

- *"Are you all right?" / "I'm fine."*
- *"Did you sleep?" / "Yes, I slept."*
- *"You hungry?" / "I'm hungry."*

**Why it matters:** No tension. The asker asks; the answerer agrees. Conversation as confirmation pattern.

**Fix patterns:**
- Reframe the answer — disagree, deflect, observe something else
- Question back
- Echo a different detail
- Refuse to answer

**Examples:**
- ❌ *"Are you all right?" / "I'm fine."*
- ✓ *"Are you all right?" / "I haven't decided."* (Kieran register)
- ✓ *"Are you all right?" / "Why are you asking?"* (deflective)
- ✓ *"Are you all right?" / She finished tying her boot before answering.* (silence as answer)

---

## 13. Trailing dot-dot-dot fluency

**What to flag:** Dialogue that uses ellipses as default emotional shorthand.

- *"I just… I don't know…"*
- *"I mean… maybe?"*
- *"I'm not… I can't…"*

**Why it matters:** When every emotional line trails off, the technique loses meaning. Ellipses are a tool; default-using them flattens character.

**Fix patterns:**
- Commit to the line — let the character finish the thought, or finish refusing to finish it
- Replace with action — *She didn't finish the sentence. She didn't have to.*
- Replace trailing ellipses with mid-sentence em-dashes for self-correction (different beat, used differently)

---

## 14. Same-character lexical repetition

**What to flag:** A character using the same uncommon word two or three times in one exchange.

**Why it matters:** Indicates the prose isn't tracking character voice over the span of the scene. Real characters do repeat themselves — but consciously, as voice tic. Default repetition is drift.

**Audit:** For chapters with significant dialogue, do a frequency check on uncommon words within character-attributed lines. Flag any uncommon word appearing 3+ times in one character's dialogue within a single chapter unless it's a documented voice tic.

**Fix:** Vary. Or — turn the repetition INTO a voice tic by making it deliberate (the character is fixated on this word; the prose acknowledges it).

---

## A note on category weighting

In a typical pass-1 dialogue audit, **bare confirmations**, **filler exchanges**, **on-the-nose emotional naming**, and **explainer dialogue** are the highest-leverage categories. They produce the most flat lines and yield the biggest voice-quality gain when fixed.

In pass-2 and pass-3 audits, **speaker-voice collapse**, **lexical repetition**, **tic openers**, and **politeness density** surface bugs that only become visible once the surface is clean.

If a pass-3 audit on the same chapter only has three new items, that's a healthy chapter. Don't pad.
