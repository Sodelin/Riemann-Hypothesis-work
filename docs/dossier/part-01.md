# Riemann Hypothesis: Multi-Agent Proof Attempt and Adversarial Research Dossier

**Date:** 2026-08-01  
**Status:** Two completed multi-agent research cycles. No proof of the Riemann Hypothesis was found or is claimed.  
**Source ledger audited:** `Riemann_Hypothesis_Parallel_Proof_Ledger_2026-08-01.md`  
**Companion expert packet:** `Finite_Laguerre_Admissible_Kernel_Expert_Review_Packet_2026-08-01.md`  
**Companion interval certificate:** `theta_slice_interval_certificate.py`  
**Success rule:** “Solved” means a complete implication chain to RH survives independent algebraic, analytic, source, and counterexample audits. An equivalent reformulation or a theorem-strength missing lemma does not count.

**Cycle-II revision:** This version adds a targeted novelty review, a reporting decision, an exact Epstein–Eisenstein modular regrouping, a theta-slice obstruction, a Fenchel refinement of Suzuki’s barriers, a minor reproducibility correction to one printed constant, a proof of strict log-concavity for the finite-hierarchy construction, and a human-validation protocol. It also corrects the novelty context of the finite-hierarchy theorem: arbitrary finite-prefix insufficiency was already proved by Brandon Muranaka in 2003; only the strengthened all-\(N\), strictly-log-concave admissible-kernel statement remains a candidate contribution.

## 0. Executive decision brief

### 0.1 Current verdict

The second cycle did **not** solve RH. It did materially change what, if anything, should be reported.

1. **Do not report “finite Laguerre checks are insufficient” as new.** Muranaka's 2003 master's thesis proves that for every \(N\) there is a function in \(\mathrm{L\!-\!P}^{*}\) satisfying \(L_0,\ldots,L_N\ge0\) on the real line while \(L_{N+1}\) is negative somewhere.
2. **One strengthening remains a candidate research result.** Section 8 constructs, for every \(N\) and every strip width \(\tau>0\), a strictly log-concave admissible Fourier kernel whose transform has nonreal zeros inside \(|\operatorname{Im}z|\le\tau\) while passing \(L_0,\ldots,L_N\) globally. The proof, including global strict log-concavity, has survived multi-instance adversarial audit, but the literature review cannot certify originality. It needs review by a specialist in entire functions and the Laguerre–Pólya class.
3. **A second-cycle identity is mathematically exact but not a proof.** Section 9.7 expresses the full tilted autocorrelation of \(\xi\) as a fourth-order differential operator applied to a completed rectangular Epstein zeta function. It repairs the termwise theta-cell convergence failure by preserving modular cancellation. Its constants and continuation were separately reconstructed in the multi-instance audit. Positive-definite monotonicity of its derivative remains exactly RH-equivalent.
4. **No public priority claim is presently justified.** The appropriate next act is a short, private referee packet asking two narrow questions—correctness and prior art—not an “RH breakthrough” announcement.

### 0.2 Novelty, usefulness, and action matrix

| Output | Correctness status | Closest located prior art | Novelty status | Likely usefulness | Action |
|---|---|---|---|---|---|
| Full generalized Laguerre hierarchy characterizes \(\mathrm{L\!-\!P}\) | Established literature | Csordas–Varga; Csordas–Vishnyakova | Known | Foundational | Cite only |
| Arbitrary finite-prefix insufficiency | Established literature | Muranaka, Theorem 2.5/10.2 (2003) | Known | Important context | Cite explicitly; do not claim |
| Finite-prefix insufficiency within **strictly log-concave admissible Fourier kernels**, with nonreal zeros in any prescribed strip | Internally proved and adversarially cross-audited | Muranaka is broader/weaker; Csordas gives an \(N=1\), non-admissible predecessor | **Potentially new; unverified** | High as a sharp route-exclusion theorem | Private specialist review, then decide on a short note |
| Tilted-autocorrelation / positive-definite-order criterion | Exact corollary of known modulus monotonicity plus Bochner | Sondow–Dumitrescu; Csordas | New packaging at most | Conceptually useful | Keep as exposition, not a standalone novelty claim |
| Epstein–Eisenstein formula and completed-remainder factorization | Constants, continuation, and cross-scale completion cross-audited | Completed Eisenstein series, Chowla–Selberg expansion, and regularized Mellin transform | Classical in substance; possibly project-specific packaging | Moderate; yields an unconditional PD grouping and two exact route exclusions | Record with classical citations; do not make a novelty claim |
| Non-positive-definite theta-slice certificate | Self-contained directed-rounding interval certificate | No focused originality search | Possibly new but narrow | Useful route exclusion | Keep in dossier; no standalone claim |
| Fenchel-energy equivalent family for Suzuki’s prime-shock barriers | Exact convex-duality derivation and dominance proof; finite scan only | No focused originality search | Unknown | Moderate to high proof-engineering value | Send privately to Suzuki or a specialist; no standalone claim |
| Missing \(-\tfrac12\log\pi\) in Suzuki’s displayed derivative constant | Separately re-derived by two model instances and checked against the paper’s numerical roots | No erratum located in the journal version or arXiv v4 | Minor source correction | Prevents failed reproduction; theorem unaffected | Send a courteous private erratum note to the author/editor |
| Gaussian-mixture tail obstruction and generic tilt counterexample | Internally proved | No exact match located | Elementary project observations | Useful for avoiding dead ends | Include as supporting lemmas, not standalone papers |
| Prime-shock / prefix Legendre barriers | Exact algebraic repackaging | Suzuki's screw-function criterion | Expository/computational | Useful for diagnostics | Cite Suzuki; label as repackaging |
| A proof of RH | Not obtained | — | — | — | Make no claim |

