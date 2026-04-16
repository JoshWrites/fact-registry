#!/usr/bin/env python3
"""
Research index lookup. Returns matching entries from INDEX.md and BIBLIOGRAPHY.md
for a given query. Designed to be called by an LLM assistant to find relevant
research without reading the full index.

Usage:
    python tools/lookup.py "entity resolution"
    python tools/lookup.py "code links evidence"
    python tools/lookup.py --tags contradiction-detection
    python tools/lookup.py --file-for "should we link facts to code"
"""

import argparse
import re
import sys
from pathlib import Path

RESEARCH_DIR = Path(__file__).parent.parent / "research"
INDEX_PATH = RESEARCH_DIR / "INDEX.md"
BIBLIO_PATH = RESEARCH_DIR / "BIBLIOGRAPHY.md"


def load_entries(path):
    """Parse a markdown file into searchable entries.

    Each entry is a block of consecutive non-blank lines that contains
    a link, tag, or is part of a Q&A lookup pair.
    """
    entries = []
    current_block = []
    current_section = ""

    for line in path.read_text().splitlines():
        # Track section headers
        if line.startswith("## ") or line.startswith("### "):
            if current_block:
                entries.append({
                    "section": current_section,
                    "text": "\n".join(current_block),
                    "source": path.name,
                })
                current_block = []
            current_section = line.lstrip("#").strip()
            continue

        if line.strip() == "" or line.startswith("---"):
            if current_block:
                entries.append({
                    "section": current_section,
                    "text": "\n".join(current_block),
                    "source": path.name,
                })
                current_block = []
            continue

        current_block.append(line)

    # Final block
    if current_block:
        entries.append({
            "section": current_section,
            "text": "\n".join(current_block),
            "source": path.name,
        })

    return entries


def score_entry(entry, terms):
    """Score an entry against search terms. Higher = more relevant."""
    text = entry["text"].lower()
    section = entry["section"].lower()
    score = 0

    for term in terms:
        term_lower = term.lower()
        # Exact phrase match in text
        score += text.count(term_lower) * 2
        # Match in section name
        score += section.count(term_lower) * 3
        # Tag match (stronger signal)
        if f"tags:" in text.lower() and term_lower in text.lower():
            score += 5

    return score


def search(query, tags_only=False, file_for=False, top_n=5):
    """Search index and bibliography for matching entries."""
    terms = [t.strip() for t in query.split() if t.strip()]

    # Also try the full query as a phrase
    phrase_terms = [query.lower()]

    all_entries = []

    if INDEX_PATH.exists():
        all_entries.extend(load_entries(INDEX_PATH))
    if BIBLIO_PATH.exists():
        all_entries.extend(load_entries(BIBLIO_PATH))

    if tags_only:
        # Only match entries where query terms appear in TAGS
        results = []
        for entry in all_entries:
            text = entry["text"].lower()
            if "tags:" not in text:
                continue
            tag_line = [l for l in text.split("\n") if "tags:" in l.lower()]
            if tag_line and any(t.lower() in tag_line[0] for t in terms):
                results.append((10, entry))
        results.sort(key=lambda x: -x[0])
    else:
        scored = []
        for entry in all_entries:
            s = score_entry(entry, terms) + score_entry(entry, phrase_terms)
            if s > 0:
                scored.append((s, entry))
        scored.sort(key=lambda x: -x[0])
        results = scored

    if file_for:
        # Return just the local file paths mentioned in matching entries
        files = set()
        for _, entry in results[:top_n]:
            for match in re.findall(r'\[.*?\]\(((?!https?://)[^\)]*\.md(?:#[^\)]*)?)\)', entry["text"]):
                # Strip to just the .md file (with optional #anchor)
                files.add(match)
        return files

    return results[:top_n]


def main():
    parser = argparse.ArgumentParser(description="Search the fact-registry research index")
    parser.add_argument("query", nargs="*", help="Search terms")
    parser.add_argument("--tags", action="store_true", help="Search tags only")
    parser.add_argument("--file-for", action="store_true", help="Return only file paths to read")
    parser.add_argument("-n", type=int, default=5, help="Max results (default: 5)")
    args = parser.parse_args()

    if not args.query:
        parser.print_help()
        sys.exit(1)

    query = " ".join(args.query)

    if args.file_for:
        files = search(query, file_for=True, top_n=args.n)
        if files:
            print("Read these files for context:")
            for f in sorted(files):
                print(f"  research/{f}")
        else:
            print("No matching research found.")
        return

    results = search(query, tags_only=args.tags, top_n=args.n)

    if not results:
        print(f"No results for: {query}")
        return

    print(f"Results for: {query}")
    print(f"{'=' * 60}")

    for score, entry in results:
        source_label = f"[{entry['source']}]"
        if entry["section"]:
            source_label += f" → {entry['section']}"
        print(f"\n{source_label} (relevance: {score})")
        # Truncate long entries to keep output focused
        text = entry["text"]
        if len(text) > 300:
            text = text[:300] + "..."
        print(text)


if __name__ == "__main__":
    main()
