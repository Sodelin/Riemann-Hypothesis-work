# Odd Null-Mode Equation

**Route ID:** `W-N`  
**Status:** `EXACT_REDUCTION / BLOCKED`  
**Purpose:** attack a hypothetical first odd-sector degeneracy directly rather than preserve an arbitrarily small positive spectral margin.

## 1. Motivation

Yoshida's criterion says positivity of the Weil form on all nonzero odd compactly supported smooth test functions implies RH. Suzuki's current operator framework identifies the localized self-adjoint operator `A_a` representing the Weil form and gives an exact distributional kernel for it.

If an odd-sector support continuation ever reaches a nonzero null vector `v`, then the load-bearing equality case is

`A_a v = 0`.

This route studies that equation directly.

## 2. Exact distributional operator

Suzuki v2, Section 2.5, writes

`A_a v = (-g'') * v`

on `(-a,a)`, with zero extension outside the interval, and gives

`-g''(t)`
` = -(1/2) Pf(1/|t|) -(2A+1)delta_0`
`   - sum_{n>=2} Lambda(n)/sqrt(n) [delta_{log n}+delta_{-log n}]`
`   - r''(t)`.

Therefore, on smooth test vectors, the null equation is

`0 = -(1/2) Pf integral_{-a}^a v(y)/|x-y| dy`
`    -(2A+1)v(x)`
`    - sum_{n<=exp(2a)} Lambda(n)/sqrt(n)`
`        [v(x-log n)+v(x+log n)]`
`    - integral_{-a}^a r''(x-y)v(y)dy`,

with shifted values understood via zero extension.

This is an exact singular-integral + finite-delay equation. The arithmetic part is finite at each support radius.

## 3. Derivative-space version

Let `D=i d/dx`. Suzuki proves

`B_a = D* G_a D`

with

`G_a=P_a G P_a`

on zero-mean derivative functions.

For odd `v in H_0^1(-a,a)`, `u=Dv` is even and zero mean. Conversely the derivative map takes the odd Dirichlet Sobolev space onto the even zero-mean derivative space.

If the odd localized form is positive semidefinite and `v` is a null vector, then

`<G_a u,u>=0`.

On a positive-semidefinite self-adjoint block this implies

`G_a u=0`.

Thus the equality case may equivalently be attacked as injectivity of `G_a` on the even zero-mean sector.

## 4. Critical regularity warning

Do **not** assume a conjectural null vector is smooth.

Historical work already proves nondegeneracy on several classical smooth/periodic test spaces. The RH-equivalent obstruction can live only after completion. Bombieri's numerical finite-section experiments also reported near-null eigenvectors whose mass concentrates toward the support boundary.

Suzuki explicitly cautions that for a general vector in the operator/form domain, pointwise values in the displayed distributional formula need not be meaningful; the identity survives in the form-limit sense.

Therefore invalid moves include:

- repeated classical differentiation of a hypothetical null eigenfunction without a regularity theorem;
- evaluating it pointwise at prime-shift locations;
- assuming ordinary boundary traces beyond what the form domain supplies;
- proving injectivity only for `C_c^infty` and calling that RH progress.

Any useful null-mode theorem must either establish the needed regularity from the equation or work directly in the form/distribution setting.

## 5. Why the equation is still useful

The operator has a very rigid decomposition:

1. a universal logarithmic/hypersingular archimedean part;
2. a finite set of translations by `log(p^m)` at fixed support;
3. a smooth convolution remainder.

This creates three concrete attack classes:

### N-A — elliptic/logarithmic regularity
Prove that a null vector in the form domain automatically gains enough interior/boundary regularity to justify a stronger equation.

### N-P — prime-delay propagation
Once regularity is available, exploit the finite translated copies and zero extension near the boundary to force vanishing or incompatible boundary data.

### N-F — finite-section/null certificate
Use Yoshida/Bombieri finite-codimension positivity or a certified Galerkin dictionary to show that a zero vector would have to lie simultaneously in a shrinking collection of low-dimensional vulnerable spaces whose intersection is trivial.

## 6. Current best interpretation

The null equation is **not** a proof yet. It is the equality-case form of the same global obstruction.

Its value is that it changes the next question from

`prove an arbitrarily small positive lower bound`

to

`rule out one exact kernel vector`.

That distinction is potentially important because numerical and historical work suggests the positive margin may tend extremely close to zero even if RH is true.

## 7. Source

Masatoshi Suzuki, `Weil's quadratic form via the screw function`, arXiv:2606.09096v2 (17 Aug 2026), especially equations (2.9)--(2.11) and the discussion of the localized operators.

The finite-codimension/nondegeneracy caution traces back to Yoshida and is summarized in Suzuki 2023/2026 and Bombieri 2000.
