# Fixed-L Schur-Complement Certificate for the Full Weil Form

**Claim ID:** `W-SCHUR-01`  
**Status:** `PROVED_SYMBOLIC` as an abstract operator theorem.  
**RH status:** fixed-support sufficient certificate architecture only; no global RH claim.  
**Novelty:** standard Schur-complement/operator theory specialized to the current Weil decomposition; no novelty claim.

## 1. Exact fixed-L decomposition

Fix \(L>0\), let

\[
H_L=L^2([-L/2,L/2])
\]

with zero extension to \(L^2(\mathbb R)\), and let \(A_L=A_{AP,L}\) be the self-adjoint operator associated with the archimedean + pole form from `ARCHIMEDEAN_POLE_FINITE_INDEX.md`.

For the prime part define, schematically,

\[
q_{P,L}[f]
=-2\sum_{n\le e^L}\frac{\Lambda(n)}{\sqrt n}
\Re\langle f,U_{\log n}f\rangle_{L^2(\mathbb R)},
\tag{1.1}
\]

where \(U_a f(x)=f(x-a)\) acts on zero-extended functions.

Because \(f\star\widetilde f\) is supported in \([-L,L]\), terms with \(\log n>L\) vanish. Thus the sum is finite.

For each shift let \(P_L\) denote orthogonal projection back to \(H_L\) and put

\[
K_a=P_LU_a|_{H_L}.
\]

Then \(\|K_a\|\le1\), and the real quadratic form (1.1) is represented by the bounded self-adjoint operator

\[
B_L
=-\sum_{n\le e^L}\frac{\Lambda(n)}{\sqrt n}
\bigl(K_{\log n}+K_{\log n}^*\bigr).
\tag{1.2}
\]

Consequently

\[
\|B_L\|
\le
2\sum_{n\le e^L}\frac{\Lambda(n)}{\sqrt n}.
\tag{1.3}
\]

This global norm bound is intentionally crude. The certificate theorem below allows sharper block-specific bounds.

The full fixed-support diagonal Weil form is therefore

\[
q_{W,L}[f]
=a_{AP,L}[f]+\langle B_Lf,f\rangle.
\tag{1.4}
\]

## 2. Spectral split of the reference operator

From `W-AP-FINITEINDEX`, let

\[
F_L=\mathbf1_{(-\infty,0]}(A_L)H_L,
\qquad
G_L=F_L^\perp.
\tag{2.1}
\]

Then

\[
\dim F_L<\infty,
\]

and for some \(c_L>0\),

\[
a_{AP,L}[g]\ge c_L\|g\|^2,
\qquad g\in\mathcal D_L\cap G_L.
\tag{2.2}
\]

Because \(F_L\) is a spectral subspace of \(A_L\), the reference form has no cross term between \(F_L\) and \(G_L\).

Write the bounded prime operator in block form relative to

\[
H_L=F_L\oplus G_L:
\]

\[
B_L=
\begin{pmatrix}
B_{FF}&B_{FG}\\
B_{GF}&B_{GG}
\end{pmatrix},
\qquad B_{FG}=B_{GF}^*.
\tag{2.3}
\]

Let \(A_F=A_L|_{F_L}\), a finite-dimensional Hermitian operator.

## 3. Complement-positivity condition

Assume a certified number \(b_L\ge0\) satisfies

\[
\|B_{GG}\|\le b_L<c_L.
\tag{3.1}
\]

Set

\[
\delta_L=c_L-b_L>0.
\tag{3.2}
\]

Then the lower-right operator/form

\[
C_L:=A_L|_{G_L}+B_{GG}
\tag{3.3}
\]

obeys

\[
C_L\ge \delta_L I
\tag{3.4}
\]

in form sense on \(G_L\). Hence \(C_L\) is invertible and

\[
0<C_L^{-1}\le \delta_L^{-1}I.
\tag{3.5}
\]

## 4. Exact Schur complement theorem

Define the finite-dimensional operator on \(F_L\)

\[
M_L:=A_F+B_{FF},
\tag{4.1}
\]

and let

\[
D_L:=B_{GF}:F_L\to G_L.
\tag{4.2}
\]

### Theorem 4.1 — exact fixed-L criterion

Under (3.1), the full fixed-support form \(q_{W,L}\) is nonnegative on its form domain if and only if the finite-dimensional Schur complement

\[
S_L
:=
M_L-D_L^*C_L^{-1}D_L
\tag{4.3}
\]

is positive semidefinite on \(F_L\).

### Proof

Write \(f=x+y\) with \(x\in F_L\), \(y\in G_L\). Then

