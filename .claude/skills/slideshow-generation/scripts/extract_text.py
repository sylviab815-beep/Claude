#!/usr/bin/env python3
"""Extract plain text from .docx, .epub, or .pdf. Emits to stdout."""
import sys
from pathlib import Path


def extract_docx(path: Path) -> str:
    from docx import Document
    doc = Document(str(path))
    return "\n".join(p.text for p in doc.paragraphs if p.text.strip())


def extract_epub(path: Path) -> str:
    from ebooklib import epub, ITEM_DOCUMENT
    from html.parser import HTMLParser

    class Stripper(HTMLParser):
        def __init__(self):
            super().__init__()
            self.chunks = []
        def handle_data(self, data):
            self.chunks.append(data)

    book = epub.read_epub(str(path))
    out = []
    for item in book.get_items():
        if item.get_type() == ITEM_DOCUMENT:
            s = Stripper()
            s.feed(item.get_content().decode("utf-8", errors="ignore"))
            out.append("".join(s.chunks))
    return "\n".join(out)


def extract_pdf(path: Path) -> str:
    from pypdf import PdfReader
    reader = PdfReader(str(path))
    return "\n".join((p.extract_text() or "") for p in reader.pages)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: extract_text.py <manuscript-path>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1]).expanduser().resolve()
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        return 2

    ext = path.suffix.lower()
    if ext == ".docx":
        print(extract_docx(path))
    elif ext == ".epub":
        print(extract_epub(path))
    elif ext == ".pdf":
        print(extract_pdf(path))
    else:
        print(f"Unsupported extension: {ext}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
