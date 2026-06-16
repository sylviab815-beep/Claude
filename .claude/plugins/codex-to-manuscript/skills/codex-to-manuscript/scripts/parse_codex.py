#!/usr/bin/env python3
"""
parse_codex.py

Extract structured data from a codex file (.docx or .pdf).

The codex contains, in roughly this order:
  - Story concept (Title, Genre/Subgenre, Tropes, Hook, Pitch, Story Summary)
  - Structure & Technical Details (Antagonist, Setting, Word Count Target, Chapter Count,
    Tense, POV Mode, Alternating POVs, POV Roster, Beat Template)
  - Locked Elements (Locked Tropes, Added Tropes, Key Market Conventions, Mandatories)
  - Characters (Main / Secondary / Incidental — each with Full Name, Age, Gender, Role,
    Physical Description, Personality, Strengths/Flaws, Internal Conflict, Backstory,
    Key Relationships, Character Arc, Thematic Tie-In)
  - Locations (Name, Type, Physical/Mood Description, Notable Features, Who Uses It,
    Relevance to Plot)
  - Objects (Name, Description/Use, Owner/Origin, Narrative Significance)
  - Lore & Rules (Topic, Category, Description, Impact on Daily Life, Connection to Theme)
  - Historical Events (Event Name, Era, Summary, Lasting Impact)
  - Subplots (Title, Involved Characters, Subplot Summary, Thematic Connection,
    Progression, Resolution)

Outputs a single JSON dict to stdout (or to --out path) with all parsed fields.

Usage:
  python parse_codex.py --in /path/to/codex.docx [--out /path/to/parsed_codex.json]
  python parse_codex.py --in /path/to/codex.pdf [--out /path/to/parsed_codex.json]
"""

import argparse
import json
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Text extraction
# ---------------------------------------------------------------------------

def extract_text_from_docx(path: Path) -> str:
    """Extract paragraphs from a .docx, joined by newlines."""
    from docx import Document
    doc = Document(str(path))
    lines = []
    for para in doc.paragraphs:
        text = para.text.strip()
        if text:
            lines.append(text)
    return "\n".join(lines)


def extract_text_from_pdf(path: Path) -> str:
    """Extract text from a .pdf using pdfplumber, falling back to pypdf."""
    try:
        import pdfplumber
        lines = []
        with pdfplumber.open(str(path)) as pdf:
            for page in pdf.pages:
                txt = page.extract_text() or ""
                for line in txt.splitlines():
                    if line.strip():
                        lines.append(line.strip())
        return "\n".join(lines)
    except ImportError:
        pass
    # Fallback to pypdf
    try:
        from pypdf import PdfReader
        reader = PdfReader(str(path))
        chunks = []
        for page in reader.pages:
            txt = page.extract_text() or ""
            for line in txt.splitlines():
                if line.strip():
                    chunks.append(line.strip())
        return "\n".join(chunks)
    except ImportError:
        raise RuntimeError(
            "Neither pdfplumber nor pypdf is installed. "
            "Install one: pip install pdfplumber  OR  pip install pypdf"
        )


def extract_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".docx":
        return extract_text_from_docx(path)
    if suffix == ".pdf":
        return extract_text_from_pdf(path)
    if suffix in (".txt", ".md"):
        return path.read_text(encoding="utf-8")
    raise ValueError(f"Unsupported codex format: {suffix}")


# ---------------------------------------------------------------------------
# Field parsing
# ---------------------------------------------------------------------------

def _strip_md(s: str) -> str:
    """Strip leading bullets, asterisks, and surrounding markdown emphasis."""
    s = s.strip()
    s = re.sub(r"^[\*\-••]+\s*", "", s)  # leading bullets
    # Collapse any "Word:**" pattern (left-over bold close after colon)
    s = re.sub(r"\*+:\s*\*?\*?", ": ", s)
    s = re.sub(r"^\*\*(.+?)\*\*\s*:?\s*", "", s)  # leading **Bold:**
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)  # strip remaining bold
    s = re.sub(r"\*+(.+?)\*+", r"\1", s)  # strip italics / stragglers
    s = s.replace("**", "")
    return s.strip()


