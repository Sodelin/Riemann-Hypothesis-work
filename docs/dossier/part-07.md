| Review safeguard | Status | Consequence |
|---|---|---|
| Preregistered protocol | No | Query evolution may favor claims discovered during the search |
| Multiple independent search tracks | Partial | Reduces individual omission, but shared-model correlation remains |
| Primary-source verification | Yes for decisive claims | Muranaka, Csordas, Newman, and policy claims were checked in full text |
| Duplicate theorem extraction | Yes for the two candidate results | Formulas and constants were independently reconstructed |
| Complete bibliographic databases | No | Novelty cannot be certified |
| Backward/forward citation chasing | Partial | Good around the core authors; not exhaustive |
| Version control for current preprints | Yes where material | Prevents relying on claims withdrawn in later versions |
| External domain-expert review | Not yet | Blocks publication-grade confidence |
| Reproducible search log | Substantial but not complete | Supports a scoping review, not a formal systematic review |

The review is strong enough to say that the **bare finite-prefix theorem is known** and that the Epstein identity is **classical in substance**. It is only moderately informative about whether the all-\(N\), strictly-log-concave admissible-kernel construction is new. “No exact precedent located” is the strongest warranted language.

### 11.4 Where the search was most vulnerable

The most dangerous recurring pattern was **promotion by resemblance**:

- a positive kernel was mistaken for a positive-definite kernel;
- a positive summed generating function was mistaken for positive coefficients;
- one Laguerre inequality was mistaken for the whole hierarchy;
- low-order alternating derivatives were mistaken for complete monotonicity;
- an equivalent operator positivity statement was mistaken for a proof of that positivity.

The countermeasure was to ask, at every promotion step, what exact cone the object belongs to and in which variable. Pointwise positivity, Hankel positivity in \(n\), and positive definiteness in \(r\) are different properties.

### 11.5 How the psychology analogy actually helped

The useful psychological analogy was not a replacement for proof. It was a way to track measurement validity:

- \(L_1\) is a screen, not a diagnosis;
- the full hierarchy is the complete diagnostic battery;
- summed positivity can have good face validity while hiding a negative component;
- inner factors are latent variables invisible to a boundary-modulus instrument;
- multi-agent independence reduces correlated error, while adversarial review tests convergent claims for a shared blind spot.

Every analogy was translated back into an equation, a domain condition, or a counterexample before it influenced the mathematical verdict.

### 11.6 Search-policy and reporting reflection

The supplied benchmark-style prompt improved the project when interpreted as research governance: maintain route diversity, do not count equivalent lemmas as progress, and audit exact multiplicities/signs/domains. Its instruction to assume a proof exists was rejected. In an open problem, that instruction changes the loss function from “find truth” to “produce a proof-shaped object,” which is precisely the wrong optimization pressure.

The user's role is real but should be described accurately: conceptualization of the project, design of the search protocol, insistence on persistence and multi-agent adversarial review, project administration, and curation. Those contributions do not by themselves make someone the mathematical guarantor of a proof. CRediT roles can describe contribution but do not determine authorship. A human author of a mathematical note must understand, verify, and accept responsibility for the complete argument. Significant generative-AI use should be disclosed in the methods or acknowledgments; the AI system should not be listed as an author.

## 12. Robustness and adversarial audit

### 12.1 Three-axis evidence model

Correctness, originality, and usefulness were rated separately:

| Candidate | Correctness | Originality | Usefulness | Robust conclusion |
|---|---|---|---|---|
| Muranaka-style finite-prefix obstruction | Established | Known | High context value | Cite, never claim |
| All-\(N\), strictly-log-concave admissible-kernel lift in §8 | High internal confidence | Unresolved; plausible | High as a sharp route barrier | Best candidate for human review |
| Arbitrarily thin strip | Correct | Mostly scaling once a counterexample exists | Modest | Supporting feature, not headline novelty |
| Strict log-concavity of the §8 kernel | Complete three-region proof; separately refereed by a model instance | No focused prior-art search beyond the closest kernel examples | High strengthening value | Include in the candidate theorem; require human audit |
| Epstein–Eisenstein identity and completed remainder | High | Classical in substance | Moderate | Record the unconditional PD grouping and the failed factorization |
| Theta-slice non-PD certificate | High, with explicit error budget | Not assessed | Moderate route-exclusion value | Keep as a supporting result |
| Fenchel-energy equivalent family | High algebraic confidence | Not assessed | Moderate to high proof-engineering value | Seek author/specialist feedback; no standalone paper |
| Suzuki displayed-constant correction | Very high | Minor erratum, not a theorem | High for reproducibility | Notify author/editor privately |
| RH proof | Absent | — | — | No claim |

This separation prevents two common errors: treating a correct identity as research progress merely because its notation is new, and treating failure to locate a source as proof of originality.

