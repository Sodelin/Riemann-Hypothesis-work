# Fixed-Support Finite-Index Theorem for the Archimedean + Pole Sector

**Claim family:** `W-AP-*`  
**Status:** `PROVED_SYMBOLIC` using standard closed-form / compact-resolvent functional analysis plus the formally established upstream Gamma facts.  
**Novelty:** no novelty claim; the functional-analytic mechanism is standard.  
**RH status:** auxiliary architecture only; this does **not** prove RH or global Weil positivity.

## 1. Motivation

The exact diagonal Weil formula derived in this cycle is

\[
Q(f)
=
P(f)
-2\sum_{n\ge1}\frac{\Lambda(n)}{\sqrt n}
\Re\langle f,\tau_{\log n}f\rangle
+
\int_{\mathbb R}\mu(r)|\widehat f(r)|^2\,dr,
\]

where the paper Fourier convention is

\[
\widehat f(r)=\int_{\mathbb R}f(x)e^{irx}\,dx,
\]

\[
\mu(r)=\frac1{2\pi}
\left[
\Re\psi\!\left(\frac14+\frac{ir}{2}\right)-\log\pi
\right],
\]

and the pole sector is

\[
P(f)
=2\left|\int f(x)\cosh(x/2)\,dx\right|^2
-2\left|\int f(x)\sinh(x/2)\,dx\right|^2.
\]

The Gamma multiplier is not pointwise positive, so the old target “positive local Gamma energy” is false. The correct fixed-support question is whether the combined archimedean + pole form has only finitely many bad directions.

It does.

## 2. Upstream Gamma facts used

`anthropics/zeta-23-lean` proves the Gamma facts assembled in its `Zeta23/GammaFacts/Complete.lean`. The source commentary records, in the normalization above:

1. `mu` is even and smooth;
2. `mu` is increasing in `|r|`;
3. \(\mu(r)\ge \mu(0)>-1\);
4. \[
   \mu(r)=\frac1{2\pi}\log\frac{|r|}{2\pi}+O(r^{-2})
   \qquad(|r|\to\infty).
   \]

In particular,

\[
\inf_{r\in\mathbb R}\mu(r)>-\infty,
\qquad
\mu(r)\longrightarrow+\infty
\quad (|r|\to\infty).
\tag{2.1}
\]

These two consequences are the only special-function input required below.

## 3. Fixed-support Hilbert space

Fix \(L>0\) and put

\[
I_L=[-L/2,L/2].
\]

Let

\[
H_L=\{f\in L^2(\mathbb R):\operatorname{supp}f\subseteq I_L\ \text{a.e.}\}.
\]

This is a closed subspace of \(L^2(\mathbb R)\), naturally identified with \(L^2(I_L)\).

Set

\[
m_0:=\mu(0),
\qquad
w(r):=\mu(r)-m_0+1.
\]

By (2.1),

\[
w(r)\ge1,
\qquad
w(r)\to\infty\quad(|r|\to\infty).
\tag{3.1}
\]

Define the form domain

\[
\mathcal D_L
=
\left\{
 f\in H_L:
 \int_{\mathbb R}w(r)|\widehat f(r)|^2\,dr<\infty
\right\}.
\tag{3.2}
\]

Smooth compactly supported functions in the interior of \(I_L\) lie in \(\mathcal D_L\) and are dense in \(H_L\), so \(\mathcal D_L\) is densely defined.

## 4. Closedness of the weighted Fourier form

Define

\[
a_{0,L}[f]
:=
\int_{\mathbb R}w(r)|\widehat f(r)|^2\,dr,
\qquad f\in\mathcal D_L.
\tag{4.1}
\]

Equip \(\mathcal D_L\) with the graph norm

\[
\|f\|_{\mathcal D_L}^2
=
\|f\|_2^2+a_{0,L}[f].
\tag{4.2}
\]

### Lemma 4.1

`(D_L, ||.||_{D_L})` is complete; hence `a_{0,L}` is a densely defined closed nonnegative quadratic form on `H_L`.

### Proof

Let \(f_j\) be Cauchy in (4.2). Then \(f_j\to f\) in \(L^2\) for some \(f\in H_L\), because \(H_L\) is closed.

The weighted Fourier transforms are Cauchy in \(L^2(w(r)dr)\), hence converge to some \(g\) in that space. Since \(w\ge1\), this also gives ordinary \(L^2(dr)\) convergence.