def _kv_after(label: str, text: str) -> str:
    """
    Find the first inline value following a labeled line like:
        **Title:** The Bog Witch's Mistake
        Title: The Bog Witch's Mistake
        *   **Title:** The Bog Witch's Mistake
    Returns the text after the colon, including wrapped continuation lines, but
    stops at the next field. The capture stops when the following line begins a
    new bullet, a markdown header (### ...), another "Label:" line, a blank line,
    or end-of-text. Wrapped continuation lines (which do not start with any of
    those markers) are kept.

    Robust to PDF-extraction quirks: handles labels containing punctuation such
    as "?" (e.g. "Alternating POVs?:") and stops cleanly at "###" section
    headers so values never bleed into the next section.
    """
    stop = (
        r"(?="
        r"\n\s*[\*\-•]"                                          # next line starts with a bullet
        r"|\n\s*#{1,6}\s"                                        # next line is a markdown header
        r"|\n\s*\*{0,2}[A-Z][A-Za-z0-9 ?/()&'\-]{0,40}\*{0,2}\s*:"  # next line is a "Label:" line
        r"|\n\n"                                                 # blank line
        r"|\Z)"                                                  # end of text
    )
    pattern = re.compile(
        r"(?:^|\n)\s*[\*\-••]*\s*\*?\*?" + re.escape(label)
        + r"\*?\*?\s*:\s*(.+?)" + stop,
        re.IGNORECASE | re.DOTALL,
    )
    m = pattern.search(text)
    if not m:
        return ""
    val = m.group(1)
    # Collapse whitespace, strip md
    val = re.sub(r"\s+", " ", val).strip()
    return _strip_md(val)


def parse_concept(text: str) -> dict:
    """Pull the top-of-codex concept fields."""
    concept = {}
    for label in [
        "Title", "Genre/Subgenre", "Genre", "Tropes or Themes", "Tropes",
        "Hook (1 line)", "Hook", "Pitch (short blurb)", "Pitch",
        "Story Summary",
    ]:
        v = _kv_after(label, text)
        if v:
            key = label.split(" (")[0].strip().lower().replace(" ", "_").replace("/", "_")
            concept[key] = v
    return concept


def parse_structure(text: str) -> dict:
    """Pull structure & technical details."""
    fields = {}
    for label in [
        "Word Count Target", "Chapter Count Target", "Tense", "POV Mode",
        "Alternating POVs", "Alternating POVs?", "POV Roster", "Beat Template",
    ]:
        v = _kv_after(label, text)
        if v:
            key = (label.replace("?", "")
                   .strip().lower().replace(" ", "_"))
            fields[key] = v
    return fields


def parse_antagonist(text: str) -> dict:
    """Pull antagonist details."""
    antag = {}
    # Find the Antagonist section. Anchor to a line-start "**Antagonist:**"
    # header (require the colon) so the bare word can't match prose elsewhere.
    sec = _section(text, r"(?:^|\n)\*{0,2}Antagonist\*{0,2}\s*:",
                   r"(?:^|\n)\*{0,2}Setting\*{0,2}\s*:")
    if not sec:
        return antag
    for label in ["Type", "Goal", "Method"]:
        v = _kv_after(label, sec)
        if v:
            antag[label.lower()] = v
    return antag


def parse_setting(text: str) -> dict:
    """Pull setting fields."""
    # Anchor to a line-start "**Setting:**" header (require the colon) so the
    # bare word "setting" in the pitch/summary can't be mistaken for the header.
    sec = _section(text, r"(?:^|\n)\*{0,2}Setting\*{0,2}\s*:",
                   r"(?:^|\n)\*{0,2}Structure\*{0,2}\s*:")
    setting = {}
    if not sec:
        return setting
    for label in ["Primary Setting (time/place)", "Primary Setting", "Vibe Keywords",
                  "Special Rules or Systems", "Special Rules"]:
        v = _kv_after(label, sec)
        if v:
            key = label.split(" (")[0].strip().lower().replace(" ", "_")
            setting[key] = v
    return setting


