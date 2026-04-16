#!/usr/bin/env python3
"""
Query the research index. Uses SQLite FTS5 for full-text search across
summaries, tags, sections, and file paths.

Searches concepts, not just keywords. "linking docs to source code" will
find entries about Swimm, Mintlify, and evidence linking even if you
don't remember those names.

Usage:
    python tools/lookup.py "linking documentation to code"
    python tools/lookup.py "entity resolution growing registry"
    python tools/lookup.py "what failed and why"
    python tools/lookup.py --files-only "contradiction detection"
    python tools/lookup.py --tags "wikidata"

Run build_index.py first if the index doesn't exist or sources changed.
"""

import argparse
import sqlite3
import sys
from pathlib import Path

DB_PATH = Path(__file__).parent / "research_index.db"


def ensure_index():
    if not DB_PATH.exists():
        print("Index not found. Building...", file=sys.stderr)
        import build_index
        build_index.build()


def search(query, tags_only=False, top_n=8):
    conn = sqlite3.connect(DB_PATH)

    if tags_only:
        # Simple LIKE search on tags column
        terms = [t.strip() for t in query.split()]
        conditions = " AND ".join(f"tags LIKE '%{t}%'" for t in terms)
        rows = conn.execute(
            f"SELECT summary, file_path, anchor, tags, section, source_file "
            f"FROM entries WHERE {conditions} LIMIT ?",
            (top_n,),
        ).fetchall()
    else:
        # FTS5 search — handles natural language queries
        # Convert natural query to FTS terms (OR between words for broader matching)
        fts_query = " OR ".join(query.split())
        rows = conn.execute(
            "SELECT e.summary, e.file_path, e.anchor, e.tags, e.section, e.source_file "
            "FROM entries_fts fts "
            "JOIN entries e ON e.id = fts.rowid "
            "WHERE entries_fts MATCH ? "
            "ORDER BY rank "
            "LIMIT ?",
            (fts_query, top_n),
        ).fetchall()

    conn.close()
    return rows


def main():
    parser = argparse.ArgumentParser(
        description="Search the fact-registry research index"
    )
    parser.add_argument("query", nargs="+", help="Search terms or natural language query")
    parser.add_argument("--tags", action="store_true", help="Search tags only")
    parser.add_argument("--files-only", action="store_true", help="Return only file paths to read")
    parser.add_argument("-n", type=int, default=8, help="Max results (default: 8)")
    args = parser.parse_args()

    ensure_index()

    query = " ".join(args.query)
    results = search(query, tags_only=args.tags, top_n=args.n)

    if not results:
        print(f"No results for: {query}")
        return

    if args.files_only:
        seen = set()
        for _, file_path, anchor, *_ in results:
            if not file_path:
                continue
            ref = f"research/{file_path}"
            if anchor:
                ref += f"#{anchor}"
            if ref not in seen:
                seen.add(ref)
                print(ref)
        return

    print(f"─── Results for: {query} ───")
    for summary, file_path, anchor, tags, section, source in results:
        ref = ""
        if file_path:
            ref = f"research/{file_path}"
            if anchor:
                ref += f"#{anchor}"

        # Truncate summary for readability
        if len(summary) > 200:
            summary = summary[:200] + "..."

        print(f"\n[{source} → {section}]")
        print(f"  {summary}")
        if ref:
            print(f"  → READ: {ref}")
        if tags:
            print(f"  TAGS: {tags}")


if __name__ == "__main__":
    main()
