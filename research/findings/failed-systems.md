# Landscape: Systems That Failed
**Date:** 2026-04-16
**Status:** complete
**Tags:** landscape, knowledge-bases, failure-patterns, historical

## Summary
Seven major systems attempted automated or semi-automated knowledge base construction and either failed outright or fell far short of their goals. Their failures cluster into seven recurring patterns that any new system must address.

## Findings

### Systems

**Google Knowledge Vault (2014)**
Automated extraction of 1.6 billion triples from the web, but only 17% reached 90% confidence. Google's manually curated Knowledge Graph remained superior for production use. Lesson: expect roughly 17% of automated extractions to be trustworthy without human review.

**IBM Watson / MD Anderson ($62M, 2013-2017)**
Never used on real patients despite years of development. Could not adapt when the underlying schema changed. Required manual curation by domain experts, creating an expertise bottleneck that made the system unmaintainable. Lesson: extraction must be re-runnable and schema-independent.

**Cyc (1984-present, $200M+, 40 years)**
Attempted to encode common-sense knowledge in formal logic. The world does not decompose into clean hierarchies. Edge cases are infinite. Lesson: don't lock in schema early; resist adding fields for edge cases.

**Semantic Web / Linked Data (2001-ongoing)**
Built on the fatal assumption that humans would voluntarily bear the annotation cost. Link rot accumulated as source documents changed. Lesson: LLMs can avoid the annotation bottleneck, but staleness detection is still needed.

**NELL (CMU, 2010-2018)**
Continuous self-feeding extraction from the web. Errors compounded over time through feedback loops. Accumulated 120 million beliefs with steadily degrading accuracy. Lesson: separate extraction from resolution, and make resolution re-runnable.

**Enterprise systems (Palantir, expert.ai, Sinequa)**
Palantir requires embedded engineering teams for every deployment — not automated knowledge construction. Others (expert.ai, Sinequa) enhance search but do not build structured KBs.

**YAGO (success case for contrast)**
Works because its source data (Wikipedia infoboxes) is already partially structured. Demonstrates that structured input dramatically reduces the extraction problem.

### Seven Recurring Failure Patterns

1. **Precision/recall wall** — Automated extraction hits a ceiling where improving one degrades the other.
2. **Error compounding** — Self-feeding systems amplify mistakes over time.
3. **Schema rigidity** — Systems that lock in schema early cannot adapt to evolving domains.
4. **Annotation/maintenance burden** — Systems requiring human annotation at scale cannot sustain throughput.
5. **Source instability** — Links rot, documents change, extracted facts go stale.
6. **Bottleneck of expertise** — When only domain experts can curate, the system cannot scale.
7. **Domain mismatch** — Techniques proven on news/web text fail on technical documentation.

## Sources
- Google Knowledge Vault — Search Engine Land (2014), Wikipedia
- IBM Watson — IEEE Spectrum, Slate, JNCI Oxford Academic, Dolfing case study
- Cyc — Outsider Art retrospective, Yuxi Liu essay
- Semantic Web — Kurt Cagle (LinkedIn), Philippe Fournier-Viger
- NELL — Wikipedia
- DeepDive — Stanford KBC project
- YAGO 4.5 — SIGIR 2024
- Construction of Knowledge Graphs: A Survey — arXiv 2302.11509
