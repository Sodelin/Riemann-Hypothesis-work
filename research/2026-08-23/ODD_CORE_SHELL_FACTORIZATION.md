# Odd Core/Shell Factorization Criterion

**Route ID:** `W-O`  
**Claim IDs:** `O-SHELL-01`, `O-FACTOR-01`  
**Status:** `PROVED_SYMBOLIC` as an exact Hilbert-space decomposition plus a standard bounded block-positivity theorem.  
**Novelty:** no novelty claim for the operator theorem; the value is its specialization to the current support-propagation problem.  
**RH status:** certificate architecture only; the required arithmetic contraction has not been proved.

## 1. Why the previous Schur architecture was insufficient

For the compact screw-kernel operator `G_a`, positivity does not give a uniform spectral gap: positive eigenvalues may accumulate at zero. Therefore a criterion requiring

`G_a >= delta I`, `delta>0`,

is structurally mismatched to the localized compact formulation.

The correct block criterion must work for **positive semidefinite compact diagonal blocks without bounded inverses**.

## 2. Nested support spaces

Fix

`0<a<b`

and let

`delta=b-a`.

Let

`C=(-a,a)`

be the old core and

`S=(-b,-a) union (a,b)`

be the new symmetric shell.

Work in the even zero-mean space

`E_b^0 = {u in L^2(-b,b) : u even, integral u=0}`.

This is the derivative image of the odd `H_0^1` sector described in `ODD_COMPACT_THRESHOLD_CRITERION.md`.

## 3. Exact orthogonal decomposition

For `u in E_b^0`, let

`u_C = 1_C u`,

`u_S = 1_S u`.

Put

`m = integral_C u_C = - integral_S u_S`.

Define the normalized even mean carriers

`e_C = (1/(2a)) 1_C`,

`e_S = (1/(2delta)) 1_S`.

Both have integral one.

Now set

`u_C^0 = u_C - m e_C`,

`u_S^0 = u_S + m e_S`,

and

`e_T = e_C-e_S`.

Then

`integral_C u_C^0 = 0`,

`integral_S u_S^0 = 0`,

and

`u = u_C^0 + u_S^0 + m e_T`.

Moreover this decomposition is **orthogonal in L^2**:

- core and shell supports are disjoint;
- `<u_C^0,e_C>=0` because `u_C^0` has zero core mean;
- `<u_S^0,e_S>=0` because `u_S^0` has zero shell mean;
- the irrelevant carrier pieces have disjoint support.

Thus

`E_b^0 = E_C^0 direct_sum N_{a,b}`

orthogonally, where

`E_C^0 = {even zero-mean L^2 functions supported in C}`

and

`N_{a,b} = E_S^0 direct_sum span{e_T}`.

The new sector consists of zero-mean shell fluctuations plus **one scalar mean-transfer direction**. There are no hidden infinite-dimensional mean constraints.

## 4. Exact old-core identification

Let `G_b` be Suzuki's compressed screw-kernel operator on `E_b^0`.

If `x in E_C^0`, then `x` is already zero mean and supported in `(-a,a)`. Therefore its quadratic form is exactly the old localized form:

`<G_b x,x> = <G_a x,x>`.

Likewise the sesquilinear core-core form agrees with that of `G_a`.

Hence the upper-left block of `G_b` relative to

`E_b^0 = E_C^0 direct_sum N_{a,b}`

is exactly

`A = G_a`.

No approximation is involved.

## 5. Block form

Write

`G_b = [[A,B],[B*,C_new]]`

relative to the orthogonal decomposition above, where

- `A=G_a` on the old even-zero-mean core;
- `C_new` is the exact compression of `G_b` to the new shell/mean-transfer sector;
- `B` contains every core-to-new coupling, including all old prime shocks, the archimedean kernel, pole information already encoded by the screw kernel, and the newly activated arithmetic threshold.

This is the precise object that a threshold-induction proof must control.

## 6. Gapless block positivity theorem

### Theorem O-FACTOR-01

