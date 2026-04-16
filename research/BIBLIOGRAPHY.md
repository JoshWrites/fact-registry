# Bibliography

Sources organized by topic. Each entry has a one-line summary, the finding(s) that reference it, and tags for searchability.

---

## Entity Resolution and Coreference

- **EDC: Extract, Define, Canonicalize** (Zhang & Soh, EMNLP 2024) [arXiv 2404.03868](https://arxiv.org/abs/2404.03868) — Three-phase KG construction: open IE, schema induction, post-hoc canonicalization. Self-canonicalization mode works but always underperforms target-aligned. Closest methodology to our pipeline. → [academic-cdcr-nlp.md#claim-normalization](findings/academic-cdcr-nlp.md#claim-normalization) — TAGS: entity-resolution, canonicalization, pipeline

- **iText2KG** (Lairgi et al., WISE 2024) [arXiv 2409.03284](https://arxiv.org/abs/2409.03284) — Incremental KG construction with zero-shot LLMs. Four-module pipeline. Acknowledges entity duplication remains unsolved in incremental mode. → [academic-cdcr-nlp.md#entity-linking](findings/academic-cdcr-nlp.md#entity-linking) — TAGS: entity-resolution, incremental, growing-kb

- **DIAL-KG** (2025) [arXiv 2603.20059](https://arxiv.org/abs/2603.20059) — Schema-free incremental KG with Meta-Knowledge Base governing entity profiles and schema evolution. → [academic-cdcr-nlp.md#entity-linking](findings/academic-cdcr-nlp.md#entity-linking) — TAGS: entity-resolution, schema-evolution, incremental

- **SciCo-Radar** (Forer & Hope, 2024) [arXiv 2409.15113](https://arxiv.org/abs/2409.15113) — Context-dependent definitions for scientific cross-document coreference. Best model: 64.3 F1 on lexically diverse text vs 76.5 on easy splits. Shows performance gap on domain-specific content. → [academic-cdcr-nlp.md#cdcr-benchmarks](findings/academic-cdcr-nlp.md#cdcr-benchmarks) — TAGS: cdcr, domain-specific, performance-gap

- **xCoRe** (Urbani et al., EMNLP 2025) — Three-step CDCR pipeline: mention detection, intra-document clustering, cross-document merging. SOTA on ECB+. → [academic-cdcr-nlp.md#cdcr-benchmarks](findings/academic-cdcr-nlp.md#cdcr-benchmarks) — TAGS: cdcr, sota, pipeline

- **Contrastive Entity Coreference for Historical Texts** (EMNLP 2024) — Handles near-identical entities that refer to different things. Requires 190M+ training pairs with hard negatives. → [academic-cdcr-nlp.md#hard-cases](findings/academic-cdcr-nlp.md#hard-cases) — TAGS: cdcr, hard-cases, near-miss-entities

- **Diverse Word Choices, Same Reference** (2026) [arXiv 2602.17424](https://arxiv.org/abs/2602.17424) — Studies lexical diversity in coreference. Best model drops from 76.5 to 64.3 F1 on diverse subsets. → [academic-cdcr-nlp.md#hard-cases](findings/academic-cdcr-nlp.md#hard-cases) — TAGS: cdcr, lexical-diversity, performance-gap

- **Piecing Together CDCR Datasets** (2026) [arXiv 2603.00621](https://arxiv.org/abs/2603.00621) — Unification effort across CDCR datasets. Confirms models trained on one domain transfer poorly to others. → [academic-cdcr-nlp.md#cdcr-benchmarks](findings/academic-cdcr-nlp.md#cdcr-benchmarks) — TAGS: cdcr, benchmarks, domain-transfer

## Contradiction Detection and Fact Verification

- **VitaminC** (Schuster et al., 2021) [arXiv 2103.08541](https://arxiv.org/abs/2103.08541) — Contrastive evidence pairs for training fact verification models. Training on VitaminC improves adversarial accuracy ~10%. Standard benchmark. → [academic-cdcr-nlp.md#contradiction-detection](findings/academic-cdcr-nlp.md#contradiction-detection) — TAGS: contradiction-detection, benchmark, nli

- **TripleCheck** (biomedical, 2025) — Decomposes claims into atomic triples, verifies each via alignment with retrieved context + cross-checking against KG. Labels: supported/unsupported/contradicted. → [academic-cdcr-nlp.md#contradiction-detection](findings/academic-cdcr-nlp.md#contradiction-detection) — TAGS: contradiction-detection, claim-decomposition, biomedical

- **CLEF CheckThat! 2025** [arXiv 2503.14828](https://arxiv.org/abs/2503.14828) — Includes claim normalization and numerical fact-checking. METEOR ~0.53 for normalization. → [academic-cdcr-nlp.md#claim-normalization](findings/academic-cdcr-nlp.md#claim-normalization) — TAGS: claim-normalization, fact-checking, benchmark

- **(D)RAGged Into a Conflict** (Google Research, 2025) — Contradictory retrieved documents significantly degrade LLM output quality. Validates pre-publication consistency checking. → [successful-patterns.md#rag-research](findings/successful-patterns.md#rag-research) — TAGS: contradiction-detection, rag, downstream-harm

- **RAG Contradiction Detection** (2025) [arXiv 2504.00180](https://arxiv.org/abs/2504.00180) — Even SOTA LLMs struggle with context validation. Performance varies by contradiction type. → [successful-patterns.md#rag-research](findings/successful-patterns.md#rag-research) — TAGS: contradiction-detection, rag, llm-limitations

- **ContraDoc** (NAACL 2024) — Detects self-contradictions within a single document. Does not handle cross-document. → [off-the-shelf.md#research-prototypes](findings/off-the-shelf.md#research-prototypes) — TAGS: contradiction-detection, single-document, limitation

## LLMs for Coreference and Knowledge Construction

- **CRAC 2025 Shared Task** [arXiv 2509.17796](https://arxiv.org/abs/2509.17796) — "Can LLMs Dethrone Traditional Approaches?" Answer: no. LLMs alone cannot outperform specialized CDCR systems. Winning pattern is LLM + specialized component. → [academic-cdcr-nlp.md#llm-cdcr](findings/academic-cdcr-nlp.md#llm-cdcr) — TAGS: llm-limitations, cdcr, hybrid-approach

- **Synergetic Event Understanding** (Min et al., ACL 2024) [arXiv 2406.02148](https://arxiv.org/abs/2406.02148) — LLM summarizes, fine-tuned small model refines. Hybrid outperforms either alone. Pure GPT-4 few-shot lags ~10% behind specialized methods. → [academic-cdcr-nlp.md#llm-cdcr](findings/academic-cdcr-nlp.md#llm-cdcr) — TAGS: hybrid-approach, cdcr, llm-augmented

- **Tree-KG** (ACL 2025) — Expandable KG from textbook structures. F1 of 0.81 on annotated datasets. → [academic-cdcr-nlp.md#claim-normalization](findings/academic-cdcr-nlp.md#claim-normalization) — TAGS: kg-construction, textbooks, structured-source

- **CorefInst** (2025) [arXiv 2509.17505](https://arxiv.org/abs/2509.17505) — Instruction-tuned LLMs for multilingual coreference. → [academic-cdcr-nlp.md#llm-cdcr](findings/academic-cdcr-nlp.md#llm-cdcr) — TAGS: llm-coreference, multilingual

## Claim Decomposition

- **FActScore** — LLM decomposition of text into atomic factual claims. ~90% precision with GPT-4-class models. → [academic-cdcr-nlp.md#claim-decomposition](findings/academic-cdcr-nlp.md#claim-decomposition) — TAGS: claim-decomposition, llm, precision

- **SAFE** (Google) — Similar to FActScore. Validates LLM decomposition approach for fact-checking pipelines. → [academic-cdcr-nlp.md#claim-decomposition](findings/academic-cdcr-nlp.md#claim-decomposition) — TAGS: claim-decomposition, google, fact-checking

## Failed and Abandoned Systems

- **Google Knowledge Vault** (2014) [Search Engine Land](https://searchengineland.com/google-builds-next-gen-knowledge-graph-future-201640) — 1.6B extracted triples, only 17% at 90% confidence. Never deployed. Manual KG remained superior. → [failed-systems.md#systems](findings/failed-systems.md#systems) — TAGS: failed-system, precision-wall, web-scale

- **IBM Watson / MD Anderson** ($62M) [IEEE Spectrum](https://spectrum.ieee.org/how-ibm-watson-overpromised-and-underdelivered-on-ai-health-care), [Slate](https://slate.com/technology/2022/01/ibm-watson-health-failure-artificial-intelligence.html), [JNCI](https://academic.oup.com/jnci/article/109/5/djx113/3847623), [Dolfing Case Study](https://www.henricodolfing.com/2024/12/case-study-ibm-watson-for-oncology-failure.html) — $62M, never used on real patients. Bottleneck of expertise, schema fragility. → [failed-systems.md#systems](findings/failed-systems.md#systems) — TAGS: failed-system, expertise-bottleneck, medical

- **Cyc** (1984-present) [Outsider Art](https://outsiderart.substack.com/p/cyc-historys-forgotten-ai-project), [Yuxi Liu](https://yuxi-liu-wired.github.io/essays/posts/cyc/) — 40 years, $200M+, 30M rules. Ontology doesn't scale. Cautionary tale. → [failed-systems.md#systems](findings/failed-systems.md#systems) — TAGS: failed-system, ontology-overreach, formal-logic

- **Semantic Web** [Kurt Cagle](https://www.linkedin.com/pulse/why-semantic-web-has-failed-kurt-cagle), [Fournier-Viger](https://data-mining.philippe-fournier-viger.com/the-semantic-web-and-why-it-failed/) — Annotation burden exceeded value. Link rot. → [failed-systems.md#systems](findings/failed-systems.md#systems) — TAGS: failed-system, annotation-burden, link-rot

- **NELL** (CMU) [Wikipedia](https://en.wikipedia.org/wiki/Never-Ending_Language_Learning) — Error compounding over time in self-feeding extraction loop. → [failed-systems.md#systems](findings/failed-systems.md#systems) — TAGS: failed-system, error-compounding, self-feeding

- **Construction of Knowledge Graphs: A Survey** [arXiv 2302.11509](https://arxiv.org/abs/2302.11509) — Comprehensive survey of KG construction approaches and their limitations. → [failed-systems.md#seven-recurring-failure-patterns](findings/failed-systems.md#seven-recurring-failure-patterns) — TAGS: survey, failure-patterns, kg-construction

## Successful Small-Scale Patterns

- **FDA Structured Product Labeling (SPL)** [FDA SPL Resources](https://www.fda.gov/industry/fda-data-standards-advisory-board/structured-product-labeling-resources) — Schema-enforced extraction with validation at authoring time. Consistency enforced by regulator. → [successful-patterns.md#converged-pattern](findings/successful-patterns.md#converged-pattern) — TAGS: success, pharma, schema-enforcement

- **S1000D BREX** [s1000d.org](https://s1000d.org/) — Machine-readable business rules validated automatically against every data module. → [successful-patterns.md#converged-pattern](findings/successful-patterns.md#converged-pattern) — TAGS: success, aviation, automated-validation

- **IrisCheck** [irissoftwaresuite.com](https://www.irissoftwaresuite.com/irischeck.html) — Validates S1000D data modules against BREX rules. → [successful-patterns.md#converged-pattern](findings/successful-patterns.md#converged-pattern) — TAGS: success, aviation, validation-tool

- **Karpathy LLM Wiki Pattern** (April 2026) [GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — Raw sources → LLM-compiled wiki → contradiction detection at ingest. 5K+ stars in days. → [successful-patterns.md#converged-pattern](findings/successful-patterns.md#converged-pattern) — TAGS: success, llm-era, wiki-pattern, architecture

- **Synthadoc** [GitHub](https://github.com/axoviq-ai/synthadoc) — Ingest-time contradiction detection. Flags contradictions with `status: contradicted`, preserves both claims with citations. → [successful-patterns.md#converged-pattern](findings/successful-patterns.md#converged-pattern) — TAGS: success, llm-era, contradiction-detection, human-review

- **KnowledgeBase Guardian** (Dataroots) [GitHub](https://github.com/datarootsio/knowledgebase_guardian) — Embed corpus, retrieve similar on ingest, LLM checks for contradictions. Gatekeeper pattern only. → [off-the-shelf.md#llm-open-source](findings/off-the-shelf.md#llm-open-source) — TAGS: tool, gatekeeper-pattern, no-entity-identity

- **Kira Systems / Luminance** — Legal contract analysis. Kira: 90%+ extraction with pre-trained clause types. Luminance: anomaly/deviation detection rather than schema extraction. → [successful-patterns.md#legal](findings/successful-patterns.md#legal) — TAGS: success, legal, extraction, anomaly-detection

## Data Models and Information Science

- **Wikidata Help:Ranking** [wikidata.org](https://www.wikidata.org/wiki/Help:Ranking) — Preferred/normal/deprecated rank system. Never delete, just re-rank. Two preferred values = conflict. → [wikidata-model.md#steal-these](findings/wikidata-model.md#steal-these) — TAGS: data-model, wikidata, rank-system, conflict-detection

- **Wikidata Help:Statements** [wikidata.org](https://www.wikidata.org/wiki/Help:Statements) — (entity, property, value) triple with qualifiers and references. Core data unit. → [wikidata-model.md#steal-these](findings/wikidata-model.md#steal-these) — TAGS: data-model, wikidata, claim-structure

- **Wikidata Help:Qualifiers** [wikidata.org](https://www.wikidata.org/wiki/Help:Qualifiers) — Temporal scoping (valid_from/valid_until), context metadata on claims. → [wikidata-model.md#steal-these](findings/wikidata-model.md#steal-these) — TAGS: data-model, wikidata, temporal, provenance

- **Wikidata Help:Merge** [wikidata.org](https://www.wikidata.org/wiki/Help:Merge/en) — Entity merging: move statements to survivor, redirect defunct item. At small scale, single SQL transaction. → [wikidata-model.md#steal-these](findings/wikidata-model.md#steal-these) — TAGS: data-model, entity-merging, operational

- **Wikidata 2020 Property Constraints Report** [wikidata.org](https://www.wikidata.org/wiki/Wikidata:2020_report_on_Property_constraints) — 15 constraints with 100+ exceptions each. False positive rate significant. Constraints are hints, not enforcement. → [wikidata-model.md#dont-steal-these](findings/wikidata-model.md#dont-steal-these) — TAGS: data-model, wikidata, constraints, false-positives

- **WikiProject: Limits of Wikidata** [wikidata.org](https://www.wikidata.org/wiki/Wikidata:WikiProject_Limits_of_Wikidata) — No negation support, granularity ceiling, no temporal reasoning. → [wikidata-model.md#wikidata-failures](findings/wikidata-model.md#wikidata-failures) — TAGS: data-model, wikidata, limitations

- **Quality of Wikidata** [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1570826821000536) — 68% of statements have references. Of those, 61% relevant and authoritative. Overall quality score 0.58/1.0. → [wikidata-model.md#steal-these](findings/wikidata-model.md#steal-these) — TAGS: data-model, wikidata, provenance, quality

- **Provenance in Collaborative Knowledge Graphs** [Springer](https://link.springer.com/chapter/10.1007/978-3-319-68288-4_32) — Provenance tracking patterns for collaborative KGs. → [wikidata-model.md#steal-these](findings/wikidata-model.md#steal-these) — TAGS: data-model, provenance

- **Wikibase DataModel Primer** [mediawiki.org](https://www.mediawiki.org/wiki/Wikibase/DataModel/Primer) — Technical reference for Wikibase internals. → [wikidata-model.md](findings/wikidata-model.md) — TAGS: data-model, wikibase, reference

- **Professional Wiki: Wikibase Strengths and Weaknesses** [professional.wiki](https://professional.wiki/en/articles/wikibase-strengths-and-weaknesses) — Wikibase requires Docker+MediaWiki+MySQL+ES. Impractical for <10K items. → [wikidata-model.md#dont-steal-these](findings/wikidata-model.md#dont-steal-these) — TAGS: data-model, wikibase, operational-overhead

## Library Science

- **FRBR** (Functional Requirements for Bibliographic Records) — Work→Expression→Manifestation→Item hierarchy. Applicable as structural skeleton for fact→phrasing→passage. Limitation: assumes expressions are equivalent, ours may contradict. → [library-science.md#frbr](findings/library-science.md#frbr) — TAGS: information-science, hierarchy, cataloging

- **SKOS** (Simple Knowledge Organization System) — Concept vs label distinction. Concept is stable, labels can change. Use opaque IDs, not human-readable strings. → [library-science.md#skos](findings/library-science.md#skos) — TAGS: information-science, concept-identity, naming

- **PROV-O** (Provenance Ontology) — Entity, Activity, Agent model for provenance. Warning: recording provenance is easy; building queries that use it is hard. → [library-science.md#provenance](findings/library-science.md#provenance) — TAGS: information-science, provenance

- **LCSH / VIAF** — Authority control: canonical names + variant forms. Maintenance is expensive but deduplication without it is worse. → [library-science.md#authority-control](findings/library-science.md#authority-control) — TAGS: information-science, authority-control, entity-identity

- **Ranganathan's Laws of Library Science** — "Every reader his book, every book its reader." Applied: can someone find the fact without knowing which article has it? If yes, enough metadata. → [library-science.md#ranganathans-test](findings/library-science.md#ranganathans-test) — TAGS: information-science, sufficiency-test, usability

## Evidence Linking and Documentation Maintenance

- **Swimm Auto-Sync** [swimm.io](https://swimm.io/blog/how-does-swimm-s-auto-sync-feature-work) — Tracks code changes and flags stale docs. Works when doc author = code author. Breaks on major restructures. → [evidence-linking.md#code-links](findings/evidence-linking.md#code-links) — TAGS: evidence-linking, code-docs, auto-sync

- **Mintlify Docs on Autopilot** [mintlify.com](https://www.mintlify.com/blog/docs-on-autopilot) — Monitors PRs, drafts doc updates. Assumes developer-facing API docs. → [evidence-linking.md#code-links](findings/evidence-linking.md#code-links) — TAGS: evidence-linking, code-docs, automation

- **"Documentation Without Maintenance Burden"** [event-driven.io](https://event-driven.io/en/how_to_successfully_do_documentation_without_maintenance_burden/) — Principles for reducing doc maintenance. → [evidence-linking.md#scale-argument](findings/evidence-linking.md#the-scale-argument) — TAGS: evidence-linking, maintenance, principles

- **Quantstruct** (YC W25) [ycombinator.com](https://www.ycombinator.com/companies/quantstruct) — Monitors PRs and product changes for doc staleness. Focused on "when to update," not contradiction detection. → [off-the-shelf.md#ai-doc-tools](findings/off-the-shelf.md#ai-doc-tools) — TAGS: tool, staleness-detection, no-contradiction

## Methodology and Process

- **Architecture Decision Records** [adr.github.io](https://adr.github.io/) — Structured format for documenting architecture decisions with context, options, and consequences. → project methodology — TAGS: methodology, documentation

- **Karpathy LLM Wiki v2** [GitHub Gist](https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaf681e2) — Extensions and lessons from the LLM Wiki pattern. → project methodology — TAGS: methodology, llm-workflow

- **Context Engineering for Multi-Agent LLM Assistants** [arXiv 2508.08322](https://arxiv.org/abs/2508.08322) — Research on structuring context for multi-session LLM work. → project methodology — TAGS: methodology, context-management, multi-session

- **ICML 2026 LLM Attribution Policy** [icml.cc](https://icml.cc/Conferences/2026/CallForPapers) — LLMs cannot be listed as authors. Acknowledge in methods/tools section. → METHODOLOGY.md — TAGS: methodology, attribution, publication
