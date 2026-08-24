# Odd Local Mean Compensation

**Route ID:** `W-O`  
**Claim IDs:** `O-LOCAL-CARRIER-01`, `O-NEWBLOCK-01`  
**Status:** `PROVED_SYMBOLIC` as a decomposition and asymptotic positivity mechanism, using the previously derived local cusp and fresh-shock bounds.  
**RH status:** this removes the apparent scalar obstruction from the *new diagonal block*. The old-core/new-boundary cross block remains the active wall.

## 1. Why the uniform carrier was the wrong coordinate

The orthogonal decomposition in `ODD_CORE_SHELL_FACTORIZATION.md` compensated a nonzero shell mean using the uniform core carrier

`e_C=(1/(2a))1_[-a,a]`.

That produced a global mean-transfer vector and the scalar limit studied in `ODD_MEAN_TRANSFER_LIMIT.md`.

The scalar is mathematically valid for that chosen vector, but it is **not intrinsic to the support-extension problem**. The choice of a carrier with integral one inside the old core is not unique.

For induction, it is better to transfer the mean only across the physical boundary.

## 2. Local inner carrier

Fix

`0<a<b`, `delta=b-a`,

old core

`C=(-a,a)`,

and outer shell

`S=(-b,-a) union (a,b)`.

Define the inner boundary strips

`I_in=(-a,-a+delta) union (a-delta,a)`

and the normalized even carrier

`c_in=(1/(2delta))1_{I_in}`.

Then

`integral c_in=1`.

Let `u` be even with total mean zero on `(-b,b)`. Write

`u=u_C+u_S`

by restriction to core and shell, and put

`m=integral_C u_C=-integral_S u_S`.

Define

`x=u_C-m c_in`,

`n=u_S+m c_in`.

Then

`u=x+n`,

`x` is even, supported in the old core, and `integral x=0`, while

`n` is even, has total mean zero, and is supported in the two boundary bands

`I_- = (-a-delta,-a+delta)`,

`I_+ = (a-delta,a+delta)`.

Because `n` is even and has total mean zero,

`integral_{I_+} n=integral_{I_-} n=0`.

### Theorem O-LOCAL-CARRIER-01

Every even zero-mean vector on the enlarged interval admits a unique representation

`u=x+n`

with

- `x` in the old even zero-mean core space;
- `n` in the image of the local boundary-compensation map above.

The new coordinate is localized to a width-`2delta` neighborhood of each boundary. No global scalar mean-transfer coordinate is required.

The representation is not `L2`-orthogonal, but it is linear and bounded for every fixed `a,delta`; block-form arguments may therefore be written at the quadratic-form level rather than relying on orthogonal projection coordinates.

## 3. Enlarging the new sector for a positivity proof

The actual image of the boundary-compensation map is a proper linear subspace of

`H_bd(a,delta)`
` = {n even : supp n subset I_- union I_+,`
`                integral_{I_+}n=integral_{I_-}n=0}`.

Therefore it is enough to prove positivity on the larger space `H_bd(a,delta)`.

This enlarged space is the direct analogue of the zero-mean shell space from `ODD_ADAPTIVE_SHELL_MESH.md`, except that each connected component now straddles the old support boundary.

## 4. Same-band coercivity

Each connected boundary band has length `2delta` and carries zero mean.

Write a profile `h` on one band and its primitive `p`, so `p` vanishes at both ends.

Suzuki's local logarithmic-cusp expansion and the Fourier uncertainty estimate give

`Q_local(h)`
`>= [ log(1/(4*pi*delta)) - 1/pi - R0(2delta)(2delta) ] ||p||_2^2`,

where `R0(2delta)` bounds the second derivative of the smooth local remainder.

Thus the local coercive coefficient tends to `+infinity` as `delta->0`.

## 5. Coupling of the positive and negative boundary bands

The distance between the two boundary bands lies in

`[2a-2delta,2a+2delta]`.

### Artificial mesh step away from an arithmetic threshold

If this interval contains no `log q` for a prime power, the active prime-hinge sum is affine throughout the cross-distance range. Since each boundary band has zero mean, every affine arithmetic contribution vanishes exactly.

The remaining archimedean cross kernel is smooth. After integrating by parts in both band variables, its absolute value is bounded by