def parse_locked_elements(text: str) -> dict:
    """Pull locked tropes, added tropes, key market conventions, mandatories.

    The LOCKED ELEMENTS section sits between "### LOCKED ELEMENTS" and the
    first character / lore section header (e.g. "### **Main Characters**" or a
    "Here are the character entries" sentence).
    """
    out = {}
    # Try to find the end of locked elements — first character header, lore
    # header, or "Here are the character entries" text.
    sec = _section(
        text,
        r"###?\s*\**\s*LOCKED ELEMENTS\s*\**",
        r"###?\s*\**\s*(Main Characters|Characters|Character Entries|Locations?|Location Entries|Objects?|Object Entries|Lore|Historical Events|Subplots)\s*\**|"
        r"\n\s*Here are the character entries|"
        r"\n\s*Here are the (location|object|lore|historical|subplot) entries",
    )
    if not sec:
        sec = text

    next_label_re = (
        r"\n+\s*\*{0,2}(?:\(Added\)\s*Tropes|Added\s*Tropes|"
        r"Key Market Conventions|Mandatories|"
        r"Main Characters|Characters|Character Entries|"
        r"Locations?|Objects?|Lore|Historical Events|Subplots)"
    )

    out["locked_tropes"] = _list_after(
        sec, r"\*?\*?Locked Tropes\*?\*?\s*:?", stop_re=next_label_re
    )
    out["added_tropes"] = _list_after(
        sec,
        r"\*?\*?\(Added\)\s*Tropes\*?\*?\s*:?|\*?\*?Added\s*Tropes\*?\*?\s*:?",
        stop_re=next_label_re,
    )
    out["key_market_conventions"] = _list_after(
        sec, r"\*?\*?Key Market Conventions\*?\*?\s*:?", stop_re=next_label_re
    )
    out["mandatories"] = _list_after(
        sec, r"\*?\*?Mandatories[^:\n]*\*?\*?\s*:?", stop_re=next_label_re
    )
    return out


def _section(text: str, start_re: str, end_re: str) -> str:
    """Return text between a starting regex match and the next end regex match (or EOF)."""
    sm = re.search(start_re, text, re.IGNORECASE)
    if not sm:
        return ""
    rest = text[sm.end():]
    em = re.search(end_re, rest, re.IGNORECASE)
    if em:
        return rest[:em.start()]
    return rest


def _list_after(text: str, label_re: str, stop_re: str = None) -> list:
    """
    After a label, collect bullet/numbered items until the next labeled section
    or a blank-line break followed by another label.

    Stops when it encounters another label-style line (any line ending with `:`
    that looks like a section header), an empty line followed by such a line,
    or the supplied `stop_re`.
    """
    m = re.search(label_re, text, re.IGNORECASE)
    if not m:
        return []
    rest = text[m.end():]
    # Default stop pattern: next labeled section header. Allow leading
    # parentheses (e.g. "(Added) Tropes:") and bold markers.
    if stop_re is None:
        stop_re = (
            r"\n\s*\*?\*?[\(]?[A-Z][A-Za-z ()\-/&]+\*?\*?\s*:\s"
        )
    end = re.search(stop_re, rest)
    chunk = rest[:end.start()] if end else rest

    items = []
    for line in chunk.splitlines():
        s = line.strip()
        if not s:
            continue
        m2 = re.match(r"^(?:[\*\-••]|\d+\.)\s+(.+)$", s)
        if m2:
            items.append(_strip_md(m2.group(1)))
    return items


# ---------------------------------------------------------------------------
# Entity parsing — characters / locations / objects / lore / events / subplots
# ---------------------------------------------------------------------------

