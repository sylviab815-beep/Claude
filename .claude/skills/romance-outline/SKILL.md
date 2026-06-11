---
name: romance-outline
description: >
  Interactive romance novel/novella outlining workflow that guides you step-by-step
  from genre selection through a complete chapter outline. Optionally uses K-Lytics
  market reports for data-driven trope selection, generates 5 story ideas, develops
  hook/pitch, builds detailed character bios, maps trope scenes, plots the romance
  arc, creates supporting characters and settings, and produces a fully labeled
  chapter outline with intimate moment placeholders. MANDATORY TRIGGERS: "romance
  outline", "outline a romance", "romance story outline", "outline my romance",
  "romance plotting", "plot a romance", "romance novella outline", "romance novel
  outline", "outline template", or any mention of outlining/plotting a romance story.
  Use this skill even if the user just says "outline" when the context involves
  romance writing.
---

# Romance Outline Template

Guide the user through an interactive, step-by-step process to develop a romance story idea into a fully detailed chapter outline. This workflow is specifically designed for romance and its subgenres. Every step pauses for user input before proceeding.

## Core Principles

- **One step at a time**: Complete each step fully, present the output, and WAIT for user feedback before moving on. Never skip ahead or combine steps.
- **Market-informed** (when available): If the user provides a K-Lytics report, use it to identify highly marketable tropes and reader expectations. If not, use your own deep knowledge of the romance market to guide trope selection.
- **Detail-oriented outlines**: Every chapter in the final outline must include POV character, summary, tone, goal, complication, decision, consequence, and feelings — all clearly labeled with which tropes each chapter furthers.
- **Fresh and original**: All names, places, and titles must avoid overused AI-generated patterns. See the bundled Names & Places Avoidance List.

## Names & Places Avoidance List

Read the file `references/ai-names-avoidance.md` bundled with this skill. It contains comprehensive lists of overused AI-generated names, places, businesses, title words, and descriptive cliches. ALL generated content must avoid these throughout the entire workflow.

## Number & Time Diversity (Anti-7 Bias)

LLMs default to 7 for "random" numbers. Actively avoid this pattern in all generated content — ages, times, dates, quantities, addresses, durations. Distribute numbers across all ending digits. After completing any outline, scan for the digit 7 and replace most instances with other numbers.

## Workflow

Read `references/workflow-steps.md` for the complete step-by-step instructions for each phase of the outlining process.

## Output Formats

### Character Bio Format (for Novelcrafter)
```
Name:
Age:
Occupation:
Physical Description:
Personality Traits:
Backstory:
Internal Conflict:
External Goal:
Relationship to Other Characters:
Arc/Growth:
Quirks/Habits:
Voice/Speech Patterns:
```

### Supporting Character Bio Format (for Novelcrafter)
```
Name:
Role in Story:
Relationship to Main Characters:
Key Personality Traits:
Brief Backstory:
Purpose in Plot:
```

### Chapter Outline Format
Each chapter entry must include:
- **Chapter Number & Title**
- **POV Character** (alternate between H1 and H2; one POV per chapter)
- **Chapter Summary** (3-5 sentences minimum)
- **Trope Tags** (clearly label which tropes this chapter furthers)
- **Chapter Tone**
- **Chapter Goal**
- **Complication**
- **Character Decision/Choice**
- **Consequence of That Choice**
- **POV Character's Feelings**
