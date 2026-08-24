# Latest RH Research State

## Resolution status

**Unresolved. No proof or disproof of the Riemann Hypothesis is claimed.**

## Active cycle

The current research cycle began 2026-08-23 and is organized around a Lean-oriented missing-gap graph plus adversarial route testing.

Read in this order:

1. `research/2026-08-23/README.md`
2. `research/2026-08-23/LEAN_GAP_GRAPH.md`
3. `research/2026-08-23/EXACT_DIAGONAL_WEIL_FORM.md`
4. `research/2026-08-23/ROUTE_A_PRIME_SHIFT_GRAPH.md`
5. `research/2026-08-23/CLAIM_LEDGER.csv`
6. `proof-search/APPROACH_REGISTRY.md`
7. `proof-search/FAILURE_LEDGER.md`
8. `CONTINUATION.md`

## Strongest current structural advance

Using the normalization in Anthropic's `zeta-23-lean` explicit-formula infrastructure, the diagonal test `k=f⋆f̃` gives an exact decomposition into:

- a rank-two indefinite pole moment form;
- prime-power translation correlations at shifts `log n`;
- the real Gamma/digamma Fourier multiplier sector.

This validates the translation-graph interpretation of the prime sector but simultaneously kills the naive idea that the remaining sector is a pointwise positive diagonal reservoir.

## Current primary route

**W — Weil / explicit-formula positivity**, with experimental subroute:

**W-A — prime-shift graph + exact low-rank/archimedean operator treatment.**

The abstract finite block lemma and support/edge lemmas are small formalization targets. The Riemann-specific local/global coercivity statements remain unproved and may be false.

## Current hard questions

1. Does the combined archimedean-plus-pole quadratic form have any useful coercivity after restricting support or separating a finite-dimensional indefinite sector?
2. Can the full exact Weil form be partitioned into blocks without destroying the arithmetic cancellation needed for positivity?
3. Is the proposed normalized spectral domination theorem false, merely stronger than needed, or a genuine new bridge?
4. Can the older Laguerre/tilted-autocorrelation interface be connected to the Weil interface by an explicit positivity-preserving transform?
5. What exact admissible-test separation theorem is needed for a clean formal reverse Weil criterion?

## Formal state

- Upstream: `anthropics/zeta-23-lean`, pinned in the local `lean/` package.
- Local formal source exists for small seam/energy targets.
- Local claims are **not** promoted to `LEAN_VERIFIED` without an observed successful clean build/audit.

## Historical state

The 2026-08-01 dossier remains preserved under `docs/`. It contains exact reformulations, no-go results, finite-Laguerre candidate work, and the prior global gap analysis. Its conclusions should be read as historical inputs to the new cycle, not overwritten.
