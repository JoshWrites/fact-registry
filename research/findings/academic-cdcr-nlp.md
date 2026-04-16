# Academic: Cross-Document Coreference and NLP
**Date:** 2026-04-16
**Status:** complete
**Tags:** academic, cdcr, nli, entity-linking, embeddings, claim-decomposition

## Summary
The academic state of the art in cross-document coreference resolution (CDCR), natural language inference (NLI), claim decomposition, and entity linking provides strong building blocks but no complete solution. Best CDCR models achieve 91.9 F1 on news benchmarks but drop to 64.3 on lexically diverse text. No benchmark exists for technical documentation. The winning pattern emerging from recent work combines LLMs with specialized NLP components rather than using either alone.

## Findings

### Cross-Document Coreference Resolution (CDCR)
Best models achieve 91.9 F1 on the ECB+ news benchmark but drop to 64.3 F1 on lexically diverse text. No benchmark exists for technical documentation, where the same concept is routinely described with different terminology across articles. LLMs alone cannot do CDCR effectively (CRAC 2025 shared task results). The winning pattern pairs an LLM with a specialized coreference component.

### Natural Language Inference (NLI)
DeBERTa-v3-large-mnli achieves 91.1% on MultiNLI. Catches explicit contradictions reliably but misses an estimated 30-40% of implicit contradictions (where the conflict requires domain knowledge or inference). Practical approach: use NLI as a fast filter to catch obvious contradictions, then use an LLM as judge for the remainder.

### Claim Decomposition
FActScore and SAFE demonstrate roughly 90% precision for LLM-based decomposition of text into atomic claims. EDC (EMNLP 2024) is the closest published methodology to what a fact registry needs: extract claims, define their scope, canonicalize them — all with no predefined schema.

### Growing-KB Entity Linking
An underexplored problem. Most entity linking research assumes a fixed target KB (e.g., Wikipedia). iText2KG (WISE 2024) and DIAL-KG (2024-2025) address the growing-KB scenario where new entities appear over time, but both report entity duplication as an unsolved problem.

### Embeddings for Technical Text
E5 and BGE embedding models outperform OpenAI ada-002 for short technical phrases. For clustering extracted claims into canonical groups, HDBSCAN handles 60-70% of cases automatically. The remaining 30-40% (ambiguous or novel entities) requires LLM-assisted resolution.

### Open Problems
- **Contradiction vs. version difference:** Is "timeout is 24 hours" vs. "timeout is 48 hours" a contradiction, or did the product change? Temporal context is required.
- **Temporal entity evolution:** The same parameter may have had different correct values at different times.
- **Growing-KB cold start:** With no existing KB, early entity resolution has no context to leverage.
- **No technical doc benchmark:** All CDCR benchmarks use news or Wikipedia text.
- **Self-canonicalization quality:** LLMs asked to canonicalize their own extractions can hallucinate canonical forms.

## Sources
- xCoRe — EMNLP 2025
- SciCo-Radar — arXiv 2409.15113
- Synergetic Event Understanding — ACL 2024
- CRAC 2025 Shared Task — arXiv 2509.17796
- EDC (Extract, Define, Canonicalize) — EMNLP 2024, arXiv 2404.03868
- iText2KG — WISE 2024, arXiv 2409.03284
- Tree-KG — ACL 2025
- DIAL-KG — arXiv 2603.20059
- VitaminC — arXiv 2103.08541
- TripleCheck — 2025
- CLEF CheckThat! 2025 — arXiv 2503.14828
- Diverse Word Choices and Cross-Document Coreference — arXiv 2602.17424
- Contrastive Entity Coreference — EMNLP 2024
- Piecing Together CDCR Datasets — arXiv 2603.00621
