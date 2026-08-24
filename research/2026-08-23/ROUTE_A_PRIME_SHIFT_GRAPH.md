# Route A — Prime-Shift Graph / Block Positivity

**Route ID:** `W-A`  
**Status:** `CONJECTURE` as a Riemann-specific strategy; contains several independent `LEAN_TARGET` lemmas.  
**No RH claim.**

## 1. Motivation from the exact explicit formula

The new upstream Lean infrastructure makes one structural feature especially concrete.

For a compactly supported test function `k`, the literature Weil explicit formula used in `anthropics/zeta-23-lean/Zeta23/ExplicitFormula.lean` has the schematic right-hand side

`pole(k) - Σ_n Λ(n)/sqrt(n) * [k(log n)+k(-log n)] + gamma(k)`.

For the diagonal quadratic form, take

`k = f ⋆ f̃`, where `f̃(u)=conj(f(-u))`.

Then `k(a)` is a correlation of `f` with a translate of itself. Consequently, the prime-power evaluations at `a=±log n` can be regarded as **translation couplings** between pieces of `f` whose supports are separated by approximately `log n`.

This observation is exact at the convolution level. The proposed *graph domination* built on top of it is not yet proved.

## 2. Cell decomposition

Fix a support scale `L` and suppose `f` is supported in `[-L/2,L/2]`.

Partition this interval into finitely many cells `I_i` and choose a decomposition

`f = Σ_i f_i`, with `supp(f_i) ⊆ I_i`.

For a shift `a`, expand

`(f ⋆ f̃)(a) = Σ_{i,j} (f_i ⋆ f̃_j)(a)`.

A pair `(i,j)` contributes only when the support geometry permits overlap under translation by `a`. At the prime term, the allowed shifts are `a=±log n`, and only finitely many `n` can matter for fixed compact support.

Thus each finite support scale suggests a finite interaction graph:

- vertices = support cells;
- an edge `i-j` exists when a relevant prime-power shift can couple the two cells;
- edge weights come from `Λ(n)/sqrt(n)` times the corresponding correlation estimate;
- archimedean/Gamma and pole contributions remain separate and must be incorporated exactly.

## 3. The abstract block theorem

The first theorem does **not** mention zeta.

### Lemma `W-BLOCK-01`

Let `I` be a finite index set. For each `i`, let `H_i` be a real or complex Hilbert space and let `q_i : H_i -> R` satisfy

`q_i(x_i) ≥ c_i ||x_i||^2`, with `c_i>0`.

Let symmetric real cross terms `b_ij` satisfy

`|b_ij(x_i,x_j)| ≤ η_ij sqrt(c_i c_j) ||x_i|| ||x_j||`,

where `η_ij=η_ji≥0`, `η_ii=0`.

Define the symmetric matrix `E=(η_ij)` and

`Q(x)=Σ_i q_i(x_i)+2Σ_{i<j} b_ij(x_i,x_j)`.

If `λ_max(E)≤1`, then `Q(x)≥0`.

### Proof

Set

`y_i = sqrt(c_i) ||x_i|| ≥ 0`.

Then

`Q(x)`
`≥ Σ_i y_i^2 - 2Σ_{i<j} η_ij y_i y_j`
`= y^T (I-E) y`.

Since `E` is real symmetric and `λ_max(E)≤1`, the matrix `I-E` is positive semidefinite. Hence `Q(x)≥0`.

**Current status:** `PROVED_SYMBOLIC` for the finite-dimensional reduction above; `LEAN_TARGET` for formal verification.

### Audit note

Using `||E||op≤1` is a stronger sufficient hypothesis than `λ_max(E)≤1`; the latter is the exact spectral condition needed for `I-E≥0` when `E` is symmetric. A Lean implementation may start with the stronger operator-norm version if it substantially simplifies the first proof, but the strength loss must be recorded.

## 4. Exact support lemma

### Lemma `W-SHIFT-01`

Let `τ_a g(x)=g(x-a)`. Under standard integrability assumptions, if

`supp(f) ∩ supp(τ_a g) = ∅`,

then

`∫ f(x) conj(g(x-a)) dx = 0`.

Equivalently, the corresponding convolution/correlation value vanishes.

For cell-supported `f_i,f_j`, this gives an exact rule for deleting impossible graph edges before applying any estimate.

**Status:** `LEAN_TARGET`.

### Why this is valuable

It keeps arithmetic sparsity exact. We should not replace every possible prime shift by an absolute-value envelope before exploiting support geometry.

## 5. Edge-energy lemma

### Lemma `W-EDGE-01`

For a Hilbert space and `λ>0`,

`2 |<u,v>| ≤ λ ||u||^2 + λ^{-1} ||v||^2`.

For translation operators that are isometries, the same inequality applies to shifted correlations without changing the norm.

**Status:** `LEAN_TARGET`.

This gives a flexible way to allocate a cross-edge cost between its two incident vertices. The free parameter `λ` may later be optimized locally rather than taking an unnecessarily symmetric split.

## 6. Riemann-specific decomposition target

The real question is whether the exact Weil form can be organized so the abstract theorem applies without destroying the needed sign information.

### Target `W-DECOMP-01`

