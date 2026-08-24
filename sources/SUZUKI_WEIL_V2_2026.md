# Source Integration — Suzuki, `Weil's quadratic form via the screw function`, v2

**Source:** Masatoshi Suzuki, arXiv:2606.09096v2  
**Current arXiv revision:** 2026-08-17 (paper header in experimental HTML: version of 2026-08-19)  
**URL:** https://arxiv.org/abs/2606.09096  
**Integration date:** 2026-08-23  
**Status in this repository:** load-bearing prior art; not a project novelty claim.

## Why this source materially changes the active proof graph

The 2026-08-01 RH dossier knew Suzuki's screw-function/Weil framework but predated the current v2. The current revision develops much of the localized operator theory that the 2026-08-23 project independently began to reconstruct.

Accordingly, the following project ideas are **not to be claimed as new** merely because we re-derived them:

- localization of Weil's quadratic form to `[-a,a]`;
- a self-adjoint localized Weil operator with discrete lower-bounded spectrum;
- use of the lowest localized eigenvalue as a variational RH interface;
- continuity in the support scale;
- small-support positivity;
- parity-restricted variational considerations;
- passage from the distributional Weil form to a continuous screw-function kernel.

Our independent derivations remain useful as normalization checks and as inputs to formalization/certificate design, but priority belongs to the cited literature unless a genuinely stronger theorem is later isolated.

## Exact imported results / interfaces

### S1 — Weil positivity

For compactly supported smooth test functions, global nonnegativity of Weil's Hermitian quadratic form is equivalent to RH.

**Status:** literature foundation.

### S2 — Yoshida odd-test criterion

Suzuki records Yoshida's Proposition 1: if

`Q_W(v) > 0`

for every nonzero **odd** `v in C_c^∞(R)`, then RH follows.

Under RH, Weil positivity supplies the reverse nonnegativity direction. Endpoint strictness/nondegeneracy must be handled with the exact literature statement when turning this into a formal iff.

**Why it matters here:** a proof can target one parity sector instead of the full test-function space.

### S3 — localized closed form and self-adjoint operator

For every `a>0`, the localized closed form `Q_W^a` is represented by a canonical densely defined self-adjoint operator `A_a` on `L^2(-a,a)` with discrete lower-bounded spectrum. Its bottom spectral value

`lambda_a = inf Q_W^a(v)/||v||_2^2`

is an eigenvalue.

**Status:** prior art, building on Connes–Consani / Connes–Consani–Moscovici and made explicit in Suzuki's framework.

### S4 — continuity and failure criterion

Suzuki proves that `lambda_a` is continuous in `a`. Since it is positive for sufficiently small `a`, failure of RH is equivalent to `lambda_a<0` for some scale and hence forces a zero crossing at some scale.

**Status:** prior art.

### S5 — screw-function operator

Suzuki defines a continuous even screw function `g` and the compressed integral operator

`G_a = P_a G P_a`

on the zero-mean subspace `L_0^2(-a,a)`. With the Dirichlet differential operator `D=i d/dx`, the localized Weil form on `H_0^1(-a,a)` is represented through

`B_a = D* G_a D`,

and `A_a` is the Friedrichs extension of this symmetric operator.

**Status:** prior art.

### S6 — fixed-support arithmetic is finite

For fixed `a`, only finitely many prime-power translations enter the explicit Weil form. This is an exact reason finite-support certificate searches are meaningful, though a certificate family still needs a theorem covering **all** support scales to prove RH.

## Project-derived corollary to audit/formalize

The following is a direct synthesis of Yoshida's odd criterion and Suzuki's `G_a` representation; no novelty is claimed.

Let

`E_a^0 = {u in L^2(-a,a) : u is even and integral(u)=0}`.

The derivative map

`D : H_0^1(-a,a)_odd -> E_a^0`

is bijective:

- derivative of an odd `H_0^1` function is even;
- the endpoint condition forces zero integral;
- conversely, for even zero-mean `u`, `v(x)=-i integral_0^x u(t)dt` is odd, belongs to `H_0^1`, and satisfies `Dv=u`.

Therefore positivity of `G_a` on the **even zero-mean sector** for every `a` supplies exactly the odd-test Weil positivity required by Yoshida, subject to the standard density/form-domain identification.

This is recorded separately as `research/2026-08-23/ODD_COMPACT_THRESHOLD_CRITERION.md`.

## What Suzuki does not give us

This source does **not** prove RH.

It does not provide a theorem showing that the relevant localized eigenvalue remains nonnegative for all support scales. The global arithmetic cancellation remains the unresolved hinge.

It also means that simply defining a spectral flow, a lowest localized eigenvalue, or a compact screw-kernel operator is not progress by itself in this project. Those are now substrate.

## New theorem cells created by this integration

1. **O-COMPACT-01:** formalize the odd-`H_0^1` / even-zero-mean derivative bijection and the exact restricted `G_a` criterion.
2. **O-THRESH-01:** reduce all support scales to an unbounded sequence of support checkpoints by nested-space monotonicity, then choose arithmetic prime-power thresholds as the natural checkpoints.
3. **O-CERT-01:** find a finite, rigorously checkable certificate for nonnegativity of the even-zero-mean compression of `G_a` at one checkpoint, with explicit error/tail bounds.
4. **O-STEP-01:** find a theorem propagating certificates from one arithmetic threshold to the next, or a different mechanism controlling all thresholds uniformly.

`O-STEP-01` is the current theorem-strength wall. It must not be described as small merely because its statement can be short.

## Interaction with Anthropic `zeta-23-lean`

Anthropic's 2026 formal artifact supplies a separately formalized explicit formula, Gamma estimates, prime-sum estimates, zero-counting infrastructure, and a Montgomery–Vaughan weighted Hilbert inequality.

These tools should be imported where their exact hypotheses match the new odd-sector certificate problem. In particular, the Montgomery–Vaughan inequality is **not** to be applied to the prime-translation operator merely by analogy: its denominators/frequency-gap structure must be derived in the certificate representation before the theorem is relevant.

## Priority verdict

- Suzuki localized operator: `KNOWN / PRIOR_ART`.
- Odd/even-zero-mean reformulation: immediate project synthesis of cited results; `DERIVED`, no novelty claim.
- Prime-threshold certificate architecture: research-engineering proposal; novelty unresolved and currently irrelevant until it yields a theorem.
- RH proof: absent.
