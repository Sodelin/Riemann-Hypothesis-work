# RH Toolchain and Prompt-Programming Integration

**Date:** 2026-08-23

## Status

This is a methodology update only. It does not alter any mathematical claim in the RH project, and it does not claim a proof or disproof of the Riemann Hypothesis.

The reusable methodology is maintained centrally in `Sodelin/Proof-attack-structure` so that Collatz and RH do not drift into incompatible copies of the same research protocol.

Relevant shared files:

- `framework/PROMPT_PROGRAMMING.md`
- `framework/GENERAL_RESEARCH_PROMPT_PROGRAM.md`
- `framework/TOOL_AND_MODE_ROUTING.md`
- `framework/PRIOR_ART_AND_NOVELTY_PROTOCOL.md`
- `templates/PROMPT_PROGRAM_SPEC.yaml`
- `templates/PROMPT_EVAL_RECORD.md`

## Current tool jurisdictions for RH

### Wolfram

Use for exact symbolic transformations, special-function identities, integral/series manipulation, finite symbolic systems, and an independently expressed check of derivations.

Do not treat symbolic agreement as a proof of RH or as formal verification.

### Precise Special Functions

This tool is particularly relevant to RH because it provides deterministic arbitrary-precision evaluation of the Riemann zeta function, Gamma function, and related special functions through mpmath-backed arithmetic.

Use it for:

- numerical stress tests;
- sign/size checks;
- independent reproduction of values used in a derivation;
- falsification of candidate inequalities or asymptotic claims on finite ranges.

Do not infer global zero-location facts from finite precision or finite-height checks.

### Python / Codex

Use for:

- interval/numerical experiments;
- test-function construction;
- matrix/operator discretizations;
- finite block-positivity experiments;
- property tests;
- exact/reproducible scripts;
- Lean repository work and clean builds when Codex is available.

### Elicit / Consensus / Firecrawl / Scholar Sidekick / Zotero

These jointly form a prior-art and source-verification pipeline.

For every potentially novel RH lemma or proof mechanism:

1. generate a theorem fingerprint in standard analytic-number-theory language;
2. search direct, structural, equivalent, historical, and adversarial formulations;
3. use Elicit/Consensus for scholarly discovery;
4. use Firecrawl for broad web, arXiv-adjacent, repository, lecture-note, thesis, and grey-literature discovery;
5. verify identifiers and bibliographic records with Scholar Sidekick;
6. preserve the accepted corpus in Zotero;
7. compare theorem content logically, not merely by title/keywords.

No individual search tool certifies novelty.

## Mode routing

### Chat

Use for narrow theorem decomposition, alternative hypotheses, choosing the next gap node, interpreting one computational result, and designing kill tests.

### Work

Use for multi-source prior-art sweeps, cross-tool verification, literature integration, long proof-architecture tasks, and finished research artifacts.

### Codex

Use for repository-aware execution: Python, Lean, tests, build logs, code review, and reproducible computational artifacts.

The current RH queue already separates bounded Lean infrastructure from the likely theorem-strength wall. Codex time should therefore be spent first on nodes such as `W-BLOCK-01`, `W-SHIFT-01`, `W-EDGE-01`, `W-NORM-01`, and `W-CRIT-01`, rather than asking a coding agent to 'prove RH' as an undifferentiated task.

## Prompt program

The RH orchestrator should be rendered from the shared Prompt Intermediate Representation:

`P = <G, S, C, R, D, T, V, O, M, F, X>`

with RH-specific bindings:

- `G`: exact RH endpoint / accepted equivalent criterion;
- `S`: current Lean gap graph, claim ledger, route statuses, and source state;
- `C`: domain, interchange, normalization, positivity, asymptotic, and equivalence constraints;
- `R`: upstream `zeta-23-lean`, local Lean package, code, literature, Wolfram, Precise Special Functions, and scholarly tools;
- `D`: current W/T route graph and named missing nodes;
- `T`: tool jurisdictions above;
- `V`: hostile audits, numerical falsification, formal checks, semantic statement audit, prior-art review;
- `O`: lemmas, code, proof files, counterexamples, source integrations, and continuation artifacts;
- `M`: Chat/Work/Codex routing;
- `F`: correctness, falsification, gap detection, routing, calibration, novelty-overclaim, reproducibility;
- `X`: continue/block/kill/formalize/candidate-resolution transitions.

## Numerical cross-check policy

When a candidate RH derivation depends on a numerical or symbolic subclaim, prefer independently expressed checks rather than one copied formula evaluated twice.

Example:

`paper/model derivation -> Python/mpmath or interval code -> Precise Special Functions -> Wolfram symbolic/numerical check -> interpretation audit`

Agreement can raise confidence in the subclaim and catch transcription/algebra errors. It does not alter the theorem's global proof status.

## Formal verification policy

The current distinction between `LEAN_TARGET`, `UPSTREAM_LEAN`, and `LEAN_VERIFIED` remains mandatory.

For local promotion to `LEAN_VERIFIED`:

- freeze the statement;
- use a pinned Lean/Mathlib/upstream revision;
- no `sorry` in the trusted path;
- inspect axioms/dependencies;
- clean-build;
- preserve logs;
- compare formal and intended mathematical statements semantically.

## Provenance and Zenodo

GitHub records the evolving research state. A milestone GitHub release may be archived through Zenodo and receive a DOI.

Use language such as:

- `archived on Zenodo`;
- `deposited release`;
- `DOI-assigned snapshot`;
- `publicly released research artifact`.

Do not infer from a Zenodo DOI that the work is peer reviewed, journal published, mathematically correct, novel, or accepted by specialists.

## Candidate-resolution mode switch

If any RH route appears to close the global criterion, stop broad prompt search and almost entirely reallocate effort to:

1. independent reconstruction;
2. hostile analytic audit;
3. numerical/symbolic falsification of every load-bearing subclaim;
4. Lean formalization where feasible;
5. exact statement-equivalence audit;
6. exhaustive prior-art search;
7. specialist review;
8. conservative public provenance and release language.

The closer a route appears to RH, the less useful additional creative agreement becomes and the more valuable independent attempted destruction becomes.
