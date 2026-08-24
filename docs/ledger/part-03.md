- The comparison with the other ChatGPT uses retrieved visible outputs, not hidden chain-of-thought and not a full transcript export.

### 12.2 Confidence matrix

| Finding | Confidence | What could change it |
|---|---:|---|
| Equation (A1) cannot equal the centered even xi ratio for \(M\ge0\) nonzero | Very high | A materially different definition of \(G\), or a signed/bilateral measure replacing the displayed claim |
| The displayed cell shift mishandles the two cosh branches | Very high | A missing term in the source not visible in the current rendered/PDF equation that restores the \(e^{-z\ell/2}\) branch |
| The Gamma identity is invalid on the negative part of the cell interval | Very high | A separate justified analytic-continuation argument performed before interchange of divergent integrals |
| The pole-mode repair cannot remain a positive LT/GGC factorization | Very high | Leaving the positive-Laplace category or finding a cancellation-first object without the real zero in (A7) |
| Decreasing plus convex is impossible for \(h_\alpha\) as defined | Certain under smoothness/evenness | A different, nonsmooth kernel; convexity only after a positive threshold; or a different sign/shape criterion |
| \(L_1\ge0\) is insufficient for RH | Certain | Nothing; the polynomial counterexample is exact |
| The full \(K_n\) hierarchy is a promising practical route | Unknown | A uniform Gram/SOS identity would raise confidence; a low-order certified negative structural surrogate would lower it |

### 12.3 What this report does not establish

- It does not prove RH or its negation.
- It does not show that probability, GGC, Fourier, or screw-function methods can never work.
- It does not reconstruct every detail of the other thread.
- It does not claim originality for the known generalized Laguerre hierarchy.
- The generating-family warning in §9.1 and the pole-repair no-go theorem are independent deductions here, but novelty relative to the entire literature has not been established.

## 13. Source ledger / Zotero-ready records

Recommended collection: **RH / Parallel Audit / 2026-08-01**

1. **Polson, Nicholas G.** “On Hilbert's 8th Problem.” arXiv:1708.02653v23, revised July 4, 2026.  
   URL: https://arxiv.org/abs/1708.02653  
   DOI: `10.48550/arXiv.1708.02653`  
   Tags: `RH`, `GGC`, `Thorin`, `Gamma mixture`, `audited`, `equation 21`, `domain issue`.

2. **Polson, Nicholas G.** “Riemann, Thorin, van Dantzig Pairs, Wald Couples and Hadamard Factorisation.” arXiv:1804.10043v8, revised April 29, 2026 (PDF dated May 1).  
   URL: https://arxiv.org/abs/1804.10043  
   DOI: `10.48550/arXiv.1804.10043`  
   Tags: `RH`, `Thorin condition`, `Exp(3/4)`, `exponential tilt`, `Wald couple`.

3. **Polson, Nicholas G.** “RETRACTED: On Hilbert's 8th Problem.” *Brazilian Journal of Probability and Statistics* 32(3), 2018.  
   URL: https://projecteuclid.org/journals/brazilian-journal-of-probability-and-statistics/volume-32/issue-3/RETRACTED-On-Hilberts-8th-problem/10.1214/18-BJPS392.full  
   DOI: `10.1214/18-BJPS392`  
   Tags: `retracted`, `publication history`, `do not treat as current preprint`.

4. **Csordas, George.** “Fourier transforms of positive definite kernels and the Riemann \(\xi\)-Function.” arXiv:1309.0055v2, 2014.  
   URL: https://arxiv.org/abs/1309.0055  
   DOI: `10.48550/arXiv.1309.0055`  
   Tags: `positive definite kernel`, `generalized Laguerre inequality`, `K_n`, `two-copy kernel`.

