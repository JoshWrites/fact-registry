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

## How to Navigate

- **Starting a new experiment?** Read `research/INDEX.md`, find related prior work, create a new numbered directory in `experiments/`.
- **Making an architecture decision?** Read existing decisions in `research/decisions/`, write a new ADR.
- **Found something that doesn't work?** Write it up in `research/negative/` using the standard format.
- **Updating findings?** Edit the relevant file in `research/findings/`, update `research/INDEX.md`.

## Research Norms

- Cite sources. Every factual claim about prior work needs a reference.
- Log prompts. When an LLM generates a key finding, save the prompt that produced it.
- Run critical experiments multiple times. LLM outputs are non-deterministic.
- Never delete negative results. Mark them superseded if a better approach is found.
- Commit early, commit often. Git history is the chronological record.
