# D003: Wikidata Rank System for Conflict Management
**Date:** 2026-04-16
**Status:** active
**Tags:** conflict-detection, data-model, claims

## Context
When two articles state different values for the same entity+property pair, the system needs a strategy for handling the contradiction. This is inevitable in a KB with hundreds of articles maintained over time -- values change, articles go stale, and sometimes two articles simply disagree.

## Options Considered
**(A) Overwrite** -- When a new value is found, replace the old one. Simple to implement. But this loses history entirely. There is no way to detect when articles contradict because the old value is gone. If the new value turns out to be wrong, the correct old value has been destroyed.

**(B) Keep all with timestamps** -- Preserve every value ever extracted, tagged with when it was found. This retains history but provides no mechanism to mark which value is the current truth. Consumers must guess based on recency, which is unreliable (a newer article is not always more correct).

**(C) Wikidata rank system** -- Three ranks: preferred (current truth), normal (historical or contextual), deprecated (known wrong). Claims are never deleted, only re-ranked. The "best-rank" query returns preferred claims if any exist, otherwise normal. Deprecated claims are never returned unless explicitly requested. Two preferred claims with different values on the same entity+property = a detected conflict.

## Decision
Adopt the Wikidata rank system. Three ranks: preferred, normal, deprecated. The best-rank query pattern provides a clean interface for consumers while preserving full history. Conflict detection becomes a simple GROUP BY query: find entity+property pairs with more than one preferred claim carrying different values.

## Consequences
- Claims are never deleted, only re-ranked. The database is append-and-update, never append-and-delete.
- Conflict detection is a SQL GROUP BY query, not a complex reconciliation algorithm.
- Must define clear criteria for when to set preferred vs normal vs deprecated (e.g., newer article = preferred, older article = normal, retracted claim = deprecated).
- Entity merging requires updating ranks across all claims belonging to the merged entities.
- The rank field adds a small amount of complexity to every query, but the best-rank pattern is a standard SQL idiom.

## References
- Wikidata Help:Ranking documentation
- Wikidata data model deep dive research
