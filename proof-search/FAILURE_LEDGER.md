# RH Failure Ledger — Do-Not-Repeat Index

This ledger preserves failed, deflated, or precisely blocked mechanisms. It is not a ban on future work. Reopening requires a materially new mechanism that bypasses the recorded blocker.

## Codes

- `FALSE`
- `EQUIV`
- `NUMERIC`
- `TOO_WEAK`
- `ARCH_GAP`
- `FORMAL_GAP`
- `KNOWN/PRIOR_ART`

## F001 — one-sided positive Gamma/Stieltjes center mixture for Xi

**Class:** `FALSE / incompatibility`  
**Origin:** pre-August-1 GGC/Thorin route.

The attempted one-sided center-mixture representation conflicts with the required evenness/symmetry of Xi in the audited formulation.

**Do not repeat:** infer a positive one-sided mixture representation without checking symmetry exactly.

**Reopen only if:** the representation is symmetrized by a genuinely different mechanism and all measure/domain conditions are reconstructed.

## F002 — shifted-cosh branch shortcut

**Class:** `FALSE / algebraic branch error`.

A prior route mishandled the shifted `cosh`/branch structure.

**Do not repeat:** manipulate complex hyperbolic shifts as if the real-variable branch/sign structure were unchanged.

**Reopen only if:** the exact complex identity and branch conventions are written first and independently checked.

## F003 — Gamma identity used outside its positivity/domain regime

**Class:** `FALSE / domain misuse`.

A Gamma-function identity/mixture argument was applied beyond the parameter domain in which the positivity/representation statement holds.

**Do not repeat:** extend a positive-integral/Gamma identity by analytic continuation while retaining positivity without a separate theorem.

## F004 — incorrect tail-class inference

**Class:** `FALSE / asymptotic mismatch`.

An earlier probabilistic/GGC route assigned the target kernel/distribution to a tail class incompatible with its actual asymptotics.

**Do not repeat:** infer infinite-divisibility/mixture structure from a local transform identity without checking global tails.

## F005 — pole-mode tilt / positive-MGF shortcut

**Class:** `FALSE / obstruction`.

The audited pole-mode/tilt analysis obstructed a proposed positive moment-generating-function representation.

**Do not repeat:** treat a tilted kernel as a positive probability/MGF object without verifying the full sign/moment domain.

## F006 — smooth even decreasing + convex certificate

**Class:** `FALSE / no-go theorem`.

For the audited smooth even nonzero decaying kernel family, no finite tilt parameter can make the function both globally decreasing and convex on `t>0`: even smoothness gives derivative zero at the origin, and convexity plus decrease would force an incompatible shape/constancy.

**Reopen only if:** the hypotheses/certificate class are materially changed.

## F007 — first generalized Laguerre inequality is sufficient

**Class:** `FALSE / TOO_WEAK`.

Counterexample used in the August 1 audit: `p(x)=x^4-1` has a nonnegative first Laguerre expression while possessing nonreal zeros.

**Surviving statement:** the full generalized Laguerre hierarchy is relevant; one level is not enough.

**Do not repeat:** promote `L1>=0` or another fixed finite order to a real-rootedness/RH criterion.

## F008 — finite Laguerre-prefix admissibility closes RH

**Class:** `TOO_WEAK`.

The August 1 work constructed/considered strong finite-prefix admissible-kernel behavior. Finite Laguerre information does not imply the full all-order hierarchy required for real-rootedness/RH.

**Reopen only if:** a new theorem proves a genuine finite-to-all-order closure for the specific Xi class, with hypotheses verified independently.

## F009 — individual Epstein/theta-slice positivity

**Class:** `FALSE / ARCH_GAP`.

The individual-slice strategy was ruled out in the August 1 modular/Epstein analysis. Cancellation across theta scales is essential.

**Replacement architecture:** grouped/coupled theta-scale arguments preserving cancellation.

**Reopen only if:** a new grouping theorem is stated explicitly.

## F010 — Gamma multiplier as pointwise positive local energy

**Class:** `FALSE`.

In the exact diagonal Weil normalization now used, the Gamma multiplier

`G(r)=Re psi(1/4+ir/2)-log pi`

is negative at `r=0`.

Therefore the Gamma sector alone cannot be treated as a pointwise nonnegative diagonal reservoir for prime-shift errors.

**Replacement architecture:** analyze the combined exact Weil/screw operator, preserving its signed structure.

## F011 — discard pole terms when building the prime graph

**Class:** `FALSE methodology / structural loss`.

The diagonal pole contribution is an exact rank-two indefinite Hermitian form, with positive and negative moment directions. In the odd sector it reduces to one negative rank-one moment rather than disappearing.

**Do not repeat:** drop the pole sector or replace it by an unsigned error without proving that the replacement preserves the intended sufficient condition.