Paper-Plancherel makes the Fourier transform a constant multiple of an \(L^2\)-unitary map, so \(\widehat f_j\to\widehat f\) in ordinary \(L^2\). Uniqueness of the \(L^2\) limit gives \(g=\widehat f\) almost everywhere. Thus \(f\in\mathcal D_L\) and \(f_j\to f\) in the graph norm. ∎

## 5. Compact embedding of the form domain

This is the key fixed-support fact.

### Theorem 5.1

The embedding

\[
\mathcal D_L\hookrightarrow H_L
\tag{5.1}
\]

is compact.

### Proof

Consider a sequence \(f_j\) bounded in the graph norm. Then:

1. **Physical-space tightness is automatic.** Every \(f_j\) is supported in the same compact interval \(I_L\).

2. **Fourier tails are uniformly small.** For every \(R>0\),
   \[
   \int_{|r|>R}|\widehat f_j(r)|^2dr
   \le
   \frac{1}{\inf_{|r|>R}w(r)}
   \int_{\mathbb R}w(r)|\widehat f_j(r)|^2dr.
   \tag{5.2}
   \]
   The numerator is uniformly bounded in \(j\), while the denominator tends to \(+\infty\) by (3.1). Hence the Fourier tails vanish uniformly as \(R\to\infty\).

3. **Translations are uniformly continuous in \(L^2\).** By Plancherel,
   \[
   \|f_j(\cdot+h)-f_j\|_2^2
   =
   \frac1{2\pi}
   \int_{\mathbb R}
   |e^{irh}-1|^2|\widehat f_j(r)|^2dr.
   \tag{5.3}
   \]
   Split at \(|r|\le R\). On the bounded-frequency part,
   \(\sup_{|r|\le R}|e^{irh}-1|\to0\) as \(h\to0\), uniformly in \(j\). On the tail, use \(|e^{irh}-1|\le2\) together with (5.2). Thus
   \[
   \sup_j\|f_j(\cdot+h)-f_j\|_2\to0
   \qquad(h\to0).
   \tag{5.4}
   \]

Fixed tightness plus uniform translation continuity is exactly the Kolmogorov–Riesz compactness criterion in \(L^2(\mathbb R)\). Therefore every bounded sequence in \(\mathcal D_L\) has an \(L^2\)-convergent subsequence. ∎

## 6. Gamma form is closed and semibounded

Define

\[
a_{\Gamma,L}[f]
=
\int_{\mathbb R}\mu(r)|\widehat f(r)|^2dr.
\tag{6.1}
\]

Since \(\mu=w+m_0-1\), paper-Plancherel gives

\[
a_{\Gamma,L}[f]
=
a_{0,L}[f]
+2\pi(m_0-1)\|f\|_2^2.
\tag{6.2}
\]

Thus `a_{Γ,L}` is closed on the same domain and bounded below by a finite multiple of \(\|f\|_2^2\).

## 7. Pole form is a bounded finite-rank perturbation

Define the bounded linear functionals on \(H_L\)

\[
C_L(f)=\int_{I_L}f(x)\cosh(x/2)dx,
\qquad
S_L(f)=\int_{I_L}f(x)\sinh(x/2)dx.
\]

Cauchy–Schwarz gives

\[
|C_L(f)|\le \|f\|_2\,\|\cosh(x/2)\|_{L^2(I_L)},
\]

\[
|S_L(f)|\le \|f\|_2\,\|\sinh(x/2)\|_{L^2(I_L)}.
\]

Hence

\[
P_L[f]=2|C_L(f)|^2-2|S_L(f)|^2
\tag{7.1}
\]

is a bounded real quadratic form of rank at most two on \(H_L\).

Therefore

\[
a_{AP,L}:=a_{\Gamma,L}+P_L
\tag{7.2}
\]

is densely defined, closed, symmetric, and semibounded on \(\mathcal D_L\), with exactly the same form domain.

## 8. Associated operator has compact resolvent

By the first representation theorem for closed semibounded quadratic forms, there is a unique semibounded self-adjoint operator \(A_{AP,L}\) associated with \(a_{AP,L}\).

A standard form-theoretic compactness criterion says that if the form domain of a semibounded closed form is compactly embedded in the ambient Hilbert space, then the associated self-adjoint operator has compact resolvent. Theorem 5.1 supplies precisely this hypothesis.

