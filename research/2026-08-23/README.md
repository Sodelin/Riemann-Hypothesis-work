# RH Research Cycle — 2026-08-23

## Status

**OPEN RESEARCH. No proof or disproof of the Riemann Hypothesis is claimed.**

This cycle starts from the audited 2026-08-01 dossier already preserved in this repository and changes the research method in two ways:

1. use Git history as a dated research ledger, so candidate mechanisms, counterexamples, blocked routes, and formalization targets remain inspectable rather than being overwritten by the next idea;
2. search the **interstitial proof space**: identify the smallest explicit mathematical and Lean gaps between available formal infrastructure and a complete RH implication, then attack those gaps as named lemmas.

The aim is not to manufacture a long dossier. The aim is to keep the frontier sharp enough that every new result either closes a named gap, kills a route, or exposes the next missing theorem.

## Why this cycle is different

The August 1 dossier ended at several equivalent global positivity statements: the full generalized Laguerre hierarchy, positive definiteness of the associated kernels/tilts, and the Fenchel family. None was proved globally.

Since then, Anthropic released `anthropics/zeta-23-lean`, a complete sorry-free Lean 4 / Mathlib formalization of a new result proving that more than two thirds of the nontrivial zeros of zeta lie on the critical line. Its formal library includes, among other ingredients, zeta-zero definitions against Mathlib, analytic multiplicity, Weil's explicit formula, Riemann–von Mangoldt counting, Gamma estimates, prime-sum estimates, and generalized Hilbert inequalities.

That does **not** make RH close to solved. It does materially reduce the amount of analytic infrastructure that a Lean-first RH program would otherwise need to rebuild.

Upstream reference:
- https://github.com/anthropics/zeta-23-lean

## Research governance

The governance is adapted from the earlier Collatz adversarial program:

- routes are registered by mechanism, not by rhetoric;
- theorem-strength missing steps are marked `BLOCKED`, never silently assumed;
- an equivalent reformulation of RH is not counted as progress toward a proof merely because it looks different;
- numerical evidence can falsify or guide, but cannot promote a universal statement to `PROVED`;
- every route must return at least one concrete object: a lemma, formula, counterexample, reproducible computation, formal proof artifact, or precisely stated missing theorem;
- obstructed routes are not reopened unless a materially new mechanism appears;
- correctness, novelty, usefulness, and RH relevance are recorded separately.

See [`ADVERSARIAL_PROTOCOL.md`](ADVERSARIAL_PROTOCOL.md).

## Active tracks

### Track W — Weil positivity / Lean spine

This is the primary track for this cycle because the new formal explicit-formula infrastructure makes its intermediate steps unusually concrete.

The working spine is:

`Mathlib RH statement`
→ `formal zeta-zero / explicit-formula seam`
→ `our exact Weil-form normalization`
→ `formal Weil criterion interface`
→ `finite block positivity machinery`
→ `Riemann-specific uniform domination theorem`
→ `global Weil positivity`
→ `RH`.

The first four arrows contain substantial but bounded formalization work. The Riemann-specific uniform domination theorem is the likely theorem-strength wall. It is deliberately isolated rather than disguised inside the surrounding formalization.

See [`LEAN_GAP_GRAPH.md`](LEAN_GAP_GRAPH.md).

### Track T — Laguerre / tilted-autocorrelation bridge

The August 1 program remains active as a secondary cross-check:

- generalized Laguerre hierarchy `L_n / K_n`;
- tilted autocorrelation `S_alpha`;
- positive-definite order for `C_a`;
- Fenchel margins `E_k`.

The useful new question is not simply to re-prove those RH-equivalent statements. It is whether there is a **positivity-preserving transform** between this hierarchy and the Weil test-function formalism. Such a bridge could transfer a tractable estimate from one representation to another.

## First concrete mechanism under test

[`ROUTE_A_PRIME_SHIFT_GRAPH.md`](ROUTE_A_PRIME_SHIFT_GRAPH.md) develops an abstract block-positivity architecture.

Very roughly: after decomposing a compact support region into cells, prime-power terms in a Weil-type explicit formula behave as support shifts by logarithms of prime powers. The resulting quadratic form can be viewed as local coercive blocks plus graph-like couplings. An abstract operator-norm lemma can certify positivity if the normalized coupling matrix is uniformly dominated.

The **abstract block lemma is a genuine independent target** and should be formalizable. The assertion that the actual Riemann Weil form satisfies the required uniform domination is **not established** and is registered as the hard open node `W-GLOBAL-01`.

## Status vocabulary

- `LEAN_VERIFIED` — compiled in the recorded Lean/Mathlib environment and axiom-audited as required.
- `UPSTREAM_LEAN` — proved in a referenced upstream Lean artifact; not yet rebuilt/checked in this repository.
- `PROVED_SYMBOLIC` — complete mathematical derivation in this project, not yet Lean-verified.
- `LEAN_TARGET` — exact formal statement proposed; not compiled/proved yet.
- `CONDITIONAL` — proof is valid assuming an explicitly named unproved hypothesis.
- `NUMERICAL` — computational evidence only.
- `CONJECTURE` — live mathematical conjecture.
- `OPEN_EQUIVALENT` — equivalent to RH or apparently contains the full RH difficulty; not progress by itself.
- `COUNTEREXAMPLE` — explicit counterexample kills a stated claim.
- `BLOCKED` — route currently stops at a precisely identified missing theorem.
- `REJECTED` — mechanism is invalid or nonviable under its stated assumptions.

The machine-readable current state is in [`CLAIM_LEDGER.csv`](CLAIM_LEDGER.csv).

## Commit rule

A research commit should answer at least one of these questions:

1. What exact statement was added or changed?
2. What evidence supports its status?
3. What would falsify it?
4. Which previous node does it depend on?
5. What is the next smallest mathematical step?

A failed idea is worth committing if the failure is exact. Failed routes are part of the map.

## Immediate work queue

1. Formalize the abstract finite block-Schur positivity lemma (`W-BLOCK-01`).
2. Formalize exact support-overlap/translation vanishing (`W-SHIFT-01`).
3. Formalize the weighted cross-edge energy inequality (`W-EDGE-01`).
4. Pin an exact Weil-form normalization compatible with the upstream explicit formula (`W-NORM-01`).
5. State and formalize the bidirectional Weil-criterion interface in that normalization (`W-CRIT-01`), separating the easy zero-side direction from the separation/interpolation direction.
6. Only then attack the Riemann-specific uniform spectral domination problem (`W-GLOBAL-01`).

The discipline is intentionally asymmetric: we should spend Lean effort on statements that can actually be completed, while keeping the conjecture-strength theorem visible in red rather than burying it under infrastructure.