## F012 — absolute-coupling spectral bound is automatically the right RH bridge

**Class:** `EQUIV risk / ARCH_GAP`.

The candidate condition `sup_L lambda_max(E_L)<=1` for an absolute normalized coupling matrix is only a sufficient architecture. It may be false, unnecessarily strong, or encode essentially all RH difficulty.

**Disposition:** superseded as the primary route by the odd localized compact-kernel program. Preserve only sign-aware descendants such as `O-SHOCK-01`.

## F013 — “one spectral inequality away” means “almost solved”

**Class:** `EQUIV risk`.

A single syntactically short universal spectral inequality across all support scales can contain the whole global positivity problem.

**Do not repeat:** infer mathematical closeness from the number of named lemmas remaining.

## F014 — finite numerical positivity as RH evidence strong enough for promotion

**Class:** `NUMERIC`.

Finite test-function/bump/matrix experiments are useful for locating cancellation, counterexamples, and near-extremizers. They cannot prove global Weil positivity or RH.

**Legitimate use:** kill sufficient conditions, identify structure, or generate exact/certified theorem candidates.

## F015 — related-model agreement as independent verification

**Class:** `FALSE methodology`.

Multiple instances of related models can catch errors but remain correlated evidence.

**Policy:** use model diversity/hostile review internally, but reserve “independent review” for genuinely independent reconstruction/checking and qualified human/formal verification as appropriate.

## F016 — localized Weil operator / spectral flow presented as project novelty

**Class:** `KNOWN / PRIOR_ART`.

Suzuki's current arXiv:2606.09096v2, building on Yoshida, Bombieri, Connes–Consani and Connes–Consani–Moscovici, already supplies the localized closed Weil form, a self-adjoint operator with discrete lower-bounded spectrum, continuity of the lowest localized eigenvalue, small-support positivity, and the screw-function integral-operator realization.

**What survives:** our independent derivations are normalization checks and certificate-engineering inputs.

**Do not repeat:** present localization, lowest-eigenvalue flow, or the continuous screw-kernel operator as a new theorem.

**Reopen novelty only if:** a theorem strictly beyond the cited source is isolated and prior-art checked.

## F017 — positivity at one threshold has a uniform compact-operator gap

**Class:** `FALSE / ARCH_GAP`.

In the compact `G_a` representation, eigenvalues accumulate at zero. Positivity of `G_a` therefore does not give a uniform positive `L^2` spectral gap on the infinite-dimensional even-zero-mean sector.

**Consequence:** a small operator-norm perturbation cannot automatically propagate positivity from one threshold to the next.

**Replacement architecture:** use relative high-mode estimates, generalized eigenvalues against the inverse Laplacian, or an exact range/Schur condition rather than a fictitious compact-operator gap.

## F018 — summable birth cost of new prime shocks closes threshold induction

**Class:** `TOO_WEAK / ARCH_GAP`.

`O-SHOCK-SUM-01` proves that the negative boundary-energy coefficients at the moment successive prime-power shocks turn on are summable. This is genuine auxiliary structure.

However, increasing support also allows **all previously active shifts** to act on newly available degrees of freedom. The theorem does not control those old-shock/core-shell couplings.

**Do not repeat:** telescope only the newest-prime onset bounds and call the result a global positivity proof.

**Replacement target:** `O-SHELL-01` / `O-SHELL-CERT-01`.

## F019 — apply Anthropic's Montgomery–Vaughan inequality directly to the prime-shift operator

**Class:** `FORMAL/STRUCTURAL MISMATCH`.

The formal Montgomery–Vaughan theorem in `zeta-23-lean` controls weighted bilinear sums with **frequency-difference denominators**. The fixed-support Weil prime sector is a sum of translation correlations at frequencies/lengths `log q`.

There is currently no proved identity reducing the latter directly to the former.

**Do not repeat:** cite the existence of the Hilbert inequality as though it bounds the prime-shift operator automatically.

**Reopen only if:** an exact transform/duality step produces the required denominator structure and all hypotheses are verified.

## F020 — continuity of the localized eigenvalue prevents zero crossing

**Class:** `TOO_WEAK`.

Suzuki proves continuity of the lowest localized eigenvalue. A continuous positive function at small support can still reach zero later.

A useful continuation theorem would need quantitative **relative** control, for example a one-sided inequality of schematic form

`lambda_odd'(a) >= -C(a) lambda_odd(a)`

between arithmetic thresholds, plus correct threshold matching. No such theorem has been proved.

**Do not repeat:** use continuity alone as a positivity-propagation argument.

---

# Reopening template

When reopening an item append:

- **Old blocker:**
- **New mechanism:**
- **Why it bypasses the blocker:**
- **First falsification test:**
- **Exact theorem target:**
- **Outcome:**
