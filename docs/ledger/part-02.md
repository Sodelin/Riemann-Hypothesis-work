\frac{\Lambda(\frac12+\sqrt c)}
{\Lambda(\frac12+\sqrt{c+\sigma})}.
\tag{A6}
\]

The first factor is the Laplace transform of an exponential random variable with rate

\[
r=c-\frac14.
\]

To continue from \(w=c\) to the center \(w=0\), one needs \(\sigma=-c\), which corresponds to the exponential tilt \(\mathbb E[e^{cH}]\). But an \(\operatorname{Exp}(r)\) moment-generating function is finite only for tilt parameters below \(r\), and

\[
c>c-\frac14=r.
\]

For the common anchor \(c=1\), this is exactly the \(\operatorname{Exp}(3/4)\) mode and the divergent moment \(\mathbb E[e^H]\).

Could one remove that exponential mode, tilt the remainder, and put the pole cancellation back later? No—not while preserving a positive Laplace representation. The function \(\Lambda(s)\) has a pole at \(s=1\), corresponding to \(w=1/4\). Therefore

\[
R_c\!\left(\frac14-c\right)=0.
\tag{A7}
\]

If \(R_c(\sigma)=\mathbb E[e^{-\sigma Y}]\) for a positive law whose required exponential moment exists, then at the same real point

\[
R_c\!\left(\frac14-c\right)
=\mathbb E\!\left[e^{(c-1/4)Y}\right]>0.
\tag{A8}
\]

It may be infinite, but it cannot be zero. Equations (A7) and (A8) contradict each other.

**No-go conclusion.** Pole cancellation must occur before a positive probabilistic factorization is asserted. Once it occurs first, proving that the reciprocal remainder is Thorin/HCM is again essentially the unresolved real-zero problem; the low-rate atom has not supplied a shortcut.

The 2026 revision of Polson's [broader Thorin/van Dantzig paper](https://arxiv.org/abs/1804.10043) explicitly includes closure under exponential tilting only when the tilted moment is finite, which is precisely the condition violated here.

## 6. Route B: exact formalization of the two-copy kernel

The newest visible route begins with

\[
F(z)=\int_{\mathbb R}\Phi(u)e^{izu}\,du.
\]

Differentiate under the integral:

\[
F'(z)=i\int_{\mathbb R}u\Phi(u)e^{izu}\,du,
\qquad
F''(z)=-\int_{\mathbb R}u^2\Phi(u)e^{izu}\,du.
\]

Define the first Laguerre expression

\[
L_1(z):=F'(z)^2-F(z)F''(z).
\]

After multiplying the integrals and symmetrizing in \(u,v\),

\[
L_1(z)
=\frac12\int_{\mathbb R^2}(u-v)^2
\Phi(u)\Phi(v)e^{iz(u+v)}\,du\,dv.
\]

Use

\[
t=u+v,\qquad s=v,
\]

so \(u=t-s\) and \(u-v=t-2s\). Then

\[
L_1(z)=\frac12\int_{\mathbb R}\nu_2(t)e^{izt}\,dt,
\]

where

\[
\boxed{
\nu_2(t)=\int_{\mathbb R}(t-2s)^2\Phi(t-s)\Phi(s)\,ds.}
\tag{B1}
\]

This derivation is correct. It identifies the mathematical object precisely: \(\nu_2\) is the Fourier kernel of the first generalized Laguerre inequality.

## 7. Exact obstruction to the proposed decreasing-and-convex certificate

The other thread proposed finding \(\alpha\) such that

\[
h_\alpha(t):=\cosh(\alpha t)\nu_2(t)
\tag{B2}
\]

is both decreasing and convex for every \(t>0\), so that a classical Fourier-positivity criterion could be applied.

Because \(\Phi\) is smooth, even, and rapidly decreasing, \(\nu_2\) is also smooth and even. Hence \(h_\alpha\) is smooth and even for every finite \(\alpha\), and

\[
h_\alpha'(0)=0.
\tag{B3}
\]

If \(h_\alpha\) is convex on \((0,\infty)\), its derivative is nondecreasing. Smoothness at zero then gives