def _split_entries(section_text: str, header_label: str) -> list:
    """
    Split a section into individual entries by a header label like 'Full Name'
    or 'Location Name' or 'Topic Name'. Each entry runs from one header line
    to the next.
    """
    if not section_text:
        return []
    # Find positions of every header label
    pat = re.compile(
        r"(?:^|\n)\s*[\*\-••]*\s*\*?\*?" + re.escape(header_label) + r"\*?\*?\s*:\s*",
        re.IGNORECASE,
    )
    starts = [m.start() for m in pat.finditer(section_text)]
    if not starts:
        return []
    starts.append(len(section_text))
    return [section_text[starts[i]:starts[i + 1]].strip() for i in range(len(starts) - 1)]


def parse_characters(text: str) -> list:
    """
    Pull character entries. Each entry should yield:
      full_name, age, gender_pronouns, role, physical_description, style_clothing,
      personality, strengths, flaws, internal_conflict, backstory, key_relationships,
      character_arc, thematic_tie_in
    """
    # Match the keyword anywhere inside a markdown header line so headers like
    # "### MAIN CHARACTERS" and "### SECONDARY & INCIDENTAL CHARACTERS" resolve.
    sec = _section(text, r"(?:^|\n)#{1,4}[^\n]*\bCHARACTER",
                   r"(?:^|\n)#{1,4}[^\n]*\b(LOCATION|OBJECT|LORE|HISTORICAL|SUBPLOT)")
    # If no following section, capture everything until the end
    if not sec:
        sec = _section(text, r"(?:^|\n)#{1,4}[^\n]*\bCHARACTER", r"\Z")
    entries = _split_entries(sec, "Full Name")
    out = []
    for e in entries:
        ch = {"full_name": _kv_after("Full Name", e)}
        for label in [
            "Age", "Gender / Pronouns", "Gender/Pronouns", "Pronouns",
            "Role in Story", "Role",
            "Physical Description", "Style / Clothing Notes", "Style/Clothing",
            "Personality Traits", "Personality",
            "Internal Conflict (what they want vs. what they need)", "Internal Conflict",
            "Backstory Summary", "Backstory",
            "Key Relationships",
            "Character Arc Summary", "Character Arc",
            "Thematic Tie-In",
        ]:
            v = _kv_after(label, e)
            if v and label.split(" (")[0].lower().replace(" / ", "_").replace(" ", "_").replace("-", "_") not in ch:
                key = label.split(" (")[0].lower().replace(" / ", "_").replace(" ", "_").replace("-", "_")
                ch[key] = v
        # Strengths & Flaws often appear as a sub-list
        sf = _section(e, r"\*?\*?Strengths and Flaws\*?\*?\s*:?", r"\*?\*?(Internal Conflict|Backstory|Key Relationships|Character Arc)\*?\*?\s*:?")
        if sf:
            ch["strengths"] = _kv_after("Strengths", sf)
            ch["flaws"] = _kv_after("Flaws", sf)
        out.append(ch)
    return out


def parse_locations(text: str) -> list:
    sec = _section(text, r"(?:^|\n)#{1,4}[^\n]*\bLOCATION",
                   r"(?:^|\n)#{1,4}[^\n]*\b(OBJECT|LORE|HISTORICAL|SUBPLOT)")
    if not sec:
        return []
    entries = _split_entries(sec, "Location Name")
    out = []
    for e in entries:
        loc = {"name": _kv_after("Location Name", e)}
        for label in [
            "Type of Place", "Type",
            "Physical / Mood Description", "Physical Description",
            "Notable Features or Objects", "Notable Features",
            "Who Uses It and When", "Who Uses It",
            "Relevance to Plot or Character Arcs", "Relevance to Plot",
        ]:
            v = _kv_after(label, e)
            if v:
                key = label.split(" (")[0].split(" or ")[0].lower().replace(" / ", "_").replace(" ", "_")
                if key not in loc:
                    loc[key] = v
        out.append(loc)
    return out


def parse_objects(text: str) -> list:
    sec = _section(text, r"(?:^|\n)#{1,4}[^\n]*\bOBJECT",
                   r"(?:^|\n)#{1,4}[^\n]*\b(LORE|HISTORICAL|SUBPLOT)")
    if not sec:
        return []
    entries = _split_entries(sec, "Name of Object")
    out = []
    for e in entries:
        obj = {"name": _kv_after("Name of Object", e)}
        for label in ["Description and Use", "Description", "Owner or Origin",
                      "Narrative or Emotional Significance"]:
            v = _kv_after(label, e)
            if v:
                key = label.split(" or ")[0].lower().replace(" ", "_")
                if key not in obj:
                    obj[key] = v
        out.append(obj)
    return out


