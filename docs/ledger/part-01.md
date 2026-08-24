# Riemann Hypothesis Parallel Proof Ledger

**Date:** 2026-08-01  
**Status:** Active audit; no proof of the Riemann Hypothesis is claimed.  
**Purpose:** Formalize the latest visible work from a second ChatGPT thread, test it adversarially, and identify the strongest mathematically honest next target.

## 0. Executive decision brief

The second thread has moved through three recognizable routes:

1. an arithmetic/screw-function positivity formulation;
2. a generalized-gamma-convolution (GGC)/Thorin continuation based on Nicholas Polson's recent revisions; and
3. most recently, a two-copy Fourier kernel

   \[
   \nu_2(t)=\int_{\mathbb R}(t-2s)^2\Phi(t-s)\Phi(s)\,ds.
   \]

The current verdict is:

- **The Thorin continuation does not survive elementary transform checks.** The proposed center representation is one-sided while the xi function is even; a displayed change of variables mishandles a translated cosh; a Gamma-mixture identity is used outside its stated domain; and the resulting positive exponential mixture has the wrong tail class.
- **The proposed repair—remove the low-rate pole mode, tilt, then recombine—cannot remain a positive Laplace/GGC factorization.** The removed remainder must vanish at a real tilt point, while a finite moment-generating function of a positive law is strictly positive there.
- **The latest two-copy condition is impossible as stated.** A smooth even function has derivative zero at the origin. If it is convex on the positive half-line, its derivative cannot become negative; therefore it cannot also be decreasing unless it is constant.
- **Even success on the first two-copy kernel would not prove RH.** It establishes only the first generalized Laguerre inequality. A polynomial can satisfy that inequality everywhere while having nonreal zeros.
- **The corrected target is the entire hierarchy** of two-copy kernels \(K_n\), or equivalently all generalized Laguerre inequalities, not \(K_1\) alone.

Confidence in the two exact logical obstructions above is **very high**. Confidence that the corrected hierarchy is a productive proof route is **open/undetermined**: it is an exact equivalence, but no new positivity mechanism has yet been found.

## 1. Abstract

Let

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

and define the real even entire function

\[
F(z):=\xi\!\left(\frac12+iz\right).
\]

