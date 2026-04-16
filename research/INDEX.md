# Research Index

Last updated: 2026-04-16

## Project Phase: Experimental Validation

Landscape research is complete. Five hypotheses defined, awaiting controlled tests.

---

## Findings

- [Landscape: failed systems](findings/failed-systems.md) — Seven recurring failure patterns from Knowledge Vault, Watson, Cyc, Semantic Web, NELL — STATUS: complete — TAGS: prior-work, failure-modes
- [Landscape: successful patterns](findings/successful-patterns.md) — Converged architecture from pharma, aviation, legal, and LLM-era tools — STATUS: complete — TAGS: prior-work, architecture
- [Landscape: off-the-shelf survey](findings/off-the-shelf.md) — Exhaustive search confirms no existing product solves this — STATUS: complete — TAGS: prior-work, build-vs-buy
- [Academic: CDCR and NLP](findings/academic-cdcr-nlp.md) — Cross-document coreference, NLI, claim decomposition, entity linking research — STATUS: complete — TAGS: academic, entity-resolution, contradiction-detection
- [Analysis: Wikidata model](findings/wikidata-model.md) — What to steal and what to skip from Wikidata's data model — STATUS: complete — TAGS: data-model, wikidata
- [Analysis: library science](findings/library-science.md) — FRBR, authority control, SKOS, and Ranganathan's test — STATUS: complete — TAGS: data-model, information-science
- [Analysis: evidence linking](findings/evidence-linking.md) — Why persistent code/UI links aren't worth it; periodic verification instead — STATUS: complete — TAGS: architecture, maintenance

## Decisions

- [D001: SQLite over graph databases](decisions/D001-sqlite-over-graph.md) — STATUS: active — TAGS: architecture, storage
- [D002: Separate extraction from resolution](decisions/D002-extraction-resolution-separation.md) — STATUS: active — TAGS: architecture, pipeline
- [D003: Wikidata rank system](decisions/D003-rank-system.md) — STATUS: active — TAGS: data-model, conflict-detection
- [D004: No persistent evidence links](decisions/D004-no-evidence-links.md) — STATUS: active — TAGS: architecture, maintenance
- [D005: Post-hoc entity resolution](decisions/D005-post-hoc-resolution.md) — STATUS: active — TAGS: architecture, entity-resolution

## Negative Results

(None yet — experiments not started)

## Experiments

- [H1: Claim decomposition quality](experiments/H1-claim-decomposition/) — Can an LLM reliably decompose fact strings into entity+property+value? — STATUS: not started
- [H2: Entity embedding clustering](experiments/H2-entity-clustering/) — Do entity mentions cluster correctly for technical documentation? — STATUS: not started
- [H3: NLI contradiction detection](experiments/H3-nli-contradictions/) — Can NLI catch implicit contradictions in our content? — STATUS: not started
- [H4: Rank system editorial fit](experiments/H4-rank-system/) — Does Wikidata's rank model work for KB editorial workflow? — STATUS: not started
- [H5: Incremental entity duplication](experiments/H5-incremental-duplication/) — What's the duplicate rate when processing articles incrementally? — STATUS: not started

## Open Questions

- How to distinguish contradiction from version-specific difference (no prior work addresses this)
- Minimum viable entity granularity for useful conflict detection
- Whether the system needs to understand product versioning
- Optimal frequency for periodic verification sweeps