\[
h_\alpha'(t)\ge h_\alpha'(0+)=0
\qquad(t>0).
\tag{B4}
\]

If it is also decreasing, then

\[
h_\alpha'(t)\le0.
\tag{B5}
\]

Together, (B4) and (B5) force \(h_\alpha'(t)=0\) for all \(t>0\), so \(h_\alpha\) is constant. But \(h_\alpha\) is nonzero near zero and tends to zero at infinity because \(\nu_2\) is super-exponentially decreasing. Contradiction.

Therefore:

\[
\boxed{\text{No real }\alpha\text{ can make }\cosh(\alpha t)\nu_2(t)
\text{ both decreasing and convex on all }t>0.}
\]

**Plain-language translation.** The graph begins flat because it is mirror-symmetric. Convexity says its slope can only rise from that flat value. Decrease requires the slope to be negative. Those instructions point in opposite directions.

Classical decreasing-convex Fourier criteria can accommodate an even function with a cusp at zero, such as \(e^{-|t|}\). They cannot hold globally for a nonconstant smooth even kernel. This local regularity check should precede any global estimates.

## 8. Why the first Laguerre inequality is not enough

If every zero of \(F\) is real, then for real \(x\)

\[
L_1(x)=F'(x)^2-F(x)F''(x)\ge0.
\tag{B6}
\]

The converse is false. Take

\[
p(x)=x^4-1=(x-1)(x+1)(x-i)(x+i).
\]

This polynomial has the nonreal zeros \(\pm i\), but

\[
(p')^2-pp''
=16x^6-12x^2(x^4-1)
=4x^6+12x^2
\ge0
\]

for every real \(x\).

Thus positivity of the Fourier transform of \(\nu_2\), even if established, would prove only one necessary shadow of RH. George Csordas's [primary paper on positive-definite kernels and the Riemann xi function](https://arxiv.org/abs/1309.0055) treats \(L_1\ge0\) for xi as an open problem and characterizes real-rootedness using the full generalized hierarchy; it also gives examples showing that the first associated kernel can pass while a higher one fails.

## 9. The corrected hierarchy-first target

For \(n\ge0\), define the generalized Laguerre expressions

\[
L_n(x):=
\frac{1}{(2n)!}
\sum_{j=0}^{2n}
(-1)^{j+n}\binom{2n}{j}
F^{(j)}(x)F^{(2n-j)}(x).
\tag{C1}
\]

The corresponding two-copy kernels are

\[
K_n(t):=
\int_{\mathbb R}(t-2s)^{2n}
\Phi(t-s)\Phi(s)\,ds.
\tag{C2}
\]

The same calculation as in §6 gives

\[
L_n(x)=\frac1{(2n)!}
\int_{\mathbb R}K_n(t)e^{ixt}\,dt.
\tag{C3}
\]

For the Riemann xi function, the meaningful exact target is

\[
K_n\text{ is positive definite for every }n\ge0,
\tag{C4}
\]

equivalently

\[
L_n(x)\ge0
\quad\text{for every }n\ge0\text{ and every real }x.
\tag{C5}
\]

Under the standard growth hypotheses satisfied by \(F\), the full collection (C5), not merely \(n=1\), characterizes membership in the Laguerre–Pólya class and hence RH.

### 9.1 A master identity—and a warning

Set \(\tau=t^2\ge0\). Taylor expansion gives the exact generating identity

\[
F(x+it)F(x-it)
=\sum_{n=0}^\infty L_n(x)t^{2n}
=\sum_{n=0}^\infty L_n(x)\tau^n.
\tag{C6}
\]

Since \(F\) is real entire,

\[
F(x+it)F(x-it)=|F(x+it)|^2\ge0
\tag{C7}
\]

for every real \(x,t\), regardless of RH. This yields a useful structural filter:

\[
\boxed{\text{Positivity of the summed generating family is automatic and says nothing about RH.}}
\]

What RH requires is **coefficientwise** positivity in (C6), or equivalently absolute monotonicity at \(\tau=0\):

\[
\left.\frac{\partial^n}{\partial\tau^n}
|F(x+i\sqrt\tau)|^2\right|_{\tau=0}
=n!L_n(x)\ge0.
\tag{C8}
\]

This blocks another tempting shortcut: one cannot prove the hierarchy by summing it into an expression that is manifestly nonnegative, because that summed positivity holds for every real entire function.

### 9.2 The strongest honest next program

The next pass should be **hierarchy-first**:

1. Work with \(K_n\) or \(L_n\) for symbolic \(n\), not only \(n=1\).
2. Reject any criterion that is automatic for an arbitrary real entire function, such as (C7).
3. Seek a representation that is coefficientwise positive before summation—ideally a Gram or sum-of-squares representation for each \(K_n\), uniform in \(n\).
4. Expand the theta kernel into its \(m,k\) cell pairs and test whether cross-cell terms can be grouped into positive blocks. A termwise proof is unlikely; known total-positivity failures show that cancellation between blocks matters.
5. Any computational experiment should target the first failing/weakest \((n,x)\) region with certified intervals. Finite verification is reconnaissance, not proof, unless paired with a uniform analytic tail theorem.

This is not yet a proof route with a closed key lemma. It is, however, the first formulation in this sequence that (i) is actually equivalent to RH, (ii) survives the local consistency checks above, and (iii) does not confuse an aggregate necessary condition with the full conclusion.

## 10. Comparison with other currently tempting routes

| Route | What is rigorously known | Why it was not selected as the main continuation |
|---|---|---|
| Jensen/Hermite asymptotics | Fixed-degree Jensen polynomials eventually approach Hermite behavior | The asymptotic regime is largely universal and can be insensitive to nonreal zeros; the hard compact/transition range remains. See [Griffin–Ono–Rolen–Zagier](https://arxiv.org/abs/1902.07321) and [Farmer](https://arxiv.org/abs/2008.07206). |
| Total positivity of the de Bruijn–Newman kernel | A certified negative \(5\times5\) Toeplitz minor proves the kernel is not PF\(_5\) | Any plan requiring PF\(_\infty\), or even PF\(_5\), for that kernel is already false. See the [certified PF\(_5\) counterexample](https://arxiv.org/abs/2602.20313). |
| Toeplitz minors of xi coefficients | Positivity is certified for \(k\ge10^{18}r^3\) | The paper explicitly leaves the complementary region that contains the RH difficulty. See the [uniform cubic wedge result](https://arxiv.org/abs/2607.16795). |
| Weil/screw-function operator route | There is a rigorous continuous-function realization of Weil's quadratic form and a spectral-limit conjecture | The global arithmetic positivity/cross-prime cancellation remains unresolved. See [Suzuki's 2026 framework](https://arxiv.org/abs/2606.09096). |

These are not “bad ideas.” The point is to avoid treating a solved asymptotic sector or an equivalent positivity reformulation as if it supplied the missing global inequality.

## 11. Psychologically legible map of the failure

There are three distinct failure types, and keeping them separate matters:

1. **Representation failure.** The Thorin route writes the wrong kind of transform. This is like proposing a psychological scale whose items force every respondent's score downward at baseline while claiming it measures a construct known to be symmetric around baseline. The mismatch is in the instrument, before interpretation.
2. **Criterion failure.** The decreasing-and-convex condition gives mutually incompatible instructions to a smooth symmetric graph. This is a local logical contradiction, not an estimate that merely needs sharpening.
3. **Inference failure.** \(L_1\ge0\) can hold even with nonreal zeros. This is analogous to a screening measure with good sensitivity for one feature but insufficient specificity for the diagnosis. Passing it is evidence compatible with RH, not a proof of RH.

The correction is to demand the whole diagnostic battery \(L_0,L_1,L_2,\ldots\), while still asking whether there is one structural mechanism that certifies all of them together.

## 12. Process integrity and robustness

### 12.1 Evidence hierarchy

- Primary equations were checked against current arXiv versions.
- The older journal item's retracted status was checked at Project Euclid.
- Literature claims about the Laguerre hierarchy were checked against Csordas's primary paper.
- Recent route exclusions were checked against the current primary preprints themselves, including their explicit limitation statements.
