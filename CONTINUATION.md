# RH Continuation Checkpoint

This file is the canonical restart point for the active Riemann Hypothesis proof search.

## Do not restart from the August 1 brainstorming phase

The 2026-08-01 dossier is preserved as historical research. The active frontier has moved to a Lean-oriented Weil/explicit-formula program informed by newly available `zeta-23-lean` infrastructure.

## Read first

1. `LATEST.md`
2. `research/2026-08-23/LEAN_GAP_GRAPH.md`
3. `research/2026-08-23/EXACT_DIAGONAL_WEIL_FORM.md`
4. `proof-search/APPROACH_REGISTRY.md`
5. `proof-search/FAILURE_LEDGER.md`
6. `research/2026-08-23/CLAIM_LEDGER.csv`

## Current exact form

For diagonal `k=f⋆f̃`, the literature explicit-formula side has been derived symbolically as:

- pole sector `2 Re( fhat(i/2) conj(fhat(-i/2)) )`;
- prime sector `-2 Σ Λ(n)/sqrt(n) Re <f, τ_{log n} f>`;
- Gamma sector `(1/2π) ∫ |fhat(r)|² G(r) dr`.

The pole sector is rank-two indefinite. The Gamma multiplier is negative near `r=0`.

## Immediate mathematical target

Before pursuing a global prime-shift spectral bound, test the **combined archimedean-plus-pole operator** on compact-support subspaces.

Questions:

1. Is it bounded below on support `[-L/2,L/2]` after removing a finite-dimensional sector?
2. If not, can an exact counterexample kill `W-LOCAL-01` in its present form?
3. If a lower bound exists only after incorporating some prime shifts, the architecture must be redesigned around signed blocks rather than “positive local + negative edges.”
4. If the form has a finite negative index, can the negative directions be identified explicitly and handled by Schur complement/projection?

## Formalization queue

1. exact diagonal autocorrelation identity;
2. Hermitian symmetry `k(-a)=conj(k(a))`;
3. real-axis Fourier square identity;
4. pole rank-two decomposition;
5. prime translation-correlation rewrite;
6. weighted edge-energy lemma;
7. abstract finite block positivity theorem;
8. exact reverse-Weil separation statement once test class is fixed.

## Routes that remain blocked

- finite Laguerre prefix positivity alone;
- smooth even decreasing+convex kernel shortcut;
- individual theta-slice positivity strategy;
- Gamma-multiplier-alone positive local energy;
- any global spectral domination claim not first surviving finite adversarial tests.

Reopen an old route only with a new mechanism and record what old blocker it bypasses.

## Methodology

The reusable proof-search framework is maintained separately in the private `Sodelin/Proof-attack-structure` repository. This public RH repository should contain all methodology needed to understand the mathematical status without requiring access to the private repo.

## Next cycle output requirements

The next pass should commit at least one of:

- exact lower-bound theorem for a restricted support/operator class;
- explicit counterexample to the proposed local coercivity architecture;
- exact finite-dimensional matrix reduction with certified spectrum;
- new finite-rank decomposition;
- formal proof of one of the small seam lemmas;
- or a precisely stronger route replacing `W-LOCAL-01`.