def parse_lore(text: str) -> list:
    sec = _section(text, r"(?:^|\n)#{1,4}[^\n]*\bLORE",
                   r"(?:^|\n)#{1,4}[^\n]*\b(HISTORICAL|SUBPLOT)")
    if not sec:
        return []
    entries = _split_entries(sec, "Topic Name")
    out = []
    for e in entries:
        item = {"topic": _kv_after("Topic Name", e)}
        for label in ["Category", "Description",
                      "Impact on Daily Life or Conflict", "Impact on Daily Life",
                      "Connection to Theme or Main Plot", "Connection to Theme"]:
            v = _kv_after(label, e)
            if v:
                key = label.split(" or ")[0].lower().replace(" ", "_")
                if key not in item:
                    item[key] = v
        out.append(item)
    return out


def parse_events(text: str) -> list:
    sec = _section(text, r"(?:^|\n)#{1,4}[^\n]*\bHISTORICAL",
                   r"(?:^|\n)#{1,4}[^\n]*\bSUBPLOT")
    if not sec:
        return []
    entries = _split_entries(sec, "Event Name")
    out = []
    for e in entries:
        ev = {"name": _kv_after("Event Name", e)}
        for label in ["Era or Timeframe", "Era", "Summary", "Lasting Impact"]:
            v = _kv_after(label, e)
            if v:
                key = label.split(" or ")[0].lower().replace(" ", "_")
                if key not in ev:
                    ev[key] = v
        out.append(ev)
    return out


def parse_subplots(text: str) -> list:
    # End before any trailing guide sections (Prose Style Guide / Genre Guide)
    # so their content does not bleed into the final subplot's fields.
    sec = _section(text, r"(?:^|\n)#{1,4}[^\n]*\bSUBPLOT",
                   r"(?:^|\n)#{1,4}[^\n]*\b(PROSE|STYLE GUIDE|GENRE GUIDE|GENRE\b)")
    if not sec:
        sec = _section(text, r"(?:^|\n)#{1,4}[^\n]*\bSUBPLOT", r"\Z")
    if not sec:
        return []
    entries = _split_entries(sec, "Title")
    out = []
    for e in entries:
        sp = {"title": _kv_after("Title", e)}
        for label in ["Involved Characters", "Subplot Summary",
                      "Thematic Connection", "Resolution"]:
            v = _kv_after(label, e)
            if v:
                key = label.lower().replace(" ", "_")
                if key not in sp:
                    sp[key] = v
        out.append(sp)
    return out


# ---------------------------------------------------------------------------
# Top-level parse
# ---------------------------------------------------------------------------

def parse_codex_text(text: str) -> dict:
    return {
        "concept": parse_concept(text),
        "structure": parse_structure(text),
        "antagonist": parse_antagonist(text),
        "setting": parse_setting(text),
        "locked_elements": parse_locked_elements(text),
        "characters": parse_characters(text),
        "locations": parse_locations(text),
        "objects": parse_objects(text),
        "lore": parse_lore(text),
        "historical_events": parse_events(text),
        "subplots": parse_subplots(text),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Parse a codex (.docx or .pdf) into structured JSON.")
    ap.add_argument("--in", dest="inp", required=True, help="Path to codex file")
    ap.add_argument("--out", dest="out", help="Optional output path for the JSON")
    args = ap.parse_args()

    path = Path(args.inp)
    if not path.is_file():
        print(f"Codex file not found: {path}", file=sys.stderr)
        return 2

    text = extract_text(path)
    parsed = parse_codex_text(text)

    payload = json.dumps(parsed, indent=2, ensure_ascii=False)
    if args.out:
        Path(args.out).write_text(payload, encoding="utf-8")
        print(f"Wrote {args.out}")
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