For every compact support scale `L`, produce an exact finite decomposition

`Q_L(f) = Σ_i q_i(f_i) + 2Σ_{i<j} b_ij(f_i,f_j) + P_L(f)`,

where:

- the `b_ij` include all prime-power shift couplings and any other off-diagonal terms;
- `P_L` is the pole/finite-rank sector, kept explicit;
- there is no hidden remainder;
- all constants are in the same normalization as the imported explicit formula.

**Status:** `CONJECTURE / LEAN_TARGET`.

The usefulness of Route A depends on whether this decomposition has a diagonal part with genuine coercivity after the finite-rank sector is handled.

## 7. Local coercivity target

### Target `W-LOCAL-01`

Find a norm and block definition such that

`q_i(f_i) ≥ c_i ||f_i||^2`, `c_i>0`,

uniformly enough to normalize cross couplings.

**Status:** `BLOCKED`.

### Counterexample-first instruction

Before attempting a long proof, search for blocks/test functions for which the proposed local term is negative, degenerate, or has arbitrarily small Rayleigh quotient.

If coercivity fails:

1. commit an explicit witness;
2. determine whether the failure is finite-dimensional;
3. try enlarging blocks or extracting an indefinite finite-rank sector;
4. do not simply replace `c_i` by a numerically observed positive constant.

## 8. Global spectral target

Assume an exact decomposition and positive `c_i`. Define normalized edge coefficients `η_ij(L)` so that

`|b_ij(f_i,f_j)| ≤ η_ij(L) sqrt(c_i c_j) ||f_i|| ||f_j||`.

Let `E_L=(η_ij(L))`.

### Candidate theorem `W-GLOBAL-01`

`sup_L λ_max(E_L) ≤ 1`.

Together with the abstract block theorem, exact pole handling, and a valid finite-to-global exhaustion theorem, this would give a route to global Weil positivity.

**Status:** `BLOCKED / OPEN_EQUIVALENT-CANDIDATE`.

### Why the label is severe

There is no evidence yet that this spectral bound is true. A norm bound formed after absolute values may be too strong even if the original signed Weil form is nonnegative. Conversely, if it is true uniformly, proving it may contain essentially the full difficulty of RH.

The route earns continued attention only if finite experiments reveal a structural margin and that margin can be linked to arithmetic cancellation rather than brute absolute-value domination.

## 9. First finite experiment

Once `W-NORM-01` is fixed, the first computation should not scan billions of zeros. It should inspect the **smallest support scales where more than one prime-power shift is active**.

For each selected `L`:

1. choose a transparent cell basis/partition;
2. construct the exact or high-precision quadratic matrix for the restricted test family;
3. decompose diagonal, prime, Gamma, and pole sectors separately;
4. compute the smallest eigenvalue of the full matrix;
5. compute the largest eigenvalue of the normalized absolute-coupling matrix `E_L`;
6. compare the two margins;
7. perturb cell size/basis to check whether a positive margin is intrinsic or discretization-dependent.

A negative `E_L` margin does **not** refute RH. It refutes only this sufficient domination scheme.

A negative eigenvalue of an exact correctly normalized full Weil matrix on an admissible test function, if certified, would be much more consequential and would require immediate independent reconstruction before interpretation.

## 10. Possible refinements if absolute domination is too strong

Do not keep tuning the same failed scalar bound. Distinct mechanisms include:

### A. Signed matrix domination

Retain the actual phases/signs of cross terms instead of replacing them by `|b_ij|`.

### B. Block enlargement

Group strongly coupled cells into a local block and estimate only interactions between blocks.

### C. Schur complement around the pole sector

Treat the pole directions exactly as a finite-dimensional sector and take a Schur complement rather than bounding them independently.

### D. Frequency-weighted local norm

Use a norm adapted to the Gamma/archimedean multiplier, if it produces genuine coercivity.

### E. Arithmetic coloring

Exploit the discrete set of shift lengths `log(p^m)` to color/decompose the graph into families with better operator bounds.

### F. Positivity-preserving bridge from Track T

If the tilted-autocorrelation/Laguerre program yields an exact transform into the Weil form, use that structure before taking absolute values.

Each refinement must be registered as a distinct mechanism if it changes what information is retained.

## 11. Stop conditions

Route A should be suspended if any of the following is established:

1. local coercivity fails in every natural block/norm formulation and the failure is not finite-rank;
2. the normalized graph bound is provably stronger than a known false statement;
3. explicit admissible finite models violate the candidate uniform bound robustly;
4. the best surviving theorem is merely another exact restatement of global Weil positivity;
5. the decomposition loses precisely the arithmetic cancellation needed for positivity.

## 12. What would count as real progress here

Not “the graph looks sparse.”

Real progress would be one of:

- a compiled proof of `W-BLOCK-01`;
- a compiled support/shift sparsity library;
- an exact Riemann Weil block decomposition;
- a rigorous local coercivity theorem;
- a certified counterexample to local coercivity or spectral domination;
- a nontrivial uniform spectral bound for a genuine subclass of support scales/test functions;
- or a new theorem showing how to preserve signed arithmetic cancellation across blocks.

The route is designed so that even failure sharpens the global map.
