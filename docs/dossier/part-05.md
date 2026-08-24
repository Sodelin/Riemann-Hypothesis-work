> The formula holds first for \(s>1\) and extends, after cancellation of the meromorphic axis/cusp terms, to \(0<s<1\). Its Fourier transform in \(r\) is exactly
> \[
> \widehat T_\alpha(t)=|\xi(s+it)|^2.
> \]

Here is a constant-level derivation. Recall the signed full-line cells

\[
p_n(u)=A_n e^{5u/2}\left(2A_ne^{2u}-3\right)e^{-A_ne^{2u}},
\qquad A_n=\pi n^2.
\]

Their bilateral Laplace transforms are

\[
\begin{aligned}
P_n(w)
&=A_n^{-1/4-w/2}
\left(\frac w2-\frac14\right)
\Gamma\!\left(\frac54+\frac w2\right)\\
&=\frac14z(z-1)\Gamma(z/2)\pi^{-z/2}n^{-z},
\qquad z=\frac12+w.
\end{aligned}
\]

Therefore

\[
\sum_{n\ge1}P_n(w)
=\frac14z(z-1)\pi^{-z/2}\Gamma(z/2)\zeta(z)
=\frac12\xi(z).
\]

If \(p=\sum_np_n\), its tilted autocorrelation \(T_\alpha^p\) consequently has Fourier transform \(|\xi(s+it)|^2/4\). For \(m,n>0\), a beta-integral gives

\[
\int_{\mathbb R}e^{itr}
\left(m^2e^r+n^2e^{-r}\right)^{-s}\,dr
=
\frac{
\Gamma\!\left(\frac{s+it}{2}\right)
\Gamma\!\left(\frac{s-it}{2}\right)}
{2\Gamma(s)}
m^{-s-it}n^{-s+it}.
\]

Summing the four sign choices and multiplying by \(\pi^{-s}\Gamma(s)\) yields

\[
2\pi^{-s}
\Gamma\!\left(\frac{s+it}{2}\right)
\Gamma\!\left(\frac{s-it}{2}\right)
\zeta(s+it)\zeta(s-it).
\]

Under Fourier transformation, \(D_s\) multiplies by

\[
\left(s^2+t^2\right)\left((s-1)^2+t^2\right)
=|(s+it)(s-1+it)|^2.
\]

The coefficient \(1/32\) therefore gives \(T_\alpha^p\); the dossier kernel is \(\Phi=2p\), so its autocorrelation is four times larger and the coefficient becomes \(1/8\).

The two differential factors have a structural role beyond supplying the polynomial in \(\xi\). The lattice-axis terms are proportional to \(e^{\pm sr}\) and are annihilated by \(s^2-\partial_r^2\). After Poisson/modular continuation, the dual cusp terms are proportional to \(e^{\pm(s-1)r}\) and are annihilated by \((s-1)^2-\partial_r^2\). The residue at \(s=1\) is consequently removable after applying \(D_s\), which permits continuation into the critical strip without pretending that the original Epstein series converges there.

This is the strongest constructive identity of the second cycle, but it is not a positivity proof. Its ingredients are classical: \(E_s(r)\) is a completed real-analytic Eisenstein series restricted to the imaginary axis, and the regularized Mellin transform of that restriction yields the product of completed zeta functions. The differential operator is a convenient way to remove the constant terms and insert the polynomial factors that turn completed zeta functions into \(\xi\). The particular packaging may be useful, but no underlying Epstein/Rankin–Selberg novelty is claimed.

For \(0<s<1\), \(E_s\) is present through analytic continuation, not as a positive termwise lattice sum; direct differentiation of individual non-axis terms produces mixed signs. Moreover, \(T_\alpha\) is already positive definite because it is an autocorrelation. The missing statement is that

\[
\partial_s\!\left(D_sQ_s\right)
\]

is positive definite for \(1/2<s<1\), which is precisely the original RH-equivalent modulus monotonicity. The identity is valuable because it preserves modular cancellation and supplies a new coordinate system for the search, not because it shortens the logical distance to RH by itself.

A natural stronger shortcut fails. Put

\[
a(x)=2\sum_{n\ge1}e^{-\pi n^2x},
\qquad
G_t(r)=a(te^r)a(te^{-r}).
\]

The functional-equation split gives a positive Mellin weight for these theta-scale slices, suggesting that one might prove positive definiteness scale by scale. At \(t=1\), however, take the eleven points \(r_j=0.15j\) and the integer vector