### 12.2 Novelty triangulation and meta-epistemic robustness

The principal novelty conclusion was stress-tested against three counterfactuals:

1. **If Muranaka is counted**, the broad finite-prefix claim disappears; only the admissible-kernel lift survives.
2. **If classical Eisenstein theory is counted at the level of substance rather than exact typography**, the Epstein identity becomes a repackaging, not a new theorem.
3. **If strict log-concavity is demanded as part of “Riemann-like,”** the new three-region estimate shows that §8 still survives; the construction can be made globally strictly log-concave by taking the smoothing scale sufficiently large.

These counterfactuals are not cosmetic. The first two materially downgrade claims that initially looked novel; the third triggered a new proof and strengthened the surviving candidate. The resulting verdict remains conservative: there is one plausible negative theorem in entire-function theory, but no RH proof and no basis for a public priority announcement before human review.

A quantitative meta-analysis would be inappropriate. The sources do not report commensurable effect sizes; they establish heterogeneous exact theorems, examples, and equivalences. The relevant synthesis is logical—hypothesis inclusion, theorem strength, and failure modes—not statistical pooling.

### 12.3 Multi-instance referee verdict on the inherited ledger

The referee track checked every central formula A1–A8, B1–B6, and C1–C8. The two-copy and hierarchy algebra, including all signs and factorials, survived. The referee strengthened the Polson objections and corrected the terminology around absolute monotonicity. Because the reviewer was another instance of the same model family, this is a cross-audit rather than independent peer review.

### 12.4 Cross-audit of the promoted deductions

The hierarchy construction was checked by a separate model instance at its three vulnerable points: the \(B\)-coefficient formula, uniform domination at zeros of \(\cos(Rx)\), and strict decrease after smoothing. The auditor confirmed all three, with the compact-uniform derivative argument

\[
\frac{G_\varepsilon(y)}y
=\int_0^1G_\varepsilon'(\theta y)\,d\theta
\]

making the endpoint \(y=0\) rigorous. Newman’s \(b>0\) theorem and a \(b\downarrow0\) Hurwitz limit justify the real-zero property of \(\widehat{e^{-t^4}}\).

A separate audit checked the convexity-resummed hierarchy, the Fourier normalization, and the arithmetic prime-shock decomposition. It found no missing factors. It also confirmed that the Legendre description is used only after \(t_c=\log\rho\), where the background \(B\) is convex.

Cycle II added four targeted checks:

- Muranaka's theorem and explicit \(b_N=(N+\sqrt N)/2\) construction were extracted from the full thesis;
- the §8 smoothing factor \(\widehat{e^{-t^4}}\in\mathrm{L\!-\!P}\) was justified through Newman plus a Hurwitz limit, and the full derivative-tail condition was verified;
- Csordas's Example 3.12 was identified as the closest one-level, almost-admissible predecessor;
- the \(1/32\) and \(1/8\) constants, beta integral, axis cancellation, and continuation caveat in §9.7 were independently reconstructed.

It then added five further adversarial checks: the theta-slice shortcut was rejected by an explicit integer-vector quadratic form and a self-contained directed-rounding interval certificate; the Fenchel-energy update was derived both from conjugate differentiation and from its Bregman-divergence form; two model instances separately recovered the missing \(-\tfrac12\log\pi\) in Suzuki’s displayed derivative constant and reproduced the paper’s stated numerical roots; a separate referee instance reconstructed every region and constant in the strict-log-concavity proof; and the Epstein cross-scale completion was checked against both its Fourier quotient and the Laurent obstruction to parameter monotonicity. None closes the global RH inequality.

### 12.5 Confidence matrix

| Finding | Confidence | Failure mode still possible |
|---|---:|---|
| One-sided positive Gamma/Stieltjes center mixture is impossible | Very high | Only a materially different signed or bilateral representation |
| Polson pole tilt crosses the MGF boundary | Very high | None inside the stated positive-probability interpretation |
| \(K_1\) is exact but insufficient | Certain | None; \(x^4-1\) is an exact counterexample |
| Full \(K_n/L_n\) hierarchy is equivalent to RH | Very high | Normalization/growth hypotheses were explicitly checked for xi |
| Tilted-autocorrelation-order criterion is equivalent to RH | Very high | Fourier convention is fixed throughout this document |
| Convexity-resummed criterion is equivalent to RH | Very high | Independently checked, including the critical-line-zero edge case |
| \(S_\alpha\) is not a positive Gaussian scale mixture | High | Uses the standard Riemann-kernel tail bound and Bernstein representation |
| Generic tilt monotonicity counterexample | Very high | The strict negative value persists under smooth super-Gaussian regularization |
| Finite-hierarchy admissible-kernel theorem | Very high internally | Human proof check and full novelty search still absent |
