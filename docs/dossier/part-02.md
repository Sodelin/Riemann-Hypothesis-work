Three barrier results sharpen the target. First, no nonzero \(S_\alpha\) can be a positive Gaussian scale mixture: it decays super-exponentially in \(|r|\), whereas every nonzero positive Gaussian mixture has a Gaussian lower tail. Second, positive symmetric input measures do not generically make exponential tilting monotone in positive-definite order. Third, for every finite \(N\) and every prescribed zero-strip width, there are strictly log-concave admissible kernels whose transforms have nonreal zeros inside that strip while satisfying \(L_n(x)\ge0\) for all real \(x\) and all \(n\le N\). Muranaka had already established arbitrary finite-prefix insufficiency in the broader class \(\mathrm{L\!-\!P}^{*}\); the candidate strengthening here is the simultaneous all-\(N\), admissible, strictly-log-concave, arbitrarily-thin-strip realization.

The second cycle also derives an exact modular regrouping. If \(s=\alpha+1/2\) and

\[
E_s(r)=\sum_{(m,n)\in\mathbb Z^2\setminus\{(0,0)\}}
\bigl(m^2e^r+n^2e^{-r}\bigr)^{-s},
\]

then the tilted autocorrelation for the dossier's normalization of \(\xi\) is

\[
T_\alpha(r)=\frac18
\bigl(s^2-\partial_r^2\bigr)
\bigl((s-1)^2-\partial_r^2\bigr)
\left[\pi^{-s}\Gamma(s)E_s(r)\right],
\]

first for \(s>1\) and then by meromorphic continuation. The differential factors cancel the two axis/cusp terms that obstruct termwise continuation, and the Fourier transform is exactly \(|\xi(s+it)|^2\). This identity is not a proof: monotonicity of the right-hand side in positive-definite order remains RH-equivalent.

Subtracting the Eisenstein constant terms produces an unconditional all-scale positive-definite remainder \(\mathcal B_s\), but both \(\partial_s\mathcal B_s\) and the derivative of the fourth-order multiplier have rigorous sign obstructions; only their RH-strength compensation remains. On the arithmetic side, convex duality turns Suzuki’s prime-shock criterion into an exact discrete family \(\mathrm{RH}\iff E_k\ge0\) for every prime-power prefix. These are sharper coordinates and route exclusions, not a proof.

## 2. Problem, scope, and proof standard

### 2.1 Exact problem

The completed zeta function is

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

The functional equation \(\xi(s)=\xi(1-s)\) makes \(\Xi(z)=\xi(1/2+iz)\) real and even on the real axis. RH is equivalent to

\[
\Xi(z)=0\quad\Longrightarrow\quad z\in\mathbb R.
\]

### 2.2 What counts as progress

The project distinguishes five levels:

| Level | Meaning | Counts as solving RH? |
|---|---|---:|
| Identity | An exact rewriting of xi or an RH-equivalent condition | No |
| Necessary inequality | A consequence of RH, such as \(L_1\ge0\) | No |
| Sufficient lemma | A new theorem whose verified hypotheses hold for xi and imply RH | Yes, if the chain is complete |
| Numerical evidence | Finite-precision or finite-range support | No |
| Adversarially verified proof | Every implication, domain, interchange, tail, and source claim survives independent audit | Yes |

### 2.3 Why the supplied prompt structure was useful

The collaboration used an explicit registry of mathematical approach families, preserved strategic separation during the first wave, marked routes as blocked at theorem-strength gaps, required concrete formulas or counterexamples, and subjected promoted results to a separate model-instance referee. It did **not** assume that a proof must exist inside the attempted framework, because that assumption would make false positives more likely.

## 3. Approach-family registry

