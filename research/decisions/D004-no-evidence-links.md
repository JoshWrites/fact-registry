# D004: No Persistent Code/UI Evidence Links
**Date:** 2026-04-16
**Status:** active
**Tags:** verification, evidence, maintenance

## Context
Should factual claims in the registry be linked to specific code locations or UI screenshots as persistent evidence? The idea is appealing: a claim like "the timeout is 30 seconds" could point directly to the line of code that sets it, providing machine-verifiable proof. But the maintenance cost of such links must be weighed against the value they provide.

## Options Considered
**(A) Persistent code links** (file path + symbol reference) -- Direct proof that a claim matches the implementation. But every refactor, rename, or file move is a staleness event. This approach only works well when the documentation author is the code author and actively maintains both. For a KB maintained separately from the codebase, these links rot quickly.

**(B) Persistent UI screenshot links** -- Capture screenshots of the product UI as evidence for behavioral claims. Requires a screenshot pipeline, visual diffing infrastructure, and an LLM interpretation layer to determine whether a UI change invalidates a claim. The change detection layer still requires interpretation -- a button moving 10px is not a claim invalidation, but a field disappearing is.

**(C) Periodic stateless verification** -- No persistent links stored in the schema. Instead, periodically ask "is this claim still true?" against the live product, documentation, or other sources. No link maintenance. High-churn parametric claims (timeouts, rate limits, thresholds) get a `last_verified` timestamp and higher verification frequency.

## Decision
Periodic verification, not persistent links. For a single person maintaining the system, the ongoing cost of maintaining code references and screenshot pipelines exceeds the value they provide. The verification approach is stateless: each verification pass starts fresh rather than trying to track what changed since last time.

Exception: high-churn parametric claims (timeouts, rate limits, version numbers) get a `last_verified` timestamp and are prioritized for more frequent verification.

## Consequences
- No `code_ref` or `screenshot_ref` fields in the claims schema.
- Add `last_verified` and `verification_status` fields to claims.
- Need to build a verification runner as a future tool (scheduled job that re-checks claims against current sources).
- Claims lack machine-verifiable proof of correctness -- verification is periodic, not continuous.
- Dramatically simpler schema and no link-rot maintenance burden.

## References
- Swimm auto-sync limitations analysis (code link maintenance in practice)
- Mintlify Workflows analysis (documentation-code sync tooling)
- Evidence linking research (cost-benefit at different scales)