`O( delta * sup_{[2a-2delta,2a+2delta]} |B''| )`

times the primitive energy.

The adaptive-mesh choice can make this arbitrarily smaller than the logarithmic local coefficient.

### Step centered at one arithmetic threshold

Suppose `2a=log q` for a newly active distinct prime power `q`, and choose `delta` so small that no other prime-power logarithm lies in the cross-distance interval.

All older hinge terms are affine and again vanish by zero band means.

The only non-affine arithmetic term is the single fresh hinge at `log q`. Its boundary restriction is exactly of the type diagonalized in `ODD_PRIME_SHOCK_BOUNDARY_OPERATOR.md`.

Its dangerous negative spectral size is bounded by

`O( w_q delta^2 / beta_2^2 )`,

where

`w_q=Lambda(q)/sqrt(q)`

and `beta_2` is the second positive root of

`cos beta cosh beta=-1`.

This tends to zero quadratically in `delta`, while the local cusp coefficient grows like `log(1/delta)`.

## 6. New diagonal-block theorem

### Theorem O-NEWBLOCK-01

For every fixed support radius `a>0`, there exists `delta_a>0` such that for every sufficiently small support increment

`0<delta<delta_a`,

chosen so that the doubled boundary window contains at most the arithmetic threshold at its center, the screw-kernel quadratic form is strictly positive on every nonzero

`n in H_bd(a,delta)`.

Moreover a cofinal support mesh can be chosen so that this condition holds at every sufficiently late step, inserting artificial subdivisions between arithmetic thresholds and shrinking steps further at the thresholds themselves.

### Consequence

The entire actual new coordinate produced by local mean compensation has positive diagonal energy. The previously isolated global mean-transfer scalar is therefore a **coordinate artifact**, not a necessary vulnerable direction of the support-induction scheme.

This supersedes the use of `ODD_MEAN_TRANSFER_LIMIT.md` as the preferred induction coordinate. That file remains valid as a test-family identity and diagnostic.

## 7. What is still missing

For

`u=x+n`,

we have

`Q_b(u)=Q_a(x)+2 Re Q_b(x,n)+Q_b(n)`.

The first term is positive by the induction hypothesis, and the third can now be made positive by `O-NEWBLOCK-01`.

The remaining theorem is a **relative cross estimate**:

`|Q_b(x,n)|^2 <= Q_a(x) Q_b(n)`

(or an equivalent contraction/factorization statement)

for the locally compensated boundary sector.

This is exactly the missing Douglas/Ando contraction, now with a much more favorable new-sector geometry.

## 8. Why absolute `L2` estimates are not enough

At a fixed support radius, the odd localized Weil form may have a very small lowest positive Rayleigh eigenvalue. Numerical work in the current literature suggests that the margin can become extremely small.

Therefore an estimate of the form

`|Q_b(x,n)| <= epsilon(delta)||x||_2||n||_2`

is insufficient for a global proof unless `epsilon(delta)` is compared to the current spectral margin, which risks a Zeno continuation.

The desired estimate must be **relative to the Weil energies themselves**, or factor through their square roots.

## 9. New cross-block search object

Because every `n` in the enlarged boundary sector has zero mean on each tiny boundary band, the cross interaction with an old-core vector `x` admits moment cancellation.

For smooth portions of the kernel,

`g(x-y)-g(x-y_0)`

can be used before estimating, gaining a factor proportional to the boundary width.

For prime hinges, two integrations by parts localize the contribution to thin core strips centered at

`a-log q`.

This is the precise interface where the formally verified arbitrary-coefficient Montgomery-Vaughan/Hilbert machinery in `anthropics/zeta-23-lean` may become useful.

## 10. Next theorem target

`O-CROSS-REL-01`:

> Prove that the old-core/new-local-boundary cross form factors through the square roots of the two positive diagonal forms with contraction norm at most one, using the exact prime localization and archimedean logarithmic energy rather than an `L2` spectral gap.

If this theorem can be proved uniformly for a cofinal adaptive support mesh, the support induction would establish the odd Weil criterion and hence RH.

At present `O-CROSS-REL-01` remains `BLOCKED_EQUIVALENT-CANDIDATE`: it is the actual load-bearing bridge and must not be promoted merely because all diagonal sectors are now controlled.
