# Lean Gap Graph for RH

**Cycle:** 2026-08-23  
**Primary track:** Weil positivity (`W`)  
**Secondary track:** Laguerre / tilted autocorrelation (`T`)

This file is a map of proof obligations, not a claim that the obligations are easy. Its purpose is to distinguish **bounded formalization gaps** from **conjecture-strength mathematical gaps**.

## 0. The target

Let `RH` denote Mathlib's standard `RiemannHypothesis` statement for `riemannZeta`.

The project succeeds only if a complete implication chain reaches that statement (or an explicitly proved equivalent formulation) with no unproved hypotheses left in the chain.

## Track W — Weil positivity

### W0 — Canonical RH target

**Statement:** use Mathlib's `RiemannHypothesis` rather than inventing a private surrogate.

**Status:** `UPSTREAM_LEAN`.

**Reason:** `anthropics/zeta-23-lean/Zeta23/Statement.lean` already connects its strip-zero definition directly to Mathlib's `RiemannHypothesis` through `RH_implies_on_line`.

**Next check:** when local Lean work begins, pin the exact Mathlib revision and confirm the target declaration/type.

---

### W1 — Zeta-zero and explicit-formula seam

**Statement:** import or adapt the existing formal objects:

- `IsNontrivialZero`;
- analytic multiplicity `zeroMult`;
- zero configurations and Weil pairing `Z.W`;
- compactly supported `C^2` test functions;
- the literature Weil explicit formula `EF_lit`;
- the convolution test `weilTest f g = f ⋆ g̃`;
- `paperFT_weilTest`;
- the bridge from the literature formula to the paper-form bilinear identity.

**Status:** `UPSTREAM_LEAN`.

**Evidence:** `anthropics/zeta-23-lean` provides a sorry-free formalization. `Zeta23/ExplicitFormula.lean` explicitly defines the literature RHS, including

- pole terms `h(i/2)+h(-i/2)`;
- prime-power terms involving `k(log n)+k(-log n)`;
- the Gamma integral;
- and the Fourier/convolution normalization.

**What this removes:** rebuilding the entire explicit-formula analytic foundation from scratch.

**What it does not remove:** the positivity theorem required for RH.

---

### W-NORM-01 — Pin our exact Weil quadratic form

**Goal:** define a local quadratic form `Q(f)` in exactly the same normalization as the imported explicit formula, preferably as the diagonal `Z.W f f` or an equivalent real-valued form, with all Fourier signs and `2π` factors proved rather than inferred.

**Status:** `LEAN_TARGET`.

**Required outputs:**

1. exact Lean definition;
2. theorem identifying it with the zero-side sum;
3. theorem identifying it with the prime/Gamma/pole side for the chosen test class;
4. proof that `Q(f)` is real under the required symmetry/diagonal hypotheses.

**Failure mode to avoid:** switching between the classical Weil criterion's preferred test-function notation and `Zeta23`'s paper Fourier transform without a proved dictionary.

---

### W-CRIT-01 — Bidirectional Weil criterion interface

**Schematic mathematical target:** for the finalized admissible test class `A`,

`RH ↔ ∀ f ∈ A, Q(f) ≥ 0`.

The exact formulation must wait for `W-NORM-01`; this line is deliberately schematic.

**Status:** `LEAN_TARGET` / `OPEN_EQUIVALENT` as a whole.

Split it into two obligations:

#### W-CRIT-FWD — RH implies positivity

Under RH, the zero-side Weil form should reduce to a nonnegative sum/integral structure for diagonal tests.

**Status:** `LEAN_TARGET`.

This is expected to be a bounded formalization problem once the exact zero-side convention is pinned, but it is not marked proved until compiled.

#### W-CRIT-REV — positivity implies RH

Assume an off-line nontrivial zero. Construct or approximate an admissible test function whose zero-side quadratic form detects it with the wrong sign.

**Status:** `BLOCKED` pending a precise separation/interpolation theorem in the selected test class.

**Named missing theorem:** an admissible-test separation lemma strong enough to isolate an off-critical-line symmetric zero configuration while controlling the remaining zeros and preserving the test-class hypotheses.

This is a good example of an interstitial gap: it is much smaller and more explicit than “prove RH,” even though it may require serious complex/harmonic analysis to formalize.

