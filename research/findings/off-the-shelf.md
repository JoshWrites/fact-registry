# Landscape: Off-the-Shelf Solutions
**Date:** 2026-04-16
**Status:** complete
**Tags:** landscape, tools, market-survey, gap-analysis

## Summary
An exhaustive search across KB platforms, writing QA tools, AI documentation tools, knowledge graph infrastructure, LLM open-source projects, CCMS systems, and research prototypes confirms that no existing product solves end-to-end cross-document factual consistency for a help center knowledge base. The entity identity problem — recognizing that differently-worded passages are about the same thing — is solved by none of them.

## Findings

### KB Platforms (Confluence, Notion, Document360, Guru)
None offer cross-article factual consistency checking. Guru has verification timers (reminders to review articles on a schedule) but performs no semantic comparison between documents.

### Writing QA Tools (Acrolinx, Vale)
Check terminology consistency and style guide adherence. Do not check factual consistency. Cannot detect when two articles make contradictory claims.

### AI Documentation Tools (Swimm, Quantstruct YC W25)
Detect staleness when documentation is coupled to code changes. Swimm tracks code-doc links and flags when referenced code changes. Quantstruct (YC W25) does similar. Neither detects cross-document contradictions or factual drift between articles that are not code-coupled.

### Knowledge Graph Tools (Stardog, Ontotext)
Provide infrastructure (triple stores, SPARQL endpoints, ontology management) but are not solutions. Require building the entire extraction, normalization, and contradiction detection pipeline on top.

### LLM Open-Source Projects
- **KnowledgeBase Guardian (dataroots):** Implements a gatekeeper pattern — checks new content against existing KB before publication. Does not extract structured claims; operates at document level.
- **ody-refine:** Very early stage, single developer. Concept-level only.
- **Synthadoc:** Closest to what is needed. Builds a new synthesized wiki from source documents with contradiction detection. However, it creates a parallel artifact rather than auditing an existing KB.

### CCMS Systems (Paligo, MadCap Flare, DITA)
Prevent inconsistency through single-sourcing at authoring time: one source of truth, reused across outputs. Cannot detect drift in content that was not single-sourced from the start. Retrofitting an existing KB into a CCMS is a rewrite, not an audit.

### Research Prototypes
- **ContraDoc (NAACL 2024):** Contradiction detection within a single document only. Does not handle cross-document scenarios.
- **ClaimBuster:** Designed for political fact-checking claims. Domain mismatch for technical documentation.
- **Facticity.AI:** Targets public misinformation detection. Not designed for internal KB consistency.

### The Unsolved Problem
The entity identity problem — determining that "the quarantine timeout" in Article A and "messages are held for 48 hours" in Article B refer to the same configurable parameter — is addressed by none of these tools. This is the core prerequisite for cross-document consistency checking.

## Sources
- Product pages for Confluence, Notion, Document360, Guru, Acrolinx, Vale, Swimm, Stardog, Ontotext, Paligo, MadCap Flare
- Quantstruct — YC W25 page
- KnowledgeBase Guardian — GitHub (dataroots)
- ody-refine — GitHub
- Synthadoc — GitHub
- ContraDoc — NAACL 2024
- ClaimBuster, Facticity.AI — project pages
