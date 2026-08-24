9. RH is equivalently the convexity of \(a\mapsto|\xi(1/2+a+it)|^2\), or positive definiteness of \(\mathcal C_a\), throughout \(0\le a<1/2\).
10. No nonzero \(S_\alpha\) is a positive Gaussian scale mixture, because its tail is too fast.
11. Generic positive symmetric kernels need not have phase-positive exponential tilts.
12. Natural theta cells have the sign and convergence obstructions in §9.5; termwise operations fail in the unresolved strip.
13. For every finite \(N\) and strip width \(\tau\), the candidate theorem in §8 supplies a fully admissible, strictly log-concave kernel with nonreal zeros that passes \(L_0,\ldots,L_N\) globally. The mathematical derivation is internally cross-verified; external correctness and novelty review remain outstanding.
14. The screw function has the exact prime-shock and prefix Legendre-barrier forms in §10.6.
15. Suzuki’s positive shift transform is not order-reflecting.
16. A Gram factorization based only on the midpoint weight is impossible.
17. The GHS/conditional-variance inequality is valid but controls only low-order behavior.
18. The full tilted autocorrelation has the exact completed-Epstein representation in §9.7, and its constant-term-subtracted remainder \(\mathcal B_s\) is unconditionally positive definite; these facts are classical in substance and do not prove the needed derivative sign.
19. The individual theta-scale kernel \(G_1\) is not positive definite, as shown by the explicit eleven-point integer-vector witness and directed-rounding interval certificate in §9.7.
20. The unrestricted Fenchel margins satisfy \(M_k\ge E_k\), the exact update and signed-discrepancy laws in §10.6.1, and \(\mathrm{RH}\iff E_k\ge0\) for every \(k\); global nonnegativity has not been proved.
21. Suzuki’s displayed derivative constant in §4.1 is missing \(-\tfrac12\log\pi\); the corrected value reproduces the published numerical roots and leaves the theorem unchanged.
22. Neither \(\partial_s\mathcal B_s\) nor the multiplier derivative \(p_s'\) has the required fixed sign; only their coupled, RH-equivalent compensation remains.

### 14.2 Audit disposition

All claims promoted to “proved” in §14.1 received an algebraic audit by at least one model instance other than the originating instance, or an exact counterexample check. This is correlated multi-instance review, not independent peer review. Numerical claims remain labeled numerical. No claim in this dossier completed the implication to RH.

### 14.3 Exact remaining gap

Prove one—and only one is needed—of the following equivalent global statements:

\[
L_n(x)\ge0\quad\text{for every }n\ge0, x\in\mathbb R;
\]

\[
K_n\text{ is positive definite for every }n\ge0;
\]

or

\[
S_\alpha\text{ is positive definite for every }0<\alpha<\frac12.
\]

Equivalently, prove either

\[
\mathcal C_a\text{ is positive definite for every }0\le a<\frac12,
\]

or

\[
\Psi(t)\ge0\quad\text{for every }t\ge0.
\]

The last condition is also equivalent to the discrete Fenchel family

\[
E_k\ge0\quad\text{for every prime-power prefix }k.
\]

Every currently verified deduction stops strictly before all of these global statements.

### 14.4 Continuation protocol

Future rounds should reopen a blocked route only when a materially new mechanism appears. The highest-value tests are:

1. obtain a human line-by-line audit and a database-complete prior-art search for the strengthened §8 theorem;
2. seek a Gram/SOS representation for \(S_\alpha\) that couples the midpoint weight to theta-cell structure rather than factoring the weight alone;
3. use the Epstein formula only through groupings that preserve cancellation across theta scales—the individual-slice strategy is now ruled out;
4. attack the critical Toeplitz-minor regime \(k\asymp r\), not the already-controlled tail wedge;
5. seek a uniform analytic estimate for the integrated-quantile margin \(E_k\); proving it would be an RH proof, while a negative value would refute the equivalent family and RH;
6. connect Suzuki’s continuous screw kernel to the Laguerre/tilt order with an explicit positivity-preserving transform;
7. require interval-certified counterexample searches for every proposed stronger sufficient property before investing in a long proof.

### 14.5 Proportionate reporting actions

| Finding | First recipient | Form | Public claim now? |
|---|---|---|---:|
| §8 strictly-log-concave admissible-kernel theorem candidate | Entire-functions/Laguerre–Pólya specialist, then a separate prior-art specialist | Private self-contained review packet | No |
| Suzuki constant omission | Masatoshi Suzuki or the *JLMS* editorial office | Courteous private reproduction note | No priority claim; a minor erratum may later be public |
| Epstein identity, theta-slice obstruction, Fenchel refinement | Relevant specialist only if pursuing that route | Exploratory dossier or informal correspondence | No |
| RH | Nobody as a claimed result | Continue research only | No |

A concise Suzuki inquiry could read:

> While reproducing §4.1 of “Aspects of the screw function corresponding to the Riemann zeta-function,” I found that differentiating (1.1) gives
> \[
> c=\frac\pi4-\frac12\{\gamma+\log(8\pi)\},
> \]
> rather than the displayed \(\pi/4-(\gamma+3\log2)/2\). The additional \(-\tfrac12\log\pi\) comes from \(\tfrac t2[\psi(1/4)-\log\pi]\). The corrected value reproduces the two numerical critical points reported immediately afterward; the printed value does not. This appears to be a typographical omission only and does not affect Theorem 4.1. This check arose in a disclosed multi-instance generative-AI exploratory project and was then recomputed directly. Is this already known or corrected elsewhere?

---

**Current bottom line:** This attempt has not solved RH. It has, however, converted several seductive false routes into exact no-go theorems, merged the phase and hierarchy programs into one positive-definite-order target, and identified what a future proof must add rather than merely rephrase.