| ID | Approach family | Strongest verified output | Current status | Exact blocker or next test |
|---|---|---|---|---|
| A | GGC/Thorin center mixture | Four independent contradictions: parity/slope, lost cosh branch, invalid domain, wrong tail | **Blocked** | Must leave the displayed positive one-sided mixture category |
| B | Pole-mode removal and exponential tilt | Positive-MGF/real-zero contradiction; \(\operatorname{Exp}(3/4)\) moment diverges at tilt \(1\) | **Blocked** | Any repair must cancel the pole before asserting positivity |
| C | First two-copy kernel \(K_1=\nu_2\) | Exact Fourier identity for \(L_1=\Xi'^2-\Xi\Xi''\) | **Blocked as a proof endpoint** | \(L_1\ge0\) is not sufficient; \(x^4-1\) is an exact counterexample |
| D | Full generalized Laguerre hierarchy | \(K_n\) positive definite for every \(n\) is exactly equivalent to RH | **Active, exact equivalence** | No uniform Gram/SOS or coefficientwise positivity mechanism |
| E | Tilted autocorrelation / phase monotonicity | RH iff \(S_\alpha=\tfrac12\partial_\alpha T_\alpha\) is positive definite for all \(\alpha>0\) | **Active, exact equivalence** | Prove positive definiteness for \(0<\alpha<1/2\) |
| F | Gaussian-scale-mixture certificate for \(S_\alpha\) | Local alternating derivatives pass low orders; global representation is impossible by tail class | **Blocked** | Seek a PD class compatible with super-exponential spatial decay |
| G | GHS / conditional variance | Rigorous variance monotonicity from increasing \(V''\); essentially Newman’s 1991 theorem | **Verified but insufficient** | Low-order cumulant signs do not control all zeros |
| H | Conditional-moment factorization of \(K_1\) | \(\nu_2(2m)=4A(2m)h(m)\); \(A\) is PD | **Blocked shortcut** | \(h\) itself has a negative cosine-transform lobe near frequency \(22.5\) |
| I | Direct Pólya-frequency property of \(\Phi\) | Certified \(5\times5\) negative minor in current literature | **Blocked** | The Riemann kernel is not PF\(_5\) |
| J | PF\(_\infty\) of xi coefficient sequence | Exact RH equivalence; a certified uniform positive tail wedge is known | **Active but incomplete** | Critical complementary regime \(k\sim r\) remains open |
| K | Weil/screw-function/operator positivity | Exact continuous realization of Weil’s form; candidate limiting operators | **Active but incomplete** | Global prime cancellation / spectral positivity remains the conjectural step |
| L | Boundary/maximum-principle shortcut | Direct boundary sign tested and found to change | **Blocked in tested form** | Requires a different analytic quantity or boundary correction |
| M | Finite-hierarchy sufficiency | Explicit strictly-log-concave admissible counterexamples with arbitrarily thin zero strip | **Ruled out** | Any proof must use infinitely many levels or an equally global resummation |
| N | Convexity-resummed hierarchy | RH iff \(\mathcal C_a\) is PD for every \(0\le a<1/2\) | **Active, exact equivalence** | Prove the full continuum of PD inequalities |
| O | Prime-shock/screw arithmetic | RH becomes nonnegativity of an explicit piecewise-convex function, or prefix Legendre barriers | **Active, exact equivalence** | Control accumulated von Mangoldt shocks uniformly |
| P | Epstein–Eisenstein modular regrouping | Exact formula and unconditional PD completed remainder \(\mathcal B_s\); both separate monotonicity factors change sign | **Blocked factorizations; coupled route active** | Only compensation between \(D_s'\mathcal B_s\) and \(D_s\partial_s\mathcal B_s\) remains, which is RH-strength |

## 4. Shared notation and exact equivalence map

Let the even positive Riemann–Pólya kernel be normalized by

\[
\Xi(z)=\int_{\mathbb R}\Phi(u)e^{izu}\,du.
\]

For \(n\ge0\), define

\[
L_n(x)=\frac1{(2n)!}\sum_{j=0}^{2n}
(-1)^{j+n}\binom{2n}{j}
\Xi^{(j)}(x)\Xi^{(2n-j)}(x)
\]

and

\[
K_n(r)=\int_{\mathbb R}(r-2s)^{2n}\Phi(r-s)\Phi(s)\,ds.
\]

Then

\[
L_n(x)=\frac1{(2n)!}\int_{\mathbb R}K_n(r)e^{ixr}\,dr
\]

and

\[
\Xi(x+iy)\Xi(x-iy)
=\sum_{n=0}^{\infty}L_n(x)y^{2n}.
\]

The following statements are equivalent for \(\Xi\):

1. RH;
2. \(\Xi\) belongs to the Laguerre–Pólya class;
3. \(L_n(x)\ge0\) for all \(n\ge0\) and \(x\in\mathbb R\);
4. every \(K_n\) is positive definite;
5. for every real \(x\), the entire function \(\tau\mapsto|\Xi(x+i\sqrt\tau)|^2\) has nonnegative Taylor coefficients;
6. \(\alpha\mapsto|\xi(1/2+\alpha+it)|\) is strictly increasing for every \(t\) and \(\alpha>0\);
7. \(S_\alpha=\tfrac12\partial_\alpha T_\alpha\) is positive definite for every \(\alpha>0\).

The positivity

\[
|\Xi(x+i\sqrt\tau)|^2\ge0
\]

is automatic and does not imply coefficientwise positivity. For example,

\[
f(z)=1+z^2,
\qquad
|f(i\sqrt\tau)|^2=(1-\tau)^2\ge0,
\]

although the coefficient of \(\tau\) is negative.

## 5. Audit of the inherited parallel ledger

The ledger was read in full and then given to an independent adversarial referee. Its main conclusions survived. The following corrections should be carried into any revised version:

1. In the bilateral identity

   \[
   \int_{\mathbb R}e^{su}|u|e^{-\lambda|u|}\,du
   =\frac1{(\lambda-s)^2}+\frac1{(\lambda+s)^2},
   \]

   explicitly state the domain \(|\Re s|<\lambda\).
2. Replace “absolute monotonicity at \(\tau=0\)” with “nonnegativity of every Taylor coefficient at \(0\).” Absolute monotonicity normally refers to an interval; in this entire-series setting, coefficientwise positivity is equivalent to absolute monotonicity on \(\tau\ge0\).
3. Polson’s 2026 v8 does not merely provide background: it asserts RH in a theorem, but the asserted tilt crosses the MGF convergence boundary and is invalid.
4. Polson v23 contains an additional internal inconsistency: equations claiming \(M\ge0\Rightarrow k\ge0\) and representing \(U_k\) by a sine-squared transform would make \(U_k\ge0\) automatic, while later sections call that positivity open.

No sign or factorial error was found in the ledger’s formulas for \(K_n\), \(L_n\), or their master generating identity.

## 6. Route A — GGC/Thorin continuation and its exact failures

The inherited ledger’s complete derivations are retained as the source audit. The decisive center claim was

\[
\frac{\xi(1/2+s)}{\xi(1/2)}
=\int_0^\infty\frac{M(d\lambda)}{(s+\lambda)^2},
\qquad M\ge0.
\]

It cannot hold for a nonzero positive measure near \(s=0\). The xi ratio is even and has derivative zero at the center, while the right derivative of every nontrivial positive one-sided mixture is strictly negative or infinite:

\[
-G'(0+)=2\int_0^\infty\lambda^{-3}M(d\lambda)>0.
\]

This already ends the route. Three independent source-level checks agree with it:

- the shifted cosh has two exponential branches, but one is lost in the audited transition;
- \(e^{-ku}=\int_k^\infty ue^{-\lambda u}\,d\lambda\) is used where \(u<0\), where its right side diverges;
- a nonzero positive finite-rate exponential mixture cannot have the Riemann kernel’s super-exponential tail.

The pole-mode repair also fails. Removing the factor associated with \(s(s-1)\) leaves a remainder that analytically vanishes at the point corresponding to the pole of \(\Lambda(s)\). A finite MGF of a positive law is strictly positive there, never zero. In Polson v8 the explicit Thorin atom \(\delta_{3/4}\) supplies an \(\operatorname{Exp}(3/4)\) component, so the proposed tilt at \(1\) has infinite expectation.