\[
c_j=(-1)^j\binom{10}{j}
=(1,-10,45,-120,210,-252,210,-120,45,-10,1).
\]

Direct evaluation gives

\[
c^{\mathsf T}[G_1(r_j-r_k)]_{j,k=0}^{10}c
=-0.00007514539446545\ldots<0.
\]

This is more than an unstable floating-point eigenvalue. Jacobi inversion gives, for \(r\ge0\),

\[
G_1(r)=a(e^r)\{e^{r/2}[1+a(e^r)]-1\},
\]

and truncating \(a(e^r)\) after five terms leaves a tail below \(2e^{-36\pi}/(1-e^{-13\pi})\). Because \(\sum_j|c_j|=1024\), even absolute enclosures of \(10^{-11}\) for each of the eleven kernel values preserve the negative sign. The companion script `theta_slice_interval_certificate.py` implements outward-rounded decimal interval arithmetic using only positive Taylor sums and explicit geometric remainders. It certifies

\[
-0.000075145394465453985194703762565
<c^{\mathsf T}Gc<
-0.000075145394465453985194703762564,
\]

so this route exclusion no longer depends on floating-point eigenvalue trust.

The fourth-order filter cannot repair an individual slice: in Fourier space it multiplies by the nonnegative polynomial

\[
(s^2+\omega^2)((s-1)^2+\omega^2).
\]

Therefore the negative nonzero-frequency lobe survives. Any proof using §9.7 must exploit cancellation **across** theta scales rather than positivity of every scale separately.

The required cross-scale grouping can in fact be written exactly. For \(1/2<s<1\), put

\[
A_s=2\pi^{-s}\Gamma(s)\zeta(2s),
\qquad
C_s=2\pi^{1/2-s}\Gamma(s-1/2)\zeta(2s-1).
\]

The Chowla–Selberg expansion gives, for \(r>0\),

\[
Q_s(r)=A_se^{sr}+C_se^{(1-s)r}+8R_s(r),
\]

where

\[
R_s(r)=e^{r/2}\sum_{m,n\ge1}
\left(\frac nm\right)^{s-1/2}
K_{s-1/2}(2\pi mn e^r).
\]

Pairing \((m,n)\) with \((n,m)\) makes every off-diagonal block

\[
2\cosh\!\left((s-\tfrac12)\log(n/m)\right)
K_{s-1/2}(2\pi mn e^r),
\]

which is positive and strictly increasing in \(s\): the integral representation \(K_\nu(x)=\int_0^\infty e^{-x\cosh u}\cosh(\nu u)\,du\) has \(\partial_\nu K_\nu(x)>0\) for \(\nu>0\). Thus the raw nonconstant Bessel remainder increases pointwise, although this turns out to be the wrong positivity axis.

The boundary-safe even completion is

\[
\boxed{
\mathcal B_s(r)=\frac18\left[
Q_s(r)-2A_s\cosh(sr)-2C_s\cosh((1-s)r)
\right].
}
\]

On \(r>0\),

\[
\mathcal B_s(r)=R_s(r)-\frac{A_s}{8}e^{-sr}
-\frac{C_s}{8}e^{-(1-s)r}.
\]