Let `H,K` be Hilbert spaces, let `A:H->H` and `C:K->K` be bounded positive semidefinite self-adjoint operators, and let `B:K->H` be bounded.

Then

`M = [[A,B],[B*,C]] >= 0`

if and only if there exists a contraction

`Gamma : closure(range(C^(1/2))) -> closure(range(A^(1/2)))`

(with the usual harmless extension by zero on orthogonal complements) such that

`B = A^(1/2) Gamma C^(1/2)`

and

`||Gamma|| <= 1`.

This is the standard positive `2x2` operator-matrix factorization (Douglas/Ando type criterion).

### Why this is the right replacement for an inverse Schur complement

No inverse of `A` or `C` is required. Zero may lie in their spectrum and their positive eigenvalues may accumulate at zero.

The condition automatically contains the necessary range compatibility:

`range(B) subset closure(range(A^(1/2)))`

and the corresponding adjoint condition.

Therefore it is suitable for compact positive operators.

## 7. Threshold propagation criterion

Assume inductively that

`G_a >= 0`

on the old core `E_C^0`.

To prove

`G_b >= 0`

on the enlarged even-zero-mean space, it is enough and, at the exact block level, necessary to establish:

1. `C_new >= 0` on the shell/mean-transfer sector;
2. a factorization

   `B = G_a^(1/2) Gamma C_new^(1/2)`

   with `||Gamma||<=1`.

This is the **gapless support-step certificate**.

For strict positivity/nondegeneracy one additionally needs to exclude nonzero vectors in the joint equality/null directions. A sufficient strong version is injectivity of the relevant diagonal forms plus a strict contraction on the coupled closures, but the exact strict criterion should be stated separately when used with Yoshida's `>0` formulation.

## 8. What the boundary-shock theorem contributes

`O-SHOCK-01` gives an exact universal diagonalization of the part of `C_new` associated with the newest prime-power interaction near the outer boundary. `O-SHOCK-SUM-01` shows the negative onset coefficients of those fresh shocks are summable across arithmetic thresholds.

These facts can help with item 1 above.

They do **not** by themselves prove item 2, because `B` also contains couplings from all previously active arithmetic shifts.

## 9. New central mathematical question

The route is now reduced to a precise factorization problem:

> Does the arithmetic/archimedean cross operator from a newly added thin symmetric shell into the old core factor through `G_a^(1/2)` with contraction norm at most one, once the exact new-sector operator is used on the other side?

This is substantially sharper than “bound the cross terms.”

It gives three independent ways to make progress:

### A. Direct range/smoothing theorem

Show that the integral kernel defining `B` maps the new sector into `range(G_a^(1/2))`, then estimate the induced graph norm.

### B. Feature-space factorization

Construct explicit feature maps `Phi_a`, `Psi_{a,b}` such that

`A=Phi_a^* Phi_a`,

`C_new=Psi^* Psi`,

and

`B=Phi_a^* U Psi`

for a contraction `U`.

A construction that already assumes global Weil positivity is circular and must be rejected.

### C. Finite + tail factorization

Prove the factorization on a finite vulnerable spectral block by a certified matrix computation, and prove an analytic contraction on the high-mode tail from the logarithmic archimedean singularity.

This is the current preferred certificate-first variant.

## 10. First kill tests

Any proposed factorization must be tested against:

1. an altered screw kernel with the same local `|t|log|t|` singularity but a deliberately inserted negative global mode;
2. a single prime-hinge model, whose odd boundary operator has known alternating signs;
3. finite Galerkin blocks around the first few prime thresholds;
4. the range condition near high modes, where `G_a` eigenvalues approach zero.

If a proof works unchanged in a control kernel with known negative localized spectrum, it has discarded the decisive arithmetic information.

## 11. Formalization target

`O-FACTOR-LEAN`: formalize the bounded positive block-operator theorem independently of zeta.

`O-SHELL-LEAN`: formalize the orthogonal core/shell/mean-transfer decomposition.

Once those are trusted, numerical or symbolic searches can propose finite certificates for `C_new` and the contraction, while Lean checks only certificate semantics and exact imported analytic bounds.
