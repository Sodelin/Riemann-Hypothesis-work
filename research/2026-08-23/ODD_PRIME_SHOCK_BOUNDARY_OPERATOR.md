# Odd Prime-Shock Boundary Operator

**Route ID:** `W-O`  
**Claim ID:** `O-SHOCK-01`  
**Status:** `PROVED_SYMBOLIC`; standard compact-operator / fourth-order ODE ingredients should be independently reconstructed and formalized before promotion beyond this project.  
**Novelty:** no novelty claim; the Volterra/cantilever spectral calculation is classical operator theory, specialized here to the odd Weil prime-shock geometry.  
**RH status:** auxiliary sign-aware estimate only; not an RH proof.

## 1. Setup

Let `f in H_0^1(-a,a)` be odd (real or complex), and consider one prime-power translation length

`c = log q`,

with `q=p^m` and `0<c<2a`.

Put

`ell = 2a-c > 0`

and

`w_q = Lambda(q)/sqrt(q) > 0`.

The diagonal explicit formula contributes

`P_q(f) = -2 w_q Re int f(x) conj(f(x-c)) dx`.

Because both factors are supported in `[-a,a]`, the integral is over

`x in [-a+c,a]`.

## 2. Boundary-layer reflection identity

Write

`x=a-s`, `0<=s<=ell`,

and define the right-boundary profile

`h(s)=f(a-s)`.

Then

`x-c = -a+(ell-s)`.

Oddness gives

`f(-a+(ell-s)) = -f(a-ell+s) = -h(ell-s)`.

Therefore

`int f(x) conj(f(x-c)) dx`

`= - int_0^ell h(s) conj(h(ell-s)) ds`.

Let `J_ell` be reflection on `L^2(0,ell)`:

`(J_ell h)(s)=h(ell-s)`.

Then

`P_q(f)=2 w_q <h,J_ell h>`.

Since `h(0)=f(a)=0`, write `h=V_ell g`, where

`g=h'`

and

`(V_ell g)(s)=int_0^s g(t)dt`.

Hence

`P_q(f)=2 w_q <g,T_ell g>`

with the self-adjoint compact operator

`T_ell := V_ell^* J_ell V_ell`.

Using

`J_ell V_ell J_ell = V_ell^*`,

we obtain the simpler identity

`T_ell = J_ell V_ell^2`.

Its integral kernel is

`K_ell(s,t)=(ell-s-t)_+`.

This is the exact universal operator governing the birth of **every** prime-power shock in the odd sector; arithmetic enters only through `w_q` and the overlap length `ell`.

## 3. Scaling

Under the unitary rescaling

`(U_ell phi)(s)=ell^(-1/2) phi(s/ell)`,

one has

`U_ell^{-1} T_ell U_ell = ell^2 T_1`.

Therefore the spectrum of `T_ell` is `ell^2` times the spectrum of `T_1`.

## 4. Exact spectrum of `T_1`

Consider

`T=T_1=J V^2`

on `L^2(0,1)`.

Let

`T phi = lambda phi`, `lambda != 0`.

The kernel formula gives

`(T phi)(x)=int_0^(1-x) (1-x-y) phi(y)dy`.

Differentiate twice:

`lambda phi''(x)=phi(1-x)`.

Reflecting this relation and differentiating again yields

`lambda^2 phi''''(x)=phi(x)`.

The kernel also gives the boundary conditions

`phi(1)=phi'(1)=0`,

and the differentiated equation gives

`phi''(0)=phi'''(0)=0`.

Write

`beta = |lambda|^(-1/2)`.

The fourth-order equation is

`phi''''=beta^4 phi`,

so

`phi(x)=A(cosh(beta x)+cos(beta x))`
`      +B(sinh(beta x)+sin(beta x))`.

The two conditions at `x=1` have a nonzero solution exactly when

`cos(beta) cosh(beta) = -1`.

Let

`0<beta_1<beta_2<...`

be the positive roots of this equation.

To recover the sign of `lambda`, use the undifferentiated reflected relation. At a root,

`|sin beta|=tanh beta`,

and evaluation at the endpoint gives

