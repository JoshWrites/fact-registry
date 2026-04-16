# Fact Registry — LLM Co-Researcher Context

Load this file at the start of every session. It tells you where the project is, what's been decided, and where to find details.

---

## What This Project Is

A research project to build an automated system for detecting factual contradictions across a technical knowledge base. The human researcher is a technical writer maintaining a large KB for a SaaS product. They cannot stop writing new content to audit existing content. This tool must run alongside regular work, not replace it.

## Design Principles

1. **Platform-agnostic.** No assumptions about Zendesk, Confluence, or any specific CMS. The system works on any corpus of technical articles.
2. **Maintainable by one person.** If it requires more effort to maintain than the problem it solves, it has failed.
3. **Incremental.** Process new/changed articles without reprocessing the entire corpus.
4. **Error-tolerant.** Missing data for a field doesn't break the system. New data types don't break existing records.
5. **Document everything.** Negative results are as valuable as positive ones. Every experiment is logged.

## Agent-Driven Operation

This system is designed to be operated by an AI agent, directed and reviewed by a human. The human (a tech writer) sets priorities, reviews results, and makes editorial decisions. The agent runs extraction, resolution, conflict detection, and reporting. The design bar is not "can a human do this?" but "can an agent do this reliably with minimal supervision?"

This principle affects every design choice: the pipeline must be automatable, errors must be surfaceable (not silent), and the human touchpoints must be well-defined review gates rather than continuous involvement.

## Portability and Public Documentation

This project is designed to be company-agnostic and platform-agnostic. No references to specific companies, products, or platforms appear in this repo. This is a hard requirement for three reasons:
1. The tool should work on any technical KB, not just the current one
2. The repo is public and serves as a portfolio piece
3. If the research proves novel, it may warrant a conference talk or paper

All company-specific data, configurations, and article content stay in private repos. This repo contains only methodology, findings, tools, and anonymized sample data.

## Current Phase

Check `research/INDEX.md` for the authoritative state. That file is the map — this file is the compass.

## Key Decisions Made

Read `research/decisions/` for full context on each. Summary:

- **SQLite over graph DBs** — operational simplicity wins at our scale (~700 docs, ~11K facts)
- **Separate extraction from entity resolution** — raw claims are immutable; entity linking is a mutable, re-runnable layer
- **No persistent code/UI evidence links** — periodic stateless verification instead
- **Wikidata rank system adapted** — preferred/normal/deprecated ranks, never delete claims
- **Post-hoc entity resolution, not extraction-time** — mistakes in resolution are fixable without re-extraction

## What Has Been Ruled Out

- Off-the-shelf solutions (none exist for this specific problem — surveyed exhaustively)
- Graph databases (Neo4j, TypeDB, TerminusDB — operational overhead for no query benefit at our scale)
- RDF/triple stores (designed for billions of triples, not thousands)
- Persistent claim-to-code or claim-to-UI links (maintenance cost exceeds value)
- Pure LLM approaches to cross-document coreference (CRAC 2025 confirmed: LLMs alone can't do CDCR)

## How to Retrieve Prior Research

**Do not read research files directly into your main context.** Use two-pass retrieval:

**Pass 1 — Scout.** Dispatch an Explore subagent against this repo:

> "Read `research/INDEX.md` and `research/BIBLIOGRAPHY.md` in `/Users/jlevine/Documents/Repos/fact-registry`. Find everything we know about [TOPIC]. Follow links to the relevant finding/decision files and read only the matching sections. Return:
> 1. A summary of what we know (under 200 words)
> 2. For anything deep or nuanced: the exact file path and line range I should read myself (e.g. `findings/evidence-linking.md lines 11-38`)
> 3. Whether this is settled (decision made) or open (still a question)"

**Pass 2 — Targeted read.** Only if the scout says the full reasoning matters for your current task, read the specific lines it identified. Not the whole file. Not the whole directory.

**Why this pattern:** Research files will grow to thousands of lines across dozens of files. Reading them into your main context wastes tokens and dilutes focus. The scout subagent absorbs the full research corpus in its own disposable context, extracts what's relevant, and returns a focused brief. Your context gets the conclusion and a pointer, not the raw material.

**CLI fallback:** `python3 tools/lookup.py "your query"` uses SQLite FTS5 search across the index and bibliography. Useful for quick keyword lookups but lacks semantic understanding. Prefer the subagent for conceptual questions.

## How to Navigate (for adding to the research)

- **Starting a new experiment?** Scout for related prior work first, then create a new numbered directory in `experiments/`.
- **Making an architecture decision?** Read existing decisions in `research/decisions/`, write a new ADR.
- **Found something that doesn't work?** Write it up in `research/negative/` using the standard format.
- **Updating findings?** Edit the relevant file in `research/findings/`, update `research/INDEX.md`, then rebuild the search index: `python3 tools/build_index.py`.

## Research Norms

- Cite sources. Every factual claim about prior work needs a reference.
- Log prompts. When an LLM generates a key finding, save the prompt that produced it.
- Run critical experiments multiple times. LLM outputs are non-deterministic.
- Never delete negative results. Mark them superseded if a better approach is found.
- Commit early, commit often. Git history is the chronological record.
