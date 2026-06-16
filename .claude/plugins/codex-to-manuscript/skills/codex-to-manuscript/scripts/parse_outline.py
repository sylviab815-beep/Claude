#!/usr/bin/env python3
"""
parse_outline.py

Extract per-chapter beats from an outline file (.docx or .pdf).

The outline is organized by Acts and Chapters. Each chapter typically has:
  - POV (whose POV the chapter is in)
  - Chapter Goal
  - Opening Hook
  - Key Scenes (numbered list of scene beats)
  - Romantic/Relationship Development (or Subplot Development)
  - Complication or Conflict
  - Character Decision and Consequence
  - Chapter Tone
  - Tropes Advanced
  - Intimate Beat (Heat-Gated)
  - Cliffhanger (or Closing Line)

Outputs JSON to stdout (or --out) shaped like:
  {
    "title": "...",
    "acts": [
      {"act": "I", "chapters": [<chapter dict>, ...]},
      ...
    ],
    "chapters_flat": [<all chapters in order>]
  }

Usage:
  python parse_outline.py --in /path/to/outline.docx [--out /path/to/parsed_outline.json]
"""

import argparse
import json
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Text extraction (same approach as parse_codex.py)
# ---------------------------------------------------------------------------

def extract_text_from_docx(path: Path) -> str:
    from docx import Document
    doc = Document(str(path))
    out = []
    for para in doc.paragraphs:
        text = para.text.rstrip()
        if text:
            out.append(text)
    return "\n".join(out)


def extract_text_from_pdf(path: Path) -> str:
    try:
        import pdfplumber
        out = []
        with pdfplumber.open(str(path)) as pdf:
            for page in pdf.pages:
                txt = page.extract_text() or ""
                for line in txt.splitlines():
                    if line.rstrip():
                        out.append(line.rstrip())
        return "\n".join(out)
    except ImportError:
        pass
    try:
        from pypdf import PdfReader
        reader = PdfReader(str(path))
        out = []
        for page in reader.pages:
            txt = page.extract_text() or ""
            for line in txt.splitlines():
                if line.rstrip():
                    out.append(line.rstrip())
        return "\n".join(out)
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
    raise ValueError(f"Unsupported outline format: {suffix}")


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

# Matches act headers, including ones with a title after the numeral, e.g.:
#   ### **ACT I: THE ANONYMOUS CONNECTION**
#   ## ACT II
#   ACT THREE — The Reckoning
ACT_HEADER_RE = re.compile(
    r"^\s*#{0,4}\s*\**\s*ACT\s+([IVXLC0-9]+|ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT)\b[^\n]*$",
    re.IGNORECASE | re.MULTILINE,
)

# Matches headings like:
#   #### **Chapter 1: The Weight of Water and Time**
#   ## Chapter 12 - Domesticated Chaos
#   Chapter 5: The Rules of the House
CHAPTER_HEADER_RE = re.compile(
    r"^\s*#{0,6}\s*\**\s*Chapter\s+(\d+)\s*[:\-—–]\s*([^\n*]+?)\s*\**\s*$",
    re.IGNORECASE | re.MULTILINE,
)

# Inline labeled fields within a chapter section
FIELD_LABELS = [
    "POV", "Chapter Goal", "Opening Hook", "Key Scenes",
    "Romantic/Relationship Development", "Romantic / Relationship Development",
    "Subplot Development",
    "Complication or Conflict", "Conflict",
    "Character Decision and Consequence",
    "Chapter Tone", "Tone",
    "Tropes Advanced",
    "Intimate Beat (Heat-Gated)", "Intimate Beat",
    "Cliffhanger", "Closing Line", "Closing Beat",
]


def _strip_md(s: str) -> str:
    s = s.strip()
    s = re.sub(r"^[\*\-••]+\s*", "", s)
    # Strip trailing leftover bold markers like "Title:**"
    s = re.sub(r"\*+:\s*\*?\*?", ": ", s)
    s = re.sub(r"^\*\*(.+?)\*\*\s*:?\s*", "", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"\*+(.+?)\*+", r"\1", s)
    # Clean any stray ** that survived
    s = s.replace("**", "")
    return s.strip()


def _kv_after(label: str, text: str) -> str:
    pattern = re.compile(
        r"(?:^|\n)\s*[\*\-••]*\s*\*?\*?" + re.escape(label) +
        r"\*?\*?\s*:\s*(.+?)(?=\n\s*[\*\-••]*\s*\*?\*?[A-Z][A-Za-z /()\-]+\*?\*?\s*:|\n\n|\Z)",
        re.IGNORECASE | re.DOTALL,
    )
    m = pattern.search(text)
    if not m:
        return ""
    val = re.sub(r"\s+", " ", m.group(1)).strip()
    return _strip_md(val)