`lambda = sign(sin beta)/beta^2`.

The roots alternate between intervals on which `sin beta` alternates sign, beginning with `sin(beta_1)>0`. Thus

`boxed(lambda_n(T)=(-1)^(n+1)/beta_n^2)`.

Numerically,

`beta_1 = 1.875104068711961...`,
`beta_2 = 4.694091132974175...`,
`beta_3 = 7.854757438237613...`,

and therefore

`1/beta_1^2 = 0.284412871854955...`,
`1/beta_2^2 = 0.0453833934431935...`,
`1/beta_3^2 = 0.0162081871848722...`.

In particular,

`T_ell >= -(ell^2/beta_2^2) I`.

This is much sharper on the negative side than the unsigned operator-norm bound, whose constant is `1/beta_1^2`.

## 5. Prime-shock lower bound

From the exact representation,

`P_q(f) >= -2 w_q ell^2/beta_2^2 * ||g||^2_{L^2(0,ell)}`.

Now

`g(s)=-f'(a-s)`.

Because `f` is odd, `|f'|^2` is even. Therefore the derivative energy in the right boundary layer is at most half of the total derivative energy:

`||g||^2 <= (1/2)||f'||^2_{L^2(-a,a)}`.

Hence

`boxed(P_q(f) >= - [Lambda(q)/sqrt(q)] * ell^2/beta_2^2 * ||f'||_2^2)`

with

`ell = 2a-log q`.

This is a **sign-aware universal lower bound** for one active prime-power term on the odd sector.

## 6. Consecutive prime-power thresholds

Let `q_k<q_{k+1}` be consecutive distinct prime powers and set

`a_{k+1}=(1/2)log q_{k+1}`.

At this support radius, the previous prime power `q_k` has overlap length

`ell_k = log(q_{k+1}/q_k)`.

Thus its negative onset is bounded by

`P_{q_k}(f)`
`>= - c_k ||f'||_2^2`,

where

`c_k = [Lambda(q_k)/sqrt(q_k)]`
`      * [log(q_{k+1}/q_k)]^2 / beta_2^2`.

The coefficient is small when consecutive prime powers are close multiplicatively.

## 7. Why this is useful but not enough

The theorem shows that a new arithmetic shock turns on **quadratically** in its boundary-overlap length and that its dangerous spectral constant is the second cantilever singular value, not the unsigned first singular value.

However, this does **not** prove a threshold induction:

1. when the support interval grows, the test-function space gains new boundary degrees of freedom;
2. all previously active prime translations can couple those new degrees of freedom to the old core;
3. the compact screw-kernel operator has eigenvalues accumulating at zero, so there is no uniform positive `||f'||_2` margin that a small operator-norm perturbation can automatically preserve.

Therefore the naive argument

`positive at q_k + small new shock => positive at q_{k+1}`

is invalid without a **relative spectral/tail theorem**.

This obstruction should be treated as design information, not as a reason to discard the boundary-operator identity.

## 8. New target created by the lemma

### `O-RELTAIL-01`

Find a relative high-mode theorem showing that, in a basis adapted to the compact screw-kernel form, the positive archimedean tail dominates the **combined signed prime-shock tail** uniformly enough that only finitely many low modes require a threshold certificate.

A valid theorem must retain the oscillatory/sign structure of the prime shocks. Summing the absolute lower bounds in Section 5 over all active prime powers is expected to be far too crude.

### `O-SHELL-01`

For consecutive thresholds, derive an exact core/shell Schur decomposition in which all couplings created by interval enlargement are represented explicitly. Then test whether `O-SHOCK-01` supplies a useful bound on the shell block or only on one newly active edge.

## 9. Formalization targets

The lemma decomposes into unusually clean formal pieces:

1. odd support-shift reflection identity;
2. `J V J = V*` and `T=J V^2`;
3. unitary scaling `T_ell ~ ell^2 T_1`;
4. fourth-order eigen-equation and boundary conditions;
5. characteristic equation `cos beta cosh beta=-1`;
6. sign formula for eigenvalues;
7. the prime-shock lower bound.

These are independent of RH and are good candidates for proof-assistant verification.