\[
q_{W,L}[x+y]
=
\langle M_Lx,x\rangle
+2\Re\langle D_Lx,y\rangle
+\langle C_Ly,y\rangle.
\tag{4.4}
\]

Since \(C_L>0\), complete the square:

\[
\begin{aligned}
q_{W,L}[x+y]
={}&
\left\langle C_L
\left(y+C_L^{-1}D_Lx\right),
\left(y+C_L^{-1}D_Lx\right)
\right\rangle\\
&+\langle
(M_L-D_L^*C_L^{-1}D_L)x,x
\rangle.
\end{aligned}
\tag{4.5}
\]

The first term is nonnegative. Therefore \(S_L\ge0\) implies \(q_{W,L}\ge0\).

Conversely, if \(q_{W,L}\ge0\), choose

\[
y=-C_L^{-1}D_Lx.
\]

Then (4.5) reduces to \(\langle S_Lx,x\rangle\ge0\) for every \(x\in F_L\). ∎

## 5. A certificate that avoids constructing the inverse

The exact criterion (4.3) still refers to the infinite-dimensional inverse \(C_L^{-1}\). Equation (3.5) gives a purely finite sufficient condition.

Since

\[
D_L^*C_L^{-1}D_L
\le
\delta_L^{-1}D_L^*D_L,
\tag{5.1}
\]

we obtain:

### Corollary 5.1 — finite sufficient certificate

If

\[
M_L-\delta_L^{-1}D_L^*D_L\ge0
\quad\text{on }F_L,
\tag{5.2}
\]

then

\[
q_{W,L}[f]\ge0
\]

for every \(f\) in the fixed-support form domain.

Because \(F_L\) is finite dimensional, (5.2) is a finite Hermitian matrix positive-semidefiniteness test once a certified basis and certified matrix entries/bounds are supplied.

## 6. Even coarser norm certificate

If a scalar \(d_L\) satisfies

\[
\|D_L\|\le d_L,
\tag{6.1}
\]

then

\[
D_L^*D_L\le d_L^2 I_{F_L}.
\]

Therefore the stronger but simpler condition

\[
M_L\ge \frac{d_L^2}{\delta_L}I_{F_L}
\tag{6.2}
\]

also certifies full fixed-L nonnegativity.

This scalar form is likely too crude for serious RH work, but it is a useful kill test: if it fails badly, the matrix certificate may still survive; if even the matrix certificate fails, the present reference split must be revised.

## 7. Why this is certificate-first

The infinite-dimensional soundness theorem is now separated from numerical generation.

An untrusted search program may attempt to produce, for a chosen \(L\):

1. a certified description/enclosure of the finite bad subspace \(F_L\);
2. a lower bound \(c_L\) for the reference form on its complement;
3. a bound \(b_L<c_L\) for \(B_{GG}\);
4. the finite matrix \(M_L\);
5. a certified enclosure of \(D_L^*D_L\);
6. a PSD certificate for (5.2).

If those objects are rigorous, Corollary 5.1 converts them into a theorem covering **every** admissible fixed-support function, not merely the basis used to discover them.

## 8. What is currently missing

No such rigorous certificate has been produced yet.

The difficult parts are now explicit:

- identify/enclose the true \(F_L\), not merely a Ritz approximation;
- certify the complement spectral gap \(c_L\);
- exploit support/arithmetic structure to make \(b_L<c_L\) possible;
- compute sharp cross-block data without replacing all cancellation by absolute values;
- globalize over unbounded \(L\).

## 9. Important failure mode

The crude full operator bound (1.3) grows with \(L\) and is unlikely to fit under a delicate complement gap. Therefore a useful certificate almost certainly must exploit more than

\[
\|B_L\|\le2\sum_{n\le e^L}\Lambda(n)/\sqrt n.
\]

Possible structure to preserve includes:

- exact support overlap of each shift;
- parity/even-odd decomposition;
- signed arithmetic interference between shifts;
- block localization;
- spectral information about how prime shifts act specifically on \(G_L\);
- grouped prime-power operators rather than triangle inequality term by term.

If all of this structure is discarded, the certificate may simply become an impossibly strong sufficient condition.

## 10. Next formal targets

- `W-PRIME-BOUNDED`: formalize the finite bounded self-adjoint prime-shift operator at fixed \(L\).
- `W-SCHUR-ABSTRACT`: formal Hilbert-space block theorem corresponding to Theorem 4.1.
- `W-SCHUR-BOUND`: formalize Corollary 5.1.
- `W-CERT-DATA`: design a transparent finite data structure whose validity implies the hypotheses of Corollary 5.1.

The proof assistant should check the certificate semantics; numerical/LLM/SAT tools may remain untrusted certificate generators.