The two exponential corrections are essential: an even extension of \(R_s\) alone generally creates hidden \(\delta\)- and \(\delta'\)-type boundary terms at \(r=0\) after applying the fourth-order operator. Since the subtracted hyperbolic cosines lie in the nullspace of \(D_s\),

\[
D_s\mathcal B_s=T_{s-1/2}.
\]

Consequently

\[
\boxed{
\widehat{\mathcal B_s}(t)
=\frac{|\xi(s+it)|^2}
{(s^2+t^2)((s-1)^2+t^2)}
=\frac14\left|
\pi^{-(s+it)/2}\Gamma\!\left(\frac{s+it}{2}\right)
\zeta(s+it)
\right|^2\ge0.
}
\]

Thus \(\mathcal B_s\) is an unconditional positive-definite grouping of **all** theta scales. This is a real improvement over the failed individual-slice decomposition, but the hoped-for next monotonicity is false. If

\[
L(z)=\pi^{-z/2}\Gamma(z/2)\zeta(z),
\]

then near \(z=1\),

\[
L(1+w)=\frac1w+a+O(w),
\qquad
a=\frac\gamma2-\log(2\sqrt\pi)<0,
\]

and hence

\[
\frac{L'}{L}(1+w)=-\frac1w+a+O(w).
\]

Along \(w=it\), the pole term is purely imaginary. For sufficiently small fixed \(t_0\ne0\), therefore,

\[
\left.\partial_s\widehat{\mathcal B_s}(t_0)\right|_{s=1}
=\frac12|L(1+it_0)|^2
\operatorname{Re}\frac{L'}{L}(1+it_0)<0,
\]

and the inequality persists for \(s<1\) sufficiently close to one. Thus \(\partial_s\mathcal B_s\) is not positive definite in the target strip.

The operator derivative also changes sign. If

\[
p_s(t)=(s^2+t^2)((s-1)^2+t^2),
\]

then

\[
p_s'(t)=2(2s-1)(t^2+s(s-1)),
\]

which is negative for \(|t|<\sqrt{s(1-s)}\) and positive outside. The exact decomposition

\[
\partial_s|\xi(s+it)|^2
=p_s'(t)\widehat{\mathcal B_s}(t)
+p_s(t)\partial_s\widehat{\mathcal B_s}(t)
\]

therefore has signed pieces on both sides. Only their coupled compensation can prove the desired inequality, and that compensation is exactly the original RH-equivalent statement. The cross-scale completion is a useful unconditional positive-definite lemma; its two most natural monotonicity factorizations are now rigorously ruled out.

## 10. Other routes: verified deductions and route eliminations

### 10.1 Outer/inner obstruction

Boundary modulus determines only the outer factor of an analytic function. Hypothetical off-line zeros contribute inner/Blaschke factors that have unit boundary modulus. Therefore a construction based solely on boundary modulus can discard exactly the information RH asks about. This explains, structurally, why a modulus-only GGC representation is too weak unless accompanied by a phase-sensitive condition.

### 10.2 Conditional variance and the GHS inequality

For the exponentially tilted Riemann-kernel law, let \(K(r)\) be the log moment-generating function. Writing two independent copies as midpoint \(M\) and difference \(D\), monotone-likelihood-ratio ordering shows that if \(V=-\log\Phi\) has increasing \(V''(|x|)\), then the tilted variance \(K''(r)\) decreases for \(r>0\), so \(K'''(r)\le0\). The argument is rigorous but essentially recovers Newman’s 1991 GHS theorem; Csordas verified the relevant Riemann-kernel convexity properties. It supplies low-order sign information, not the whole zero theorem.

### 10.3 Conditional factorization of \(\nu_2\)

Let \(A(t)=\int\Phi(t-s)\Phi(s)\,ds\). For two independent kernel draws, with midpoint \(M\) and half-difference \(D\), define \(h(m)=\mathbb E[D^2\mid M=m]\). Then

\[
\nu_2(t)=4A(t)h(t/2).
\]

\(A\) is an autocorrelation and hence positive definite. A hoped-for proof that \(h\) is also positive definite fails numerically: two independent grids located a negative cosine-transform lobe beginning near frequency \(22.5\). The product \(A(t)h(t/2)\) may still repair that lobe; the factorization alone does not prove it.

### 10.4 Boundary maximum principle

A direct attempt to prove a strip inequality from positivity on the boundary \(\Re s=1\) failed for the tested logarithmic-convexity quantity: high-precision evaluation found sign changes at large heights. A maximum principle remains possible only after choosing a different harmonic quantity or adding a correction that is itself proved to preserve the desired implication.

### 10.5 Total positivity and coefficient tails

The direct claim that the de Bruijn–Newman/Riemann kernel is PF\(_\infty\) is false: a current interval-certified computation exhibits a negative \(5\times5\) Toeplitz minor. A different PF\(_\infty\) statement for the Maclaurin coefficient sequence remains exactly equivalent to RH. Recent work proves a uniform positive wedge \(k\ge10^{18}r^3\) for consecutive minors, but explicitly leaves the RH-critical regime \(k\sim r\) untouched.

### 10.6 Weil/screw-function operators

Suzuki’s screw function supplies an unusually concrete arithmetic equivalent. For \(t\ge0\), write

\[
\Psi(t)=B(t)-\sum_{n\le e^t}\frac{\Lambda(n)}{\sqrt n}(t-\log n),
\]

where

\[
\begin{aligned}
B(t)={}&4(e^{t/2}+e^{-t/2}-2)
+\frac t2\!\left[\frac{\Gamma'}{\Gamma}\!\left(\frac14\right)-\log\pi\right]\\
&+\frac14\!\left[
C-e^{-t/2}\Phi(e^{-2t},2,1/4)
\right].
\end{aligned}
\]

Suzuki proves the exact equivalence

\[