The Riemann Hypothesis (RH) is equivalent to every zero of \(F\) being real. This ledger audits two proposed probabilistic/Fourier routes. The first attempts to reach the critical center through positive Gamma mixtures and GGC exponential tilting. Four independent checks contradict the claimed center mixture, and a short no-go theorem blocks the suggested pole-mode repair inside the positive-Laplace category. The second route writes the first Laguerre expression \(F'^2-FF''\) as the Fourier transform of a positive-looking two-copy kernel. The proposed decreasing-and-convex criterion is internally contradictory for a smooth even kernel, and the first Laguerre inequality is only necessary, not sufficient, for real-rootedness. The audit then derives the correct infinite hierarchy and a master generating identity that is useful both as a target and as a filter against another tempting false shortcut.

## 2. Access scope and limitations

I did **not** receive the other conversation's full transcript or hidden reasoning. Account-scoped conversation retrieval exposed the latest visible assistant outputs and timestamps without requiring the user to put credentials or a password-manager extension into a cloud browser. That is enough for a mathematical audit of the displayed claims, but not enough to certify that every intermediate definition from the other thread was recovered.

The most recent visible RH-specific snapshots were:

| Approx. UTC time | Route | Visible mathematical object | Audit state |
|---|---|---|---|
| 17:59 | Screw/Weil positivity | \(\Psi(t)=\phi(t)-\sum_{\log n\le t}\Lambda(n)n^{-1/2}(t-\log n)\); \(K(t,u)=\Psi(t)+\Psi(u)-\Psi(t-u)\) | Incomplete snapshot: \(\phi\) was not defined in the retrieved text, so the claimed equivalence was not rederived here |
| 18:58–19:10 | GGC/Thorin continuation | An \(\operatorname{Exp}(3/4)\) pole mode; proposed continuation by exponential tilt; later proposal to remove the pole mode before tilting | Fails the tilt-domain test; the proposed repair is blocked by a real-zero/positive-MGF contradiction |
| 19:12 | Two-copy/Laguerre kernel | \(\nu_2(t)=\int(t-2s)^2\Phi(t-s)\Phi(s)\,ds\) | Exact derivation is valid; claimed decreasing-plus-convex certificate is impossible; endpoint is insufficient for RH |

These timestamps describe retrieved snapshots, not a guaranteed live event stream.

## 3. Notation and audit standard

The functional equation gives

\[
\xi\!\left(\frac12+w\right)=\xi\!\left(\frac12-w\right).
\]

Hence

\[
G(w):=\frac{\xi(\frac12+w)}{\xi(\frac12)}
\]

is even and analytic, with

\[
G(0)=1,\qquad G'(0)=0.
\]

Let \(\Phi\) denote an even Riemann–Pólya Fourier kernel normalized so that

\[
F(z)=\int_{\mathbb R}\Phi(u)e^{izu}\,du.
\]

The exact scalar normalization of \(\Phi\) is irrelevant to every sign and impossibility argument below.

Each proposed proof step is tested in this order:

1. parity and normalization;
2. domain of each integral identity;
3. legality of changes of variables and transform direction;
4. tail behavior;
5. distinction between a necessary condition and a sufficient one;
6. exact counterexample where available;
7. comparison with primary literature.

## 4. Route A: Thorin/GGC continuation

### 4.1 The claimed center representation

The July 4, 2026 revision of Nicholas Polson's [*On Hilbert's 8th Problem*](https://arxiv.org/html/1708.02653) displays

\[
G(s)=\frac{\xi(\frac12+s)}{\xi(\frac12)}
=\int_0^\infty \frac{M(d\lambda)}{(s+\lambda)^2},
\tag{A1}
\]

with \(M\ge 0\), interpreting the right side as a positive mixture of Gamma\((2)\) transforms. The same revision explicitly says that positivity of its reciprocal Thorin measure remains unproved and that this remaining positivity would imply RH; it does not itself claim to close that final gap.

The older journal version is marked [retracted by the journal](https://projecteuclid.org/journals/brazilian-journal-of-probability-and-statistics/volume-32/issue-3/RETRACTED-On-Hilberts-8th-problem/10.1214/18-BJPS392.full). That history does not automatically decide the 2026 preprint, so the current equations were audited directly.

### 4.2 Decisive contradiction 1: evenness versus a one-sided Stieltjes transform

Assume (A1) in a right neighborhood of zero with nonzero \(M\ge0\). For \(h>0\),

\[
\frac{G(0)-G(h)}{h}
=\int_0^\infty
\frac{2\lambda+h}{\lambda^2(\lambda+h)^2}\,M(d\lambda).
\]

As \(h\downarrow0\), monotone/Fatou reasoning gives

\[
-G'(0+)=2\int_0^\infty \lambda^{-3}M(d\lambda),
\]

which is strictly positive or infinite for nonzero positive \(M\). But symmetry of \(\xi\) gives exactly

\[
G'(0)=0.
\]

Therefore (A1) cannot represent the centered even xi ratio with a nonzero positive measure.

**Plain-language translation.** The left side is mirror-symmetric and therefore leaves the center with zero slope. Every nontrivial positive mixture on the right slopes strictly downward immediately. They cannot be the same function.

### 4.3 What the bilateral transform would have to look like

If an even density on \(\mathbb R\) were assembled from the positive-half-line Gamma building block \(|u|e^{-\lambda|u|}\), its bilateral transform would contain both directions:

\[
\int_{\mathbb R}e^{su}|u|e^{-\lambda|u|}\,du
=\frac{1}{(\lambda-s)^2}+\frac{1}{(\lambda+s)^2}.
\tag{A2}
\]

The single term \((s+\lambda)^{-2}\) in (A1) is one half-line transform, not the bilateral transform of an even law. Equation (A2) automatically has derivative zero at \(s=0\); (A1) does not.

### 4.4 Decisive contradiction 2: the translated cosh was factored incorrectly

The preprint shifts a cell variable by

\[
\ell_n=\log(\pi n^2).
\]

The relevant elementary identity is

\[
2\cosh\!\left(\frac z2(u+\ell_n)\right)
=e^{z\ell_n/2}e^{zu/2}+e^{-z\ell_n/2}e^{-zu/2}.
\tag{A3}
\]

It is **not**

\[
e^{z\ell_n/2}\,2\cosh(zu/2).
\]

Yet the displayed transition from equations (32) to (33) retains \(2\cosh(zu/2)\) and extracts only the factor \((\pi n^2)^{z/2-1/4}\). The negative exponential branch requires \((\pi n^2)^{-z/2-1/4}\). Losing that branch is exactly the kind of algebraic error that converts an even bilateral transform into the one-sided expression contradicted in §4.2.

### 4.5 Decisive contradiction 3: a positive-half-line identity is used at negative \(u\)

The Gamma building block is

\[
e^{-ku}=\int_k^\infty u e^{-\lambda u}\,d\lambda,
\qquad u>0.
\tag{A4}
\]

The preprint states the condition \(u>0\). In the subsequent cell formula the \(u\)-integral begins at

\[
-\log(\pi n^2)<0.
\]

For \(u<0\), the right side of (A4) diverges in magnitude because \(e^{-\lambda u}=e^{\lambda|u|}\). Thus (A4) cannot be substituted over the entire displayed cell domain.

### 4.6 Decisive contradiction 4: the tail class is wrong

The Riemann–Pólya kernel contains factors of the form

\[
P(e^u)e^{-\pi n^2e^{2u}}
\]

and decays faster than every ordinary exponential as \(u\to+\infty\). By contrast, any nonzero positive mixture

\[
\Psi(u)=\int_0^\infty u e^{-\lambda u}M(d\lambda)
\tag{A5}
\]

with a genuine measure on finite \(\lambda\) has some positive mass in a bounded interval \([a,b]\). It therefore obeys a lower bound of the form

\[
\Psi(u)\ge C u e^{-bu}
\]

for large \(u\), and cannot decay super-exponentially. So the claimed positive exponential mixture and the Riemann kernel cannot be identical.

### 4.7 Route-A verdict

The center Gamma-mixture construction fails before the open Thorin-positivity step. The failures are mutually reinforcing:

- parity forces zero center slope;
- the one-sided mixture forces negative center slope;
- the cosh translation loses the branch that would restore parity;
- the Gamma identity is used on a forbidden domain; and
- the resulting mixture has the wrong asymptotic tail.

The objection is not merely that “Thorin positivity remains equivalent to RH.” It is that the claimed unconditional positive input at the center is itself not the displayed xi transform.

## 5. No-go theorem for the proposed pole-mode repair

The other thread correctly noticed a lower-rate pole mode in the off-center GGC representation. Here is the exact obstruction.

Define the completed zeta without the pole-canceling polynomial by

\[
\Lambda(s):=\pi^{-s/2}\Gamma(s/2)\zeta(s),
\]

so

\[
\xi(s)=\frac12s(s-1)\Lambda(s).
\]

Set

\[
s=\frac12+\sqrt w.
\]

Then

\[
s(s-1)=w-\frac14.
\]

For an anchor \(c>1/4\), define

\[
F_c(\sigma)
:=\frac{\xi(\frac12+\sqrt c)}
{\xi(\frac12+\sqrt{c+\sigma})}.
\]

It factors algebraically as

\[
F_c(\sigma)
=\frac{c-\frac14}{c+\sigma-\frac14}
R_c(\sigma),
\qquad
R_c(\sigma):=
