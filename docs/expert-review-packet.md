# Expert Review Packet: Finite Generalized Laguerre Inequalities for Strictly Log-Concave Admissible Fourier Kernels

**Status:** AI-generated research lead; internally cross-checked, not independently verified, not ready for citation or submission  
**Date:** 2026-08-01  
**Purpose:** private correctness, prior-art, and usefulness review  
**Not claimed:** a proof of the Riemann hypothesis

## 1. The narrow question for a reviewer

Does the theorem below follow from the construction as written? If so, is the all-\(N\), fully admissible version already known, and is it useful enough to merit a short note?

The broad claim that any finite prefix of the generalized Laguerre inequalities is insufficient is **not new**. Muranaka proved it in \(\mathrm{L\!-\!P}^{*}\). The only possible contribution here is the simultaneous strengthening to every finite \(N\), a fully admissible and strictly log-concave Fourier kernel, and nonreal zeros confined to an arbitrarily thin horizontal strip.

## 2. Definitions

For a real entire function \(f\), define

\[
L_n[f](x)=\frac1{(2n)!}
\sum_{k=0}^{2n}(-1)^{n+k}\binom{2n}{k}
f^{(k)}(x)f^{(2n-k)}(x).
\]

Equivalently,

\[
f(x+iy)f(x-iy)=\sum_{n\ge0}L_n[f](x)y^{2n}.
\]

An **admissible kernel** is taken in Csordas’s sense: a \(C^\infty\) function \(\psi:\mathbb R\to(0,\infty)\) that is even, strictly decreasing on \((0,\infty)\), and whose every derivative satisfies a super-Gaussian tail bound

\[
\psi^{(j)}(t)=O_j\!\left(e^{-|t|^{2+\varepsilon}}\right)
\]

for some \(\varepsilon>0\). Its Fourier transform is

\[
\widehat\psi(z)=\int_{\mathbb R}\psi(t)e^{izt}\,dt.
\]

Strict logarithmic concavity is **not** required by this definition, but the construction below additionally satisfies it.

## 3. Candidate theorem

> **Candidate theorem.** For every integer \(N\ge1\) and every \(\tau>0\), there is an admissible kernel \(\Psi_{N,\tau}\) such that:
>
> 1. \(\Psi_{N,\tau}\) is strictly log-concave on \(\mathbb R\);
> 2. every zero of \(\widehat\Psi_{N,\tau}\) lies in \(|\operatorname{Im}z|\le\tau\);
> 3. \(\widehat\Psi_{N,\tau}\) has nonreal zeros; and
> 4. \(L_n[\widehat\Psi_{N,\tau}](x)\ge0\) for every real \(x\) and every \(0\le n\le N\).

If correct, the theorem shows that no finite truncation of the complete Laguerre hierarchy forces real-rootedness, even after imposing the standard admissible-kernel hypotheses, global strict log-concavity, and an arbitrarily thin a priori zero strip.

## 4. Construction and proof

Fix \(M=N+1\) and set

\[
P(z)=A(z)B(z),
\qquad
A(z)=\cos(Rz)^M,
\qquad
B(z)=1+\frac12\cos z,
\]

where \(R>0\) will be chosen sufficiently large.

### 4.1 The first \(N\) Laguerre inequalities

Put \(r=\cos^2(Rx)\). Then

\[
A(x+iy)A(x-iy)
=\left(r+\sinh^2(Ry)\right)^M
=\sum_{n\ge0}A_n(r)y^{2n}.
\]

Writing \(A_n(r)=R^{2n}a_n(r)\), the coefficient of \(u^{2n}\) in \((r+\sinh^2u)^M\) gives, for \(1\le n\le N=M-1\),

\[
a_n(r)\ge\binom Mn r^{M-n},
\]

while

\[
a_{n-1}(r)
\le C_{M,n-1}r^{M-n+1},
\qquad
C_{M,j}=[u^{2j}]\cosh^{2M}u.
\]

For \(0<r\le1\), therefore,

\[
\frac{A_{n-1}(r)}{A_n(r)}
\le
\frac{C_{M,n-1}}{R^2\binom Mn}.
\]

At \(r=0\), both coefficients vanish because \(n<M\). For example, choose

\[
R\ge1,
\qquad
R^2\ge
\max_{1\le n\le N}
\frac{C_{M,n-1}}{\binom Mn}.
\]

