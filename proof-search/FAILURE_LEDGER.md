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

`G(r)=Re ψ(1/4+ir/2)-log π`

is negative at `r=0`.

Therefore the Gamma sector alone cannot be treated as a pointwise nonnegative diagonal reservoir for prime-shift errors.

**Replacement architecture:** analyze the combined archimedean + finite-rank pole operator, or use another signed/global reference form.

## F011 — discard pole terms when building the prime graph

**Class:** `FALSE methodology / structural loss`.

The diagonal pole contribution is an exact rank-two indefinite Hermitian form, with positive and negative moment directions.

**Do not repeat:** drop the pole sector or replace it by an unsigned error without proving that the replacement preserves the intended sufficient condition.

## F012 — absolute-coupling spectral bound is automatically the right RH bridge

**Class:** `EQUIV risk / ARCH_GAP`.

The candidate condition `sup_L λ_max(E_L)<=1` for an absolute normalized coupling matrix is only a sufficient architecture. It may be false, unnecessarily strong, or encode essentially all RH difficulty.

**Policy:** keep `W-GLOBAL-01` blocked until finite exact/adversarial tests and a nontrivial mechanism support it.

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

---

# Reopening template

When reopening an item append:

- **Old blocker:**
- **New mechanism:**
- **Why it bypasses the blocker:**
- **First falsification test:**
- **Exact theorem target:**
- **Outcome:**