---

## Abstract finite-block layer

These lemmas are intentionally independent of zeta. They can be proved and formalized without assuming the Riemann-specific domination estimate.

### W-BLOCK-01 — finite block-Schur positivity

Let `I` be finite. For each `i ∈ I`, let `H_i` be a normed/Hilbert space and let

`q_i(x_i) ≥ c_i ||x_i||^2`, with `c_i > 0`.

For symmetric cross terms `b_ij`, suppose

`|b_ij(x_i,x_j)| ≤ η_ij sqrt(c_i c_j) ||x_i|| ||x_j||`,

where `E=(η_ij)` is a real symmetric matrix with zero diagonal and `λ_max(E) ≤ 1` (the stronger `||E||op ≤ 1` is also sufficient).

For

`Q(x)=Σ_i q_i(x_i)+2 Σ_{i<j} b_ij(x_i,x_j)`,

prove `Q(x) ≥ 0`.

**Proof skeleton:** put `y_i=sqrt(c_i)||x_i||`. Then

`Q(x) ≥ yᵀ(I-E)y ≥ 0`.

**Status:** `LEAN_TARGET`.

**RH relevance:** abstract sufficient machinery only. Proving it does not prove any Riemann-specific bound.

---

### W-SHIFT-01 — support-separation vanishing

For compactly supported functions `f,g` and translation `τ_a g(x)=g(x-a)`, prove the relevant correlation/convolution term vanishes whenever the translated supports are disjoint.

A schematic scalar form is:

if `supp f ∩ (a + supp g) = ∅`, then

`∫ f(x) * conj(g(x-a)) dx = 0`.

**Status:** `LEAN_TARGET`.

**Why it matters:** in the explicit formula, the prime-power term evaluates the convolution test `k=f⋆g̃` at `±log n`. After expanding the convolution, this is exactly where support geometry can make an edge vanish.

---

### W-EDGE-01 — weighted edge-energy bound

For a Hilbert-space shift/correlation term, formalize the weighted Cauchy inequality

`2 |⟨u,v⟩| ≤ λ ||u||² + λ⁻¹ ||v||²` for `λ>0`,

and shifted variants using the isometry of translation where appropriate.

**Status:** `LEAN_TARGET`.

**Purpose:** convert individual prime-shift cross terms into diagonal energy charges that can be assembled by `W-BLOCK-01`.

---

### W-POLE-01 — finite-rank pole-direction bookkeeping

The literature explicit formula contains the two pole-evaluation terms `h(i/2)` and `h(-i/2)`. Determine an exact finite-rank representation for these directions on the selected test space and prove the projection/Schur-complement statement needed to keep their contribution explicit rather than dropping it.

**Status:** `LEAN_TARGET` / `BLOCKED` until `W-NORM-01` fixes the chosen real form.

**Audit warning:** pole terms cannot be discarded merely because the prime graph is the visually interesting part.

---

### W-LIMIT-01 — finite-to-global exhaustion

Prove an abstract closure theorem of the following form after the exact topology is selected:

if `Q` is continuous on the admissible test space and every member can be approximated by functions handled by the finite partition/block scheme, and if the finite approximants have nonnegative `Q`, then `Q(f)≥0` globally.

**Status:** `LEAN_TARGET`.

**Audit warning:** this theorem must carry the exact topology and continuity hypotheses. “Dense” alone is not enough.

---

## The Riemann-specific hard wall

### W-DECOMP-01 — exact block decomposition of the Riemann Weil form

Starting from `W-NORM-01`, partition a compact support interval into cells and express `Q(f)` as:

- local diagonal/archimedean terms;
- finite prime-power shift couplings, because compact support makes the von Mangoldt sum finite at each support scale;
- finite-rank pole terms;
- no omitted remainder.

**Status:** `CONJECTURE` / `LEAN_TARGET` until the decomposition is written exactly.

The existence of a useful decomposition is plausible from the upstream explicit formula, but its positivity-relevant normalization has not yet been proved.

---

### W-LOCAL-01 — local coercivity

For each cell/block, prove a positive lower bound for the local diagonal contribution strong enough to normalize the cross couplings:

