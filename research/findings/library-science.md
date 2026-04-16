# Analysis: Library Science Principles
**Date:** 2026-04-16
**Status:** complete
**Tags:** analysis, library-science, frbr, skos, provenance, authority-control

## Summary
Library science offers mature frameworks for the problems a fact registry must solve — distinguishing concepts from their expressions, managing authority records, tracking provenance, and evaluating whether metadata is sufficient. The key principles translate directly, though each comes with documented failure modes that must be designed around.

## Findings

### FRBR (Functional Requirements for Bibliographic Records)

The FRBR hierarchy maps cleanly onto fact registry concepts:
- **Work** = the canonical fact (e.g., "quarantine timeout duration")
- **Expression** = a specific article's phrasing of that fact
- **Manifestation** = the specific passage where it appears

However, FRBR assumes that different Expressions of the same Work are equivalent. In a fact registry, expressions may contradict each other — that is the core problem being solved. The FRBR model must be extended with rank (which expression is authoritative) and temporal validity (when each expression was true).

### Authority Control

The core pattern: one canonical name plus a flat list of known variants. When a user searches for any variant, they find the canonical record. Key design principles:
- Make splitting and merging authority records cheap. They will need to change.
- Authority records degrade without maintenance. Plan for periodic review.
- Use opaque IDs, not human-readable strings, as primary identifiers (following the SKOS principle). Human-readable labels can change; IDs must not.

### KOS / SKOS (Knowledge Organization Systems)

The concept-vs-label distinction is fundamental. A concept is a stable unit of meaning. Labels (preferred, alternative, hidden) are the strings humans use to refer to it. Concepts persist; labels can be added, changed, or removed without disrupting the system. This maps directly to entity identity in a fact registry: the entity is the concept, and the various phrasings across articles are its labels.

### Provenance (PROV-O)

The PROV-O model defines three core types: Entity (the thing), Activity (what produced it), Agent (who/what performed the activity). For a fact registry, this tracks which LLM extraction produced which fact from which article.

Warning from the literature: recording provenance is easy; using it is hard. Provenance data is worthless unless queries and UI are built to consume it. Every provenance field must have a specific query or display that uses it, or it becomes dead weight.

### Ranganathan's Test

Ranganathan's Laws of Library Science provide a practical sufficiency test: "Can someone find the fact without knowing which article contains it?" If yes, the metadata is sufficient. Every field beyond that threshold is cost without retrieval benefit. Apply this test before adding any new field to the schema.

### Documented Failure Modes

- **Ontology overreach:** Adding ever-more-specific categories until the classification system is harder to maintain than the content it organizes.
- **Duplicate proliferation:** Without regular deduplication, authority records accumulate near-duplicates that fragment search results.
- **Maintenance abandonment:** Metadata systems that are not integrated into daily workflows get abandoned. The system must be useful to its maintainer, not just to downstream consumers.

## Sources
- FRBR (Functional Requirements for Bibliographic Records)
- RDA (Resource Description and Access)
- SKOS (Simple Knowledge Organization System)
- PROV-O (Provenance Ontology)
- LCSH (Library of Congress Subject Headings)
- VIAF (Virtual International Authority File)
- Ranganathan's Five Laws of Library Science
