# fact-registry

A research project exploring automated factual consistency management for technical knowledge bases.

## The Problem

Technical knowledge bases drift. The same fact gets stated in multiple articles, and over time those statements diverge. One article says a session expires in 10 minutes; another says 24 hours. Both are about the same feature. Neither author knows the other article exists.

At small scale, a human can read the whole KB and catch these. At 500+ articles with biweekly product releases, that stops working. The contradictions accumulate, users hit them, and trust erodes.

## The Research Question

Can we build a system that:

1. Extracts structured factual claims from technical articles
2. Resolves when two differently-worded claims are about the same entity
3. Detects conflicting values across documents
4. Supports incremental updates as articles are added or edited
5. Enables bulk correction of stale facts across the corpus

...and does so reliably enough to be maintained by one person alongside their regular writing work?

## Status

**Phase: Research and experimental validation**

We have completed a landscape survey of prior work, identified what has succeeded and failed, and defined five hypotheses that need experimental validation before building anything. See `research/INDEX.md` for the current state.

## What This Is Not

- Not a finished tool (yet)
- Not a general-purpose knowledge graph system
- Not an academic paper (yet) — though the findings may warrant one

## Structure

```
CLAUDE.md               # LLM co-researcher context (loads every session)
METHODOLOGY.md          # How LLM assistance is used in this project
research/
  INDEX.md              # Machine-readable research index with tags
  findings/             # Synthesized research findings
  decisions/            # Architecture Decision Records (ADR format)
  negative/             # What didn't work and why
experiments/            # Numbered experiments with hypotheses, methods, results
data/                   # Anonymized sample data for reproducibility
tools/                  # Scripts and utilities developed during research
```

## Attribution

This project uses LLM assistance (Claude, Anthropic) as a co-researcher for literature review, experimental design, and code generation. All findings are verified by the human researcher. LLM contributions are documented in commit messages and `METHODOLOGY.md`.

## License

TBD — will be open-sourced once initial research phase completes.