`q_i(f_i) ≥ c_i ||f_i||²`, `c_i>0`.

**Status:** `BLOCKED`.

**This may fail as stated.** If so, the counterexample should be committed and the block architecture revised, possibly by enlarging blocks, changing the norm, or retaining a finite-dimensional indefinite sector.

---

### W-GLOBAL-01 — uniform normalized-coupling domination

After exact decomposition and local coercivity, let `E_L` denote the normalized coupling matrix/operator for support scale `L`.

**Candidate sufficient theorem:**

`sup_L λ_max(E_L) ≤ 1`.

Together with `W-BLOCK-01`, the exact decomposition, pole control, and the exhaustion theorem, this would yield global Weil positivity in the chosen criterion.

**Status:** `BLOCKED` / `OPEN_EQUIVALENT-CANDIDATE`.

**Critical caution:** there is currently no proof that the actual Riemann form satisfies this bound. It may be false. It may also encode essentially all of RH. Its first treatment must therefore be adversarial and counterexample-first.

**First tests:**

- derive the smallest nontrivial exact finite matrices;
- numerically scan spectral margins at increasing support scales;
- locate near-extremizers;
- if a violation appears, certify it and kill or revise the sufficient condition;
- if margins remain positive, seek a theorem explaining the structure rather than extrapolating numerically.

---

### W6 — global Weil positivity

**Statement:** `Q(f)≥0` for every admissible test function.

**Status:** `OPEN_EQUIVALENT`.

This is not an intermediate theorem to celebrate. It is the conjecture-strength endpoint of Track W.

---

### W7 — conclude RH

Apply `W-CRIT-REV` to W6.

**Status:** `BLOCKED` by W6 and the exact formal criterion.

---

# Track T — Laguerre / tilted autocorrelation

The August 1 dossier already established the correct global frontier:

- `L_n(x) ≥ 0` for every `n,x`;
- equivalently positive definiteness of all `K_n`;
- equivalently the appropriate family of tilted-autocorrelation kernels `S_alpha` / `C_a`;
- equivalent Fenchel nonnegativity family.

These endpoints are `OPEN_EQUIVALENT`, not solved lemmas.

### T0 — exact Xi/Pólya kernel in Lean

Define the centered Xi function/kernel with exact normalization and prove the Fourier representation used by the August 1 dossier.

**Status:** `LEAN_TARGET`.

### T1 — generalized Laguerre hierarchy

Formalize `L_n`, associated kernels `K_n`, and the precise real-zero characterization needed for Xi.

**Status:** `LEAN_TARGET`.

### T2 — tilt/autocorrelation equivalence

Formalize the exact identity connecting the hierarchy to `S_alpha` / `C_a` and positive definiteness.

**Status:** `LEAN_TARGET`.

### T3 — positivity-preserving bridge to Weil space

Find an explicit transform `B` with proved properties strong enough that positivity in one formalism implies positivity in the other without assuming RH.

**Status:** `CONJECTURE`.

A successful T3 would be genuinely useful even if it does not prove positivity itself, because it would merge two currently separate RH-equivalent interfaces.

### T4 — global Gram/SOS representation

Construct a representation proving the entire tilt/Laguerre positivity family.

**Status:** `BLOCKED` / `OPEN_EQUIVALENT`.

The August 1 dossier already ruled out several naive positivity factorizations and individual theta-slice strategies, so any reopened T4 route must supply a new coupling mechanism.

# Search priority

The current ordering is intentional:

1. `W-BLOCK-01`, `W-SHIFT-01`, `W-EDGE-01`: small, reusable, falsifiable/formalizable.
2. `W-NORM-01`: pin the exact object before doing estimates.
3. `W-CRIT-FWD` and the statement layer of `W-CRIT-REV`.
4. `W-DECOMP-01`: discover whether the prime-shift graph is mathematically faithful enough to deserve more effort.
5. `W-LOCAL-01` and finite spectral experiments.
6. `W-GLOBAL-01` only if the architecture survives counterexample search.
7. In parallel, pursue `T3` as a bridge theorem rather than re-running already-blocked positivity tricks.

This is the intended compression of the search space: every move has a named theorem-shaped destination, and the conjecture-strength wall remains visible at all times.
