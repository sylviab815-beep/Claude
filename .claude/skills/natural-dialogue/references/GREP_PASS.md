# Grep Pass — Command-Line Dialogue Audit

The audit's grep commands. Run these against a chapter or manuscript file (Markdown, plain text, or any format with quote marks intact). Output: line numbers and matches; review each.

These commands assume `grep` with extended-regex support (-E flag). On macOS, also use `-i` if you want case-insensitive matching for some categories, though most patterns are designed to require correct case.

---

## Category 1: Bare confirmations

```bash
grep -nE '"\s*(Yes|No|Okay|Sure|Right|Uh-?huh|Mm-?hmm|I see|Got it|Of course)\.?\s*"' chapter.md
```

Review every hit. Replace unless bareness is doing genuine character work (stonewalling, genre-natural-during-heat, character-specific tic).

---

## Category 2: Filler exchanges

Harder to grep since it's pattern-based. Approximate:

```bash
# Greeting/parting fluff
grep -nE '"\s*(Hi|Hello|Hey|Goodbye|Bye|Thanks|Thank you|No problem|You too|Have a good)' chapter.md

# Social-script Q-and-A
grep -nE '"\s*How are you' chapter.md
grep -nE '"\s*Good\.?, you\?\s*"' chapter.md
```

Review each; cut filler exchanges unless they're characterizing.

---

## Category 3: Acknowledgment fluff

```bash
grep -nE '"\s*(I see|I understand|That makes sense|Fair enough|Mm)\.?\s*"' chapter.md
```

Allowed as documented voice tic for ONE character. Ban from others.

---

## Category 4: On-the-nose emotional naming

```bash
grep -nE '"\s*I\'?m (angry|sad|scared|hurt|broken|fine|overwhelmed|frustrated|exhausted|nervous)' chapter.md
grep -nE 'That makes me (sad|angry|scared|happy|feel)' chapter.md
grep -nE '"\s*(I love you|I hate you|I miss you)' chapter.md
```

Most should be replaced with body, action, or indirection. Some are earned and signature — author's call per instance.

---

## Category 5: Therapy-speak

```bash
grep -niE '\b(processing|holding space|that\'?s valid|let me sit with|trauma response|triggered|checking in|boundary|boundaries)\b' chapter.md
```

Note: case-insensitive (-niE) because these phrases drift in regardless of position. Some uses are literal (a therapist character; a literal boundary as in "property line"); review case-by-case.

---

## Category 6: Excessive politeness

```bash
grep -nE '"\s*(Please|Thank you|Sorry|Pardon|Excuse me)' chapter.md
grep -nE '"\s*[A-Z][a-z]+, please\b' chapter.md
```

Count occurrences per chapter. Flag if density seems wrong for the speaker register.

---

## Category 7: Generic tic openers

```bash
grep -nE '"\s*(Look|Listen|I mean|Well|So|Honestly),' chapter.md
```

Most should be cut. Acceptable as a single-character voice tic if documented.

---

## Category 8 + 9: Tag-as-meaning + Adverbs on tags

```bash
grep -nE '\b(said|asked|whispered|murmured|breathed|sighed|replied|answered) [a-z]+ly\b' chapter.md
```

Review every hit. Most adverbs should be cut; a few are load-bearing.

Also flag tag variations (whispered, murmured, breathed, sighed) — should be rare in most voice registers; acceptable when load-bearing.

```bash
grep -nE '\b(whispered|murmured|breathed|sighed|growled|hissed|spat|barked|snapped)\b' chapter.md
```

---

## Category 10: Speaker-voice collapse

Not greppable. Manual audit: take a passage, strip tags, read. Can you tell who said what?

If profile-aware mode and a voice profile is loaded: cross-reference each character's documented voice rules against their actual lines. Flag mismatches.

---

## Category 11: Explainer dialogue

```bash
grep -nE '"\s*(As you know|Remember when|You know that|Like I told you)' chapter.md
```

Plus manual audit: any line where one character tells another something both characters already know.

---

## Category 12: Question-then-same-answer

Not greppable directly. Approximate:

```bash
# Find lines that begin with "I'm" or "I am" (likely confirmation answers)
grep -nE '"\s*I\'?m (fine|okay|good|here|ready|done)' chapter.md
```

Manual audit: scan Q-A pairs for confirmation-without-complication.

---

## Category 13: Trailing ellipses

```bash
grep -nE '"\s*[A-Z][^"]*\.\.\.\s*"' chapter.md
grep -nE '\.\.\." chapter.md
```

Count per chapter. Flag if more than 2-3 per chapter; reduce to load-bearing only.

---

## Category 14: Same-character lexical repetition

Not single-grep-able. Use a frequency check instead:

```bash
# Extract one character's lines (assuming a tag pattern), then frequency-count uncommon words.
# Example for "Caspian said":
grep -B1 -A1 'Caspian said' chapter.md | tr ' ' '\n' | sort | uniq -c | sort -rn | head -30
```

Manual review: any uncommon word appearing 3+ times in one character's dialogue within a chapter.

---

## Polysyndeton (within-sentence "and X and Y and Z")

Not strictly dialogue, but often appears in dialogue and many voices ban it as default:

```bash
grep -nE '\b[a-z]+ and [a-z]+ and [a-z]+\b' chapter.md
```

Flag every triple-and chain. Convert to comma chain unless flagged as deliberate.

---

## Quick scan (run all the high-leverage ones together)

```bash
echo "=== Category 1: Bare confirmations ==="
grep -nE '"\s*(Yes|No|Okay|Sure|Right|Uh-?huh|Mm-?hmm|I see|Got it|Of course)\.?\s*"' chapter.md

echo "=== Category 4: On-the-nose emotional naming ==="
grep -nE '"\s*I\'?m (angry|sad|scared|hurt|broken|fine|overwhelmed|frustrated)' chapter.md

echo "=== Category 5: Therapy-speak ==="
grep -niE '\b(processing|holding space|that\'?s valid|let me sit with|trauma response|triggered|checking in)\b' chapter.md

echo "=== Category 7: Generic tic openers ==="
grep -nE '"\s*(Look|Listen|I mean|Well|So|Honestly),' chapter.md

echo "=== Category 8/9: Adverbs on tags ==="
grep -nE '\b(said|asked|whispered|murmured) [a-z]+ly\b' chapter.md

echo "=== Category 11: Explainer dialogue ==="
grep -nE '"\s*(As you know|Remember when|You know that|Like I told you)' chapter.md

echo "=== Category 13: Trailing ellipses ==="
grep -nE '"\s*[A-Z][^"]*\.\.\.\s*"' chapter.md
```

Save this as `dialogue-audit.sh` and run against any chapter.

---

## Notes on grep limitations

Grep is a fast triage. It catches surface patterns. It misses:

- Voice collapse (Category 10) — needs human read
- Explainer dialogue beyond keyword triggers — needs human read
- On-the-nose emotional naming with non-standard phrasing
- Lexical repetition without character-line extraction
- Most subtext/character-coherence questions

**Always pair grep with the manual audit** in DIALOGUE_CATEGORIES.md. Grep does the obvious; the audit catches the rest.
