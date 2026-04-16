# N002: Direct Index Reading Doesn't Scale
**Date:** 2026-04-16
**Status:** rejected
**Tags:** context-management, process, information-architecture

## Hypothesis
The research INDEX.md file could be read directly at the start of each session to orient the LLM co-researcher on prior work.

## What Happened
At 94 entries and ~120 lines, the index was already borderline. Projecting to hundreds of sources, reading the full index would consume significant context tokens just to find the 2-3 entries relevant to the current task. Worse, keyword search fails across sessions — terms like "Swimm" or "BREX" won't be in the LLM's vocabulary next week.

## Why It Failed
An index designed for human scanning is not optimized for LLM retrieval. Humans can skim and skip. LLMs consume every token. The cost of loading irrelevant entries scales linearly with index size.

## What We Learned
Two-pass retrieval is the right pattern: (1) a disposable subagent reads the full index in its own context, finds relevant entries with semantic understanding, and returns a focused brief; (2) the main session reads only the specific sections the scout identified. This keeps the main context clean and handles vocabulary drift across sessions.

An FTS5 SQLite lookup tool (`tools/lookup.py`) serves as a CLI fallback for quick keyword searches, but lacks the semantic understanding of a subagent scout.

## Impact on Design
Documented in CLAUDE.md as the standard retrieval procedure. The research repo's information architecture (INDEX → findings → bibliography) mirrors the fact-registry problem itself — a validation of the three-layer reference pattern.
