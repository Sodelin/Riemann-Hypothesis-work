## 7. Route B — Two-copy kernels and the complete Laguerre hierarchy

For \(n=1\),

\[
L_1(x)=\Xi'(x)^2-\Xi(x)\Xi''(x)
=\frac12\int_{\mathbb R}K_1(r)e^{ixr}\,dr,
\]

where

\[
K_1(r)=\nu_2(r)
=\int_{\mathbb R}(r-2s)^2\Phi(r-s)\Phi(s)\,ds.
\]

This identity is exact. Two attempted promotions fail:

1. A smooth even nonconstant function cannot be both decreasing and convex on all of \(t>0\): its derivative begins at zero, convexity makes the derivative nondecreasing, and decrease requires it to be nonpositive.
2. \(L_1\ge0\) is insufficient. The even polynomial \(p(x)=x^4-1\) has nonreal zeros but

   \[
   p'(x)^2-p(x)p''(x)=4x^6+12x^2\ge0.
   \]

   It fails at the next level: \(L_2(0)=-2\).

The corrected target is every \(K_n\), not \(K_1\) alone.

### 7.1 Automatic moment positivity that does not diagnose RH

For each fixed \(r\), push the positive measure

\[
\Phi(r-s)\Phi(s)\,ds
\]

forward under \(s\mapsto(r-2s)^2\). Then

\[
K_n(r)=\int_0^\infty x^n\,d\mu_r(x).
\]

Therefore \(\{K_n(r)\}_{n\ge0}\) is automatically a Stieltjes moment sequence for every nonnegative \(\Phi\). All Hankel and shifted-Hankel matrices in the hierarchy index \(n\) are positive semidefinite, independent of RH. Any proposed proof that reaches only this point has used positivity in the wrong variable: RH needs positive definiteness as a function of \(r\).

### 7.2 Exact identities and the positivity-axis mismatch

For real entire \(f,g\), coefficient extraction from

\[
f(x+iy)f(x-iy)=\sum_{n\ge0}L_n[f](x)y^{2n}
\]

gives the exact product law

\[
\boxed{L_n[fg](x)=\sum_{j=0}^nL_j[f](x)L_{n-j}[g](x).}
\]

The hierarchy kernels also satisfy

\[
\widehat K_n(x)=(2n)!\,L_n[\Xi](x),
\qquad
\sum_{n=0}^{\infty}\frac{K_n(r)}{(2n)!}y^{2n}
=(\Phi_y*\Phi_{-y})(r),
\]

where \(\Phi_y(u)=e^{yu}\Phi(u)\). For fixed \(y\), the last kernel is automatically positive definite because its Fourier transform is \(|\Xi(x+iy)|^2\ge0\). For fixed \(r\), §7.1 gives automatic Hankel positivity across \(n\). RH, however, asks for fixed-\(n\) positive definiteness across translations \(r\). Neither automatic Gram structure performs that exchange of axes.

There is also an exact derivative recursion,

