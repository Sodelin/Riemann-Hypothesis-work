# RH Approach Registry

Last structural update: 2026-08-23/24.

This is the canonical index of mechanism families. New research should update a row rather than opening an unnamed duplicate route.

## Canonical route table

| ID | Family | Exact target | Status | Main obstacle | Next action / reopen condition |
|---|---|---|---|---|---|
| W | Weil / explicit-formula positivity | Reach the standard Weil criterion through a mechanism strictly weaker/more structured than global positivity itself | `ACTIVE` | The endpoint is RH-equivalent | Work through the odd localized certificate route below |
| W-O | Odd localized screw-kernel route | Prove `Q_W(v)>0` for every nonzero odd compactly supported smooth `v`, using compact `G_a` certificates | `ACTIVE_PRIMARY` | Need an all-support mechanism, not infinitely many unrelated finite checks | Develop `O-SHELL-01`, `O-RELTAIL-01`, or a relative eigenvalue-flow theorem |
| W-O-SHOCK | Odd prime-shock boundary operator | Use exact universal shock spectrum and summable onset costs inside a threshold update theorem | `PROVED_AUX / ACTIVE_INPUT` | Controls birth of a new shock but not reorganization of all old couplings when the domain expands | Derive exact core/shell block and relative-tail estimates |
| W-O-FLOW | Relative odd lowest-eigenvalue flow | Establish a differential/one-sided estimate preventing the localized odd eigenvalue from crossing zero | `CONJECTURE / BLOCKED_MECHANISM` | No shape derivative bound relative to the eigenvalue has been proved; continuity alone is prior art | Derive a fixed-domain shape formula and attack the boundary/arithmetic term; kill if it reduces to positivity itself |
| W-SCHUR | Fixed-support finite-bad-sector / Schur certificate | Convert a rigorous finite spectral enclosure plus complement bound into full fixed-support positivity | `PROVED_AUX` as abstract certificate semantics | Producing rigorous data and globalizing over support remain open | Reuse as checker architecture, especially after parity reduction |
| W-A | Raw prime-shift block/operator route | Absolute/local block domination of prime translations | `SUPERSEDED_AS_PRIMARY` | Gamma/pole are not separately positive; absolute domination loses decisive cancellation | Reopen only if a sharper signed block theorem bypasses the recorded failure |
| S | Suzuki/Yoshida localized operator theory | Use current v2 localized Weil/screw operator and odd criterion as trusted substrate | `KNOWN / PRIOR_ART` | It supplies the interface, not global positivity | Do not claim rediscovery; integrate exact theorem statements and build beyond them |
| T | Generalized Laguerre / tilted autocorrelation | Prove full hierarchy/all-tilt positive-definite family | `BLOCKED_EQUIVALENT` | Full family is equivalent to RH; finite prefixes insufficient | Reopen only with a new Gram/SOS/closure mechanism |
| T-W | Tilt/Laguerre ↔ Weil bridge | Explicit positivity-preserving transform transferring a genuinely easier estimate | `ACTIVE_LOW_COST` | No transform with leverage currently known | Search only exact transforms; kill invertible repackagings with no new monotonicity |
| E | Epstein/theta regrouping | Cross-scale cancellation theorem proving a global sign | `BLOCKED_NO_MECHANISM` | Individual slices fail; only coupled RH-strength compensation survived August 1 | Reopen only with new grouping/cancellation theorem |
| F | Fenchel / prime-shock barriers | Uniformly prove all RH-equivalent prefix margins through a weaker analytic mechanism | `BLOCKED_EQUIVALENT` | All-prefix nonnegativity is itself an RH endpoint | Use as diagnostics/counterexample detector only unless a weaker update law appears |
| D | Direct disproof certificate | Certified nontrivial zeta zero off the critical line | `ACTIVE_LOW_COST` | No candidate known | Any candidate must receive interval/formal certification immediately |

---

# W-O — primary odd localized route

## Prior-art substrate

Suzuki v2 records Yoshida's theorem that strict positivity of the Weil form for every nonzero odd `C_c^∞` test function implies RH. Suzuki also realizes the localized Weil form through the continuous screw-function operator `G_a` and the derivative map `D=i d/dx`.

See:

- `sources/SUZUKI_WEIL_V2_2026.md`
- `research/2026-08-23/ODD_COMPACT_THRESHOLD_CRITERION.md`

## Project-derived coordinate reduction

For each `a`, odd `H_0^1(-a,a)` functions map bijectively under `D` to even zero-mean `L^2(-a,a)` functions. Therefore the odd-test problem can be studied as positivity of the compact `G_a` form on one parity/mean sector.

It is sufficient to establish the odd criterion on any unbounded sequence of support radii. The natural arithmetic checkpoints are