Then

\[
A_n(r)\ge A_{n-1}(r)
\qquad(1\le n\le N,\ 0\le r\le1).
\]

For \(q=\cos x\), write

\[
B(x+iy)B(x-iy)=\sum_{k\ge0}b_k(x)y^{2k}.
\]

Direct expansion gives

\[
b_0=\left(1+\frac q2\right)^2\ge\frac14,
\qquad
b_k=\frac{q+2^{2k-3}}{(2k)!}\quad(k\ge1).
\]

Thus \(b_1\ge-1/4\) and \(b_k\ge0\) for \(k\ge2\). The coefficient product law now yields, for \(1\le n\le N\),

\[
\begin{aligned}
L_n[P](x)
&=\sum_{j=0}^n A_j(r)b_{n-j}(x)\\
&\ge \frac14\{A_n(r)-A_{n-1}(r)\}\ge0.
\end{aligned}
\]

Also \(L_0[P](x)=P(x)^2\ge0\).

### 4.2 Positive-measure origin and nonreal zeros

The function \(\cos(Rz)^M\) is the Fourier transform of a scaled symmetric Rademacher-sum measure, and

\[
1+\frac12\cos z

\]

is the Fourier transform of the positive symmetric measure

\[
\delta_0+\frac14\delta_1+\frac14\delta_{-1}.
\]

Hence \(P\) is the Fourier transform of a positive symmetric finite measure with bounded support. Its \(B\)-factor has the nonreal zeros

\[
z=(2k+1)\pi\pm i\eta,
\qquad
\eta=\operatorname{arcosh}2,
\]

while the zeros of the cosine factor are real.

### 4.3 Scaling and smoothing

Set \(P_\delta(z)=P(\delta z)\). Scaling gives

\[
L_n[P_\delta](x)=\delta^{2n}L_n[P](\delta x)\ge0
\qquad(0\le n\le N).
\]

Let

\[
h_\lambda(t)=e^{-(t/\lambda)^4},
\qquad
H_\lambda(z)=\widehat h_\lambda(z).
\]

Pólya–Newman theory gives \(H_\lambda\in\mathrm{L\!-\!P}\). One route is Newman’s theorem for \(e^{-at^4-\beta t^2}\) with \(\beta>0\), followed by \(\beta\downarrow0\) and Hurwitz’s theorem. Therefore

\[
L_j[H_\lambda](x)\ge0
\qquad(j\ge0),
\]

and the product identity implies

\[
L_n[H_\lambda P_\delta](x)
=\sum_{j=0}^nL_j[H_\lambda](x)L_{n-j}[P_\delta](x)
\ge0
\]

for every \(n\le N\).

If \(X\) has the normalized positive measure represented by \(P\), the inverse Fourier kernel of \(H_\lambda P_\delta\), up to a positive constant, is

\[
\Psi_{\lambda,\delta}(t)
=\mathbb E\exp\!\left[-\left(\frac{t-\delta X}{\lambda}\right)^4\right].
\]

It is positive, even, and smooth. Since \(X\) has bounded support, every derivative is a finite average of a polynomial times a translated quartic exponential. Hence, for some \(c>0\),

\[
\Psi_{\lambda,\delta}^{(j)}(t)
=O_j(e^{-c|t|^4})
=O_j(e^{-|t|^3}).
\]

### 4.4 Strict decrease

Let \(|X|\le S\), \(u=t/\lambda\), and \(\varepsilon=\delta/\lambda\). Then

\[
\Psi'_{\lambda,\delta}(t)
=-\frac4\lambda
\mathbb E[(u-\varepsilon X)^3e^{-(u-\varepsilon X)^4}].
\]

For \(u\ge\varepsilon S\), the expectation is strictly positive. For \(0<u<\varepsilon S\), put \(u=\varepsilon y\) and define

\[
G_\varepsilon(y)
=\mathbb E[(y-X)^3e^{-\varepsilon^4(y-X)^4}].
\]

Symmetry makes \(G_\varepsilon\) odd, and compact-uniform convergence of the derivative gives

\[
\frac{G_\varepsilon(y)}y
=\int_0^1G_\varepsilon'(\theta y)\,d\theta
\longrightarrow y^2+3\mathbb E[X^2]>0
\]

