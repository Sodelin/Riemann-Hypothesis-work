The methodological conclusion is sharp within its stated hypotheses: **no finite prefix of the exact hierarchy, even verified globally in \(x\), supplemented by the admissible-kernel axioms and strict log-concavity, and combined with an arbitrarily thin a priori zero strip, can force real-rootedness.** This still does not match every special feature of the Riemann kernel, but it removes one previously open shape qualification from the construction.

## 9. Route C — Tilted autocorrelation order

Define

\[
f_\alpha(u)=e^{\alpha u}\Phi(u).
\]

Then \(T_\alpha\) is the autocorrelation of \(f_\alpha\):

\[
T_\alpha(r)=\int_{\mathbb R}f_\alpha\!\left(m+\frac r2\right)
f_\alpha\!\left(m-\frac r2\right)\,dm.
\]

Consequently \(T_\alpha\) is positive definite without RH. Its derivative is

\[
S_\alpha(r)=\int_{\mathbb R}m e^{2\alpha m}
\Phi\!\left(m+\frac r2\right)
\Phi\!\left(m-\frac r2\right)\,dm
\]

or, after pairing \(m\) and \(-m\),

\[
S_\alpha(r)=2\int_0^\infty m\sinh(2\alpha m)
\Phi\!\left(m+\frac r2\right)
\Phi\!\left(m-\frac r2\right)\,dm>0.
\]

Thus pointwise positivity is again automatic. RH asks for the stronger matrix condition

\[
\sum_{j,k}c_j\overline{c_k}S_\alpha(r_j-r_k)\ge0
\]

for every finite choice of points and coefficients.

Equivalently, for \(0<\alpha<\beta\),

\[
T_\beta-T_\alpha
\]

must be positive definite. This is a Loewner-order statement for autocorrelation kernels: exponential tilting must increase the entire spectrum pointwise, not merely increase total mass or pointwise kernel values.

### 9.1 Gaussian-mixture shortcut: locally plausible, globally impossible

A natural sufficient condition would be complete monotonicity of

\[
q\longmapsto S_\alpha(\sqrt q).
\]

Bernstein’s theorem would then give

\[
S_\alpha(r)=\int_0^\infty e^{-\lambda r^2}\,d\mu_\alpha(\lambda),
\]

a positive Gaussian scale mixture, hence a positive-definite kernel. High-precision reconnaissance found the required alternating derivatives at \(q=0\) through order six for \(\alpha=0.05,0.1,0.25,0.49\). This finite evidence is misleading.

The Riemann kernel obeys a bound of the form

\[
\Phi(u)\le C\exp\!\left(A|u|-c e^{2|u|}\right).
\]

For \(r,m\ge0\),

\[
e^{2|m+r/2|}+e^{2|m-r/2|}\ge e^{r+2m}.
\]

After absorbing polynomial and ordinary exponential factors, this yields

\[
0<S_\alpha(r)\le C_\alpha e^{-c_\alpha e^{r}}
\qquad(r\to+\infty).
\]

If a nonzero positive Gaussian mixture representation existed, some finite \(B\) would satisfy \(\mu_\alpha([0,B])>0\), forcing

\[
S_\alpha(r)\ge \mu_\alpha([0,B])e^{-Br^2},
\]

contradicting the super-exponential upper bound. Therefore no such global Gaussian-mixture certificate exists for any \(\alpha>0\).

### 9.2 Midpoint-only Gram factorization also fails

The positive paired weight is \(w_\alpha(m)=|m|\sinh(2\alpha|m|)\). A tempting separation would require the Hankel kernel

\[
(u,v)\longmapsto w_\alpha\!\left(\frac{u+v}{2}\right)
\]

to be positive semidefinite. But its \((0,0)\) entry is zero while its \((0,v)\) entry is positive for \(v\ne0\), impossible for a positive semidefinite kernel by Cauchy–Schwarz. Thus a Gram proof cannot arise by factorizing only the midpoint weight; any successful factorization must use special structure of \(\Phi\) itself.

### 9.3 A second, convexity-resummed hierarchy

There is an exact continuum target that begins at \(K_1\) but contains every higher kernel. Put

\[
H_t(a)=\left|\xi\!\left(\frac12+a+it\right)\right|^2
=\Xi(t-ia)\Xi(t+ia).
\]

Then

\[
H_t(a)=\sum_{n=0}^{\infty}L_n(t)a^{2n}.
\]

Differentiate twice:

\[
H_t''(a)=\sum_{n=1}^{\infty}(2n)(2n-1)L_n(t)a^{2n-2}.
\]

