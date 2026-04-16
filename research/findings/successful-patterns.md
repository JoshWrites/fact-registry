# Landscape: Patterns That Succeeded
**Date:** 2026-04-16
**Status:** complete
**Tags:** landscape, architecture, convergent-design, validation

## Summary
Four independent domains — pharmaceutical regulation, aviation maintenance, and two LLM-era open-source projects — converged on the same architectural pattern for maintaining factual consistency across documents. Their convergence suggests this pattern is structurally necessary, not accidental.

## Findings

### Converging Domains

**Pharma (FDA SPL)**
Structured Product Labeling enforces schema-validated extraction and validation at authoring time. Every drug label must conform to machine-readable structure before publication. Consistency is enforced by the format itself.

**Aviation (S1000D BREX)**
Business Rules Exchange files define machine-readable validation rules for technical publications. Automated checks run against every document before release. Errors are caught at authoring time, not discovered downstream.

**LLM-era: Karpathy LLM Wiki (April 2026, 5K+ GitHub stars)**
Extract structured facts at ingest, compile into canonical form, detect contradictions across sources. Designed for LLM-friendly knowledge compilation.

**LLM-era: Synthadoc**
Ingest-time contradiction detection with a human review queue. Documents are checked for consistency as they enter the system, with conflicts flagged rather than auto-resolved.

### The Converged Pattern

All four systems implement the same four-step architecture:

1. **Extract** structured facts at ingest time
2. **Normalize** to canonical form
3. **Compare** pairwise for contradictions
4. **Flag** for human review — do not auto-resolve ambiguity

### Adjacent Successes

**Legal domain:** Kira Systems achieves 90%+ accuracy with pre-trained clause types. Luminance uses anomaly detection to surface unusual contract terms. Both demonstrate that domain-specific pre-training dramatically improves extraction quality.

**Google RAG research (2025-2026):** Confirms that contradictory source documents degrade LLM output quality. Pre-publication consistency checking prevents downstream harm in retrieval-augmented generation pipelines.

## Sources
- FDA Structured Product Labeling (SPL) resources
- S1000D BREX specification
- IrisCheck
- Karpathy LLM Wiki — GitHub Gist (April 2026)
- Synthadoc — GitHub
- KnowledgeBase Guardian — GitHub (dataroots)
- Kira Systems, Luminance
- (D)RAGged Into a Conflict — Google Research (2025)
- RAG contradiction detection — arXiv 2504.00180