### 0.3 Reporting decision

The recommended sequence is deliberately conservative:

1. reduce the candidate material to a short technical note containing only the theorem in §8 and the exact comparison with Muranaka; keep the classical-in-substance Epstein identity separate unless an analytic-number-theory expert sees independent value in it;
2. obtain independent checks from (i) an expert in entire functions/Laguerre–Pólya theory and (ii) a separate expert focused on prior art; consult an analytic-number-theory expert only for the Epstein, theta-slice, or screw-function material;
3. ask each reviewer separately whether the statement is correct, whether it is already known, and whether the strengthening is useful enough to circulate;
4. revise until a human author can personally defend every line;
5. only then consider an arXiv preprint or journal submission, with prominent disclosure of the multi-agent generative-AI derivation and the human verification performed.

If no mathematically qualified person is willing to take responsibility for the proof, the right output is a transparent exploratory research record—not a submitted theorem. arXiv and AMS policies both place responsibility on human authors and prohibit listing an AI system as an author.

This project made a genuine multi-route attempt rather than selecting one attractive reformulation and defending it. The current result is **not a proof of RH**. It is a progressively audited research record with four kinds of output:

1. exact eliminations of false probabilistic and shape-based shortcuts;
2. a multi-instance cross-checked statement of the full generalized Laguerre hierarchy that really is equivalent to RH;
3. a phase-sensitive reformulation as monotonicity, in positive-definite order, of exponentially tilted autocorrelation kernels;
4. new barrier results showing why several finite or “manifestly positive” approximations cannot bridge the remaining gap.

The strongest live target is this. Let

\[
F(w)=\xi\!\left(\frac12+w\right)=\int_{\mathbb R}\Phi(u)e^{wu}\,du
\]

and define the tilted autocorrelation

\[
T_\alpha(r)=\int_{\mathbb R}e^{2\alpha m}
\Phi\!\left(m+\frac r2\right)
\Phi\!\left(m-\frac r2\right)\,dm.
\]

Its Fourier transform is

\[
\widehat T_\alpha(t)=|F(\alpha+it)|^2\ge 0,
\]

so every \(T_\alpha\) is automatically positive definite. Define

\[
S_\alpha(r):=\frac12\,\partial_\alpha T_\alpha(r).
\]

Then

\[
\widehat S_\alpha(t)
=\operatorname{Re}\!\left(F'(\alpha+it)\overline{F(\alpha+it)}\right)
=\frac12\partial_\alpha |F(\alpha+it)|^2.
\]

By the Sondow–Dumitrescu monotonicity theorem, RH is equivalent to \(S_\alpha\) being positive definite for every \(\alpha>0\). Only \(0<\alpha<1/2\) is unresolved; the half-plane \(\alpha>1/2\) corresponds to the classical zero-free half-plane \(\Re s>1\).

The exact bridge to the Laguerre hierarchy is

\[
T_\alpha(r)=\sum_{n=0}^{\infty}
\frac{\alpha^{2n}}{(2n)!}K_n(r),
\qquad
S_\alpha(r)=\sum_{n=1}^{\infty}
\frac{n\alpha^{2n-1}}{(2n)!}K_n(r),
\]

where

\[
K_n(r)=\int_{\mathbb R}(r-2s)^{2n}\Phi(r-s)\Phi(s)\,ds.
\]

Thus the phase-sensitive route is not separate from the hierarchy: it is its derivative-generating family. The missing theorem is not pointwise positivity—\(S_\alpha(r)>0\) is automatic—but **positive definiteness** of \(S_\alpha\), equivalently positivity of its Fourier transform for every frequency.

## 1. Abstract

Let

\[
\Xi(z)=\xi\!\left(\frac12+iz\right)
\]

be the real even Riemann xi function. RH says that every zero of \(\Xi\) is real. We audited an inherited parallel proof ledger and then ran strategically separated model-instance tracks through generalized gamma convolutions, generalized Laguerre inequalities, total positivity, phase-sensitive modulus monotonicity, conditional-variance/GHS inequalities, and Weil/screw-function operators. The inherited ledger’s principal conclusions survive multi-instance cross-audit: a displayed one-sided positive Stieltjes/Gamma mixture cannot equal the centered even xi ratio; its derivation loses one branch of a shifted cosh and applies a positive-half-line identity on negative arguments; the proposed pole-mode tilt has a divergent exponential moment; and positivity of only the first two-copy kernel is insufficient for RH.

The synthesis introduces the tilted-autocorrelation family \(T_\alpha\), for which ordinary positive definiteness is automatic, while RH becomes monotonicity of this family in Bochner/Loewner order. Its derivative \(S_\alpha\) is a positive pointwise kernel and the derivative-generating transform of the complete Laguerre hierarchy. A second resummation shows that RH is equivalent to convexity of \(a\mapsto |\xi(1/2+a+it)|^2\) throughout the critical half-strip for every \(t\).

