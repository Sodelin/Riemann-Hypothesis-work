# Adversarial Research Protocol

**Cycle:** 2026-08-23  
**Scope:** Riemann Hypothesis exploratory research  
**Rule zero:** no statement is promoted because it is aesthetically persuasive, numerically impressive, repeated by multiple related model instances, or equivalent to RH.

## 1. Purpose

The protocol exists to make persistence useful rather than repetitive. A research route is successful if it either:

- proves a genuinely new intermediate statement;
- supplies a formal proof artifact;
- supplies a reproducible calculation that falsifies a stronger candidate statement;
- identifies an exact equivalence or reduction that shrinks the unresolved interface;
- or dies cleanly with an exact obstruction.

A route that merely renames RH has not advanced the proof.

## 2. Independent-route rule

Before one mechanism becomes the default explanation, competing routes should be stated independently. At minimum distinguish:

- `W`: Weil quadratic-form / explicit-formula route;
- `T`: generalized Laguerre / tilted-autocorrelation route;
- `S`: spectral or operator realization route, if a genuinely new operator mechanism appears;
- `C`: counterexample/falsification route for stronger sufficient properties.

Cross-route borrowing is allowed only after the borrowed statement and its status are recorded.

## 3. Mechanism registry

Each live route must identify the mathematical information it preserves. Examples:

- zero locations and multiplicities;
- prime-power shifts in a test-function explicit formula;
- support geometry;
- positive definiteness;
- generalized Laguerre inequalities;
- Toeplitz minors;
- operator spectra;
- modular/theta cancellation;
- convex/Fenchel margins.

Two arguments using different notation but retaining the same information count as one mechanism unless they introduce a genuinely different theorem.

## 4. Status discipline

### `LEAN_VERIFIED`
Use only when a theorem has been compiled in the recorded environment and the relevant axiom/trust audit has been checked. A Lean-shaped statement or uncompiled code is not `LEAN_VERIFIED`.

### `UPSTREAM_LEAN`
Use for a theorem provided by a named external Lean artifact. Record repository, revision/toolchain when available, and exact theorem name. This status does not imply that this repository has independently rebuilt it.

### `PROVED_SYMBOLIC`
A complete ordinary mathematical derivation has been written and checked within the project, but not formally verified in Lean.

### `LEAN_TARGET`
The statement is precise enough to formalize, but no successful compile/proof is yet recorded.

### `CONDITIONAL`
The deduction is complete from an explicitly named hypothesis that remains unproved.

### `NUMERICAL`
Finite computation, floating-point evidence, high-precision experiment, interval certificate, or finite exact enumeration. Record which kind.

### `CONJECTURE`
A live proposed statement with no proof.

### `OPEN_EQUIVALENT`
The statement is known or argued to be equivalent to RH, or appears to retain the full global difficulty. Such a node can be a useful interface but is not counted as a solved intermediate gap.

### `COUNTEREXAMPLE`
An exact witness refutes a specified universal statement. The killed statement must be quoted exactly enough that future work cannot silently weaken it and pretend the counterexample disappeared.

### `BLOCKED`
A route currently terminates at a named missing theorem. State the missing theorem itself, not merely “needs stronger estimates.”

### `REJECTED`
The proposed mechanism is mathematically invalid under its stated assumptions or has been superseded by a decisive obstruction.

## 5. Four-axis verdict

Every substantial claim gets four separate judgments when relevant:

1. **Correctness:** proved / conditional / numerical / counterexample / unresolved.
2. **Novelty:** known / likely known / search incomplete / candidate new.
3. **Usefulness:** does it reduce a future proof burden?
4. **RH relevance:** necessary, sufficient, equivalent, merely analogous, or unrelated.

A claim can be correct and interesting while contributing zero leverage toward RH.

## 6. Anti-circularity audit

For every proposed lemma `A -> B` on a route to RH, ask:

1. Is `A` already equivalent to RH?
2. Does the proof of `A` use any result whose known proof assumes RH?
3. Is `B` actually stronger than `A`, or merely a change of representation?
4. Has an existential construction hidden a universal quantifier?
5. Has a finite-support or finite-degree theorem silently been promoted to an all-support/all-degree theorem?
6. Has positivity for one kernel, one order, one parameter, or one scale been promoted to a full hierarchy?
7. Has an interchange of sum/integral/limit been used outside a proved convergence domain?
8. Has a numerical sign pattern been promoted to a universal sign theorem?

