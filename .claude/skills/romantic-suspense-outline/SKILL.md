---
name: romantic-suspense-outline
description: >
  Interactive romantic suspense outlining workflow. Builds the dual A-plot architecture — the
  romance arc and the suspense arc as co-equal, braided storylines that escalate and resolve
  together. Generates 5 story ideas with both romance and suspense hooks, builds protagonist
  and love interest bios with thriller-level depth, develops the antagonist/threat architecture
  with information control fields, maps the information release schedule, and produces a fully
  labeled chapter outline tracking both tracks and their braid points per chapter. Optionally
  uses K-Lytics data. MANDATORY TRIGGERS: "romantic suspense outline", "outline a romantic
  suspense", "rs outline", "outline my romantic suspense", "romantic suspense plotting", "plot
  a romantic suspense", "romantic suspense novel outline", "rom-sus outline", or any mention
  of outlining, plotting, or planning a romantic suspense story. Use this skill even if the
  user just says "outline" when the context involves romantic suspense.
---

# Romantic Suspense Outline

Guide the user through an interactive, step-by-step process to develop a romantic suspense story from idea to complete chapter outline. Every step pauses for user input before proceeding.

Romantic suspense is a genre with **two co-equal A-plots** that cannot be separated:
- **The Romance Arc**: two people falling in love under impossible circumstances
- **The Suspense Arc**: an external threat or mystery that escalates throughout

This skill is built around that core truth. Everything in the outline — character bios, information architecture, chapter structure — is designed to support the braiding of these two tracks.

---

## Core Principles

- **One step at a time**: Complete each step fully, present the output, and WAIT for user feedback before moving on. Never skip ahead or combine steps.
- **Dual-track from the start**: Every story element must serve BOTH arcs. Characters exist in both worlds. Settings carry both romance and danger. The protagonist's wound drives both her romantic reluctance and her vulnerability to the threat.
- **Braiding, not paralleling**: The two arcs don't just run side by side — they intensify each other. Danger accelerates intimacy (forced proximity, shared vulnerability). Intimacy creates new vulnerability to danger (the person they love becomes a target). Design the outline so these tracks push on each other.
- **Information is a weapon**: The suspense arc depends on the careful control of what the reader knows and when. The outline must map this explicitly — every planted clue, every misdirection, every revelation has a place in the chapter order.
- **Market-informed** (when available): Use K-Lytics data if uploaded; otherwise apply your own knowledge of the romantic suspense market.
- **Detail-oriented outlines**: Every chapter in the final outline must include all required fields — both tracks, the braid point, tension level, information tracking, and romance beat. No skimping.
- **Fresh and original**: All names, places, and titles must avoid overused AI patterns. Read the bundled Names & Places Avoidance List before generating any content.

---

## Names & Places Avoidance List

Read `references/ai-names-avoidance.md` before generating any content. It contains comprehensive lists of overused AI-generated character names, place names, business names, title words, and descriptive clichés. All generated content must avoid these throughout the entire workflow.

---

## Number & Time Diversity (Anti-7 Bias)

LLMs default to 7 for "random" numbers. Actively avoid this in all generated content — ages, times, case numbers, addresses, countdown timers, durations. Distribute across all digits. Scan the completed outline for the digit 7 and replace most instances.

---

## Workflow

Read `references/workflow-steps.md` for complete step-by-step instructions for each phase.

---

## Output Formats

### Protagonist Bio Format (for Novelcrafter)
```
Name:
Age:
Occupation:
Physical Description:
Personality Traits:
Backstory:
The Wound (what hurt her in the past that still shapes her now):
The Lie She Believes (false belief driving her choices):
The Truth She Needs (what she must accept to grow):
External Goal (what she wants):
Internal Goal (what she needs):
Connection to the Threat (why she's involved — witness, target, investigator, inheritor of a secret):
Skill Set (what makes her capable of surviving this story):
Vulnerability / Blind Spot (what the threat exploits; what keeps her from trusting):
Arc/Growth:
Voice/Speech Patterns:
```

### Love Interest Bio Format (for Novelcrafter)
```
Name:
Age:
Occupation:
Physical Description:
Personality Traits:
Backstory:
Internal Conflict:
External Goal:
Connection to the Threat (protector, suspect, investigator, fellow target, or someone with hidden knowledge):
Why He's the Right Person / Wrong Person (both sides — why the protagonist is drawn to him AND why it's dangerous to trust him):
Chemistry Driver (what creates the attraction despite the circumstances):
Trust Fault Line (what makes the protagonist uncertain about him — and what makes the reader uncertain too):
Arc/Growth:
Voice/Speech Patterns:
```

