#!/usr/bin/env python3
"""
Butler Summarizer — Generate structured summaries from text files.

Usage:
    python summarizer.py <file-path>                    # Summarize a single file
    python summarizer.py <file-path> --format bullet    # Bullet-point format
    python summarizer.py <file-path> --format executive # Executive summary
    python summarizer.py <file-path> --max-lines 10     # Limit output length
    python summarizer.py <dir-path> --recursive         # Summarize all files in directory

Formats:
    bullet     — Bullet-point key takeaways (default)
    executive  — One-paragraph executive summary
    detailed   — Structured sections with headings
    outline    — Hierarchical outline format
"""

import sys
import os
import re
from pathlib import Path
from collections import Counter


def read_file(filepath):
    """Read and return file contents."""
    path = Path(filepath)
    if not path.exists():
        print(f"❌ File not found: {filepath}")
        sys.exit(1)
    if not path.is_file():
        print(f"❌ Not a file: {filepath}")
        sys.exit(1)
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def extract_sections(text):
    """Extract sections from markdown or structured text."""
    sections = []
    current_heading = "Introduction"
    current_content = []

    for line in text.split("\n"):
        if line.startswith("#"):
            if current_content:
                sections.append({
                    "heading": current_heading,
                    "content": "\n".join(current_content).strip()
                })
            current_heading = line.lstrip("#").strip()
            current_content = []
        else:
            current_content.append(line)

    if current_content:
        sections.append({
            "heading": current_heading,
            "content": "\n".join(current_content).strip()
        })

    return sections


def extract_key_sentences(text, max_sentences=5):
    """Extract the most important sentences using simple scoring."""
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 20]

    if not sentences:
        return []

    # Score sentences
    word_freq = Counter()
    for sentence in sentences:
        words = re.findall(r'\w+', sentence.lower())
        word_freq.update(words)

    # Remove very common words
    stop_words = {"the", "a", "an", "is", "are", "was", "were", "in", "on", "at",
                  "to", "for", "of", "and", "or", "but", "not", "with", "this",
                  "that", "it", "be", "as", "by", "from", "has", "have", "had",
                  "will", "would", "can", "could", "do", "does", "did"}

    scored = []
    for i, sentence in enumerate(sentences):
        words = re.findall(r'\w+', sentence.lower())
        meaningful = [w for w in words if w not in stop_words and len(w) > 2]
        score = sum(word_freq[w] for w in meaningful)
        # Boost first sentences (usually more important)
        if i < 3:
            score *= 1.5
        # Boost sentences with important keywords
        if any(kw in sentence.lower() for kw in ["important", "key", "critical", "must",
                                                    "essential", "significant", "main",
                                                    "conclusion", "result", "finding"]):
            score *= 1.3
        scored.append((score, i, sentence))

    scored.sort(reverse=True)
    top = scored[:max_sentences]
    # Return in original order
    top.sort(key=lambda x: x[1])
    return [s[2] for s in top]


def get_stats(text):
    """Get basic text statistics."""
    words = text.split()
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip()]
    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    headings = [line for line in text.split("\n") if line.startswith("#")]

    return {
        "words": len(words),
        "sentences": len(sentences),
        "paragraphs": len(paragraphs),
        "headings": len(headings),
        "reading_time_min": max(1, len(words) // 200)
    }


def format_bullet(filepath, text, max_lines=8):
    """Generate bullet-point summary."""
    stats = get_stats(text)
    key_sentences = extract_key_sentences(text, max_lines)

    print(f"# 📄 Summary: {Path(filepath).name}")
    print()
    print(f"**Source:** `{filepath}`")
    print(f"**Words:** {stats['words']:,} | **Reading time:** ~{stats['reading_time_min']} min")
    print()
    print("## Key Takeaways")
    print()
    for sentence in key_sentences:
        print(f"- {sentence.strip()}.")
    print()


def format_executive(filepath, text):
    """Generate one-paragraph executive summary."""
    stats = get_stats(text)
    key_sentences = extract_key_sentences(text, 3)

    print(f"# 📋 Executive Summary: {Path(filepath).name}")
    print()
    print(f"*{stats['words']:,} words | ~{stats['reading_time_min']} min read*")
    print()
    summary = " ".join(s.strip() + "." for s in key_sentences)
    print(summary)
    print()


def format_detailed(filepath, text):
    """Generate detailed structured summary."""
    stats = get_stats(text)
    sections = extract_sections(text)
    key_sentences = extract_key_sentences(text, 5)

    print(f"# 📑 Detailed Summary: {Path(filepath).name}")
    print()
    print(f"**Source:** `{filepath}`")
    print(f"**Stats:** {stats['words']:,} words | {stats['paragraphs']} paragraphs | ~{stats['reading_time_min']} min read")
    print()

    print("## Overview")
    print()
    for sentence in key_sentences[:3]:
        print(f"- {sentence.strip()}.")
    print()

    if sections and len(sections) > 1:
        print("## Section Breakdown")
        print()
        for section in sections:
            if section["content"]:
                section_sentences = extract_key_sentences(section["content"], 2)
                print(f"### {section['heading']}")
                for s in section_sentences:
                    print(f"- {s.strip()}.")
                print()

    print("## Document Statistics")
    print()
    print(f"| Metric | Value |")
    print(f"|--------|-------|")
    print(f"| Words | {stats['words']:,} |")
    print(f"| Sentences | {stats['sentences']} |")
    print(f"| Paragraphs | {stats['paragraphs']} |")
    print(f"| Headings | {stats['headings']} |")
    print(f"| Est. reading time | {stats['reading_time_min']} min |")


def format_outline(filepath, text):
    """Generate hierarchical outline."""
    sections = extract_sections(text)

    print(f"# 📝 Outline: {Path(filepath).name}")
    print()

    for i, section in enumerate(sections, 1):
        print(f"{i}. **{section['heading']}**")
        if section["content"]:
            key = extract_key_sentences(section["content"], 2)
            for s in key:
                print(f"   - {s.strip()}.")
    print()


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    filepath = sys.argv[1]
    fmt = "bullet"
    max_lines = 8
    recursive = False

    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--format" and i + 1 < len(sys.argv):
            fmt = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--max-lines" and i + 1 < len(sys.argv):
            max_lines = int(sys.argv[i + 1])
            i += 2
        elif sys.argv[i] == "--recursive":
            recursive = True
            i += 1
        else:
            i += 1

    if recursive and Path(filepath).is_dir():
        files = sorted(Path(filepath).rglob("*.md")) + sorted(Path(filepath).rglob("*.txt"))
        for f in files:
            text = read_file(str(f))
            format_bullet(str(f), text, max_lines)
            print("---\n")
        return

    text = read_file(filepath)

    formatters = {
        "bullet": lambda: format_bullet(filepath, text, max_lines),
        "executive": lambda: format_executive(filepath, text),
        "detailed": lambda: format_detailed(filepath, text),
        "outline": lambda: format_outline(filepath, text),
    }

    formatter = formatters.get(fmt)
    if not formatter:
        print(f"❌ Unknown format: {fmt}. Use: bullet, executive, detailed, outline")
        sys.exit(1)

    formatter()


if __name__ == "__main__":
    main()
