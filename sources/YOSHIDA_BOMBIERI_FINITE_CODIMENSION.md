# Yoshida / Bombieri Finite-Codimension Positivity Integration

**Status:** established prior-art substrate.  
**Primary references:** H. Yoshida (1992), E. Bombieri (2000, 2003), as summarized and rederived in Suzuki 2023/2026.

## 1. Load-bearing theorem

For `a>0`, Yoshida introduced periodic-support spaces `K(a)` and the finite-codimension subspaces

`K_N(a)`

obtained by imposing vanishing Fourier coefficients for `|n|<=N`.

The theorem quoted in Suzuki's review is stronger than merely saying the high-frequency tail is eventually positive:

> For every finite horizon `a_0>0` and every `mu>0`, there exists `N` such that the Weil Hermitian form is at least `mu ||phi||_2^2` for every `phi in K_N(a)` and every `0<a<=a_0`.

Thus, on any fixed finite support horizon, the infinite-dimensional high-frequency tail is uniformly coercive after removal of finitely many Fourier modes.

## 2. Effect on the current project

This changes the novelty/usefulness classification of several current observations.

The statement

`fixed support -> only finitely many low modes can remain dangerous`

is **known architecture**, not a new theorem of this project.

The project-specific shell work remains useful only insofar as it supplies:

- an explicit physical-space boundary decomposition;
- exact prime-hinge cancellation on thin zero-mean boundary bands;
- an adaptive support mesh that avoids introducing a spurious prime-gap obstruction;
- a universal fresh-shock operator with explicit spectrum;
- a candidate interface between boundary localization and modern Hilbert/Dirichlet-polynomial estimates.

## 3. Bombieri boundary-concentration observation

Bombieri's finite-section experiments observed a qualitative distinction near a critical support value: when approximate eigenvalues tend toward zero, the corresponding normalized eigenfunctions can converge weakly to zero while their `L2` mass concentrates near the boundary of the interval.

Bombieri explicitly suggested studying the asymptotic boundary-rescaled eigenfunctions.

This is highly relevant to the current local-shell analysis. It also means boundary localization is **prior-motivated**, not an originality claim.

## 4. Finite+tail certificate architecture

For a finite horizon `A`, choose `mu>0` and Yoshida's corresponding cutoff `N(A,mu)`.

Schematic decomposition:

`old core = finite low-mode sector + coercive high-frequency tail`.

The current adaptive boundary theorem gives

`new support sector = positive boundary-local sector`

for sufficiently fine mesh steps.

Therefore a fixed-horizon support propagation theorem can in principle be reduced to:

1. an analytic tail estimate on the Yoshida high modes;
2. a finite Hermitian matrix involving the low modes and boundary sector;
3. a certified positivity/Schur/factorization check for that finite matrix.

This is exactly the `finite certificate + analytic tail theorem` architecture used elsewhere in the proof-attack framework.

## 5. What it still does not solve

The cutoff `N(A,mu)` depends on the support horizon and desired coercivity. The theorem does not provide a uniform finite-dimensional core as `A->infinity`.

Therefore finite-codimension positivity alone does not globalize to RH.

The genuine remaining question is whether the low-mode certificate family admits:

- a uniform dimension bound;
- a recursive update rule;
- an arithmetic monotonicity/factorization theorem;
- or a different analytic invariant that prevents a zero crossing.

Without one of these, the phrase `only finitely many modes remain` hides an unbounded family of finite problems.

## 6. Methodological correction

Future project files should distinguish:

- **fixed-support finite vulnerability:** known from Yoshida;
- **explicit adaptive boundary decomposition:** project-specific packaging/auxiliary lemmas;
- **global low-mode control:** still open and potentially RH-strength.

Do not claim that proving a finite-tail theorem materially closes RH unless it also controls the support dependence of the finite vulnerable sector.
