# Odd Prime Cross Localization

**Route ID:** `W-O`  
**Claim ID:** `O-PRIME-CROSS-01`  
**Status:** `PROVED_SYMBOLIC` as an exact localization identity plus an `l2` collective bound under explicit zero-mean and spacing hypotheses.  
**RH status:** auxiliary cross-block theorem only. It improves the arithmetic norm, but it does not by itself compare the old primitive norm to the old Weil energy.

## 1. Geometry

Let `I` be one thin boundary interval, and let `n` be a boundary profile supported in `I` with

`integral_I n = 0`.

Let `H` be its primitive chosen to vanish at both endpoints of `I`, so

`H' = n`.

Let `x` be an old-core profile with zero mean on its old support, and let `X` be its primitive chosen to vanish at both endpoints of that support, so

`X' = x`.

For an active prime-power logarithmic shift

`c_q = log q`,

assume the local geometry is oriented so that the relevant hinge is

`h_q(t-y) = (t-y-c_q)_+`

throughout the boundary/core interaction under consideration. The opposite orientation on the symmetric boundary gives the conjugate/reflected identity.

This orientation condition is automatic on a sufficiently thin positive boundary band for the nontrivial prime shifts `c_q >= log 2`; the tiny band width is chosen below the first shift length.

## 2. Exact two-integration identity

Define the prime-hinge cross form

`C_q(x,n)`
` = integral_I integral h_q(t-y) x(y) n(t) dy dt`.

Because both primitives vanish at their relevant support endpoints, integration by parts in `y` gives

`integral h_q(t-y) X'(y) dy`
` = integral_{y < t-c_q} X(y) dy`.

A second integration by parts in `t` then gives

`C_q(x,n)`
` = - integral_I H(t) X(t-c_q) dt`.

Thus

`boxed: C_q(x,n) = - <H, X(.-c_q)>_{L2(I)}`.

No asymptotic approximation is involved.

## 3. Disjoint source strips

Let `Q(a)` be the finite set of prime powers active at a fixed support radius.

Choose the boundary width `|I|` so small that the translated source intervals

`I-c_q`, `q in Q(a)`,

are pairwise disjoint. A sufficient condition is

`|I| < (1/2) min_{q != r in Q(a)} |log q - log r|`.

The minimum is positive because `Q(a)` is finite.

For each `q`, Cauchy-Schwarz gives

`|C_q(x,n)|^2`
`<= ||H||_2^2 * integral_{I-c_q} |X(s)|^2 ds`.

Summing over the active shifts and using disjointness,

`sum_q |C_q(x,n)|^2`
`<= ||H||_2^2 ||X||_2^2`.

### Important audit correction

The functions `t -> X(t-c_q)` live on the same boundary interval `I` and are **not** being claimed orthogonal there.

The argument is instead:

1. bound each scalar coupling separately by the energy of `X` on its own source strip;
2. sum the squared scalar bounds;
3. use disjointness of the source strips only at that stage.

This distinction prevents a false orthogonality claim.

## 4. Collective von-Mangoldt bound

Let

`w_q = Lambda(q)/sqrt(q)`.

By Cauchy-Schwarz in the finite prime-power index,

`|sum_q w_q C_q(x,n)|`
`<= (sum_q w_q^2)^(1/2) (sum_q |C_q(x,n)|^2)^(1/2)`
`<= ||H||_2 ||X||_2 (sum_q Lambda(q)^2/q)^(1/2)`.

Hence the prime part of the old-core/new-boundary cross block satisfies

`boxed:`

`|C_prime(x,n)|`
`<= ||H||_2 ||X||_2`
`   * (sum_{q active} Lambda(q)^2/q)^(1/2)`,

up to the explicit factor from combining the two symmetric boundary components / the project normalization of the screw quadratic form.

The normalization factor must be pinned when this lemma is inserted into the full `G_a` operator; the localization mechanism and `l2` arithmetic dependence are invariant.

## 5. Size of the arithmetic factor

Classical estimates imply

`sum_{n<=Y} Lambda(n)^2/n = O((log Y)^2)`.

The main contribution comes from primes, for which

`sum_{p<=Y} (log p)^2/p ~ (1/2)(log Y)^2`,

while higher prime powers are lower order for this purpose.

At a support scale with active shifts up to approximately

`Y = exp(2a)`,

we therefore have

`(sum_{q<=exp(2a)} Lambda(q)^2/q)^(1/2) = O(a)`.

Thus the collective prime cross coefficient grows only linearly in the support radius in the primitive norm.

This is substantially sharper than the triangle-inequality envelope

`sum_q Lambda(q)/sqrt(q)`,

which is exponentially larger in `a`.

## 6. Relation to Anthropic's Montgomery-Vaughan machinery

`anthropics/zeta-23-lean` formally proves weighted Montgomery-Vaughan / Hilbert inequalities and arbitrary-coefficient Dirichlet-polynomial prime-side estimates.

Those theorems embody the same key discipline: exploit separation of logarithmic frequencies before applying absolute values.

The final `PPUpper` theorem from that project is **not** imported here as a proof, because it is formulated for a different long-`T`, smoothed Gram-matrix geometry.

In the present thin-boundary physical-space setting, source-strip localization gives the needed `l2` gain directly and exactly.

## 7. What remains

The estimate is still of the form

`|C_prime(x,n)| <= O(a) ||X||_2 ||H||_2`.

The new boundary diagonal form controls `||H||_2^2` strongly through the logarithmic cusp on sufficiently thin bands.

The unresolved factor is the old core:

> Can `||X||_2` on the relevant finite vulnerable sector be controlled **relative to the old Weil energy** `Q_a(x)` strongly enough to imply the Douglas/Ando contraction?

A global inequality

`||X||_2^2 <= C(a) Q_a(x)`

would simply be an inverse spectral-gap statement and cannot be assumed uniformly.

The next legitimate options are therefore:

1. restrict to Yoshida's finite vulnerable low-mode space and certify the relative primitive norm there;
2. prove a null-mode exclusion theorem so the low-mode inverse never actually blows up at finite support;
3. replace the primitive norm by a feature norm naturally generated by `G_a^(1/2)`.

## 8. Formalization targets

- `O-PRIME-HINGE-IBP-LEAN`: the exact double-integration identity.
- `O-PRIME-STRIP-L2-LEAN`: pairwise-disjoint source-strip square-sum bound.
- `O-PRIME-WEIGHT-LEAN`: finite weighted Cauchy step.

These are zeta-independent once the finite shift/weight family is supplied.
