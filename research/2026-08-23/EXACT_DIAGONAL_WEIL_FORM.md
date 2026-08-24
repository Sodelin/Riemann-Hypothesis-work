# Exact Diagonal Weil-Form Decomposition

**Claim ID:** `W-DIAG-01`  
**Status:** `PROVED_SYMBOLIC` from the displayed upstream definitions; Lean formalization still `LEAN_TARGET`.  
**Purpose:** replace the schematic “prime graph” picture by the exact diagonal algebra before any positivity estimate is attempted.

## 1. Upstream normalization

In `anthropics/zeta-23-lean/Zeta23/ExplicitFormula.lean`, for a compactly supported `C^2` test function `k`, the literature right-hand side is

\[
\operatorname{RHS}(k)
=
\widehat k(i/2)+\widehat k(-i/2)
-
\sum_{n\ge 1}\frac{\Lambda(n)}{\sqrt n}
\bigl(k(\log n)+k(-\log n)\bigr)
+
\frac1{2\pi}\int_{\mathbb R}\widehat k(r)\,G(r)\,dr,
\]

where

\[
G(r)=\Re\psi\!\left(\frac14+\frac{ir}{2}\right)-\log\pi,
\]

and the paper Fourier transform convention is

\[
\widehat f(z)=\int_{\mathbb R} f(u)e^{izu}\,du.
\]

The upstream file defines

\[
\widetilde f(u)=\overline{f(-u)},
\qquad
k=f\star\widetilde f,
\]

and proves

\[
\widehat{k}(z)
=
\widehat f(z)\,\overline{\widehat f(\overline z)}.
\]

## 2. Autocorrelation identity

For the diagonal test `k=f⋆f̃`, direct expansion gives

\[
k(a)
=
\int_{\mathbb R} f(t)\overline{f(t-a)}\,dt.
\tag{2.1}
\]

Therefore

\[
k(-a)=\overline{k(a)}.
\tag{2.2}
\]

For real `r`, the Fourier-factorization identity gives

\[
\widehat{k}(r)=|\widehat f(r)|^2.
\tag{2.3}
\]

## 3. Exact prime-shift sector

By (2.2),

\[
k(\log n)+k(-\log n)
=2\Re k(\log n).
\]

Using (2.1), the prime contribution is exactly

\[
-2\sum_{n\ge1}\frac{\Lambda(n)}{\sqrt n}
\Re\int_{\mathbb R}
 f(t)\overline{f(t-\log n)}\,dt.
\tag{3.1}
\]

Equivalently, with translation

\[
(\tau_a f)(t)=f(t-a),
\]

this is

\[
-2\sum_{n\ge1}\frac{\Lambda(n)}{\sqrt n}
\Re\langle f,\tau_{\log n}f\rangle.
\tag{3.2}
\]

For compactly supported `f`, only finitely many prime-power shifts can contribute because `k` is compactly supported. This is the exact arithmetic-sparsity fact behind Route A.

## 4. Exact pole sector

Define

\[
A:=\widehat f(i/2),
\qquad
B:=\widehat f(-i/2).
\]

Then

\[
\widehat k(i/2)=A\overline B,
\qquad
\widehat k(-i/2)=B\overline A,
\]

so the two pole terms are

\[
A\overline B+B\overline A
=2\Re(A\overline B).
\tag{4.1}
\]

Diagonalizing the rank-two Hermitian form,

\[
2\Re(A\overline B)
=
\frac{|A+B|^2-|A-B|^2}{2}.
\tag{4.2}
\]

Because

\[
A=\int f(u)e^{-u/2}\,du,
\qquad
B=\int f(u)e^{u/2}\,du,
\]

we may also write

\[
A+B=2\int f(u)\cosh(u/2)\,du,
\]

\[
A-B=-2\int f(u)\sinh(u/2)\,du.
\]

Hence the pole sector is exactly

\[
2\left|
\int f(u)\cosh(u/2)\,du
\right|^2
-
2\left|
\int f(u)\sinh(u/2)\,du
\right|^2.
\tag{4.3}
\]

**Structural consequence:** the pole contribution is finite rank and indefinite, with one positive and one negative moment direction before degeneracies are considered. It must not be dropped or replaced by a positive scalar envelope.

## 5. Exact Gamma sector

For real `r`, (2.3) turns the archimedean integral into

\[
\frac1{2\pi}
\int_{\mathbb R}
|\widehat f(r)|^2
\left[
\Re\psi\!\left(\frac14+\frac{ir}{2}\right)-\log\pi
\right]dr.
\tag{5.1}
\]

The multiplier in brackets is **not pointwise nonnegative**. At `r=0`, the classical quarter-argument digamma identity gives

\[
\psi(1/4)=-\gamma-\frac\pi2-3\log2,
\]

so

\[
G(0)
=-\gamma-\frac\pi2-3\log2-\log\pi<0.
\tag{5.2}
\]

A numerical diagnostic places the first positive crossing near

\[
r\approx 6.2898359888369,
\]

but this decimal is `NUMERICAL` only and is not needed for (5.2).

**Route consequence:** `W-LOCAL-01` cannot simply declare the Gamma multiplier to be a positive diagonal energy. Any useful coercive block must exploit support uncertainty, combine the Gamma sector with the finite-rank pole sector, retain signed couplings, or use another genuinely positive reference form.

## 6. Combined exact diagonal formula

Putting the three sectors together,

\[
\boxed{
\begin{aligned}
\operatorname{RHS}(f\star\widetilde f)
={}&
2\Re\!\left(
\widehat f(i/2)\overline{\widehat f(-i/2)}
\right)\\
&-2\sum_{n\ge1}\frac{\Lambda(n)}{\sqrt n}
\Re\langle f,\tau_{\log n}f\rangle\\
&+\frac1{2\pi}\int_{\mathbb R}
|\widehat f(r)|^2G(r)\,dr.
\end{aligned}}
\tag{6.1}
\]

Subject to the upstream explicit-formula hypotheses, this is the exact prime/Gamma/pole side of the diagonal Weil form in the selected convention.

## 7. Immediate formalization targets

### `W-DIAG-AUTOCORR`
Prove in Lean:

`weilTest f f a = ∫ t, f t * conj (f (t-a))`.

### `W-DIAG-HERMITIAN`
Prove:

`weilTest f f (-a) = conj (weilTest f f a)`.

### `W-DIAG-REALFT`
Reuse/derive from upstream `paperFT_weilTest`:

for real `r`, `paperFT (weilTest f f) r = |paperFT f r|^2` in the correct complex-valued representation.

### `W-DIAG-POLE`
Prove the rank-two identities (4.1)-(4.3).

### `W-DIAG-PRIME`
Rewrite the finite prime sum as real translation correlations.

### `W-DIAG-FULL`
Assemble (6.1) directly from the upstream literature formula.

All are `LEAN_TARGET` until actually compiled.

## 8. New adversarial question

The next route question is now sharper than “can we prove local coercivity?”

> Can the **archimedean-plus-rank-two pole operator**, restricted to a compact support cell or a carefully chosen finite union of cells, supply a quantitative lower bound that can absorb the signed prime-shift graph?

That question may have a negative answer. It is now precise enough to attack by exact finite models, analytic inequalities, and eventually Lean.
