# Analysis: Wikidata Data Model
**Date:** 2026-04-16
**Status:** complete
**Tags:** analysis, data-model, wikidata, design-decisions

## Summary
Wikidata's data model contains several patterns worth adopting for a small-scale fact registry — particularly its rank system and temporal qualifiers — but much of its infrastructure is designed for a scale and generality that would be counterproductive for a focused KB consistency system.

## Findings

### What to Steal

**Rank system (preferred / normal / deprecated)**
Never delete facts; rank them instead. The "best rank" query pattern: return preferred-rank statements if any exist, otherwise return normal-rank statements. Deprecated rank means the data is wrong (not merely outdated — outdated facts should use temporal qualifiers instead). This cleanly handles the case where a product parameter changes: the old value gets deprecated, the new value gets preferred rank.

**Temporal qualifiers (valid_from, valid_until)**
Separate from extraction timestamps. These record when the fact was true in the world, not when the system learned about it. Critical for distinguishing "this contradicts that" from "this superseded that."

**Entity merging**
At the scale of a product KB (hundreds to low thousands of entities), merging duplicate entities is a single-transaction UPDATE operation. No need for the bot infrastructure Wikidata uses.

**Property-level constraints**
Rather than building a generic constraint engine, implement 3-5 specific SQL queries that enforce the constraints that actually matter (e.g., "no entity should have two preferred-rank values for the same property at the same time").

### What NOT to Steal

- **SPARQL** — Overkill for a system with a known, small schema. Standard SQL queries suffice.
- **Wikibase software** — Docker + MediaWiki + MySQL + Elasticsearch for fewer than 1,000 documents is absurd overhead.
- **Generic constraint engine** — Building a general-purpose constraint system invites the Cyc problem. Hardcode the 3-5 constraints that matter.
- **Multilingual support** — Not needed for a single-language product KB.
- **Qualifier nesting** — Qualifiers on qualifiers add complexity without value at this scale.

### Wikidata's Own Failures

- **No negation:** Cannot express "this is NOT true," only "this is deprecated." Limits expressiveness.
- **Soft constraints grow stale:** Constraint violations accumulate faster than they are fixed. Without enforcement, constraints become suggestions.
- **Granularity ceiling:** Designed for breadth (millions of entities, shallow depth) not depth (hundreds of entities, rich detail per entity). Technical documentation needs depth.
- **No built-in temporal reasoning:** Temporal qualifiers exist but SPARQL has no native time-interval logic. Temporal queries require manual filter construction.

## Sources
- Help:Ranking, Help:Statements, Help:Qualifiers — wikidata.org
- Wikibase DataModel Primer — mediawiki.org
- Help:Merge — wikidata.org
- 2020 Property Constraints Report — Wikidata
- Provenance in Collaborative Knowledge Graphs — Springer
- WikiProject: Limits of Wikidata
- Quality of Wikidata — ScienceDirect
- Professional Wiki Wikibase assessment
