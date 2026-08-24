# Odd Compact-Kernel / Discrete-Threshold Criterion

**Route ID:** `W-O`  
**Claims:** `O-DERIV-01`, `O-COMPACT-01`, `O-THRESH-01`  
**Status:** `PROVED_SYMBOLIC` as the elementary synthesis stated below, conditional only on the cited Yoshida/Suzuki form identities and their domains.  
**Novelty:** none claimed; this is a proof-engineering corollary of prior art.  
**RH status:** a cleaner sufficient/equivalent-interface architecture, **not** a proof of RH.

## 1. Literature inputs

We use two prior-art facts as recorded in `sources/SUZUKI_WEIL_V2_2026.md`.

1. Yoshida's odd-test criterion, as quoted by Suzuki: if `Q_W(v)>0` for every nonzero odd `v in C_c^∞(R)`, then RH follows.
2. Suzuki's localized screw-function representation: on `H_0^1(-a,a)`, with `D=i d/dx` and `G_a` the compressed continuous-kernel operator on the zero-mean subspace,

   `Q_W^a(v) = <G_a Dv, Dv>`.

The exact formal version should import/cite the original theorem statements rather than treat this memo as a replacement for them.

## 2. The odd derivative space

For `a>0`, define

`H^-_a = {v in H_0^1(-a,a) : v(-x) = -v(x) a.e.}`

and

`E^0_a = {u in L^2(-a,a) : u(-x)=u(x) a.e. and integral_{-a}^a u(x) dx = 0}`.

### Lemma O-DERIV-01

The operator

`D = i d/dx`

restricts to a bijection

`D : H^-_a -> E^0_a`.

### Proof

Let `v in H^-_a`.

- The weak derivative of an odd Sobolev function is even a.e., hence `Dv` is even.
- Since `v` has zero trace at both endpoints,

  `integral_{-a}^a Dv(x) dx = i(v(a)-v(-a)) = 0`.

Thus `Dv in E^0_a`.

Conversely, let `u in E^0_a` and define

`v(x) = -i integral_0^x u(t) dt`.

Because `u` is even, its primitive from zero is odd, so `v` is odd. Since

`0 = integral_{-a}^a u = 2 integral_0^a u`,

we have `v(a)=v(-a)=0`, hence `v in H_0^1(-a,a)`. Finally `Dv=u` a.e.

Injectivity follows because `Dv=0` makes `v` a.e. constant and the Dirichlet trace forces that constant to be zero.

Therefore `D` is bijective between the two stated spaces. ∎

## 3. Compact-kernel form of the odd criterion

For `v in H^-_a`, put `u=Dv in E^0_a`. Suzuki's identity gives

`Q_W^a(v) = <G_a u,u>`.

### Corollary O-COMPACT-01 — strict form

Suppose that for every `a>0` and every nonzero `u in E^0_a` lying in the derivative image of an odd compactly supported smooth test function,

`<G_a u,u> > 0`.

Then RH holds.

### Proof

Every nonzero odd `v in C_c^∞(R)` is contained in `(-a,a)` for some `a`. Its derivative image `u=Dv` is nonzero and lies in `E^0_a`. The hypothesis gives

`Q_W(v)=Q_W^a(v)=<G_a u,u> > 0`.

Yoshida's odd-test criterion then implies RH. ∎

### Closure warning

Do **not** silently replace the derivative image of `C_c^∞` by the entire `E^0_a` when making a strict-positivity statement. Density transfers nonnegativity under continuity, but strict positivity can be lost in a limit. The exact operator-domain/nondegeneracy formulation must be used if the full closed space is desired.

For certificate search, positivity on all of `E^0_a` is a stronger and cleaner sufficient condition, but it must be labeled as such.

## 4. Discrete support checkpoints

The continuum `a>0` is unnecessary for the **sufficient** odd-test criterion.

Let

`0 < a_1 < a_2 < ...`, with `a_k -> infinity`.

### Theorem O-THRESH-01

Assume that for every `k` and every nonzero odd `v in C_c^∞((-a_k,a_k))`,

