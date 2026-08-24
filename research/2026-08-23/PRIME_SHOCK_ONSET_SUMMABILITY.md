# Summability of Odd Prime-Shock Onset Costs

**Claim ID:** `O-SHOCK-SUM-01`  
**Depends on:** `O-SHOCK-01`  
**Status:** `PROVED_SYMBOLIC` given any standard unconditional next-prime bound with exponent `theta<3/4`.  
**Novelty:** no novelty claim; elementary consequence of the boundary-shock lemma plus classical prime-gap estimates.  
**RH status:** structural auxiliary theorem only.

## 1. Onset coefficient

Let

`q_1<q_2<...`

be the increasing sequence of distinct prime powers.

At the next support threshold

`a_{k+1}=(1/2)log q_{k+1}`,

the previous prime power `q_k` has boundary-overlap length

`ell_k = log(q_{k+1}/q_k)`.

By `O-SHOCK-01`, its dangerous odd-sector contribution satisfies

`P_{q_k}(f) >= -c_k ||f'||_2^2`,

where

`c_k = [Lambda(q_k)/sqrt(q_k)]`
`      * [log(q_{k+1}/q_k)]^2 / beta_2^2`,

and `beta_2=4.6940911329...` is the second positive root of

`cos beta cosh beta=-1`.

## 2. General summability theorem

### Theorem

Assume that for all sufficiently large `x`, there is a prime in

`(x, x+C x^theta]`

for some constants `C>0` and

`theta<3/4`.

Then

`sum_k c_k < infinity`.

### Proof

Because every prime is a prime power, the next distinct prime power after `q_k` occurs no later than the next prime after `q_k`. Hence, for all sufficiently large `k`,

`q_{k+1}-q_k <= C q_k^theta`.

Using `log(1+y)<=y` for `y>=0`,

`log(q_{k+1}/q_k)`
`= log(1+(q_{k+1}-q_k)/q_k)`
`<= C q_k^(theta-1)`.

Also

`Lambda(q_k) <= log q_k`.

Therefore

`c_k`
`<= (C^2/beta_2^2)`
`   (log q_k) q_k^(-1/2+2theta-2)`

`= (C^2/beta_2^2)`
`   (log q_k) q_k^(2theta-5/2)`.

Since the `q_k` form a subset of the positive integers,

`sum_k (log q_k) q_k^(2theta-5/2)`
`<= sum_{n>=2} (log n)n^(2theta-5/2)`.

The latter converges precisely when

`2theta-5/2 < -1`,

i.e.

`theta<3/4`.

The finitely many initial terms do not affect convergence. ∎

## 3. Unconditional applicability

Classical prime-in-short-interval theorems give an exponent strictly below `3/4` (for example the Baker–Harman–Pintz `0.525` scale; later work also studies/improves the lower-bound short-interval exponent).

Thus the hypothesis required above is far weaker than RH and is available unconditionally.

The theorem should cite the precise prime-gap source/version chosen in any manuscript or formal development. The convergence argument itself only needs **some** proved exponent `<3/4`.

## 4. Meaning

The result separates two phenomena.

### Summable phenomenon

The negative boundary-energy cost at the **moment each new prime-power shock turns on** has finite total mass across all thresholds.

### Still-uncontrolled phenomenon

When the interval grows from `a_k` to `a_{k+1}`, all previously active prime-shift operators can interact with the newly available boundary degrees of freedom. `O-SHOCK-SUM-01` does not control those old-shock/core-shell couplings.

Therefore the theorem does **not** yield a telescoping proof of positivity.

## 5. Why the obvious induction still fails

A tempting argument would be

`positive at threshold k`
`+ summably small new-shock cost`
`=> positive at threshold k+1`.

This is invalid for two reasons.

1. The support space itself expands; the new vectors are not perturbations of vectors in the old space.
2. In the compact `G_a` representation, positive eigenvalues can accumulate at zero, so positivity does not furnish a uniform spectral gap that an operator-norm perturbation automatically preserves.

This is now a recorded no-shortcut constraint.

## 6. Refined missing theorem

The remaining step should target the **support-enlargement coupling**, not the mere creation of new prime shocks.

### `O-SHELL-01`

For consecutive thresholds, decompose the even-zero-mean derivative space on `(-a_{k+1},a_{k+1})` into an old-core component, a finite-dimensional mean-correction sector, and new symmetric boundary shells. Derive the exact block form of `G_{a_{k+1}}` relative to this decomposition.

### `O-SHELL-CERT-01`

Find a sign-aware Schur/relative-tail condition under which positivity of the old core plus explicit shell inequalities implies positivity at the next threshold.

`O-SHOCK-01` and `O-SHOCK-SUM-01` should enter only where their hypotheses match the shell block. They must not be used to replace all older arithmetic couplings by absolute values.
