# Odd Adaptive Shell Mesh

**Route ID:** `W-O`  
**Claim IDs:** `O-MESH-01`, `O-SHELL-ZM-01`  
**Status:** `PROVED_SYMBOLIC` modulo the already imported Suzuki local expansion/Fourier formula.  
**RH status:** this removes the artificial prime-gap obstruction from the zero-mean shell block; it does not yet prove the mean-transfer/core-coupling step.

## 1. Correction to the previous checkpoint

The earlier threshold-only organization used consecutive distinct prime powers

`a_k = (1/2) log q_k`

as the only support radii. That was convenient because the von-Mangoldt hinge set is constant between consecutive thresholds, but it introduced an unnecessary dependence on worst-case prime gaps.

Yoshida's odd criterion only needs positivity on a **cofinal unbounded family of support radii**. Therefore we are free to insert arbitrarily many artificial support radii inside any prime-free interval.

The correct strategy is:

1. include every arithmetic threshold `a_q=(1/2)log q`;
2. subdivide every interval between consecutive thresholds as finely as needed;
3. make every individual shell step small enough that the universal logarithmic cusp dominates the smooth opposite-shell curvature.

No prime-gap theorem is required for this subdivision.

## 2. One arithmetic-free shell step

Fix `0<a<b`, put `delta=b-a`, and assume

- `delta < log 2`;
- the open distance interval `(2a,2b)` contains no `log q` for a prime power `q`.

Endpoints may coincide with arithmetic thresholds.

Let

`S=(-b,-a) union (a,b)`

and let `u` be even, supported in `S`, with zero shell mean. By evenness, the mean on each connected shell is zero.

Write the right-shell profile

`h(s)=u(a+s)`, `0<s<delta`,

and its primitive

`p(s)=integral_0^s h(t)dt`.

Then

`p(0)=p(delta)=0`.

## 3. Exact cancellation of all prime hinges in the shell diagonal block

Suzuki's screw kernel can be written

`g(t)=-B(|t|)+sum_q w_q (|t|-log q)_+`,

`w_q=Lambda(q)/sqrt(q)`.

### Same-side interactions

Two points in the same connected shell are at distance `<delta<log2`, so no prime-power hinge is active.

### Opposite-shell interactions

Their distance ranges in `[2a,2b]`. Because there is no arithmetic threshold in the open interval, the active hinge set is constant there. Hence the total von-Mangoldt contribution is an affine function

`alpha + beta(s+t)`

of the two right-shell coordinates.

The quadratic form of every affine function against `h(s)conj(h(t))` vanishes because

`integral h = 0`.

Therefore the complete prime-power contribution to the zero-mean shell diagonal block is **exactly zero**.

## 4. Same-side cusp lower bound

Suzuki's local expansion at the origin separates the universal singular piece

`(1/2)|t|log|t| + A0|t|`

from an even `C^2` remainder. The Fourier calculation used in the previous shell note gives, for one connected shell,

`Q_same(h)`
`>= [log(1/(2*pi*delta)) - 1/pi - R0(delta) delta] ||p||_2^2`,

where `R0(delta)` is any valid bound for the second derivative of the smooth local remainder on `|t|<=delta`.

The two connected shells contribute twice this amount.

## 5. Opposite-shell curvature bound without removing a first moment

The arithmetic hinges have vanished, so the opposite-shell kernel is simply

`-B(2a+s+t)`.

Integrating by parts once in each shell variable gives

`Q_cross(h)`
`= - integral_0^delta integral_0^delta`
`    B''(2a+s+t) p(s)conj(p(t)) ds dt`.

The historical dossier already records the exact smooth curvature

`B''(t)=A(t)`

with

`A(t)=e^(t/2)+e^(-t/2)-e^(-t/2)/(1-e^(-2t))`.

For `t>t_c`, `A(t)>0`; moreover the last term is positive, so

`A(t) < e^(t/2)+e^(-t/2)`.

Thus, for sufficiently large `a`,

`M2(a,b):=sup_{2a<=t<=2b} |B''(t)|`

may be bounded by

`M2(a,b) <= e^b+e^(-a)`

(and any sharper monotonicity bound can be substituted).

