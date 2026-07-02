# Guided Intake — Building a Voice Profile From Scratch

A step-by-step interview the skill uses to walk an author through filling in a new profile. Run this when the user wants help building a profile rather than filling in `profiles/_TEMPLATE.md` themselves.

## How to run this intake

1. Confirm the user wants the guided version. If they'd rather fill in the template manually, point them at `profiles/_TEMPLATE.md` and stop.
2. Ask for a pen name first. Decide the filename: `profiles/<pen-name>.md` (lowercase, hyphens for spaces).
3. Create the file with the template's section headings already in place. Empty values for now.
4. Walk through the sections below in order. Ask one section at a time. Wait for the answer. Write it into the profile. Read it back. Confirm. Move on.
5. **Never invent answers.** If the user is stuck on a section, offer concrete examples drawn from `profiles/_EXAMPLE.md` to spark a decision, but do not put words in their mouth.
6. **Push for specificity.** If an answer is vague ("I want punchy prose"), ask a follow-up that forces a concrete rule ("Punchy how — average sentence length? Fragments at action peaks? Three-beat closers?"). Vague profiles produce vague drafts.
7. At the end, save the file, summarize what's in it, and tell the user how to invoke it ("ask me to draft as <pen name>").

---

## Intake questions, in order

### Section 1 — Identity

- "What pen name does this profile belong to?"
- "What genre and subgenre? Adult, YA, NA?"
- "Are there one or two comp authors whose voice your prose lives near? I won't copy them — I just want a calibration point."
- "If you had to describe this voice in one sentence, what would it say?"

### Section 2 — POV & tense

- "First person, close third, omniscient, or multi-POV?"
- "Past or present tense?"
- "If multi-POV, list each POV character and one line on what makes their voice register different."
- "Do you ever switch POV mid-chapter, mid-scene, or never?"
- "Where does interiority live in this voice — the character reporting body data, naming emotions directly, stream-of-consciousness, or kept minimal?"

### Section 3 — Sentence rhythm

- "Default sentence length: short and punchy, medium, long and layered, or deliberately mixed?"
- "Fragments — banned, earned at peaks only, frequent, or load-bearing signature?"
- "Em-dashes — sparse, moderate, or heavy?"
- "Do you use the colon-then-list move? Show me an example from your published prose if you have one."
- "Same-starter parallels — three sentences in a row that begin the same way: signature move you want preserved, allowed, or fix-on-sight?"
- "Three-beat paragraph closers — three short sentences ending a paragraph: signature, allowed, or no?"
- "Negation patterns — _Not anger. Something colder._ — signature, earned, or no?"

### Section 4 — Paragraph density

- "What's a default paragraph length for this voice?"
- "Do paragraphs get shorter or longer at action peaks?"
- "What about at intimacy peaks?"
- "What about at interior reflection?"
- "Breathable pages or dense pages?"

### Section 5 — Dialogue mechanics

- "Default dialogue tag — `said`, varied, or no tags?"
- "`asked` for questions or `said` for everything?"
- "Adverbs on tags — banned, rare, or allowed?"
- "Action beats instead of tags — preferred, mixed, or rare?"
- "Dialect or accent — phonetic spelling, suggestion-only via word choice, or none?"
- "Do you use internal quotation without quote marks for remembered speech?"
- "Are there speaking-of-things-not-said rules — does the prose name the pause when a character doesn't answer?"

### Section 6 — Banned vocabulary

- "Now the heart of the profile: words and constructions that should never appear in a first draft of yours. Give me five to start. We can add more."
- For each: "Why is this banned? Are there any exceptions — literal idiom uses, voice tics, anything?"
- "Are there borderline words you allow but want me to flag for review? Words like 'somehow,' 'almost,' 'moment' that earn their place but lose it if they pile up?"

### Section 7 — Preferred vocabulary & signature moves

- "What does this voice DO that an editing reflex might 'fix' out? Give me three to five signature moves to preserve."
- "Concrete examples are gold here. If you have a passage that captures a signature move, paste it; I'll extract the rule."

### Section 8 — AI-tell guardrails

- "Do you want me to use the universal AI tell library by default? Most authors say yes — it catches the LLM defaults that drift in regardless of voice."
- "Are there voice-specific AI tells you've noticed and want banned? Patterns like 'a sense of unease' or 'the air seemed to thicken' that aren't in your voice but creep in?"

### Section 9 — Genre & trope guardrails

- "Heat level — sweet, steamy, on-page, fade-to-black, off-page-only?"
- "Three to five tropes this voice leans into — what readers come to you for."
- "Three to five tropes this voice avoids — what readers will not get from you."
- "Hard content lines — what never appears, even from villains?"
- "Soft content lines — what can appear but with rules?"

### Section 10 — Worldbuilding hooks

- "Do you write a series or shared world? If yes, what's the world's name?"
- "Setting type — contemporary, secondary world, historical, near-future?"
- "Recurring proper nouns I should always capitalize? Place names, magic system terms, organizations, anything else?"
- "Recurring common nouns I should keep lowercase? Things the prose names but does not grandify with capitals?"
- "Recurring motifs or objects — things that show up in scene without being announced?"

### Section 11 — Character voice rules

- "Tell me about your protagonist's voice tics. What do they notice that other characters wouldn't? What do they avoid naming directly?"
- "How dense is their internal monologue?"
- "Recurring love interest or co-lead — speech register, distinctive vocabulary, banter rules?"
- "Recurring secondary characters with distinctive voices?"

### Section 12 — Things the voice DOES

- "Anything signature that didn't fit cleanly above? Free-form list. I'll preserve these."

### Section 13 — Things the voice AVOIDS

- "Patterns that drift in from default LLM prose or from genre defaults that this voice rejects? Free-form list. I'll watch for these."

### Section 14 — Post-draft grep checklist

- "Section 6 (banned vocab) auto-feeds the grep pass. Anything else you want me to search for after every draft? Patterns too contextual to ban outright but worth flagging?"

### Section 15 — Notes

- "Anything else I should know about how you want me to draft for this voice?"

---

## After the intake

1. Show the user the completed profile.
2. Tell them where it lives: `profiles/<pen-name>.md`.
3. Tell them how to invoke it: "ask me to draft as <pen name>" or "use the <pen name> profile."
4. Suggest they treat it as a living document — when an editorial pass surfaces a new tic to avoid, add it to the profile so the next session catches it during generation.
5. If they have multiple pen names, offer to run intake again for the next one.
