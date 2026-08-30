# Research-object bank pointer

Reusable source, annotation, prior-art, and formal-artifact snapshots from this project are indexed in the private repository [`Sodelin/research-article-annotation-zettelkastten-notebook-repo`](https://github.com/Sodelin/research-article-annotation-zettelkastten-notebook-repo).

The first migration is pinned to source commit `9b00c807c7603074073a1bc96d28b55c57177585`. Bank objects must record the source path, source commit, content digest, transformation relation, and access class. Copies are immutable provenance snapshots for cross-project discovery; they are not automatically current after this repository changes.

This repository remains authoritative for RH-specific theorem statements, Lean source, route and failure status, claim ledgers, and any later correction. Importing or validating a bank record cannot promote a mathematical claim, convert `LEAN_TARGET` to `LEAN_VERIFIED`, establish novelty, or imply a proof or disproof of the Riemann Hypothesis.

When an upstream object changes:

1. create a new bank object version rather than overwriting the old snapshot;
2. retain the old object and its dependency edges;
3. mark dependent annotations and verdicts stale when their pinned digest no longer matches;
4. update mathematical status only here, through this repository's existing review gates.

