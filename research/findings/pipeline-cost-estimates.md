# Early Pipeline Cost Estimates
**Date:** 2026-04-16
**Status:** preliminary
**Tags:** pipeline, costs, estimates, early-research

## Summary
Initial rough cost estimates for a one-time full-corpus processing pass through the proposed pipeline. These are back-of-envelope numbers from early research, NOT final architecture decisions. The pipeline described here is one candidate approach under evaluation.

## The Pipeline Being Costed
This estimate covers a specific candidate pipeline (see research/INDEX.md for current status of each component):

1. **Claim decomposition** — Claude API decomposes ~11K existing fact strings into (entity, property, value) triples
2. **Entity clustering** — Local embedding models (E5/BGE) + HDBSCAN cluster entity mentions
3. **Entity resolution** — Claude API names clusters, confirms/splits/merges
4. **Conflict detection** — DeBERTa-v3-large (local, via sentence-transformers) as NLI filter, Claude API confirms flagged contradictions

## One-Time Full-Corpus Estimates
- Decomposition: ~$5-10 (Claude API, batched)
- Entity resolution: ~$3-5 (Claude API)
- Conflict detection confirmation: ~$2-3 (Claude API for hard cases only)
- Total one-time: **under $20**

## What This Estimate Misses
**This is a one-time cost for the initial corpus.** It does not account for:

- **Ongoing per-article cost:** Every new article and every edited article triggers extraction and resolution. The *marginal cost per article* is the number that matters for sustainability, and we have not estimated it.
- **Periodic full reconciliation:** Entity deduplication may require periodic full-corpus passes. Unknown frequency and cost.
- **Verification sweeps:** Periodic "is this claim still true?" checks against the live product. Unknown scope and cost.
- **Re-resolution after entity merges/splits:** When the entity registry changes, downstream claims may need re-evaluation.
- **Model cost changes:** API pricing changes over time. Local model requirements (GPU/CPU) have infrastructure costs.

## Technical Notes
- DeBERTa-v3-large-mnli runs locally via Hugging Face sentence-transformers, NOT via Ollama (it's an encoder model, not generative)
- Embedding (E5/BGE) runs locally, milliseconds per item, effectively free
- HDBSCAN clustering is CPU-only, effectively free at this scale
- The 17% trust threshold (from Google Knowledge Vault research) suggests ~83% of extractions will need some form of review — the human review cost is not included in these estimates

## Status
These are early research estimates. The pipeline itself is a hypothesis under evaluation (see experiments H1-H5). Do not treat these as budgeted costs.