Using

`(integral |p|)^2 <= delta ||p||_2^2`,

one opposite-shell cross term obeys

`Q_cross(h) >= -M2(a,b) delta ||p||_2^2`.

The full even shell has the two conjugate cross blocks, so combining both same-side blocks and both cross blocks yields

`Q_shell(u)`
`>= 2 [ log(1/(2*pi*delta)) - 1/pi`
`       - R0(delta)delta - M2(a,b)delta ] ||p||_2^2`.

### Theorem O-SHELL-ZM-01

If

`log(1/(2*pi*delta)) - 1/pi`
`> delta [R0(delta)+M2(a,b)]`,

then the localized screw-kernel form is strictly positive on every nonzero even zero-mean fluctuation supported in the new symmetric shell.

No first-moment deletion is required.

## 6. An explicit asymptotically safe step scale

For example, for large `b`, choose each artificial step so that

`delta <= e^(-b)/(1+b)^2`.

Then

`M2(a,b) delta`
`<= (e^b+e^(-a)) e^(-b)/(1+b)^2`
`= O((1+b)^(-2))`.

Also `R0(delta)delta ->0`, while

`log(1/delta) >= b + 2log(1+b)`.

Therefore the left side tends to `+infinity` and the curvature error tends to zero.

Hence all sufficiently late steps satisfying this mesh bound have a strictly positive zero-mean shell-fluctuation block.

## 7. Construction of a cofinal arithmetic-adapted mesh

Let

`T={ (1/2)log q : q is a distinct prime power }`.

`T` is locally finite and unbounded.

Between two consecutive points of `T`, insert a finite partition so that every subinterval `(a,b)` satisfies

`b-a <= e^(-b)/(1+b)^2`

(and any finite number of earlier exceptional intervals may be subdivided further by direct computation/certification).

Include every point of `T` itself as a mesh point.

The resulting ordered mesh

`0<a_1<a_2<...`, `a_n->infinity`,

has these properties:

1. every open doubled interval `(2a_n,2a_{n+1})` contains no prime-power logarithm;
2. every sufficiently late step satisfies `O-SHELL-ZM-01`;
3. the mesh is cofinal, so positivity at every mesh radius is sufficient for the global odd criterion.

### Theorem O-MESH-01

The zero-mean shell-fluctuation sector creates **no asymptotic arithmetic obstruction** to a support-induction proof: there exists a cofinal support mesh, adapted to every prime threshold, on which that infinite-dimensional diagonal shell block is unconditionally strictly positive for all sufficiently late steps.

## 8. What remains after this correction

The earlier `ODD_SHELL_EVENTUAL_FINITE_VULNERABILITY.md` used consecutive-threshold widths and therefore left a first-moment direction unresolved under only the Baker-Harman-Pintz exponent. That restriction is now superseded for the induction architecture.

On the adaptive mesh, the new sector

`N_{a,b}=E_S^0 direct_sum span{e_T}`

has:

- an infinite-dimensional zero-mean shell block that is eventually positive by `O-SHELL-ZM-01`;
- one scalar mean-transfer direction `e_T`;
- a coupling functional between that scalar and the positive shell block.

Thus the intrinsic new-shell diagonal vulnerability has been reduced from two scalar directions to **one scalar mean-transfer degree of freedom** plus its factorization into the shell energy space.

The still harder problem is the old-core/new-sector block factorization from `O-FACTOR-01`.

## 9. Why this matters

This correction is methodological as well as mathematical.

The threshold-only discretization accidentally converted a freely refinable support parameter into a prime-gap problem. Once the endpoint criterion is remembered, that obstruction disappears: support radii are a proof-engineering choice, not arithmetic data.

This is exactly the kind of false wall the proof-attack framework is intended to expose.

## 10. Formal targets

- `O-MESH-LEAN`: construct/cofinalize an abstract locally-finite threshold-adapted mesh.
- `O-SHELL-AFFINE-LEAN`: prove affine hinge cancellation under zero shell mean.
- `O-SHELL-CURV-LEAN`: prove the two-integration curvature estimate.
- `O-SHELL-ZM-LEAN`: combine the local cusp lower bound and curvature estimate.
