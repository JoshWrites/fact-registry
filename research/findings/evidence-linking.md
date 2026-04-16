# Analysis: Evidence Linking to Code/UI
**Date:** 2026-04-16
**Status:** complete
**Tags:** analysis, evidence-linking, code-docs, verification, maintenance

## Summary
Persistent links between documentation facts and their evidence in code or UI are not worth building for a small team. The maintenance cost of keeping links alive through refactors, redesigns, and releases exceeds their value. Periodic stateless verification — asking "is this still true?" against the live product — achieves the same goal at far lower cost.

## Findings

### Code Links: Why They Break

Linking a documented fact to a specific file and symbol (e.g., "the default timeout is set in `config/defaults.py:QUARANTINE_TIMEOUT`") requires tracking file paths and symbol names across every refactor. Every rename, move, or restructuring is a staleness event. Swimm's auto-sync approach works when the documentation author is also the code author and updates both in the same PR. For a KB maintained separately from the codebase, this coupling creates more maintenance burden than it solves.

### UI Links: Why They Break

Linking a documented fact to a UI screenshot or element requires:
1. Capturing screenshots on every build
2. Running visual diff to detect changes
3. Interpreting whether the change affects the documented claim

The change detection layer (steps 1-2) is solvable with existing tools. The interpretation layer (step 3) requires an LLM or human to determine whether a visual change invalidates the documentation. This is equivalent in cost to just re-verifying the claim directly.

### The Scale Argument

For a single maintainer or small team, persistent link maintenance does not pay for itself. The overhead of maintaining the linking infrastructure — updating broken links, resolving ambiguous matches, handling false positives from refactors — exceeds the time saved by knowing exactly where evidence lives.

### Recommended Alternative: Periodic Stateless Verification

Instead of maintaining persistent links, run periodic verification passes where an LLM is given a documented claim and asked: "Is this claim still true in the current version of the product?" This approach is:
- **Stateless:** No link infrastructure to maintain.
- **Resilient to refactors:** Does not care where in the code the behavior is implemented.
- **Resilient to UI changes:** Does not depend on screenshot pipelines.
- **Re-runnable:** Can be run at any frequency without accumulated state.

### Exception: High-Churn Parametric Claims

Claims about specific numeric parameters that change frequently (timeouts, rate limits, storage quotas, version numbers) warrant a `last_verified` timestamp and a higher verification frequency than narrative claims. These are the most likely to go stale and the easiest to verify programmatically.

## Sources
- Swimm auto-sync documentation
- Mintlify Docs on Autopilot
- "Documentation Without Maintenance Burden" — event-driven.io
- "CI/CD for LLM Documentation Errors" — Medium
