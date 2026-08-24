import Zeta23.Unconditional

namespace RHResearch

/--
Scalar weighted Young inequality underlying the planned shift-edge estimates.

This is intentionally zeta-independent. It is the first small theorem in the active
2026-08-23 gap graph that we want CI to compile before building the larger block lemma.
-/
theorem weighted_young (u v λ : ℝ) (hλ : 0 < λ) :
    2 * u * v ≤ λ * u ^ 2 + v ^ 2 / λ := by
  have hs : 0 ≤ (λ * u - v) ^ 2 := sq_nonneg (λ * u - v)
  have hmul : 2 * λ * u * v ≤ λ ^ 2 * u ^ 2 + v ^ 2 := by
    nlinarith
  have hdiv :
      (2 * λ * u * v) / λ ≤ (λ ^ 2 * u ^ 2 + v ^ 2) / λ :=
    (div_le_div_iff_of_pos_right hλ).2 hmul
  calc
    2 * u * v = (2 * λ * u * v) / λ := by
      field_simp [ne_of_gt hλ]
    _ ≤ (λ ^ 2 * u ^ 2 + v ^ 2) / λ := hdiv
    _ = λ * u ^ 2 + v ^ 2 / λ := by
      field_simp [ne_of_gt hλ]

#print axioms RHResearch.weighted_young

end RHResearch
