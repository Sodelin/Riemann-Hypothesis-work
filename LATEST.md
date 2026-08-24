# Latest RH Research State

## Resolution status

**Unresolved. No proof or disproof of the Riemann Hypothesis is claimed.**

## Active cycle

The current research cycle began 2026-08-23 and now uses the shared proof-attack discipline developed across the RH, Collatz, and private `Proof-attack-structure` repositories.

Read in this order:

1. `sources/SUZUKI_WEIL_V2_2026.md`
2. `research/2026-08-23/ODD_COMPACT_THRESHOLD_CRITERION.md`
3. `research/2026-08-23/ODD_PRIME_SHOCK_BOUNDARY_OPERATOR.md`
4. `research/2026-08-23/PRIME_SHOCK_ONSET_SUMMABILITY.md`
5. `research/2026-08-23/ODD_CORE_SHELL_FACTORIZATION.md`
6. `proof-search/APPROACH_REGISTRY.md`
7. `proof-search/FAILURE_LEDGER.md`
8. `research/2026-08-23/CLAIM_LEDGER.csv`
9. `CONTINUATION.md`

Historical context and earlier exact identities remain under `docs/` and `research/2026-08-23/EXACT_DIAGONAL_WEIL_FORM.md`.

## Prior-art correction that changed the frontier

Suzuki's current 2026 v2 already develops the localized Weil/screw-function operator, discrete lower-bounded spectrum, lowest localized eigenvalue, continuity in support scale, and small-support positivity. Yoshida's earlier criterion, as cited by Suzuki, shows that strict Weil positivity for every nonzero **odd** compactly supported smooth test function suffices for RH.

Therefore localized spectral flow itself is now treated as `KNOWN / PRIOR_ART`, not as a project theorem.

The active project question is what can be proved **beyond** that substrate.

## Current primary route: W-O

### Odd compact-kernel formulation

For fixed support radius `a`, the derivative operator

`D=i d/dx`

bijects odd `H_0^1(-a,a)` functions with even zero-mean `L^2(-a,a)` functions. Suzuki's screw-kernel identity therefore converts the odd Weil problem to a compact integral-operator positivity problem on one parity/mean sector.

### Discrete arithmetic checkpoints

It is enough to prove strict odd-test positivity at any unbounded sequence of support radii. The natural checkpoints are

`a_k=(1/2)log q_k`,

where `q_k` are the distinct prime powers. This discretizes **where to search** but does not weaken the theorem-strength endpoint.

### Exact fresh-shock operator

For an odd test function, a prime-power shift `c=log q` with overlap length

`ell=2a-c`

is governed exactly by the universal compact operator

`T_ell=J_ell V_ell^2`

with kernel

`(ell-s-t)_+`.

Its eigenvalues are

`lambda_n=(-1)^(n+1) ell^2/beta_n^2`,

where

`cos(beta_n) cosh(beta_n)=-1`.

The first dangerous negative constant is

`1/beta_2^2 ≈ 0.04538339344`.

Hence one prime shock obeys the sign-aware lower bound

`P_q(f) >= -[Lambda(q)/sqrt(q)] (2a-log q)^2/beta_2^2 ||f'||_2^2`.

### Summable shock births

At consecutive prime-power thresholds, the negative **onset** costs are summable using any classical next-prime exponent `<3/4`. Thus the instant at which new prime shocks enter is not by itself the divergent obstruction.

The hard part is that enlarging support lets **all previously active shifts** couple to the newly available degrees of freedom.

## Strongest current certificate architecture

For `0<a<b`, the enlarged even-zero-mean space decomposes orthogonally into:

1. the old even zero-mean core on `(-a,a)`;
2. zero-mean symmetric boundary-shell fluctuations;
3. one scalar mean-transfer direction.

Relative to this split,

`G_b = [[G_a,B],[B*,C_new]]`.

Because compact positive operators need not have a positive spectral gap, the correct block theorem is the gapless factorization criterion:

`[[A,B],[B*,C]] >= 0`

iff `A,C>=0` and

`B=A^(1/2) Gamma C^(1/2)`

for a contraction `Gamma` (with standard closure/range conventions).

Thus the exact threshold-propagation target is:

1. prove `C_new>=0`;
2. prove the old-core/new-shell cross operator factors contractively through `G_a^(1/2)` and `C_new^(1/2)`.

This is `O-SHELL-CERT-01`.

## Current theorem-strength wall

The most important missing mechanisms are now:

### `O-SHELL-CERT-01`
A sign-aware core/shell contraction theorem that propagates positivity from one support scale to the next without assuming an unavailable uniform compact-operator gap.

### `O-RELTAIL-01`
A relative high-mode theorem showing that the archimedean structure controls the combined signed arithmetic tail strongly enough that only a finite vulnerable block needs explicit certification.

### `O-FLOW-01`
Alternative route: derive a relative shape inequality such as

`lambda_odd'(a) >= -C(a) lambda_odd(a)`

between arithmetic thresholds, with locally integrable `C` and correct matching. Gronwall plus small-support positivity would prevent a finite zero crossing. No such estimate has been proved.

These are real theorem-strength bridges. Their short statements are not evidence that RH is close in a conventional complexity sense.

## Numerical state

`verification/odd_weil_finite_basis.py` is diagnostic only. Finite-basis lowest odd-sector values rapidly approach the `1e-8` numerical scale as support grows. Tiny apparent negative values are not sign-certified and are explicitly **not** interpreted as counterexamples.

The main design conclusion is that a proof demanding a comfortable support-uniform spectral gap is poorly matched to the observed geometry.

## Formal state

- Anthropic's `zeta-23-lean` remains pinned as upstream formal infrastructure.
- Small local Lean targets exist in this repository.
- No local theorem is promoted to `LEAN_VERIFIED` without an observed successful clean build and axiom audit.
- The new odd/core-shell/factorization lemmas are currently `PROVED_SYMBOLIC` or `LEAN_TARGET`, not formally verified.

## Immediate next work

1. derive the exact core-to-shell screw-kernel block in coordinates suitable for the Douglas/Ando contraction criterion;
2. determine whether the local `|t|log|t|` singularity gives unconditional positivity/coercivity on sufficiently thin zero-mean shell fluctuations;
3. preserve old-prime signs rather than summing absolute shift norms;
4. search for a finite+tail factorization in which a certified low block is paired with an analytic high-mode contraction;
5. independently test any proposed factorization on altered false screw kernels before investing in a proof;
6. formalize the small universal operator lemmas only after their exact statements survive these audits.

The project is deliberately continuing from this frontier rather than restarting broad RH brainstorming.
