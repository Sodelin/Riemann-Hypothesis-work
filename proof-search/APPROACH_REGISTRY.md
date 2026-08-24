# RH Approach Registry

Last structural update: 2026-08-23/24.

This is the canonical index of mechanism families. New research should update a row rather than opening an unnamed duplicate route.

| ID | Family | Exact target | Status | Main obstacle | Reopen / next action |
|---|---|---|---|---|---|
| W | Weil / explicit-formula positivity | Exact criterion interface and a weaker mechanism proving global Weil positivity | `ACTIVE` | Global positivity is RH-strength; need a genuinely weaker structural theorem | Pin exact criterion and attack local/operator structure |
| W-A | Prime-shift block/operator route | Decompose exact diagonal Weil form into analyzable signed blocks and prove/certify positivity | `ACTIVE` | Archimedean and pole sectors are not separately positive; crude domination may destroy cancellation | Stress-test combined archimedean+pole operator; derive smallest exact matrices |
| T | Generalized Laguerre / tilted autocorrelation | Prove full hierarchy / all-tilt positive-definite family or a weaker sufficient mechanism | `BLOCKED_EQUIVALENT` | Full global family is equivalent to RH; finite prefixes insufficient | Reopen global route only with new Gram/SOS or transform mechanism |
| T-W | Positivity-preserving transform between tilt/Laguerre and Weil interfaces | Explicit transform carrying positivity in one formalism to the other without assuming RH | `ACTIVE_LOW_COST` | No transform currently known/proved | Search exact transform identities; test on known no-go kernels |
| E | Epstein/theta regrouping | Cancellation-preserving theta-scale grouping yielding a global positivity estimate | `BLOCKED_NO_MECHANISM` | Individual-slice strategy was ruled out; grouping theorem missing | Reopen only with cross-scale cancellation mechanism |
| F | Fenchel / integrated-quantile margins | Prove all prime-prefix margins nonnegative using a weaker uniform analytic estimate | `BLOCKED_EQUIVALENT` | All-prefix global inequality is an RH-equivalent endpoint; no weaker uniform estimate yet | Search only for a new mechanism controlling the critical prefix regime |
| S | Suzuki/screw-kernel bridge | Explicit positivity-preserving transform into a tractable Weil/Laguerre order | `ACTIVE_LOW_COST` | Exact bridge theorem missing | Work only if transform uses structure not already equivalent to RH |
| D | Direct disproof certificate | Certified nontrivial zeta zero with real part != 1/2 | `ACTIVE_LOW_COST` | No candidate known; finite verification without a witness cannot prove RH | Preserve counterexample lane; any numerical candidate requires interval/formal certification immediately |

## W — Weil / explicit-formula route

### Known foundation

Anthropic's `zeta-23-lean` supplies substantial explicit-formula/zero-counting/Gamma/prime-sum infrastructure in Lean.

### Current exact object

The diagonal test `k=f⋆f̃` yields the exact pole + prime-translation + Gamma decomposition recorded in `research/2026-08-23/EXACT_DIAGONAL_WEIL_FORM.md`.

### Required mechanism

A theorem weaker/more structured than global Weil positivity that can actually be proved for the Riemann form.

### Kill tests

- Does the proposed sufficient condition fail on an exact finite test family?
- Does it become false because the Gamma multiplier changes sign?
- Does absolute-value domination destroy signed cancellation?
- Is the “new” global bound simply Weil positivity in different notation?

## W-A — prime-shift blocks

### Search object

Finite-support/cell restrictions of the exact quadratic form, with:

- sparse translation couplings at `log(p^m)`;
- exact low-rank pole sector;
- archimedean Fourier multiplier;
- signed rather than automatically absolute couplings.

### Current blocker

`W-LOCAL-01`: no useful local coercive reference form has been proved. The Gamma sector alone cannot serve because its multiplier is negative near zero.

### Next action

Study the combined archimedean+pole operator first. If local coercivity fails robustly, commit a counterexample and redesign the route before touching a global graph bound.

## T — Laguerre / tilt

### Known foundation

The August 1 dossier identified the full hierarchy/all-tilt positivity as a correct RH-equivalent endpoint and ruled out several finite/shape shortcuts.

### Do not repeat

- first Laguerre inequality alone;
- finite-prefix positivity as real-rootedness proof;
- smooth even decreasing+convex certificate;
- weight-only midpoint factorization without theta coupling.

## T-W — transform bridge

This route is allowed to remain active because a transform theorem could be genuine progress even if both endpoint families are RH-equivalent: it may transfer a tractable estimate or certificate class from one representation to the other.

**Kill test:** if the transform is invertible/equivalent but supplies no new monotone/positivity information, classify it as architectural only.

## E — Epstein/theta

The individual-theta-slice positivity route is closed by the August 1 obstruction. Any reopening must identify a grouping that preserves cancellation across theta scales.

## F — Fenchel

The all-prefix margin family is retained as a clean interface/counterexample detector. It is not described as “one inequality away” from RH without a mechanism controlling all prefixes.

## S — Suzuki/screw kernel

Only pursue explicit transforms/identities that can be audited independently. Do not infer RH from qualitative Hilbert-space analogies.

## D — disproof lane

A single rigorously certified nontrivial zero off the critical line would disprove RH. Numerical searches are therefore legitimate witness searches, but absence of a witness below any height is not evidence sufficient for proof.

## Duplicate-route rule

Before opening a new RH route:

1. Which row is it closest to?
2. What new mathematical information does it preserve?
3. What recorded blocker does it bypass?
4. What is the first exact falsification test?

Without a concrete answer to 2–3, treat it as a wording variant rather than a new proof architecture.
