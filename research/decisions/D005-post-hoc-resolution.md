# D005: Post-Hoc Entity Resolution Over Extraction-Time
**Date:** 2026-04-16
**Status:** active
**Tags:** entity-resolution, pipeline, matching

## Context
Entity resolution -- matching raw mention strings to canonical entities -- can happen at extraction time or as a separate pass. D002 established that extraction and resolution are separate pipeline stages. This decision addresses the specific resolution strategy: how should the resolution pass work?

## Options Considered
**(A) Extraction-time resolution** -- The LLM sees an article and produces canonical entity IDs directly, resolving mentions as part of extraction. Single pass, no separate resolution infrastructure. But this couples resolution quality to the extraction prompt, makes resolution errors unrecoverable without re-extraction, and provides no mechanism for bulk correction.

**(B) Embed-then-cluster** -- Embed all entity mentions into a vector space, cluster with HDBSCAN or similar, then have the LLM name each cluster as a canonical entity. Good for initial bootstrap when no entity registry exists yet. Handles synonyms and variant spellings naturally through embedding similarity. But expensive to re-run incrementally and requires tuning cluster parameters.

**(C) Incremental matching** -- New mentions are matched against an existing entity registry. Exact match and alias match cover approximately 80% of cases. Unresolved mentions go to the LLM for classification: new entity, alias of existing entity, or ambiguous. Cheap per-mention (one LLM call per unresolved mention, not per claim).

## Decision
Incremental matching (C) for ongoing operation, with embed-then-cluster (B) for the initial bootstrap. At approximately 700 documents, the entire entity list fits comfortably in a single LLM context window. The bootstrap pass uses embedding similarity to discover the initial entity clusters and their aliases. After bootstrap, incremental matching handles new articles cheaply: exact and alias matching resolves most mentions without any LLM calls, and the LLM only sees the genuinely novel mentions.

## Consequences
- Need a canonical entities table with an aliases list per entity.
- Need an embedding step for the initial bootstrap phase.
- Incremental matching is cheap: one LLM call per unresolved mention, not per claim. Most mentions resolve via exact or alias match.
- Entity deduplication requires periodic reconciliation passes to catch entities that should have been merged but were created separately.
- The entity registry grows monotonically -- new entities are added, existing ones gain aliases, but nothing is deleted (only merged).

## References
- iText2KG analysis (entity duplication as an unsolved problem in extraction pipelines)
- DIAL-KG approach to entity linking
- Academic cross-document coreference resolution (CDCR) research
- Entity-claim systems research section on incremental resolution strategies
