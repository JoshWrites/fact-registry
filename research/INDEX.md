# Research Index

Last updated: 2026-04-16

## Project Phase: Experimental Validation

Landscape research is complete. Five hypotheses defined, awaiting controlled tests.

---

## Quick Lookup

Common questions mapped to the specific section that answers them. Read the section, not the whole file. Follow to BIBLIOGRAPHY.md for full sources.

### Has this been tried before?
- **Has anyone built this?** No off-the-shelf solution exists → [off-the-shelf.md](findings/off-the-shelf.md) (whole file, it's the survey)
- **What systems tried and failed?** Seven major systems → [failed-systems.md#systems](findings/failed-systems.md#systems)
- **What are the common failure modes?** Seven patterns → [failed-systems.md#seven-recurring-failure-patterns](findings/failed-systems.md#seven-recurring-failure-patterns)
- **What HAS worked at small scale?** Four domains converged on same architecture → [successful-patterns.md#converged-pattern](findings/successful-patterns.md#converged-pattern)

### Entity resolution
- **How do you know two facts are about the same thing?** Open problem. Best approaches → [academic-cdcr-nlp.md#entity-linking](findings/academic-cdcr-nlp.md#entity-linking)
- **Can LLMs do cross-document coreference?** Not alone. Need hybrid → [academic-cdcr-nlp.md#llm-cdcr](findings/academic-cdcr-nlp.md#llm-cdcr)
- **What accuracy to expect on technical docs?** ~64 F1, drops from 76 on easy text → [academic-cdcr-nlp.md#cdcr-benchmarks](findings/academic-cdcr-nlp.md#cdcr-benchmarks)
- **What makes entity matching hard?** Lexical diversity, near-miss entities, temporal evolution → [academic-cdcr-nlp.md#hard-cases](findings/academic-cdcr-nlp.md#hard-cases)
- **How to build an entity registry from scratch?** Incremental matching → [D005](decisions/D005-post-hoc-resolution.md), sources: iText2KG, DIAL-KG in [BIBLIOGRAPHY.md#entity-resolution](BIBLIOGRAPHY.md#entity-resolution-and-coreference)

### Contradiction detection
- **Can NLI find contradictions?** Explicit yes, implicit misses 30-40% → [academic-cdcr-nlp.md#contradiction-detection](findings/academic-cdcr-nlp.md#contradiction-detection)
- **What's the best approach?** NLI as filter, LLM as judge → [academic-cdcr-nlp.md#contradiction-detection](findings/academic-cdcr-nlp.md#contradiction-detection)
- **Do contradictions in source docs actually hurt?** Yes, degrades RAG output → [successful-patterns.md#rag-research](findings/successful-patterns.md#rag-research)

### Data model
- **Why SQLite over a graph database?** Scale doesn't justify operational overhead → [D001](decisions/D001-sqlite-over-graph.md)
- **How to handle conflicting values?** Wikidata rank system: preferred/normal/deprecated → [wikidata-model.md#steal-these](findings/wikidata-model.md#steal-these), [D003](decisions/D003-rank-system.md)
- **What to steal from Wikidata?** Ranks, temporal qualifiers, entity merging, property constraints → [wikidata-model.md#steal-these](findings/wikidata-model.md#steal-these)
- **What NOT to steal from Wikidata?** SPARQL, Wikibase software, generic constraints → [wikidata-model.md#dont-steal-these](findings/wikidata-model.md#dont-steal-these)
- **How should entities be identified?** Opaque IDs, not human strings. SKOS principle → [library-science.md#skos](findings/library-science.md#skos)
- **How to merge duplicate entities?** Single SQL transaction at our scale → [wikidata-model.md#steal-these](findings/wikidata-model.md#steal-these)

### Architecture
- **Should extraction and entity resolution be one step?** No. Separate them. Raw claims immutable, resolution re-runnable → [D002](decisions/D002-extraction-resolution-separation.md)
- **Should we link facts to code or UI screenshots?** No. Periodic verification instead → [evidence-linking.md](findings/evidence-linking.md), [D004](decisions/D004-no-evidence-links.md)
- **What does the pipeline look like?** Extract → embed → cluster → resolve → detect conflicts → store → verify periodically

### Claim decomposition
- **Can LLMs break facts into entity+property+value?** ~90% precision (FActScore, SAFE) → [academic-cdcr-nlp.md#claim-decomposition](findings/academic-cdcr-nlp.md#claim-decomposition)
- **Is there a schema-free approach?** EDC (EMNLP 2024), but self-canonicalization underperforms → [BIBLIOGRAPHY.md#entity-resolution](BIBLIOGRAPHY.md#entity-resolution-and-coreference)

### Meta / process
- **How much metadata is enough?** Ranganathan's test: can you find the fact without knowing the article? → [library-science.md#ranganathans-test](findings/library-science.md#ranganathans-test)
- **What's the risk of over-engineering the schema?** Cyc spent 40 years adding fields → [failed-systems.md#systems](findings/failed-systems.md#systems) (Cyc entry)
- **How to prevent maintenance abandonment?** Automate. If updates require effort proportional to corpus size, they stop → [library-science.md#failure-modes](findings/library-science.md#failure-modes)

---

## Findings

- [Landscape: failed systems](findings/failed-systems.md) — STATUS: complete — TAGS: prior-work, failure-modes
- [Landscape: successful patterns](findings/successful-patterns.md) — STATUS: complete — TAGS: prior-work, architecture
- [Landscape: off-the-shelf survey](findings/off-the-shelf.md) — STATUS: complete — TAGS: prior-work, build-vs-buy
- [Academic: CDCR and NLP](findings/academic-cdcr-nlp.md) — STATUS: complete — TAGS: academic, entity-resolution, contradiction-detection
- [Analysis: Wikidata model](findings/wikidata-model.md) — STATUS: complete — TAGS: data-model, wikidata
- [Analysis: library science](findings/library-science.md) — STATUS: complete — TAGS: data-model, information-science
- [Analysis: evidence linking](findings/evidence-linking.md) — STATUS: complete — TAGS: architecture, maintenance

## Decisions

- [D001: SQLite over graph databases](decisions/D001-sqlite-over-graph.md) — STATUS: active — TAGS: architecture, storage
- [D002: Separate extraction from resolution](decisions/D002-extraction-resolution-separation.md) — STATUS: active — TAGS: architecture, pipeline
- [D003: Wikidata rank system](decisions/D003-rank-system.md) — STATUS: active — TAGS: data-model, conflict-detection
- [D004: No persistent evidence links](decisions/D004-no-evidence-links.md) — STATUS: active — TAGS: architecture, maintenance
- [D005: Post-hoc entity resolution](decisions/D005-post-hoc-resolution.md) — STATUS: active — TAGS: architecture, entity-resolution

## Negative Results

(None yet — experiments not started)

## Experiments

- H1: Claim decomposition quality — STATUS: not started
- H2: Entity embedding clustering — STATUS: not started
- H3: NLI contradiction detection — STATUS: not started
- H4: Rank system editorial fit — STATUS: not started
- H5: Incremental entity duplication — STATUS: not started

## Open Questions

- How to distinguish contradiction from version-specific difference (no prior work)
- Minimum viable entity granularity for useful conflict detection
- Whether the system needs to understand product versioning
- Optimal frequency for periodic verification sweeps
- Can a single tech writer maintain this alongside regular content work (the real test)

## Bibliography

Full source list with summaries, deep links, and tags: [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md)
