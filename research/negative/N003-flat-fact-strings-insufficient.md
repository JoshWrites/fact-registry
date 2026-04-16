# N003: Flat Fact Strings Are Insufficient for Conflict Detection
**Date:** 2026-04-16
**Status:** rejected
**Tags:** data-model, fact-extraction, false-start

## Hypothesis
Storing extracted facts as free-text strings grouped by label (the `content_facts` table: 11,535 rows across 730 articles) would be sufficient for detecting contradictions across articles.

## What Happened
The flat strings capture *what articles say* but not *what they say it about*. Two strings — "the link to the report is active for 10 minutes" and "click the hyperlink within the next day to view the report" — share no keywords but are claims about the same entity (report download link) with conflicting values (10 min vs 1 day). No string comparison, embedding similarity, or label grouping can reliably detect this without decomposing each fact into entity + property + value.

## Why It Failed
The fact string is a sentence. The unit of comparison for conflict detection is a claim: a specific entity has a specific property with a specific value. Without decomposition, the system has no way to know two differently-worded sentences are about the same thing.

## What We Learned
The flat store remains useful as raw material — it preserves what the LLM actually extracted from each article and can be re-processed. But the conflict detection pipeline requires a structured claim layer on top: entity resolution to match entities across articles, property normalization to align attributes, and value extraction to compare.

## Impact on Design
This finding motivates the entire entity-centric claim architecture. The `content_facts` table stays as a source artifact. The claims schema (entities, claims, claim_entity_links) is the layer that enables conflict detection.