uniformly for \(0\le y\le S\). Thus \(\Psi'_{\lambda,\delta}(t)<0\) for every \(t>0\) once \(\lambda/\delta\) is sufficiently large.

### 4.5 Strict log-concavity

The same scale choice can be made globally strictly log-concave. Let \(Z\) be a nondegenerate symmetric finite-support variable in \([-1,1]\), with \(1\) in its support, and define

\[
p=\Pr(Z=1),\qquad
d=\min_{z\in\operatorname{supp}Z,\ z<1}(1-z),\qquad
K=\frac{1-p}{p}.
\]

Symmetry gives \(p\le1/2\), hence \(K\ge1\) and the logarithm below is positive.

For \(\psi_a(u)=\mathbb E e^{-(u-aZ)^4}\), put \(c=1/10\). We claim that \((\log\psi_a)''<0\) on \(\mathbb R\) whenever

\[
0<a^2<
\min\left\{
\frac1{6\sqrt3},
\frac1{20},
\frac{3d}{4000},
\frac{d}{2000\log((169/75)K)}
\right\}.
\tag{1}
\]

Under the probability law obtained by tilting \(Z\) by \(e^{-(u-aZ)^4}\), set \(Y=u-aZ\). Direct differentiation gives

\[
(\log\psi_a)''(u)
=16\operatorname{Var}(Y^3)-12\mathbb EY^2.
\tag{2}
\]

Symmetry reduces the proof to \(u\ge0\). Three regions suffice.

For \(0\le u\le2a\), \(|Y|\le3a\), and therefore

\[
(\log\psi_a)''(u)
\le(1296a^4-12)\mathbb EY^2<0.
\]

For \(2a\le u\le c/a\), Popoviciu’s inequality and \(a\le u/2\) give

\[
\operatorname{Var}(Y^3)
\le\frac14\bigl((u+a)^3-(u-a)^3\bigr)^2
\le\frac{169}{16}a^2u^4,
\]

while \(\mathbb EY^2\ge(u-a)^2\ge u^2/4\). Hence

\[
(\log\psi_a)''(u)
\le u^2(169c^2-3)<0.
\]

For \(u\ge c/a\), put \(v=u-a\). The second bound in (1) implies \(v\ge c/(2a)\ge a\). Convexity of \(y\mapsto y^4\) gives, for every support point \(z<1\),

\[
(u-az)^4-v^4\ge4adv^3.
\]

If \(q\) is the tilted probability of \(Z<1\), then \(q\le K e^{-4adv^3}\). Since \(Y\in[v,v+2a]\),

\[
\operatorname{Var}(Y^3)
\le676K a^2v^4e^{-4adv^3},
\]

and \(\mathbb EY^2\ge v^2\). Thus

\[
(\log\psi_a)''(u)
\le12v^2\left[
\frac{2704}{3}Ka^2v^2e^{-4adv^3}-1
\right].
\]

The third bound in (1) makes \(a^2v^2e^{-4adv^3}\) decreasing from \(v=c/(2a)\) onward. The fourth gives

\[
\frac{2704}{3}Ka^2v^2e^{-4adv^3}
\le
\frac{169}{75}K e^{-d/(2000a^2)}<1.
\]

This proves the lemma.

For this packet’s measure,

\[
X=R\sum_{j=1}^{M}\varepsilon_j+Y_0,
\]

where the \(\varepsilon_j\) are independent equiprobable signs and \(\Pr(Y_0=0)=2/3\), \(\Pr(Y_0=\pm1)=1/6\). With \(S=MR+1\) and \(Z=X/S\), the condition \(R\ge1\) gives

\[
p=\frac1{6\cdot2^M},
\qquad
d=\frac1S,
\qquad
K=6\cdot2^M-1.
\]

Moreover,

\[
\Psi_{\lambda,\delta}(\lambda u)
=\mathbb E e^{-(u-aZ)^4},
\qquad
a=\frac{\delta S}{\lambda}.
\]

After \(\delta\) fixes the zero strip, \(\lambda\) can be increased until (1) holds. Therefore

\[
\frac{d^2}{dt^2}\log\Psi_{\lambda,\delta}(t)
=\frac1{\lambda^2}(\log\psi_a)''(t/\lambda)<0
\]

for every real \(t\).

### 4.6 Zero strip

The nonreal zeros inherited from \(B(\delta z)\) are

\[
z=\frac{(2k+1)\pi\pm i\eta}{\delta}.
\]

Choose \(\delta\ge\eta/\tau\), and then choose \(\lambda\) large enough for strict decrease and condition (1). The cosine factor and \(H_\lambda\) have only real zeros, so all zeros lie in \(|\operatorname{Im}z|\le\tau\), and some are nonreal. This completes the proposed proof.

## 5. Closest located prior art

1. **Muranaka (2003), Theorem 2.5 with Appendix 10.1.** For every \(N\), the explicit function
   \[
   g_N(z)=e^{-z^2}(z^2+b_N),
   \qquad b_N=\frac12(N+\sqrt N),
   \]
   belongs to \(\mathrm{L\!-\!P}^{*}\), satisfies the first \(N\) extended Laguerre inequalities globally, and fails the next. This fully anticipates the broad finite-prefix obstruction.

2. **Csordas (2014), Example 3.12.** The kernel
   \[
   \varphi(t)=e^{-t^2}(15+t^2+t^4)
   \]
   is positive, even, strictly decreasing, and strictly log-concave; its transform has nonreal zeros while \(L_1\ge0\). It fails the super-Gaussian derivative-tail clause, so it is not fully admissible under Csordas’s definition.

No exact precedent was located for the all-\(N\), fully admissible, strictly-log-concave construction. That statement is a search result, **not** a novelty certificate. MathSciNet, zbMATH, and specialist knowledge are still required.

Primary links:

- Muranaka thesis: https://scholarspace.manoa.hawaii.edu/items/b4074696-4315-4790-9687-08dcb2e9a0e7
- Csordas 2014: https://arxiv.org/abs/1309.0055
- Newman 1976: https://www.math.northwestern.edu/~auffing/papers/Newman.pdf

## 6. Requested audit

Please check these points independently:

1. Does the coefficient bound for \(A_n/A_{n-1}\) remain uniform at \(r=0\)?
2. Does the \(\beta\downarrow0\) Hurwitz argument establish \(\widehat{e^{-t^4}}\in\mathrm{L\!-\!P}\) with all required nondegeneracy details?
3. Is the strict-decrease argument uniform on the shrinking region \(0<t<\delta S\)?
4. Does the three-region proof in §4.5 establish strict log-concavity globally, including its endpoint atom, support-gap, and scaling claims?
5. Does multiplication by \(H_\lambda\) preserve every claimed Laguerre inequality and the exact zero-strip statement?
6. Is there earlier work proving this all-\(N\), fully admissible, strictly-log-concave version?
7. If correct and not already known, is this sufficiently useful to circulate as a short route-exclusion note?

A negative answer—proof error, exact precedent, or insufficient interest—is a successful review outcome and should stop public circulation.

## 7. Attribution and disclosure

This packet was produced through a multi-instance generative-AI research process initiated and curated by a human user. The human contribution includes conceptualization, search-protocol design, project administration, and curation. The mathematical derivation has not yet been reconstructed by a qualified human expert. Model agreement is not independent peer review.

If the result survives expert review, any manuscript should:

- identify only humans who meet the venue’s authorship standard as authors;
- disclose significant generative-AI assistance and the verification performed;
- describe contributions accurately, for example with CRediT roles; and
- avoid any claim that this proves or materially advances the Riemann hypothesis itself.

## 8. Suggested private inquiry

**Subject:** Private correctness/prior-art question on finite Laguerre inequalities for admissible kernels

Dear Professor [Name],

I am asking for a narrow private check of an AI-generated mathematical argument, not announcing a result. The attached note claims that for every finite \(N\), one can construct a fully admissible, strictly log-concave Fourier kernel whose transform has nonreal zeros but satisfies the first \(N\) generalized Laguerre inequalities globally. Muranaka already proved the broad finite-prefix phenomenon in \(\mathrm{L\!-\!P}^{*}\); the possible strengthening is the fully admissible, strictly-log-concave all-\(N\) construction.

Would you be willing to say whether (a) the proof has an obvious flaw, (b) this exact strengthening is already known, and (c) it would be useful if correct? I am not a specialist and will not circulate it publicly without qualified human verification. Generative AI produced and cross-checked the derivation; no independent peer review has occurred.

Thank you for any brief guidance.

Sincerely,  
[Name]