Its Fourier kernel is

\[
\mathcal C_a(r)
=\int_{\mathbb R}(r-2s)^2\Phi(r-s)\Phi(s)
\cosh\!\bigl(a(r-2s)\bigr)\,ds,
\]

and

\[
\mathcal C_a(r)
=\sum_{k=0}^{\infty}\frac{a^{2k}}{(2k)!}K_{k+1}(r).
\]

Therefore

\[
H_t''(a)=\int_{\mathbb R}\mathcal C_a(r)e^{itr}\,dr.
\]

This gives another exact equivalence:

\[
\boxed{\mathrm{RH}\iff
\mathcal C_a\text{ is positive definite for every }0\le a<\frac12.}
\]

This is the kernelized form of Jensen’s classical convexity criterion, not a new proof of it. It also connects exactly to the phase kernel. For \(a>0\), put

\[
R_a(r)=\frac1{2a}\partial_aT_a(r).
\]

Then

\[
R_a
=\frac12\sum_{k=0}^{\infty}
\frac{a^{2k}}{(2k+1)!}K_{k+1},
\qquad
R_a=\frac1{2a}\int_0^a\mathcal C_u\,du,
\qquad
R_0=\frac12K_1.
\]

Its Fourier transform is \(H_t'(a)/(2a)\), so positive definiteness of \(R_a\) is the same phase-monotonicity criterion as positive definiteness of \(S_a/a\). Convexity of \(H_t\) is a sufficient mechanism for that monotonicity, and the all-\(a\), all-\(t\) condition is itself RH-equivalent.

The forward implication follows from the nonnegative Laguerre coefficients. Conversely, \(H_t''(a)\ge0\), together with \(H_t'(0)=0\), makes \(H_t\) nondecreasing on \(0\le a<1/2\). An off-line zero at \(a_0>0\) would give \(H_t(a_0)=0\). If \(H_t(0)>0\), monotonicity immediately contradicts this. If \(H_t(0)=0\), monotonicity forces \(H_t\) to vanish throughout \([0,a_0]\), and analyticity would make the corresponding xi function identically zero. Thus there is no off-line zero.

This corrects an overly restrictive reading of the first ledger. One does not logically have to prove every \(K_n\) positive definite one at a time; one may instead prove positive definiteness of the resummed continuum \(\mathcal C_a\). The task is still genuinely global: \(\mathcal C_0=K_1\), and a single endpoint remains insufficient.

The deformation differs from the Dimitrov–Xu kernel \(\cosh(ar)K_1(r)\). Here the cosh acts on the **difference variable inside the convolution**, \(r-2s\), so its Taylor expansion generates \(K_2,K_3,\ldots\) with the correct coefficients.

### 9.4 Generic tilt monotonicity is false

Positive even input measures do not automatically make \(T_\alpha\) increase in positive-definite order. Consider the Laplace transform of a positive symmetric finite measure

\[
F_0(w)=2\cosh w+\cosh 2w.
\]

At frequency \(t=\pi\),

\[
\operatorname{Re}\!\left(
F_0'(\alpha+i\pi)\overline{F_0(\alpha+i\pi)}
\right)
=2(\sinh2\alpha-\sinh\alpha)
(\cosh2\alpha-2\cosh\alpha).
\]

The first factor is positive, while the second is negative for

\[
0<\alpha<
\operatorname{arcosh}\!\left(\frac{1+\sqrt3}{2}\right).
\]

Hence the phase kernel fails positive definiteness even though the underlying measure is positive and symmetric and the physical-space derivative kernel is pointwise positive. Convolution with a sufficiently narrow normalized \(e^{-u^4/\varepsilon^4}\) approximate identity changes both \(F_0\) and \(F_0'\) continuously at the displayed point, so the strict negative value persists for a positive, even, smooth, super-Gaussian density. Positivity, evenness, analyticity, and rapid tails are therefore not enough. Any proof must use structure special to the full theta kernel.

### 9.5 Theta cells: sign and convergence obstructions

The natural full-line theta cells are signed, not individually positive. With \(A_n=\pi n^2\), take

\[
p_n(u)=A_n e^{5u/2}\bigl(2A_ne^{2u}-3\bigr)e^{-A_ne^{2u}}.
\]

Their bilateral Laplace transforms can be evaluated exactly:

\[
P_n(w)
=A_n^{-1/4-w/2}
\left(\frac w2-\frac14\right)
\Gamma\!\left(\frac54+\frac w2\right),
\qquad \Re w>-\frac52.
\]

But \(\sum_nP_n(w)\) is a zeta Dirichlet series and converges termwise only for \(\Re w>1/2\). The entire unresolved strip \(0<\Re w<1/2\) therefore lies outside the domain where a theta-cell/Fubini proof can sum individual transformed cells. The boundary \(w=1/2\) is especially deceptive: every \(P_n(1/2)\) vanishes because of the displayed linear factor, while the analytically continued full transform is nonzero because that zero cancels the pole of the zeta factor.

Even diagonal-cell positivity fails. For \(0<\alpha<1/2\), the diagonal phase expression contains

\[
P_n(\alpha)^2
\left[
-\frac12\log A_n
+\frac1{\alpha-1/2}
+\frac12\psi\!\left(\frac54+\frac\alpha2\right)
\right]<0.
\]

The exact diagonal autocorrelation also has a signed hyperbolic-secant form:

\[
T_{n,\alpha}(r)
=C_{n,\alpha}\operatorname{sech}^{\alpha+5/2}r
\left[
\frac{(\alpha+5/2)(\alpha+7/2)}9\operatorname{sech}^2r
-\frac{2(\alpha+1)}3
\right],
\qquad C_{n,\alpha}>0.
\]

It is positive definite as an autocorrelation, but it is pointwise negative for large \(|r|\), so differentiating it in \(\alpha\) does not produce an SOS certificate.

A related reflected-half-line calculation reaches the same warning from high-frequency asymptotics. If \(p'(0)\ne0\), then

\[
F_p(w)=\frac{2p'(0)}{w^2}+O(|w|^{-4}),
\qquad
F_p'(w)=-\frac{4p'(0)}{w^3}+O(|w|^{-5}),
\]

and, for \(w=\alpha+it\),

\[
\operatorname{Re}\!\left(F_p'(w)\overline{F_p(w)}\right)
=-\frac{8\alpha p'(0)^2}{|w|^6}+O(|t|^{-8})<0
\]

at sufficiently high frequency. Thus no term-by-term cell proof survives without a new modular regrouping or a justified analytic continuation that preserves positivity. The infinite theta cancellation is part of the problem’s structure, not a technical detail that can be discarded.

### 9.6 Operator and polarization rewrites are circular

Let \(A_\alpha\) be multiplication by \(F(\alpha+it)\). The tilted autocorrelation convolution operator is

\[
C_\alpha=A_\alpha^*A_\alpha.
\]

Where \(F\ne0\), define \(B_\alpha=A_\alpha'A_\alpha^{-1}=M_{F'/F}\). Then

\[
C_\alpha'
=A_\alpha^*(B_\alpha^*+B_\alpha)A_\alpha.
\]

Consequently \(C_\alpha'\succeq0\) is exactly the pointwise condition

\[
\operatorname{Re}\frac{F'(\alpha+it)}{F(\alpha+it)}\ge0,
\]

which is the original RH-equivalent monotonicity inequality. The operator factorization adds no independent positivity.

Similarly,

\[
\operatorname{Re}(F'\overline F)
=\frac14\left(|F+F'|^2-|F-F'|^2\right)
\]

is a difference of Gram squares, not a sum-of-squares certificate. Both rewrites are useful diagnostics, but treating either as manifest positivity would be circular.

### 9.7 Cycle-II route: modular regrouping through a rectangular Epstein zeta function

The theta-cell obstruction in §9.5 can be repaired at the level of exact identities by summing *before* entering the unresolved strip. This produces a modularly complete object rather than an illegally continued sum of individual cells.

For \(\operatorname{Re}s>1\), define the rectangular Epstein zeta function

\[
E_s(r)=
\sum_{(m,n)\in\mathbb Z^2\setminus\{(0,0)\}}
\left(m^2e^r+n^2e^{-r}\right)^{-s}
\]

and its completion

\[
Q_s(r)=\pi^{-s}\Gamma(s)E_s(r).
\]

Let

\[
D_s=
\left(s^2-\partial_r^2\right)
\left((s-1)^2-\partial_r^2\right).
\]

> **Proposition (exact identity; classical in substance).** Put \(s=\alpha+\tfrac12\). For the normalization
> \[
> F(w)=\xi\!\left(\frac12+w\right)
> =\int_{\mathbb R}\Phi(u)e^{wu}\,du,
> \]
> the tilted autocorrelation satisfies
> \[
> \boxed{
> T_\alpha(r)=\frac18D_sQ_s(r).
> }
> \]
