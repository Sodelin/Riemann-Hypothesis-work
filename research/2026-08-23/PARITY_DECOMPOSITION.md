# Exact Parity Decomposition of the Fixed-Support Weil Form

**Claim ID:** `W-PARITY-01`  
**Status:** `PROVED_SYMBOLIC`.  
**RH status:** auxiliary structural theorem only.  
**Novelty:** elementary symmetry consequence; no novelty claim.

## 1. Reflection symmetry

Fix `L>0` and work in

\[
H_L=L^2([-L/2,L/2])
\]

with zero extension to \(L^2(\mathbb R)\).

Let

\[
(Rf)(x)=f(-x).
\]

Then \(R\) is a unitary self-adjoint involution:

\[
R^2=I.
\]

Hence

\[
H_L=H_L^+\oplus H_L^-,
\]

where

\[
H_L^+=\{f:Rf=f\}
\]

is the even subspace and

\[
H_L^-=\{f:Rf=-f\}
\]

is the odd subspace.

These subspaces are orthogonal.

## 2. Gamma sector preserves parity

The archimedean form is

\[
a_{\Gamma,L}[f]
=\int_{\mathbb R}\mu(r)|\widehat f(r)|^2dr,
\]

with \(\mu(-r)=\mu(r)\).

At the sesquilinear level,

\[
a_{\Gamma,L}[f,g]
=\int_{\mathbb R}\mu(r)\widehat f(r)\overline{\widehat g(r)}dr.
\]

If \(f\) is even and \(g\) is odd, then \(\widehat f\) is even and \(\widehat g\) is odd in the paper Fourier convention, so the integrand is odd. Therefore

\[
a_{\Gamma,L}[f,g]=0,
\qquad f\in H_L^+,\ g\in H_L^-.
\tag{2.1}
\]

Equivalently, the associated Gamma operator commutes with reflection.

## 3. Pole sector splits into one rank-one direction per parity

Recall

\[
C(f)=\int f(x)\cosh(x/2)dx,
\qquad
S(f)=\int f(x)\sinh(x/2)dx,
\]

and

\[
P[f]=2|C(f)|^2-2|S(f)|^2.
\]

Since \(\cosh(x/2)\) is even and \(\sinh(x/2)\) is odd,

\[
C(g)=0\quad(g\text{ odd}),
\qquad
S(f)=0\quad(f\text{ even}).
\]

Thus

\[
P[f_+ + f_-]
=
2|C(f_+)|^2
-
2|S(f_-)|^2.
\tag{3.1}
\]

There is no even-odd cross term.

Therefore:

- on \(H_L^+\), the pole sector is a **positive rank-one** form;
- on \(H_L^-\), the pole sector is a **negative rank-one** form.

This is sharper than treating the pole contribution merely as a rank-two indefinite perturbation on the full space.

## 4. Prime sector preserves parity

Let \(U_a\) be translation on zero-extended \(L^2(\mathbb R)\):

\[
(U_af)(x)=f(x-a).
\]

Reflection conjugates translations by

\[
RU_aR=U_{-a}.
\tag{4.1}
\]

The self-adjoint prime-shift contribution at shift \(a\) is proportional to

\[
U_a+U_{-a}
\]

after compression to \(H_L\). By (4.1),

\[
R(U_a+U_{-a})R=U_a+U_{-a}.
\]

Hence every symmetric prime-shift operator commutes with reflection, and so does the finite sum

\[
B_L
=-\sum_{n\le e^L}
\frac{\Lambda(n)}{\sqrt n}
(K_{\log n}+K_{\log n}^*).
\]

Therefore

\[
\langle B_Lf_+,f_-\rangle=0
\qquad
(f_+\text{ even},\ f_-\text{ odd}).
\tag{4.2}
\]

## 5. Full fixed-L direct sum

Combining (2.1), (3.1), and (4.2), the exact fixed-support Weil form satisfies

\[
q_{W,L}[f_++f_-]
=
q_{W,L}^+[f_+]
+
q_{W,L}^-[f_-].
\tag{5.1}
\]

Thus

\[
q_{W,L}\ge0\text{ on }H_L
\]

if and only if

\[
q_{W,L}^+\ge0\text{ on }H_L^+
\quad\text{and}\quad
q_{W,L}^-\ge0\text{ on }H_L^-.
\tag{5.2}
\]

## 6. Parity split of the reference finite-index theorem

The archimedean+pole operator \(A_{AP,L}\) commutes with \(R\), so its spectral projections commute with \(R\). Therefore the finite nonpositive subspace decomposes as

\[
F_L=F_L^+\oplus F_L^-,
\]

with

\[
F_L^\pm=F_L\cap H_L^\pm.
\tag{6.1}
\]

Both are finite dimensional.

The positive complement likewise splits by parity, and separate positive gaps may be defined:

\[
c_L^+>0,
\qquad
c_L^->0,
\]

on the corresponding complements when nonempty.

## 7. Consequence for the Schur certificate

Instead of one finite-dimensional Schur matrix on \(F_L\), build two independent certificates:

\[
S_L^+\ge0
\quad\text{on }F_L^+,
\]

\[
S_L^-\ge0
\quad\text{on }F_L^-.
\]

This has several advantages:

1. matrix sizes are reduced;
2. no artificial even-odd coupling bounds are introduced;
3. the pole contribution has known one-sided sign in each sector;
4. numerical eigenvectors can be classified by parity;
5. any future analytic estimate may exploit different mechanisms in the two sectors.

The odd sector is structurally more exposed to the negative pole moment, while the even sector receives a positive pole contribution. This does not imply that all negative reference directions are odd: the Gamma multiplier itself is negative at low frequency, so negative even modes can appear as support grows.

## 8. Numerical diagnostic alignment

The committed finite-basis calculation uses

\[
(1-t^2)^3P_k(t),
\]

and Legendre parity gives even basis vectors for even \(k\) and odd basis vectors for odd \(k\).

The computed matrices have even-odd cross entries at numerical roundoff scale, providing a direct implementation check of the exact symmetry theorem.

Preliminary finite-basis spectra show, for example, that near \(L=1\) both an even and an odd negative direction are visible in sufficiently rich bases. This observation is **NUMERICAL only** and is not needed for the parity proof.

## 9. Formalization targets

- `W-REFLECT`: define reflection on fixed-support `L2` and its involutive/unitary properties.
- `W-GAMMA-PARITY`: even multiplier implies parity invariance.
- `W-POLE-PARITY`: cosh/sinh moment split.
- `W-PRIME-PARITY`: `R U_a R = U_-a` and symmetric shift commutation.
- `W-PARITY-FULL`: full direct-sum theorem.

## 10. Search consequence

Future fixed-L certificate search should be parity-aware by default. Any numerical code that produces substantial even-odd matrix coupling is likely implementing a normalization, quadrature, or projection incorrectly.
