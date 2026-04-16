#!/usr/bin/env python3
"""
Build a SQLite research index from INDEX.md and BIBLIOGRAPHY.md.
Run this after editing either file. The lookup tool queries the result.

Usage:
    python tools/build_index.py
"""

import re
import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent.parent
RESEARCH = ROOT / "research"
DB_PATH = ROOT / "tools" / "research_index.db"

DDL = """
CREATE TABLE IF NOT EXISTS entries (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    source_file TEXT NOT NULL,
    section     TEXT,
    summary     TEXT NOT NULL,
    file_path   TEXT,
    anchor      TEXT,
    tags        TEXT,
    entry_type  TEXT
);

CREATE VIRTUAL TABLE IF NOT EXISTS entries_fts USING fts5(
    summary, tags, section, file_path,
    content=entries,
    content_rowid=id
);

CREATE TRIGGER IF NOT EXISTS entries_ai AFTER INSERT ON entries BEGIN
    INSERT INTO entries_fts(rowid, summary, tags, section, file_path)
    VALUES (new.id, new.summary, new.tags, new.section, new.file_path);
END;

CREATE TRIGGER IF NOT EXISTS entries_ad AFTER DELETE ON entries BEGIN
    INSERT INTO entries_fts(entries_fts, rowid, summary, tags, section, file_path)
    VALUES ('delete', old.id, old.summary, old.tags, old.section, old.file_path);
END;
"""


def parse_bibliography(path):
    """Parse BIBLIOGRAPHY.md into entries."""
    entries = []
    section = ""
    for line in path.read_text().splitlines():
        if line.startswith("## "):
            section = line.lstrip("# ").strip()
            continue
        if not line.startswith("- **"):
            continue

        # Extract the summary (everything before the → arrow or TAGS:)
        summary = line.lstrip("- ").strip()

        # Extract file path reference
        file_refs = re.findall(r'→ \[([^\]]*)\]\(([^)]+)\)', line)
        file_path = ""
        anchor = ""
        if file_refs:
            _, ref = file_refs[0]
            if "#" in ref:
                file_path, anchor = ref.split("#", 1)
            else:
                file_path = ref

        # Extract tags
        tags = ""
        tag_match = re.search(r'TAGS:\s*(.+)$', line)
        if tag_match:
            tags = tag_match.group(1).strip()
            # Remove tags from summary
            summary = summary[:summary.rfind("— TAGS:")].strip()

        entries.append({
            "source_file": "BIBLIOGRAPHY.md",
            "section": section,
            "summary": summary,
            "file_path": file_path,
            "anchor": anchor,
            "tags": tags,
            "entry_type": "source",
        })

    return entries


def parse_index(path):
    """Parse INDEX.md quick lookup section into entries."""
    entries = []
    section = ""
    question = ""

    for line in path.read_text().splitlines():
        if line.startswith("### "):
            section = line.lstrip("# ").strip()
            continue
        if line.startswith("- **") and "**" in line[4:]:
            # This is a Q&A entry
            q_match = re.match(r'- \*\*(.+?)\*\*\s*(.*)', line)
            if q_match:
                question = q_match.group(1)
                rest = q_match.group(2).strip()

                file_refs = re.findall(r'\[([^\]]*)\]\(([^)]+)\)', rest)
                file_path = ""
                anchor = ""
                if file_refs:
                    _, ref = file_refs[0]
                    if "#" in ref:
                        file_path, anchor = ref.split("#", 1)
                    else:
                        file_path = ref

                # Extract tags if present
                tags = ""
                tag_match = re.search(r'TAGS:\s*(.+)$', rest)
                if tag_match:
                    tags = tag_match.group(1).strip()

                # Clean the answer portion
                answer = re.sub(r'→\s*\[.*', '', rest).strip()

                entries.append({
                    "source_file": "INDEX.md",
                    "section": section,
                    "summary": f"{question} — {answer}",
                    "file_path": file_path,
                    "anchor": anchor,
                    "tags": tags,
                    "entry_type": "question",
                })
            continue

        # Decision/finding entries
        if line.startswith("- ["):
            match = re.match(r'- \[([^\]]+)\]\(([^)]+)\)\s*—\s*(.*)', line)
            if match:
                title = match.group(1)
                ref = match.group(2)
                rest = match.group(3)

                file_path = ref
                anchor = ""
                if "#" in ref:
                    file_path, anchor = ref.split("#", 1)

                tags = ""
                tag_match = re.search(r'TAGS:\s*(.+)$', rest)
                if tag_match:
                    tags = tag_match.group(1).strip()

                entries.append({
                    "source_file": "INDEX.md",
                    "section": section,
                    "summary": f"{title} — {rest}",
                    "file_path": file_path,
                    "anchor": anchor,
                    "tags": tags,
                    "entry_type": "finding" if "finding" in ref else "decision",
                })

    return entries


def build():
    entries = []

    if (RESEARCH / "INDEX.md").exists():
        entries.extend(parse_index(RESEARCH / "INDEX.md"))
    if (RESEARCH / "BIBLIOGRAPHY.md").exists():
        entries.extend(parse_bibliography(RESEARCH / "BIBLIOGRAPHY.md"))

    # Rebuild database
    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = sqlite3.connect(DB_PATH)
    conn.executescript(DDL)

    for e in entries:
        conn.execute(
            "INSERT INTO entries (source_file, section, summary, file_path, anchor, tags, entry_type) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (e["source_file"], e["section"], e["summary"], e["file_path"], e["anchor"], e["tags"], e["entry_type"]),
        )

    conn.commit()
    count = conn.execute("SELECT COUNT(*) FROM entries").fetchone()[0]
    print(f"Built index: {count} entries in {DB_PATH}")
    conn.close()


if __name__ == "__main__":
    build()