Any “yes” that is not explicitly discharged blocks promotion.

## 7. Adversarial checklist for analytic statements

Check, at minimum:

- all quantifiers and parameter ranges;
- endpoint conventions and strict/non-strict inequalities;
- positivity and nonvanishing assumptions;
- normalization constants and Fourier-transform conventions;
- domains of analytic continuation;
- absolute versus conditional convergence;
- interchange of limits, sums, derivatives, and integrals;
- local regularity at symmetry points;
- uniformity in scale/support/order;
- dependence of constants on hidden parameters;
- whether a test-function class is dense enough for the claimed criterion;
- whether the claimed positivity is scalar, matrix, kernel, or operator positivity;
- whether multiplicity is being preserved.

## 8. Adversarial checklist for Lean statements

For each formal theorem candidate:

- record exact imports;
- record Lean and Mathlib versions;
- distinguish definitions copied from upstream from local definitions;
- avoid `sorry`, `by_contra` loops hidden behind unproved helper axioms, or local `axiom` declarations;
- run `#print axioms` on headline theorems when possible;
- verify coercions and extended-real/natural multiplicity conventions;
- prove equivalence between the local mathematical notation and the actual Mathlib/Zeta23 definitions;
- keep the conjecture-strength assumption visible in theorem signatures.

A proof of `P -> RH` is not a proof of RH while `P` remains an axiom or hypothesis.

## 9. Counterexample-first rule

Before proving a proposed *stronger sufficient condition*, try to kill it.

Priority falsification tools:

- exact symbolic examples;
- small matrices and finite support configurations;
- interval arithmetic for delicate signs;
- high-precision scans to locate candidate witnesses;
- random/adversarial test functions followed by exact or certified reconstruction;
- limiting cases and symmetry points.

A failed sufficient condition should be preserved as a `COUNTEREXAMPLE` or `REJECTED` node, not erased.

## 10. Route-kill and reopen rule

A route is suspended when:

- its central sufficient condition has a counterexample;
- its next theorem is exactly equivalent to RH with no new mechanism for proving it;
- repeated modifications preserve the same obstruction;
- or its supposed advantage depends on an unproved global estimate at least as hard as the original target.

A suspended route can reopen only if a materially new mechanism appears, such as:

- a new formal library theorem;
- a new positivity-preserving transform;
- a new compactness/localization theorem;
- a new exact identity that changes the information available;
- or a rigorous bound that removes the recorded obstruction.

## 11. Concrete-output requirement

Every research pass must end with at least one of:

- a proved lemma;
- a precise Lean theorem target;
- a compiled Lean theorem;
- an exact identity;
- an explicit counterexample;
- a certified numerical witness;
- a reproducible program;
- a source/prior-art correction;
- or a precisely stated missing theorem.

“Promising,” “seems positive,” and “may generalize” are not outputs.

## 12. Git provenance rule

Git commits are part of the research record.

Commit:

- new lemma statements before or with proof attempts;
- counterexamples with the exact claim they refute;
- changes in route status;
- source corrections;
- formalization environment changes;
- and failed mechanisms when the failure teaches a reusable lesson.

Do not rewrite a failed route into a clean success narrative. The history is valuable because it shows what was tried and why it stopped.

## 13. Promotion gate for any purported RH proof

A candidate implication chain to RH is not called a proof until all of the following hold:

1. Every node is either a standard cited theorem or independently reconstructible proof.
2. No node is `CONJECTURE`, `NUMERICAL`, `BLOCKED`, `OPEN_EQUIVALENT`, or an unproved formal hypothesis.
3. Every analytic interchange and parameter-uniform estimate is justified.
4. The final statement matches a standard formulation of RH without narrowing the zero/test-function class.
5. A separate adversarial reconstruction attempts to falsify every nontrivial step.
6. If Lean is used as the certification path, the final theorem compiles with an explicit trust/axiom audit.
7. Independent qualified human review is still requested before any public breakthrough claim.

Until then the repository remains a research ledger, not a proof announcement.
