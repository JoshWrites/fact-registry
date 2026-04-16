# N001: Labels Do Not Scope Entity Identity
**Date:** 2026-04-16
**Status:** rejected
**Tags:** entity-resolution, labels, false-start

## Hypothesis
Labels assigned to articles (e.g., `poc-report`, `sso`) would narrow the entity identity problem enough to make it tractable. Two facts extracted under the same label would be about the same domain, making entity matching a within-label comparison rather than an all-against-all problem.

## What Happened
The hypothesis broke on a concrete counterexample: an article labeled `poc-report` contains six different hyperlinks, each with its own expiry window. The label tells us the article is *about* POC reports, but it cannot distinguish which of the six expiry facts corresponds to which entity. Two articles both labeled `poc-report` might each mention "the link" — but which link?

## Why It Failed
Labels are topic markers, not entity identifiers. They operate at the article level (this article is about X), not the fact level (this specific claim is about entity Y within X). An article about POC reports might discuss the download link, the share link, the API endpoint, the email notification link — all different entities, all under the same label.

## What We Learned
Entity identity requires its own layer, below the label level. Labels can pre-filter (only compare facts from articles with overlapping labels) but cannot replace entity resolution. The entity+property+value decomposition is necessary — there is no shortcut through the label system.

## Impact on Design
This finding directly motivated the entity registry architecture (see D005). The flat `content_facts` table (fact strings grouped by label) is useful as raw material but cannot drive conflict detection.
