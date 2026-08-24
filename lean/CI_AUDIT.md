# Lean CI audit trigger

This file exists to create a pull-request-triggered CI run that can be inspected through the connected GitHub audit tooling.

The PR is not evidence that a theorem is correct by itself. Promotion to `LEAN_VERIFIED` requires the pinned package to build successfully, the target theorem to contain no `sorry`/local axioms, and the relevant axiom output to be inspected.