### Antagonist / Threat Architecture Format
```
Name (if revealed) or Nature of Threat:
Type of Threat (person, organization, pattern of events, buried secret with consequences):
Surface Presentation (how the world sees this threat — or why it isn't obvious):
True Nature:
Goal (what they want):
Method (how they pursue it — their specific playbook):
Why They're Formidable (what makes them a genuine danger):
Connection to Protagonist:
Connection to Love Interest:
Motive (the real why — not just "evil"):
Their Flaw / Weakness (what ultimately enables their defeat):
Information Advantage (what do they know that the protagonist doesn't?):
Information Vulnerability (what don't they know that will eventually matter?):
Reveal Schedule (when does the reader/protagonist learn each layer of the truth?):
```

### Supporting Character Bio Format (for Novelcrafter)
```
Name:
Role in Story:
Relationship to Protagonist:
Relationship to Love Interest:
Trustworthiness (is the reader right to trust them?):
Key Personality Traits:
Brief Backstory:
Purpose in Plot (romance, suspense, or both?):
Information They Hold (what do they know that matters?):
```

### Braid Map Format

The braid map is the romantic suspense outline's unique planning tool. It shows where the two arcs intersect and how each track affects the other. Format:

**BRAID POINT [N]: [Chapter Range or Story Beat]**
- **Romance Status**: Where are the protagonists in their relationship at this point?
- **Suspense Status**: What's happening in the external threat?
- **How They Collide**: How does the danger specifically affect the romance here? OR How does the romantic connection change the stakes of the danger?
- **What This Creates**: What is the net emotional effect — what does the reader feel from having BOTH happening at once?

---

### Chapter Outline Format

Each chapter entry must include ALL of the following — both tracks tracked, every field filled in:

```
Chapter [N]: [Title]
POV: [Character — one POV per chapter, established in first paragraph]
Chapter Summary: (3-5 sentences — be specific)

ROMANCE TRACK:
  Romance Arc Beat: [Which beat this chapter hits — first alliance, deepening, the almost, trust break, black moment, etc.]
  Romance Progress: [Where are the couple now vs. where they were?]
  Romantic Tension Note: [What specific charged moment, near-miss, or vulnerability happens?]

SUSPENSE TRACK:
  Tension Level: [1-10]
  Information Released: [What does the reader/protagonist learn this chapter?]
  Information Withheld: [What is deliberately kept hidden?]
  Threat Escalation: [How is the danger worse now than before this chapter?]
  Twist/Plant: [Does this chapter plant a clue or pay off a previous plant?]

BRAID POINT:
  How the tracks collide: [How does the danger affect the romance OR the romance create new danger?]

Trope Tags: [Which tropes this chapter furthers]
Chapter Tone: [dread, charged, urgent, tender, paranoid, vulnerable, false calm, shock, etc.]
Chapter Goal: [What this chapter accomplishes for the dual-arc story]
Complication: [What goes wrong or creates friction]
Character Decision: [What the POV character chooses]
Consequence: [What results — including how it affects BOTH tracks]
POV Character's Feelings: [Emotional state]
```

---

## The Nine Romance Arc Beats

These beats must all appear in the outline, distributed across the chapter structure:

1. **Meet / Alliance**: They come together under the pressure of danger — chemistry AND the obstacle established simultaneously
2. **Forced Cooperation**: They're working together despite reasons not to trust each other
3. **First Real Connection**: A quiet, vulnerable moment between action beats — they see each other clearly
4. **Deepening Stakes**: The love interest becomes personally connected to the danger (target, suspect, or someone the protagonist now needs to protect)
5. **The Almost**: A near-intimate moment interrupted by danger, duty, or the protagonist's own fear — more charged than the thing itself
6. **Trust Break / Misunderstanding**: Something from the suspense arc appears to confirm the protagonist's worst fear about the love interest. Must feel earned from the evidence available.
7. **Black Moment**: Both tracks shatter simultaneously — maximum danger AND the relationship breaks. Maximum isolation. The test: can the protagonist act without him?
8. **The Turn**: The protagonist acts on love first (or uses the courage love gave her) to resolve the external threat — or the reverse, but they must connect
9. **HEA / HFN**: After the danger resolves, the emotional payoff. The declaration. The future. Never rush this — it's what the reader came for.

---

## The Suspense Information Schedule

Before writing the chapter outline, map the information architecture explicitly:

| Chapter | What the reader learns | What stays hidden | What the reader believes (possibly false) |
|---------|------------------------|-------------------|--------------------------------------------|
| ...     | ...                    | ...               | ...                                         |

Every planted clue needs a corresponding payoff. Every misdirection needs a later correction. The reader should be able to re-read and say "it was all there" — not "where did that come from?"