`a_k=(1/2)log q_k`,

where `q_k` runs over distinct prime powers, because the diagonal correlation for shift `log q` turns on at `2a=log q`.

This is a search-coordinate theorem, not a reduction in conjecture strength.

## Exact new auxiliary mechanism

`O-SHOCK-01` shows that a newly active prime-power term on the odd sector is governed by the universal boundary operator

`T_ell=J_ell V_ell^2`

with eigenvalues

`(-1)^(n+1) ell^2/beta_n^2`,

where `cos beta_n cosh beta_n=-1`.

The dangerous negative constant is `1/beta_2^2≈0.04538339344`, much smaller than the unsigned operator norm constant `1/beta_1^2≈0.28441287185`.

`O-SHOCK-SUM-01` further shows that the negative **onset** coefficients at consecutive prime-power thresholds are summable using any standard prime-gap exponent `<3/4`.

## Main obstacle revealed

The summable onset theorem does **not** give threshold induction. Expanding the support interval exposes new vectors to every previously active shift. In the compact `G_a` picture, positive eigenvalues accumulate at zero, so positivity has no uniform `L^2` spectral gap that a small operator-norm perturbation automatically preserves.

The main target is therefore the **support-enlargement coupling**, not simply the appearance of the next prime.

## Active theorem cells

### `O-SHELL-01`

Derive an exact decomposition of the even-zero-mean space at `a_{k+1}` into:

- old zero-mean core;
- new zero-mean symmetric shells;
- one scalar mean-transfer direction.

Write the exact `G_{a_{k+1}}` block form.

### `O-SHELL-CERT-01`

Find a generalized Schur/range condition that uses old-core positivity without assuming an unavailable uniform gap.

### `O-RELTAIL-01`

Prove that high spectral modes are protected by the positive archimedean logarithmic singularity while the combined signed arithmetic shock tail is lower order in the correct relative norm.

### `O-FLOW-01`

Alternative: prove, piecewise between arithmetic thresholds, a bound of the schematic form

`lambda_odd'(a) >= -C(a) lambda_odd(a)`

with locally integrable `C` and correct threshold matching. Starting from known small-support positivity, Gronwall would prevent a finite zero crossing and Yoshida's odd criterion would imply RH.

This is a real theorem-strength target. Do not assume it is true.

## Falsification tests

- compute exact/interval low-dimensional models near prime thresholds;
- search for a candidate vector violating any proposed shell inequality;
- check whether a proposed relative estimate would also force positivity for a deliberately altered false screw kernel;
- separate continuity from quantitative relative control;
- reject any update law whose hypothesis already says the next threshold is positive.

---

# W-SCHUR — certificate semantics

The project has a standard fixed-support Schur theorem in

`research/2026-08-23/FIXED_L_SCHUR_CERTIFICATE.md`.

It remains useful as a soundness layer for finite data, but Suzuki/Connes–Consani localized operator theory is now the preferred prior-art substrate. No novelty is assigned to merely having a localized spectral split.

---

# W-A — raw block route

The original prime-shift graph picture remains an exact visualization of the diagonal prime sector. It is no longer the primary architecture because:

- Gamma multiplier changes sign;
- pole sector is indefinite;
- finite-basis diagnostics show extreme cancellation;
- absolute coupling bounds are structurally too strong;
- Suzuki's continuous-kernel localization gives a cleaner global fixed-support object.

The sign-aware boundary-shock lemma survives as a useful descendant of this route.

---

# S — source status

Suzuki's current v2 should be treated as prior-art infrastructure, not as a route requiring rediscovery. In particular, localized self-adjoint operators, continuity of the lowest eigenvalue, small-support positivity, and the screw-kernel representation are not project novelty.

The current project question is what can be proved **beyond** that substrate by combining parity restriction, exact threshold geometry, formal explicit-formula infrastructure, and certificate search.

---

# T / T-W / E / F

These retain the dispositions from the August 1 dossier:

- the full Laguerre/tilt family is a valid RH-equivalent endpoint;
- finite hierarchy information is insufficient;
- individual theta slices do not have the needed positivity;
- Fenchel/all-prefix positivity is an exact diagnostic endpoint but remains global;
- an explicit positivity-preserving bridge can reopen cross-route work only if it transfers genuinely easier information rather than notation.

---

# D — disproof lane

A single rigorously certified nontrivial zero with real part different from `1/2` disproves RH. Numerical searches are witness searches only; absence of a witness below any finite height does not count as proof evidence.

---

# Duplicate-route rule

Before opening a new RH route, answer:

1. Which row is it closest to?
2. What new mathematical information does it preserve?
3. What recorded blocker does it bypass?
4. What is the first exact falsification test?

Without concrete answers to 2–3, treat it as a wording variant rather than a new proof architecture.
