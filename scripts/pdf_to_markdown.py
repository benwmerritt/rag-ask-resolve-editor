#!/usr/bin/env python3
"""
PDF to Markdown Converter for DaVinci Resolve Manual

Converts a large PDF manual into chapter-split markdown files
suitable for RAG ingestion.

Usage:
    python3 scripts/pdf_to_markdown.py [pdf_path] [output_dir]

    Defaults:
        pdf_path: pdf/DaVinci Resolve.pdf
        output_dir: transcripts/davinci-manual/transcripts/
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple, Optional

try:
    import pymupdf
except ImportError:
    print("Error: pymupdf not installed. Run: pip3 install pymupdf")
    sys.exit(1)


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text[:60].rstrip('-')


def is_chapter_heading(text: str, font_size: float, avg_font_size: float) -> bool:
    """
    Detect if text is likely a chapter heading.

    Heuristics:
    - Significantly larger font than average
    - Contains chapter-like keywords
    - Relatively short (headings aren't paragraphs)
    """
    text_clean = text.strip()

    # Too long for a heading
    if len(text_clean) > 100:
        return False

    # Font size significantly larger than average
    if font_size > avg_font_size * 1.3:
        # Check for chapter patterns
        chapter_patterns = [
            r'^chapter\s+\d+',
            r'^part\s+\d+',
            r'^\d+\s+[A-Z]',  # "1 Introduction"
            r'^the\s+\w+\s+page',  # "The Edit Page"
            r'^using\s+',
            r'^working\s+with',
            r'^introduction',
            r'^appendix',
            r'^index$',
            r'^glossary',
        ]

        for pattern in chapter_patterns:
            if re.match(pattern, text_clean.lower()):
                return True

        # All caps short text is often a heading
        if text_clean.isupper() and len(text_clean) < 50:
            return True

        # Title case with large font
        if font_size > avg_font_size * 1.5 and len(text_clean.split()) <= 8:
            return True

    return False


def extract_page_text_with_fonts(page) -> List[Tuple[str, float]]:
    """Extract text blocks with their font sizes."""
    blocks = []

    # Get text with detailed info
    text_dict = page.get_text("dict", flags=pymupdf.TEXT_PRESERVE_WHITESPACE)

    for block in text_dict.get("blocks", []):
        if block.get("type") != 0:  # Skip non-text blocks
            continue

        for line in block.get("lines", []):
            line_text = ""
            line_sizes = []

            for span in line.get("spans", []):
                text = span.get("text", "")
                size = span.get("size", 12)
                line_text += text
                if text.strip():
                    line_sizes.append(size)

            if line_text.strip() and line_sizes:
                avg_size = sum(line_sizes) / len(line_sizes)
                blocks.append((line_text, avg_size))

    return blocks


def clean_text(text: str) -> str:
    """Clean up common PDF artifacts."""
    # Remove page numbers at start/end of lines
    text = re.sub(r'^\d+\s*$', '', text, flags=re.MULTILINE)

    # Remove excessive whitespace
    text = re.sub(r'\n{4,}', '\n\n\n', text)

    # Fix common ligature issues
    text = text.replace('ﬁ', 'fi').replace('ﬂ', 'fl')

    # Remove soft hyphens
    text = text.replace('\xad', '')

    return text.strip()


def generate_frontmatter(title: str, chapter_num: int) -> str:
    """Generate YAML frontmatter for markdown file."""
    return f"""---
title: "{title}"
source: "DaVinci Resolve User Manual"
doc_type: "manual"
chapter: {chapter_num}
---

"""


def convert_pdf_to_markdown(
    pdf_path: Path,
    output_dir: Path,
    min_chapter_pages: int = 5
) -> List[Path]:
    """
    Convert PDF to chapter-split markdown files.

    Args:
        pdf_path: Path to input PDF
        output_dir: Directory for output markdown files
        min_chapter_pages: Minimum pages before starting new chapter

    Returns:
        List of created file paths
    """
    print(f"Opening PDF: {pdf_path}")
    doc = pymupdf.open(pdf_path)
    total_pages = len(doc)
    print(f"Total pages: {total_pages}")

    # First pass: calculate average font size across document sample
    print("Analyzing document structure...")
    sample_sizes = []
    sample_pages = min(100, total_pages)

    for i in range(0, sample_pages):
        page = doc[i]
        blocks = extract_page_text_with_fonts(page)
        sample_sizes.extend([size for _, size in blocks])

    avg_font_size = sum(sample_sizes) / len(sample_sizes) if sample_sizes else 12
    print(f"Average font size: {avg_font_size:.1f}")

    # Second pass: extract content and detect chapters
    print("Extracting content...")
    chapters = []
    current_chapter = {
        "title": "Introduction",
        "content": [],
        "start_page": 0
    }

    for page_num in range(total_pages):
        if page_num % 100 == 0:
            print(f"  Processing page {page_num + 1}/{total_pages}...")

        page = doc[page_num]
        blocks = extract_page_text_with_fonts(page)

        for text, font_size in blocks:
            text_clean = text.strip()
            if not text_clean:
                continue

            # Check for new chapter
            if (is_chapter_heading(text_clean, font_size, avg_font_size) and
                page_num - current_chapter["start_page"] >= min_chapter_pages):

                # Save current chapter if it has content
                if current_chapter["content"]:
                    chapters.append(current_chapter)

                # Start new chapter
                current_chapter = {
                    "title": text_clean,
                    "content": [],
                    "start_page": page_num
                }
                print(f"  Found chapter: {text_clean[:50]}... (page {page_num + 1})")
            else:
                current_chapter["content"].append(text_clean)

    # Don't forget the last chapter
    if current_chapter["content"]:
        chapters.append(current_chapter)

    doc.close()

    print(f"\nFound {len(chapters)} chapters")

    # Write chapters to files
    output_dir.mkdir(parents=True, exist_ok=True)
    created_files = []

    for i, chapter in enumerate(chapters, 1):
        title = chapter["title"]
        slug = slugify(title)
        filename = f"{i:02d}-{slug}.md"
        filepath = output_dir / filename

        # Build markdown content
        content_text = "\n\n".join(chapter["content"])
        content_text = clean_text(content_text)

        # Add heading and frontmatter
        markdown = generate_frontmatter(title, i)
        markdown += f"# {title}\n\n"
        markdown += content_text

        filepath.write_text(markdown, encoding="utf-8")
        created_files.append(filepath)
        print(f"  Created: {filename} ({len(content_text):,} chars)")

    return created_files


def main():
    # Default paths
    script_dir = Path(__file__).parent.parent
    default_pdf = script_dir / "pdf" / "DaVinci Resolve.pdf"
    default_output = script_dir / "transcripts" / "davinci-manual" / "transcripts"

    # Parse arguments
    pdf_path = Path(sys.argv[1]) if len(sys.argv) > 1 else default_pdf
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else default_output

    if not pdf_path.exists():
        print(f"Error: PDF not found: {pdf_path}")
        sys.exit(1)

    print(f"PDF to Markdown Converter")
    print(f"=" * 50)
    print(f"Input:  {pdf_path}")
    print(f"Output: {output_dir}")
    print()

    files = convert_pdf_to_markdown(pdf_path, output_dir)

    print()
    print(f"=" * 50)
    print(f"Done! Created {len(files)} markdown files")
    print(f"Output directory: {output_dir}")


if __name__ == "__main__":
    main()
