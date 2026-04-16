# D002: Separate Extraction from Entity Resolution
**Date:** 2026-04-16
**Status:** active
**Tags:** pipeline, extraction, entity-resolution

## Context
When extracting claims from KB articles, should the LLM assign canonical entity IDs at extraction time, or should raw claims be resolved to entities in a separate pass? This is a pipeline architecture decision about whether extraction and resolution are one step or two.

## Options Considered
**(A) Extraction-time assignment** -- The LLM reads an article and produces fully resolved claims with canonical entity IDs in a single pass. Simpler pipeline, fewer moving parts. But if the LLM assigns the wrong entity, every downstream record is poisoned. Fixing requires re-extracting the entire article, not just re-linking.

**(B) Post-hoc resolution** -- Extraction produces raw triples: (raw entity mention, property, value). The raw mention string is preserved exactly as it appeared in the source article. Resolution happens in a separate pass, matching raw mentions to canonical entities. Resolution can be re-run independently without touching the extraction output.

## Decision
Post-hoc resolution. The raw mention string is preserved as ground truth -- it is the literal text from the article and is always correct in that sense. Resolution produces a mapping table (raw mention -> canonical entity) that can be regenerated, corrected in bulk, or overridden per-record without re-extracting anything. At 11K claims, re-running resolution takes seconds.

## Consequences
- Two-pass pipeline: extract first, resolve second.
- The raw claims table is immutable after extraction. It represents exactly what the LLM found in each article.
- Entity links are mutable. They can be corrected, overridden, or regenerated without invalidating extraction work.
- Need an audit log for link changes so resolution decisions are traceable.
- Slightly more complex pipeline orchestration, but each step is independently testable and debuggable.

## References
- NELL failure analysis (error compounding from baked-in entity assignment at extraction time)
- Entity-claim systems research
- EDC paper (EMNLP 2024) on decoupled extraction and resolution
