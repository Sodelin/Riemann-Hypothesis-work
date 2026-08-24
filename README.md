# Riemann Hypothesis Work

This repository is a documentation and active-research archive for an exploratory, AI-assisted program concerning the Riemann Hypothesis.

## Status

**No proof or disproof of the Riemann Hypothesis is claimed.** The materials record proof attempts, adversarial audits, exact route eliminations, equivalent reformulations, candidate lemmas, formalization targets, computational certificates, and questions for independent expert review.

The 2026-08-01 cycle is preserved as the historical audited dossier. An active 2026-08-23 cycle now uses Git history as a claim/method ledger and attacks an explicit Lean-oriented gap graph rather than treating every reformulation as fresh progress.

## Active research cycle

- [`research/2026-08-23/README.md`](research/2026-08-23/README.md) — cycle overview and work queue.
- [`research/2026-08-23/ADVERSARIAL_PROTOCOL.md`](research/2026-08-23/ADVERSARIAL_PROTOCOL.md) — status rules, falsification gates, route-kill/reopen rules, and proof-promotion standard.
- [`research/2026-08-23/LEAN_GAP_GRAPH.md`](research/2026-08-23/LEAN_GAP_GRAPH.md) — named nodes between current Lean infrastructure and a complete RH implication.
- [`research/2026-08-23/ROUTE_A_PRIME_SHIFT_GRAPH.md`](research/2026-08-23/ROUTE_A_PRIME_SHIFT_GRAPH.md) — first experimental Weil/prime-shift block-positivity route.
- [`research/2026-08-23/EXACT_DIAGONAL_WEIL_FORM.md`](research/2026-08-23/EXACT_DIAGONAL_WEIL_FORM.md) — exact diagonal decomposition into prime-shift correlations, Gamma multiplier, and rank-two pole sector.
- [`research/2026-08-23/CLAIM_LEDGER.csv`](research/2026-08-23/CLAIM_LEDGER.csv) — machine-readable claim/status ledger.
- [`research/2026-08-23/TOOLCHAIN_AND_PROMPT_INTEGRATION.md`](research/2026-08-23/TOOLCHAIN_AND_PROMPT_INTEGRATION.md) — current jurisdictions for Wolfram, Precise Special Functions, scholarly/prior-art tools, Chat/Work/Codex routing, Lean, GitHub, and Zenodo archival.
- [`lean/`](lean/) — pinned Lean 4 research package importing the current `Zeta23` formal infrastructure; local theorems remain `LEAN_TARGET` until a successful build/audit is observed.

The reusable prompt-programming, prior-art, and mode-routing architecture is maintained centrally in `Sodelin/Proof-attack-structure` rather than duplicated here. RH-specific mathematical status remains authoritative in this repository.

## Historical repository structure

- `docs/parallel-audit-ledger.md` — audit of earlier GGC/Thorin and two-copy Laguerre routes.
- `docs/expert-review-packet.md` — narrow review packet for the candidate finite-Laguerre admissible-kernel theorem.
- `docs/dossier/` — the full 2026-08-01 multi-agent research dossier, split into parts for readable version control.
- `code/theta_slice_interval_certificate.py` — directed-rounding interval certificate used in one route-exclusion check.

## Verification standard

An identity or RH-equivalent reformulation is not counted as a proof. Numerical evidence is not counted as a proof. Agreement among related AI model instances is not independent peer review. A result should be treated as established only after its implication chain, domains, interchanges, estimates, and prior-art status survive independent reconstruction and review.

The active cycle additionally distinguishes `LEAN_TARGET`, `UPSTREAM_LEAN`, and `LEAN_VERIFIED`. A theorem does not become locally `LEAN_VERIFIED` merely because it is written in Lean-shaped syntax or is known to exist in an upstream repository.

The current toolchain adds independent symbolic, arbitrary-precision, literature, and repository checks, but tool agreement does not change the evidential standard for RH.

## Attribution and archival language

These materials were produced through a generative-AI-assisted research process initiated and curated by a human user. The mathematical derivations have not all been independently reconstructed by qualified human experts. Any future manuscript or public mathematical claim should disclose significant AI assistance and identify only humans meeting the relevant authorship standard as authors.

A future Zenodo deposit or DOI should be described as an archived/deposited research snapshot unless there is a separate peer-review or journal-publication event. A DOI provides persistence and citability; it does not itself certify correctness, novelty, or acceptance.
