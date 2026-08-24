# Odd Virial / Support-Shape Derivative

**Route ID:** `W-V`  
**Claim IDs:** `V-SCALE-01`, `V-HINGE-CANCEL-01`, `V-SIGN-FAIL-01`  
**Status:** exact symbolic derivative on smooth vectors away from arithmetic thresholds; naive universal positive-crossing claim **REJECTED by numerical diagnostic**.  
**RH status:** no proof. The route remains potentially useful only if a sign theorem can be derived specifically on an exact null eigenspace, not on arbitrary vectors.

## 1. Fixed-interval scaling

Suzuki v2 Section 4.2 uses the exact scaling

`w(t)=v(a t)` on `[-1,1]`

and defines

`q_a(w)`
` = integral_{-1}^1 integral_{-1}^1`
`   [g(a(x-y))/a] w'(x) conj(w'(y)) dx dy`.

The localized Rayleigh quotient is

`R(a,w)=q_a(w)/||w||_2^2`.

This matches the scaling independently derived in the project and gives a fixed form domain on which a support derivative can be studied.

## 2. Shape derivative away from prime thresholds

For a smooth fixed test vector `w` and a support radius `a` such that no distance `a|x-y|` crosses a prime-power hinge under an infinitesimal variation, differentiate the kernel:

`d/da [g(a r)/a]`
` = [a r g'(a r)-g(a r)]/a^2`.

Define the virial kernel

`h(t)=t g'(t)-g(t)`.

Then

`q_a'(w)`
` = (1/a^2) integral integral h(a(x-y)) w'(x)conj(w'(y)) dxdy`.

At a normalized eigenvector whose eigenvalue is `0`, the derivative of the normalization denominator does not contribute to the Feynman-Hellmann crossing form, provided the required differentiability/simple-eigenvalue hypotheses are available.

The formula must be interpreted one-sided/distributionally at arithmetic thresholds, where `g'` has jumps.

## 3. Arithmetic simplification of h

Write the historical/current screw normalization as

`g(t)=-Psi(t)` for `t>=0`,

with, between consecutive prime-power logarithms,

`Psi(t)=B(t)-t W_k+D_k`,

where

`W_k=sum_{j<=k} Lambda(q_j)/sqrt(q_j)`,

`D_k=sum_{j<=k} [Lambda(q_j)/sqrt(q_j)] log q_j`.

Then

`h(t)=t g'(t)-g(t)`
` = Psi(t)-t Psi'(t)`
` = B(t)-t B'(t)+D_k`.

### Theorem V-HINGE-CANCEL-01

Between arithmetic thresholds, the cumulative prime **slope** `W_k` cancels exactly from the support virial kernel.

The prime dependence survives only through the weighted location sum `D_k`.

At a threshold `t=log q`, the virial kernel has the corresponding one-sided jump inherited from the slope jump of `Psi`.

This is a genuine structural compression, but it is not itself a sign theorem.

## 4. What would have solved the first-null problem

Suppose `a_*` were the first odd-sector support radius at which the localized form became degenerate, and `w_*` a nonzero null vector.

A theorem of the form

`<H_{a_*} w_*, w_*> > 0`,

where `H_a` is the virial form above, would be incompatible with a downward first crossing of the lowest odd eigenvalue and could rule out `a_*`.

A weaker nonnegative crossing theorem would require additional higher-order/monotonicity information to exclude tangential crossing.

This was therefore tested before being promoted.

## 5. Numerical hostile test

Using the repository's existing diagnostic

`verification/odd_weil_finite_basis.py`,

the lowest generalized odd-sector Ritz value is strongly decreasing while positive in the well-resolved small-support regime. Representative values from the same diagnostic architecture are approximately:

- `a=0.30`: lowest Ritz value `~2.70e-1`, finite-difference derivative `~-3.36`;
- `a=0.40`: `~2.65e-2`, derivative `~-7.02e-1`;
- `a=0.50`: `~7.09e-4`, derivative `~-3.55e-2`;
- `a=0.60`: `~2.52e-6`, derivative `~-1.90e-4`.

These numbers are **NUMERICAL ONLY** and are not certified eigenvalue signs at large support. Their use here is only to falsify the optimistic heuristic that the support virial form should generically point upward on near-ground-state vectors.

### Status V-SIGN-FAIL-01

`REJECTED`: there is no numerical support for a universal positive virial/crossing form on the low odd sector.

Do not use the exact cancellation in Section 3 to claim a sign.

## 6. Surviving possibility

The route is not completely closed because an exact null vector, if one exists, satisfies additional equations that a generic near-ground-state vector does not.

A legitimate reopening would need to combine

`G_a u=0`

with the virial identity and derive a sign/cancellation **from the null equation itself**.

Without that extra mechanism, the virial route is merely another representation of the first-crossing problem.

## 7. Primary-source calibration

Suzuki v2 gives the exact fixed-domain form

`q_a(w)=double integral [g(a(x-y))/a] w'(x)conj(w'(y))`

in Section 4.2. The current project should cite that formula directly when using the support derivative.

The prime-prefix identity for `Psi` is retained from the audited August-1 dossier/current screw normalization.

## 8. Next route decision

Do not spend the next cycle trying to prove `h>=0` pointwise or as a universal quadratic kernel; direct numerical evaluation already shows `h` changes sign, and the low-mode derivative diagnostic points downward.

The active global lanes should instead be:

1. exact first-null exclusion/Feshbach reduction;
2. Suzuki's real-zero characteristic-function compact-limit bridge;
3. any new mechanism that turns the null equation into a strict contradiction.