5. **Griffin, Michael; Ono, Ken; Rolen, Larry; Zagier, Don.** “Jensen polynomials for the Riemann zeta function and other sequences.” arXiv:1902.07321, 2019.  
   URL: https://arxiv.org/abs/1902.07321  
   DOI: `10.48550/arXiv.1902.07321`  
   Tags: `Jensen polynomial`, `Hermite asymptotics`, `RH equivalence`.

6. **Farmer, David W.** “Jensen polynomials are not a plausible route to proving the Riemann Hypothesis.” arXiv:2008.07206, 2020.  
   URL: https://arxiv.org/abs/2008.07206  
   DOI: `10.48550/arXiv.2008.07206`  
   Tags: `Jensen polynomial`, `route audit`, `universality`.

7. **Michalowski, Wojciech.** “On the Pólya Frequency Order of the de Bruijn–Newman Kernel: Certified Failure at Order Five.” arXiv:2602.20313v2, July 20, 2026.  
   URL: https://arxiv.org/abs/2602.20313  
   DOI: `10.48550/arXiv.2602.20313`  
   Tags: `PF5`, `certified counterexample`, `interval arithmetic`, `route exclusion`.

8. **Michalowski, Wojciech.** “An explicit uniform cubic wedge for consecutive Toeplitz minors of the Riemann xi coefficients.” arXiv:2607.16795, July 18, 2026.  
   URL: https://arxiv.org/abs/2607.16795  
   DOI: `10.48550/arXiv.2607.16795`  
   Tags: `Toeplitz minor`, `PF infinity`, `tail regime`, `certified computation`.

9. **Suzuki, Masatoshi.** “Weil's quadratic form via the screw function.” arXiv:2606.09096, June 8, 2026.  
   URL: https://arxiv.org/abs/2606.09096  
   DOI: `10.48550/arXiv.2606.09096`  
   Tags: `Weil criterion`, `screw function`, `operator`, `spectral conjecture`.

Suggested relations:

- Record 1 **is audited by** this ledger.
- Record 2 **supplies background for** the pole-mode discussion.
- Record 3 **is earlier version/history of** Record 1, but should not be conflated with v23.
- Record 4 **formalizes** the hierarchy replacing the insufficient \(\nu_2\)-only endpoint.
- Records 5–9 **are compared with** the hierarchy-first program.

## 14. Compact theorem ledger

### Proven within this audit

1. A nonzero positive mixture \(\int(s+\lambda)^{-2}M(d\lambda)\) cannot equal the centered even xi ratio in a neighborhood of zero.
2. The cell translation in the audited preprint cannot factor a shifted cosh using only one factor \((\pi n^2)^{z/2}\).
3. The identity \(e^{-ku}=\int_k^\infty ue^{-\lambda u}d\lambda\) cannot be used for the negative \(u\) values present in the displayed cell integral.
4. A super-exponentially decaying kernel cannot be a nonzero positive mixture of finite-rate exponentials.
5. Removing the \(\operatorname{Exp}(c-1/4)\) pole mode cannot leave a positive Laplace transform through the point where the remainder must vanish.
6. \(\nu_2\) is exactly the Fourier kernel of \(F'^2-FF''\).
7. No smooth even nonconstant \(\cosh(\alpha t)\nu_2(t)\) can be both decreasing and convex on all \(t>0\).
8. The first Laguerre inequality does not imply real-rootedness.
9. Positivity of the master sum \(|F(x+i\sqrt\tau)|^2\) is automatic; RH requires coefficientwise positivity.

### Still open

1. Prove or disprove \(L_n(x)\ge0\) for all \(n,x\) for the Riemann xi function.
2. Find a uniform positive-definite/Gram representation for all \(K_n\).
3. Connect the arithmetic screw-function representation to the Fourier hierarchy in a way that creates, rather than assumes, global prime cancellation.

---

**Bottom line:** the useful result of this parallel pass is not a counterfeit RH proof. It is a pair of exact route eliminations, a no-go theorem for the proposed probabilistic repair, and a corrected hierarchy that states precisely what a successful two-copy argument would actually have to prove.
