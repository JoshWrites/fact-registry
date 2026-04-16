# N004: No System Distinguishes Contradiction from Version Difference
**Date:** 2026-04-16
**Status:** open-problem
**Tags:** contradiction-detection, versioning, open-problem

## The Problem
When two articles state different values for the same entity and property, it could mean:
- **Contradiction:** One is wrong. The timeout was always 10 minutes; the article saying 24 hours is incorrect.
- **Version difference:** The timeout was 10 minutes in v3 and changed to 24 hours in v4. Both articles are correct for their version.

## What We Found
No existing system — academic or commercial — distinguishes these cases. CDCR research assumes statements are about the same point in time. NLI models classify entailment/contradiction/neutral but have no concept of temporal validity. Wikidata handles this with temporal qualifiers (valid_from/valid_until) but the assignment of those qualifiers is manual.

## Why It Matters
If the system flags every version-specific difference as a contradiction, it produces overwhelming false positives. If it ignores version differences, it misses real contradictions. The user's product has biweekly releases — version-specific changes are common.

## Current Status
Unsolved. This is a genuine open problem. Potential approaches to test:
- Use article `edited_at` timestamps as a proxy for version context
- Look for version indicators in the article text (release notes, version numbers)
- Ask the LLM to distinguish during conflict detection ("is this a contradiction or a version change?")

None of these have been tested. This is listed as an open question in the research INDEX.