Therefore:

\[
(A_{AP,L}+cI)^{-1}
\quad\text{is compact for sufficiently large }c>0.
\tag{8.1}
\]

Equivalently, the spectrum of \(A_{AP,L}\) is purely discrete, every eigenvalue has finite multiplicity, and the eigenvalues tend to \(+\infty\).

References for the standard form theorem/criterion include Kato's first representation theorem and standard compact-resolvent form criteria; modern examples routinely use the implication “compact embedding of form domain \(\Rightarrow\) compact resolvent.”

## 9. Main theorem: finite nonpositive index

### Theorem `W-AP-FINITEINDEX`

For every fixed \(L>0\), the nonpositive spectral subspace

\[
F_L
:=
\mathbf 1_{(-\infty,0]}(A_{AP,L})H_L
\tag{9.1}
\]

is finite dimensional.

Moreover, if

\[
H_L=F_L\oplus F_L^\perp,
\]

then there exists a constant \(c_L>0\) such that

\[
a_{AP,L}[f]\ge c_L\|f\|_2^2
\tag{9.2}
\]

for every \(f\in\mathcal D_L\cap F_L^\perp\).

### Proof

Compact resolvent and semiboundedness imply that the eigenvalues of \(A_{AP,L}\), repeated with multiplicity, form a discrete sequence tending to \(+\infty\). Hence only finitely many eigenvalues can lie in \(( -\infty,0]\), proving \(\dim F_L<\infty\).

On the orthogonal complement, the spectrum is bounded below by the first strictly positive eigenvalue \(c_L\). The spectral theorem then gives (9.2). ∎

## 10. What this changes in Route W-A

The old target

> find a positive local diagonal energy on every block

was too strong and, in its Gamma-only version, false.

The correct fixed-support architecture is now:

\[
H_L=F_L\oplus F_L^\perp,
\qquad \dim F_L<\infty,
\tag{10.1}
\]

with:

- exact finite-dimensional treatment on \(F_L\);
- positive coercivity \(c_L\) on \(F_L^\perp\);
- prime-shift couplings handled as a perturbation of this split form.

This naturally suggests a Schur-complement / finite-certificate strategy.

## 11. Proposed certificate architecture

At fixed \(L\), a candidate positivity certificate for the **full** Weil form could contain:

1. an explicit finite-dimensional basis approximating/capturing \(F_L\), with rigorous enclosure if used as proof data;
2. a certified lower bound \(c_L\) on the complement;
3. certified operator/cross-block bounds for the finite prime-shift sector;
4. a finite Hermitian Schur-complement matrix proving positivity on the bad sector after coupling;
5. a theorem converting these data into \(Q_L[f]\ge0\) for every admissible \(f\) supported in \(I_L\).

The general checker/soundness theorem should be proved independently of any numerically generated certificate.

## 12. The hard wall has moved, not disappeared

This theorem is **fixed-L**.

Nothing here proves that:

- \(\dim F_L\) is uniformly bounded as \(L\to\infty\);
- \(c_L\) stays uniformly positive;
- prime-shift coupling norms remain uniformly controlled;
- a finite set of certificates covers all \(L\);
- the full Weil form is positive;
- RH follows.

Indeed, early finite-basis numerics suggest that the number of negative archimedean+pole directions grows with \(L\), so a uniform fixed-rank correction is not currently plausible.

The next theorem-strength question is therefore not “is the local form positive?” but:

> Can the growing finite-index bad sector and the prime-shift couplings be controlled by a recursive/uniform structure strong enough to globalize over all support scales?

That is a substantially sharper target than the original local-coercivity slogan.

## 13. Formalization targets

- `W-AP-DOMAIN`: define the fixed-support weighted Fourier form domain.
- `W-AP-CLOSED`: prove closedness/semiboundedness.
- `W-AP-COMPACT`: formalize compact embedding, likely via a suitable Mathlib compactness theorem or a custom Kolmogorov–Riesz bridge.
- `W-AP-POLE-BOUNDED`: prove the rank-two pole perturbation is bounded.
- `W-AP-FINITEINDEX`: obtain finite nonpositive spectral subspace from compact resolvent.
- `W-LOCAL-02`: coercivity on `F_L^⊥`.

These are local auxiliary results. Their successful formalization must not be promoted into evidence for the unresolved global RH node beyond the exact implications recorded above.
