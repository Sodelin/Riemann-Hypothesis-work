# Source Integration: Anthropic 2026 Zeta Result and Formal Infrastructure

## Bibliographic/source identity

Primary process/result source:

- Anthropic, **“Learning more about Claude's mathematical capabilities”**, Aug. 10, 2026  
  https://www.anthropic.com/research/riemann-zeta

Formal repository:

- `anthropics/zeta-23-lean`  
  https://github.com/anthropics/zeta-23-lean

The formal repository accompanies the paper **“More than two thirds of the zeros of the Riemann zeta function lie on the critical line.”**

## Exact relevance to this project

Anthropic's result is **not a proof of RH** and Anthropic explicitly says it does not expect the technique itself to lead to an RH proof.

Its importance here is twofold:

1. mathematical representations/ideas involving Weil quadratic forms, on/off-line zero directions, and non-diagonal treatment;
2. a substantial Lean/Mathlib infrastructure that removes lower-level formalization work from our gap graph.

## Formal infrastructure imported as `UPSTREAM_LEAN`

The upstream repository states that it provides sorry-free Lean formalizations including:

- definitions tied directly to Mathlib's `riemannZeta` and analytic multiplicity;
- nontrivial zero configuration machinery;
- Weil bilinear/quadratic form definitions;
- the literature explicit-formula normalization;
- convolution test functions `f⋆g̃` and Fourier-factor identities;
- Riemann–von Mangoldt zero counting;
- Gamma/digamma estimates;
- prime-sum/Chebyshev–Mertens estimates;
- generalized Hilbert inequalities;
- related Dirichlet-L explicit-formula machinery.

The repository pins Lean `v4.33.0-rc2` and a Mathlib revision in its Lake configuration.

## Important formal nuance

In the explicit-formula source, the literature formula is represented as a proposition/hypothesis at an abstract zero-configuration layer and then instantiated/proved through the larger formal development. Local use must track the exact theorem that discharges that hypothesis for the zeta configuration rather than treating a definition such as `EF_lit Z` as a theorem by naming alone.

## Project notation seam

The upstream paper Fourier convention is

`paperFT f z = ∫ f(u) exp(i z u) du`.

For real frequency it proves the dictionary to Mathlib's Fourier transform with the `-τ/(2π)` scaling.

The upstream convolution test is

`weilTest f g = f ⋆ tilde g`, `tilde g(u)=conj(g(-u))`,

with a proved transform factorization.

Our active diagonal route uses `g=f` and derives exact real translation correlations plus the pole/Gamma decomposition. That local derivation is recorded separately and remains a local symbolic result until formalized.

## Proof-graph nodes affected

### Closed/reduced infrastructure nodes

- defining a canonical zeta zero set/multiplicity from Mathlib;
- rebuilding the entire Fourier normalization from scratch;
- basic Weil convolution transform identity;
- much of the explicit-formula analytic substrate;
- substantial zero-counting/Gamma/prime-sum background.

### Still open

- exact local diagonal seam theorem in our preferred presentation;
- full formal Weil criterion equivalence for our selected admissible test class;
- off-line-zero separation/interpolation theorem for the reverse criterion;
- any theorem proving global Weil positivity;
- the local/global coercivity mechanism in Route W-A;
- all RH-equivalent endpoint positivity statements.

## New theorem targets produced by integration

### W-DIAG formal seam

Turn the upstream definitions into a theorem stating the exact diagonal form as:

- rank-two pole moments;
- von-Mangoldt-weighted translation correlations;
- Gamma Fourier multiplier.

### W-CRIT reverse interface

Formalize a precise test-function separation theorem proving that positivity of the selected Weil quadratic form rules out an off-critical-line zero.

### W-A finite block experiments

Use the exact prime shifts `log(p^m)` and finite support to build finite-dimensional restricted quadratic forms for adversarial testing.

## What the source does NOT prove for us

It does not prove:

- RH;
- global positivity of our candidate Weil form;
- local coercivity of the archimedean+pole operator;
- the prime-shift spectral domination theorem;
- equivalence of every old August-1 RH reformulation with the exact new local Lean objects without seam proofs;
- novelty of any local theorem we derive.

## Methodology imported from Anthropic's process

The public process also motivates:

- persistent artifact-based coordination;
- explicit failed-idea ledgers;
- independent/hostile proof review;
- aggressive numerical falsification;
- literature synthesis;
- prior-art search after a candidate theorem appears;
- formalization after/alongside mathematical validation.

The general methodology is maintained in the separate private `Proof-attack-structure` repository; this public file states enough to understand why the RH project's workflow changed.

## Next audit

Before local formal claims are promoted:

1. pin exact upstream commit used in `lean/lakefile.toml`;
2. clean-build the local package;
3. inspect headline upstream axiom output relevant to imported theorems;
4. prove/check our normalization seam rather than relying on notation resemblance;
5. record any upstream revision that changes theorem statements or trusted definitions.