def _key_scenes(chapter_text: str) -> list:
    """
    Pull numbered key scenes after the 'Key Scenes:' label.
    Looks for lines like '1. Title: body' or '1. body' or '*   1. body'.
    """
    m = re.search(r"\*?\*?Key Scenes\*?\*?\s*:\s*", chapter_text, re.IGNORECASE)
    if not m:
        return []
    rest = chapter_text[m.end():]
    # Stop at the next labeled field
    end_re = re.compile(
        r"\n\s*\*?\*?(Romantic|Subplot|Complication|Conflict|Character Decision|"
        r"Chapter Tone|Tone|Tropes Advanced|Intimate Beat|Cliffhanger|Closing)",
        re.IGNORECASE,
    )
    em = end_re.search(rest)
    chunk = rest[:em.start()] if em else rest

    scenes = []
    current_lines = []
    current_idx = None
    line_pat = re.compile(r"^\s*[\*\-••]*\s*(\d+)\.\s+(.+)$")
    for line in chunk.splitlines():
        if not line.strip():
            continue
        m2 = line_pat.match(line)
        if m2:
            if current_idx is not None:
                scenes.append({
                    "index": current_idx,
                    "text": " ".join(current_lines).strip()
                })
            current_idx = int(m2.group(1))
            current_lines = [_strip_md(m2.group(2))]
        else:
            if current_idx is not None:
                current_lines.append(_strip_md(line))
    if current_idx is not None:
        scenes.append({"index": current_idx, "text": " ".join(current_lines).strip()})
    return scenes


def parse_outline_text(text: str) -> dict:
    # Find acts (optional)
    act_matches = list(ACT_HEADER_RE.finditer(text))
    acts = []
    if act_matches:
        for i, am in enumerate(act_matches):
            start = am.end()
            end = act_matches[i + 1].start() if i + 1 < len(act_matches) else len(text)
            act_label = am.group(1)
            acts.append({"act": act_label, "start": start, "end": end})
    else:
        acts = [{"act": "ALL", "start": 0, "end": len(text)}]

    chapters_flat = []
    acts_out = []

    for act in acts:
        act_text = text[act["start"]:act["end"]]
        ch_matches = list(CHAPTER_HEADER_RE.finditer(act_text))
        chapters = []
        for i, cm in enumerate(ch_matches):
            ch_num = int(cm.group(1))
            ch_title = cm.group(2).strip()
            body_start = cm.end()
            body_end = ch_matches[i + 1].start() if i + 1 < len(ch_matches) else len(act_text)
            body = act_text[body_start:body_end]
            chapter = {
                "act": act["act"],
                "chapter_number": ch_num,
                "chapter_title": ch_title,
            }
            for label in FIELD_LABELS:
                if label.lower().startswith("key scenes"):
                    continue
                v = _kv_after(label, body)
                if v:
                    key = (label.lower()
                           .replace("/", "_")
                           .replace(" - ", "_")
                           .replace("-", "_")
                           .replace("(", "")
                           .replace(")", "")
                           .replace(" ", "_"))
                    if key not in chapter:
                        chapter[key] = v
            chapter["key_scenes"] = _key_scenes(body)
            chapter["raw_body"] = body.strip()
            chapters.append(chapter)
            chapters_flat.append(chapter)
        acts_out.append({"act": act["act"], "chapters": chapters})

    return {
        "act_count": len(acts_out),
        "chapter_count": len(chapters_flat),
        "acts": [{"act": a["act"], "chapters": a["chapters"]} for a in acts_out],
        "chapters_flat": chapters_flat,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Parse an outline (.docx or .pdf) into structured JSON.")
    ap.add_argument("--in", dest="inp", required=True, help="Path to outline file")
    ap.add_argument("--out", dest="out", help="Optional output path for the JSON")
    args = ap.parse_args()

    path = Path(args.inp)
    if not path.is_file():
        print(f"Outline file not found: {path}", file=sys.stderr)
        return 2

    text = extract_text(path)
    parsed = parse_outline_text(text)

    payload = json.dumps(parsed, indent=2, ensure_ascii=False)
    if args.out:
        Path(args.out).write_text(payload, encoding="utf-8")
        print(f"Wrote {args.out}")
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
