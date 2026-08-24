# Odd Mean-Transfer Limit

**Route ID:** `W-O`  
**Claim IDs:** `O-MEAN-LIMIT-01`, `O-MEAN-PREFIX-01`  
**Status:** `PROVED_SYMBOLIC` for the limit identities; positivity is `OPEN_NECESSARY`.  
**RH status:** this is one explicit low-mode necessary condition arising from the adaptive core/shell induction. It is not known here to be sufficient for RH.

## 1. The scalar that survives a thin shell

Fix `a>0`, let `b=a+delta`, and use the normalized mean carriers

`e_C=(1/(2a)) 1_[-a,a]`,

`e_S=(1/(2delta)) 1_{[-b,-a] union [a,b]}`,

with mean-transfer direction

`e_T=e_C-e_S`.

Both carriers have total integral one, so `e_T` is even and has zero mean.

As `delta->0+`, the shell carrier converges weakly to the symmetric endpoint probability measure

`nu_a=(1/2)(delta_{-a}+delta_a)`,

while the core carrier is the uniform probability measure

`mu_a=(1/(2a))1_[-a,a] dx`.

Because Suzuki's screw function `g` is continuous, the quadratic energy converges to

`M(a)=int int g(x-y) d(mu_a-nu_a)(x)d(mu_a-nu_a)(y)`.

## 2. Exact evaluation

The three pieces are

`E_mumu`
` = (1/(2a^2)) integral_0^{2a} (2a-t)g(t)dt`,

`E_munu`
` = (1/(2a)) integral_0^{2a} g(t)dt`,

and, since `g(0)=0`,

`E_nunu=(1/2)g(2a)`.

Therefore

`M(a)=E_mumu-2E_munu+E_nunu`

simplifies to

`M(a)`
` = (1/2)g(2a) - (1/(2a^2)) integral_0^{2a} t g(t)dt`.

Put `T=2a`. Then

`M(T)`
` = (1/2)g(T) - (2/T^2) integral_0^T t g(t)dt`.

In the historical screw notation `g=-Psi`,

`M(T)`
` = -(1/2)Psi(T) + (2/T^2) integral_0^T t Psi(t)dt`.

### Theorem O-MEAN-LIMIT-01

The displayed expression is the exact thin-shell limit of the mean-transfer quadratic energy.

If the odd Weil criterion is globally positive, then necessarily

`M(T)>=0`

for every `T>0` for which the limiting argument is taken. This is a necessary condition only.

## 3. Prime-prefix formula

Write

`Psi(t)=B(t)-sum_{b_q<=t} w_q(t-b_q)`,

where

`b_q=log q`,

`w_q=Lambda(q)/sqrt(q)`,

and the sum runs over distinct prime powers.

Define the purely archimedean part

`M_B(T)=-(1/2)B(T)+(2/T^2) integral_0^T tB(t)dt`.

For a fixed event `b=b_q<=T`,

`integral_b^T t(t-b)dt`
` = T^3/3 - bT^2/2 + b^3/6`.

Combining its endpoint contribution with its integrated contribution gives

`w_q [ -T/6 + b_q/2 - b_q^3/(3T^2) ]`.

Hence

`M(T)`
` = M_B(T)`
`   + sum_{b_q<=T} w_q`
`       [ -T/6 + b_q/2 - b_q^3/(3T^2) ]`.

Equivalently, with prefix moments

`W(T)=sum w_q`,

`D(T)=sum w_q b_q`,

`C_3(T)=sum w_q b_q^3`,

we have

`M(T)=M_B(T)-T W(T)/6 + D(T)/2 - C_3(T)/(3T^2)`.

### Theorem O-MEAN-PREFIX-01

The thin-shell mean-transfer condition is an exact scalar prime-prefix inequality involving only three weighted prefix moments plus the explicit archimedean background.

## 4. Sign structure of one prime event

The contribution of one event `b` is

`c_b(T)`
` = -w_b/(6T^2) [T^3-3bT^2+2b^3]`
` = -w_b/(6T^2)(T-b)(T^2-2bT-2b^2)`.

Thus a newly entered event initially contributes positively, but an old event contributes negatively once

`T/b > 1+sqrt(3)`.

Therefore positivity cannot be proved term-by-term in the prime sum. Any proof must preserve cancellation between old prime events and the archimedean background or exploit a stronger prefix identity.

## 5. Numerical reconnaissance

A private diagnostic reconstructed `B` from the exact curvature

`B''(t)=e^(t/2)+e^(-t/2)-e^(-t/2)/(1-e^(-2t))`

and evaluated the prefix formula over prime powers through approximately

`T=15` (`e^T` about `3.3e6`).

The sampled values remained positive. Among sampled prime-power endpoints, the smallest observed value was approximately

`0.0117`.

**Status: NUMERICAL ONLY.**

This scan is not interval-certified, does not cover all `T`, and does not justify promoting `M(T)>=0` to a theorem.

## 6. Why this scalar is not automatically RH-equivalent

The transform

`Psi -> -(1/2)Psi(T)+(2/T^2)integral_0^T tPsi(t)dt`

is not order-reflecting on arbitrary functions. For example power-law test functions already show that the sign of the transform and the sign of the original function need not agree.

Therefore even a proof of `M(T)>=0` for every `T` would need a separate implication theorem before it could be described as an RH proof.

Its current role is narrower: it is the low-mode scalar needed by the adaptive support-induction architecture.

## 7. Piecewise-linear interpretation

The finite-`delta` mean-transfer derivative corresponds to an odd piecewise-linear boundary-hat test in `H_0^1(-b,b)`:

- slope `1/(2a)` on `0<x<a`;
- slope `-1/(2delta)` on `a<x<b`;
- peak value `1/2` at `x=a`;
- zero at `x=0` and `x=b`;
- odd extension to the negative side.

Thus `M(T)` is the limiting Weil energy of a canonical odd boundary-layer hat family.

## 8. Next attacks

1. Search prior art for this exact boundary-hat scalar.
2. Determine whether `M(T)>=0` is unconditionally provable from known explicit-prime estimates.
3. If not, identify its exact relation to the Suzuki/Fenchel prefix margins.
4. Do not confuse positivity of this one test family with global odd Weil positivity.
