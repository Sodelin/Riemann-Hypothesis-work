# RH Continuation Checkpoint

This file is the canonical restart point for the active Riemann Hypothesis proof search.

## Resolution status

**RH remains unresolved. No proof or disproof is claimed.**

## Do not restart from earlier brainstorming

The active frontier has moved beyond:

- the 2026-08-01 multi-route brainstorming phase;
- naive Gamma-positive local energy;
- raw absolute prime-shift graph domination;
- treating the localized spectral operator as project novelty.

Suzuki v2 now supplies much of the localized Weil/screw-function operator theory as prior art. The current project builds on that substrate.

## Read first

1. `LATEST.md`
2. `sources/SUZUKI_WEIL_V2_2026.md`
3. `research/2026-08-23/ODD_COMPACT_THRESHOLD_CRITERION.md`
4. `research/2026-08-23/ODD_PRIME_SHOCK_BOUNDARY_OPERATOR.md`
5. `research/2026-08-23/PRIME_SHOCK_ONSET_SUMMABILITY.md`
6. `research/2026-08-23/ODD_CORE_SHELL_FACTORIZATION.md`
7. `proof-search/APPROACH_REGISTRY.md`
8. `proof-search/FAILURE_LEDGER.md`
9. `research/2026-08-23/CLAIM_LEDGER.csv`

For normalization history also read `research/2026-08-23/EXACT_DIAGONAL_WEIL_FORM.md`.

## Exact current endpoint interface

Use Yoshida's odd-test Weil criterion as the primary sufficient endpoint:

> strict positivity of the Weil form for every nonzero odd compactly supported smooth test function implies RH.

Via Suzuki's screw-function operator and the derivative map, this becomes an even-zero-mean compact-kernel positivity problem at each support radius.

## Results already obtained in this cycle

### 1. Odd derivative equivalence

`D=i d/dx` bijects odd `H_0^1(-a,a)` with even zero-mean `L^2(-a,a)`.

### 2. Unbounded checkpoint exhaustion

It is enough to establish odd-test positivity on any unbounded support sequence. Use the arithmetic checkpoints

`a_k=(1/2)log q_k`,

where `q_k` are distinct prime powers.

This is only search-space compression; the all-threshold statement remains global.

### 3. Exact prime-shock birth operator

A single odd prime-power shift with overlap `ell=2a-log q` is represented by

`T_ell=J_ell V_ell^2`,

whose spectrum is

`(-1)^(n+1) ell^2/beta_n^2`,

`cos beta_n cosh beta_n=-1`.

The dangerous negative constant is `1/beta_2^2≈0.04538339344`.

### 4. Summable onset costs

The negative coefficients at which consecutive prime-power shocks are born form a summable sequence using any standard next-prime exponent `<3/4`.

This does **not** control the old shocks on the newly enlarged support.

### 5. Exact core/shell decomposition

For `0<a<b`, the enlarged even-zero-mean space splits orthogonally into:

- old zero-mean core;
- new zero-mean symmetric shell;
- one mean-transfer scalar direction.

The old-core block of `G_b` is exactly `G_a`.

### 6. Gapless block positivity

For compact positive diagonal blocks, do not use an inverse Schur complement requiring a spectral gap. Use the standard contraction factorization:

`[[A,B],[B*,C]]>=0`

iff `A,C>=0` and

`B=A^(1/2) Gamma C^(1/2)`

for a contraction `Gamma`, with the standard range/closure conventions.

This is the correct support-propagation language for the localized screw operator.

## Primary current target

### `O-SHELL-CERT-01`

For consecutive support checkpoints, prove:

1. the exact new shell/mean-transfer block `C_new` is positive;
2. the exact core-to-new cross block has the factorization

   `B=G_a^(1/2) Gamma C_new^(1/2)`

   with `||Gamma||<=1`.

If this can be established recursively for every checkpoint, odd-test positivity follows at all compact supports and hence RH follows by Yoshida.

This is not yet proved.

## Secondary bridge targets

### `O-RELTAIL-01`

Seek a finite+tail theorem: certify a finite vulnerable block and prove an analytic contraction on the high-mode tail using the logarithmic archimedean singularity while retaining signed prime arithmetic.

### `O-FLOW-01`

Alternative continuation route: derive a relative lowest-eigenvalue estimate of the schematic form

`lambda_odd'(a)>=-C(a)lambda_odd(a)`

between arithmetic thresholds. Continuity alone is not enough.

## Immediate derivation to attempt next

Write the screw-kernel cross block explicitly on the decomposition

`E_b^0 = E_a^0 direct_sum E_shell^0 direct_sum span{mean-transfer}`.

Then:

1. isolate the singular near-boundary `|t|log|t|` part;
2. determine whether zero shell mean makes its self-block unconditionally positive at sufficiently small shell width;
3. compute the old-core/new-shell cross map for that singular kernel exactly or to a sharp relative norm;
4. treat smooth archimedean and arithmetic pieces as signed perturbations only after the singular structure is preserved;
5. test the proposed contraction on a false control kernel before promotion.

## Formalization queue

Highest-value independent formal targets now are:

1. `O-DERIV-LEAN` — odd derivative / even-zero-mean bijection;
2. `O-SHOCK-LEAN` — reflected boundary identity and `T_ell=J V^2`;
3. `O-SHELL-LEAN` — exact orthogonal core/shell/mean-transfer split;
4. `O-FACTOR-LEAN` — gapless positive block factorization theorem;
5. exact imported Suzuki/Yoshida statement interface;
6. only then any RH-specific certificate checker.

Do not label these `LEAN_VERIFIED` until a pinned clean build and axiom audit is observed.

## Numerical policy

`verification/odd_weil_finite_basis.py` is reconnaissance only. Near-zero floating-point eigenvalues are not signs. Any candidate negative must be reconstructed with rigorous Fourier/quadrature tails and interval arithmetic before interpretation.

## Reopening discipline

Before reopening a historical route, state:

- old blocker;
- genuinely new mechanism;
- why it bypasses the blocker;
- first falsification test;
- exact theorem target.

If no new mechanism exists, remain at the current odd core/shell frontier instead of generating a renamed route.

## Methodology source

The general proof-search framework is maintained in the private `Sodelin/Proof-attack-structure` repository. This public repository remains self-contained enough that its mathematical status can be understood without private access.