\[
L_{n+1}[f]
=\frac{4L_n[f']-\partial_x^2L_n[f]}
{(2n+2)(2n+1)}.
\]

The subtraction is the obstruction to a direct induction on \(n\).

## 8. Finite-hierarchy barrier theorem

> **Candidate theorem (internally proved; literature originality not established).** For every finite \(N\ge1\) and every \(\tau>0\), there exists an admissible kernel \(\Psi_{N,\tau}\) in the sense of Csordas—\(C^\infty\), positive, even, strictly decreasing on \((0,\infty)\), with every derivative decaying faster than \(\exp(-|t|^{2+\varepsilon})\) for some \(\varepsilon>0\)—which is additionally strictly log-concave on \(\mathbb R\), whose Fourier transform has only zeros in \(|\operatorname{Im}z|\le\tau\), has nonreal zeros, and satisfies
> \[
> L_n(x)\ge0\qquad(0\le n\le N,\ x\in\mathbb R).
> \]

The construction and its uniform estimates survived two multi-instance cross-audits. These are correlated consistency checks, not independent human refereeing. The novelty qualification is essential. Muranaka's Theorem 2.5/10.2 (2003) already proves that for every \(N\) there is a function \(g\in\mathrm{L\!-\!P}^{*}\) satisfying \(L_k[g]\ge0\) for \(0\le k\le N\) and failing at \(N+1\). His explicit choice is

\[
g(z)=e^{-z^2}(z^2+b_N),
\qquad
b_N=\frac12\left(N+\sqrt N\right).
\]

That establishes the broad finite-prefix phenomenon. The possible contribution here is narrower and stronger: the counterexample is the Fourier transform of a strictly log-concave admissible kernel and its nonreal zeros can be confined to an arbitrarily thin horizontal strip. A targeted search found no exact precedent for this conjunction, but absence from a search is not a novelty certificate.

There is also a close one-level precedent. Csordas's Example 3.12 (2014) uses

\[
\varphi(t)=e^{-t^2}(15+t^2+t^4),
\]

which is positive, even, strictly decreasing, and strictly log-concave; its transform has nonreal zeros while \(L_1\ge0\). That kernel satisfies clauses (i)–(iv) of the admissible-kernel definition but fails clause (v), the super-Gaussian derivative-tail condition. Thus the plausible novelty is specifically the **all-\(N\), fully admissible, strictly-log-concave** construction. The thin-strip feature is a useful normalization but, by itself, is largely a scaling corollary.

The construction begins with

\[
P(z)=\cos(Rz)^M\left(1+\frac12\cos z\right),
\qquad M=N+1.
\]

Put \(A(z)=\cos(Rz)^M\), \(B(z)=1+\tfrac12\cos z\), and \(r=\cos^2(Rx)\). The key identity is

\[
A(x+iy)A(x-iy)
=\left(r+\sinh^2(Ry)\right)^M
=\sum_{n\ge0}A_n(r)y^{2n}.
\]

Writing \(A_n(r)=R^{2n}a_n(r)\), direct coefficient bounds give, for \(1\le n\le N\),

\[
\frac{A_{n-1}(r)}{A_n(r)}
\le
\frac{C_{M,n-1}}{R^2\binom Mn}
\quad(r>0),
\qquad
C_{M,j}=[u^{2j}]\cosh^{2M}u.
\]

At \(r=0\), both coefficients vanish because \(n<M\). Thus, for example, any choice satisfying

\[
R\ge1,
\qquad
R^2\ge
\max_{1\le n\le N}
\frac{C_{M,n-1}}{\binom Mn}
\]

makes

\[
A_n(r)\ge A_{n-1}(r)
\qquad(1\le n\le N,\ 0\le r\le1).
\]

For \(q=\cos x\), the coefficients

\[
B(x+iy)B(x-iy)=\sum_{k\ge0}b_k(x)y^{2k}
\]

are explicit:

\[
b_0=\left(1+\frac q2\right)^2\ge\frac14,
\qquad
b_k=\frac{q+2^{\,2k-3}}{(2k)!}\quad(k\ge1).
\]

Hence \(b_1\ge-1/4\) and \(b_k\ge0\) for \(k\ge2\). The product law now yields

\[
L_n[P](x)
=\sum_{j=0}^nA_j(r)b_{n-j}(x)
\ge\frac14\bigl(A_n(r)-A_{n-1}(r)\bigr)\ge0
\]

for every \(x\) and \(1\le n\le N\).

The factor \(B\) has the nonreal zeros

\[
z=(2k+1)\pi\pm i\eta,
\qquad \eta=\operatorname{arcosh}2.
\]

Moreover, \(P\) is the Fourier transform of a positive symmetric finite measure: \(\cos(Rz)^M\) is a scaled Rademacher-sum characteristic function, and \(B\) is the transform of \(\delta_0+\tfrac14\delta_1+\tfrac14\delta_{-1}\).

To obtain a smooth kernel, scale \(P\) to \(P_\delta(z)=P(\delta z)\) and multiply it by

\[
H_\lambda(z)=\widehat{h_\lambda}(z),
\qquad
h_\lambda(t)=e^{-(t/\lambda)^4}.
\]

Scaling preserves the verified signs:

\[
L_n[P_\delta](x)
=\delta^{2n}L_n[P](\delta x)\ge0
\qquad(0\le n\le N).
\]

Pólya–Newman theory places \(H_\lambda\) in the Laguerre–Pólya class. One precise route is Newman's 1976 theorem for densities \(\exp(-a t^4-\beta t^2)\) with \(\beta>0\), followed by \(\beta\downarrow0\) and Hurwitz's theorem; the resulting transform has order \(4/3<2\). If \(X\) has the normalized measure represented by \(P\), the inverse Fourier kernel of \(H_\lambda P_\delta\), up to a positive constant, is

\[
\Psi_{\lambda,\delta}(t)
=\mathbb E\exp\!\left[-\left(\frac{t-\delta X}{\lambda}\right)^4\right].
\]

It is positive, even, smooth, and super-Gaussian. More precisely, because \(X\) has finite support, every derivative is a finite average of a polynomial times a translated quartic exponential; hence for some \(c>0\),

\[
\Psi_{\lambda,\delta}^{(j)}(t)
=O_j\!\left(e^{-c|t|^4}\right)
=O_j\!\left(e^{-|t|^3}\right)
\qquad(|t|\to\infty).
\]

Thus it satisfies the full derivative-tail clause in the admissible-kernel definition. Since \(L_j[H_\lambda]\ge0\), the product law preserves all \(L_n\ge0\) through \(n=N\).

It remains to justify strict decrease, which is where a merely qualitative “small perturbation” argument would be inadequate. Let \(|X|\le S\), \(u=t/\lambda\), and \(\varepsilon=\delta/\lambda\). Then

\[
\Psi'_{\lambda,\delta}(t)
=-\frac4\lambda
\mathbb E\!\left[(u-\varepsilon X)^3e^{-(u-\varepsilon X)^4}\right].
\]

For \(u\ge\varepsilon S\), the expectation is strictly positive. For \(0<u<\varepsilon S\), write \(u=\varepsilon y\) and

\[
G_\varepsilon(y)
=\mathbb E\!\left[(y-X)^3e^{-\varepsilon^4(y-X)^4}\right].
\]

Symmetry makes \(G_\varepsilon\) odd, and uniformly for \(0\le y\le S\),

\[
\frac{G_\varepsilon(y)}y
\longrightarrow y^2+3\mathbb E[X^2]>0
\qquad(\varepsilon\downarrow0).
\]

Thus \(\Psi'_{\lambda,\delta}(t)<0\) for all \(t>0\) once \(\lambda/\delta\) is sufficiently large.

The smoothing can also be made globally **strictly log-concave**. The needed quantitative lemma is as follows. Let \(Z\) be a nondegenerate symmetric finite-support variable in \([-1,1]\), with \(1\) in its support, and set

\[
p=\Pr(Z=1),\qquad
d=\min_{z<1}(1-z),\qquad
K=\frac{1-p}{p}.
\]

Symmetry gives \(p\le1/2\), so \(K\ge1\) and the logarithm below is positive.

For

\[
\psi_a(u)=\mathbb E e^{-(u-aZ)^4},
\]

take \(c=1/10\). If

\[
0<a^2<
\min\left\{
\frac1{6\sqrt3},
\frac1{20},
\frac{3d}{4000},
\frac{d}{2000\log((169/75)K)}
\right\},
\tag{8.1}
\]

then \((\log\psi_a)''(u)<0\) for every real \(u\). To prove this, tilt the law of \(Z\) by \(e^{-(u-aZ)^4}\) and write \(Y=u-aZ\). Direct differentiation gives

\[
(\log\psi_a)''(u)
=16\operatorname{Var}(Y^3)-12\mathbb EY^2.
\tag{8.2}
\]

Symmetry reduces the proof to \(u\ge0\). On \(0\le u\le2a\), \(|Y|\le3a\), so

\[
(\log\psi_a)''(u)
\le(1296a^4-12)\mathbb EY^2<0.
\]

On \(2a\le u\le c/a\), Popoviciu’s variance inequality, \(a\le u/2\), and \(Y\in[u-a,u+a]\) give

\[
\operatorname{Var}(Y^3)
\le\frac14\bigl((u+a)^3-(u-a)^3\bigr)^2
\le\frac{169}{16}a^2u^4,
\]

and \(\mathbb EY^2\ge u^2/4\). Hence

\[
(\log\psi_a)''(u)
\le u^2(169c^2-3)<0.
\]

For \(u\ge c/a\), put \(v=u-a\). The second bound in (8.1) gives \(v\ge c/(2a)\ge a\). Under the tilted law, the mass \(q\) away from the endpoint \(Z=1\) satisfies

\[
q\le K e^{-4adv^3}.
\]

Since \(Y\in[v,v+2a]\),

\[
\operatorname{Var}(Y^3)
\le676K a^2v^4e^{-4adv^3},
\]

and therefore

\[
(\log\psi_a)''(u)
\le12v^2\left[
\frac{2704}{3}Ka^2v^2e^{-4adv^3}-1
\right].
\]

The function \(a^2v^2e^{-4adv^3}\) is decreasing from \(v=c/(2a)\) onward by the third bound in (8.1), while the fourth bound makes

\[
\frac{2704}{3}Ka^2v^2e^{-4adv^3}
\le
\frac{169}{75}K
e^{-d/(2000a^2)}<1.
\]

This proves the lemma in all three regions.

For the present construction, the normalized measure represented by \(P/P(0)\) is the law of

\[
X=R\sum_{j=1}^{M}\varepsilon_j+Y_0,
\]

where \(\varepsilon_j=\pm1\) equiprobably and \(\Pr(Y_0=0)=2/3\), \(\Pr(Y_0=\pm1)=1/6\). With \(R\ge1\), put \(S=MR+1\) and \(Z=X/S\). Then

\[
p=\frac1{6\cdot2^M},
\qquad d=\frac1S,
\qquad K=6\cdot2^M-1.
\]

Because \(a=\delta S/\lambda\), increasing \(\lambda\) makes (8.1) hold without altering the already-fixed zero strip. Finally,

\[
\frac{d^2}{dt^2}\log\Psi_{\lambda,\delta}(t)
=\frac1{\lambda^2}
(\log\psi_a)''(t/\lambda)<0.
\]

Finally, the nonreal zeros inherited from \(B\) are

\[
z=\frac{(2k+1)\pi\pm i\eta}{\delta}.
\]

Choose \(\delta\ge\eta/\tau\) and then \(\lambda\gg\delta\). All other zeros supplied by \(\cos(R\delta z)^M\) and \(H_\lambda\) are real, proving the stated zero-strip version.