`Q_W(v)>0`.

Then RH holds.

### Proof

Take any nonzero odd `v in C_c^∞(R)`. Its compact support is contained in `(-A,A)` for some finite `A`. Since `a_k -> infinity`, choose `k` with `a_k>A`. Then `v in C_c^∞((-a_k,a_k))`, so the assumed checkpoint positivity gives `Q_W(v)>0`. Yoshida's criterion now implies RH. ∎

No continuity of a lowest eigenvalue is needed for this reduction. It is simply exhaustion by nested support windows.

## 5. Arithmetic checkpoint choice

Let

`2 = q_1 < q_2 < ...`

be the increasing sequence of **distinct prime powers**. Since `q_k -> infinity`, either of the sequences

`a_k = (1/2) log q_k`

or

`a_k = log q_k`

is an unbounded checkpoint sequence and therefore is sufficient in Theorem `O-THRESH-01`.

The half-log choice is particularly natural for the diagonal explicit formula because a correlation of functions supported in `[-a,a]` can first feel a translation of length `log q` only when

`log q < 2a`.

Thus new prime-power interactions enter at the geometric thresholds

`a = (1/2) log q`.

### Endpoint convention

At exact equality `log q=2a`, compactly supported smooth/Dirichlet test functions have no positive-measure overlap with their translate by `log q`, so the new correlation term vanishes. A future formalization should state this explicitly rather than rely on a picture of touching supports.

## 6. What the reduction does and does not buy

The theorem turns

`all support radii a>0`

into

`all prime-power support thresholds a_k`.

That is a countable, arithmetically meaningful search coordinate. It does **not** make the remaining proof finite.

The unresolved statement

`Q_W(v)>0 for every odd v at every threshold k`

is still sufficient for RH and may retain essentially the whole difficulty.

Therefore `O-THRESH-01` is categorized as a **search-space coordinate theorem**, not a theorem-strength reduction by itself.

## 7. Certificate target at one checkpoint

At a fixed `a_k`, work with the compact self-adjoint integral operator `G_{a_k}` on the even zero-mean sector.

A finite certificate architecture should aim to establish a statement of the following form:

> `CERT(a_k) -> <G_{a_k}u,u> > 0` for every nonzero `u` in the target even zero-mean test space.

The certificate may contain, for example:

- a finite Galerkin block enclosing the low spectrum;
- interval-certified matrix entries/eigenvalue bounds;
- an analytic coercive estimate for the orthogonal tail;
- exact treatment of the finite prime-power terms active below `2a_k`;
- rigorous quadrature/tail bounds for the archimedean component.

The **general certificate soundness theorem** must be proved independently of any generated certificate.

## 8. The true next missing lemma

### `O-STEP-01`

Find a mechanism that proves valid certificates for **all** arithmetic thresholds, rather than separately computing indefinitely many finite cases.

Acceptable forms include:

1. an induction/update theorem from threshold `q_k` to `q_{k+1}`;
2. an eventual uniform analytic theorem plus finitely many certified base thresholds;
3. a monotone/invariant certificate quantity whose update under each new prime-power shock preserves positivity;
4. a new exact transform reducing the infinite threshold sequence to another already controlled object.

### Equivalent-strength warning

A statement of the form

`the smallest odd-sector eigenvalue is nonnegative at every threshold`

with no independent update mechanism is just the desired global positivity repackaged. Mark that `BLOCKED_EQUIVALENT`, not “one lemma from RH.”

## 9. Immediate falsification program

Before attempting `O-STEP-01`, use finite-basis numerics only to answer structural questions:

- Does the lowest odd-sector Rayleigh value appear to retain a robust positive gap?
- Does it approach zero rapidly?
- Which prime thresholds produce the largest spectral shocks?
- Are near-null vectors stable under basis enlargement and Fourier cutoff?

Any apparent negative value must be interval-certified before it is interpreted as a mathematical counterexample. Numerical near-zero values are expected to be especially dangerous.

The companion diagnostic is `verification/odd_weil_finite_basis.py`.
