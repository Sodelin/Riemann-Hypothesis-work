#!/usr/bin/env python3
"""Finite-basis diagnostic for the fixed-support archimedean + pole Weil sector.

STATUS: NUMERICAL DIAGNOSTIC ONLY.

This script does NOT prove positivity, negativity, RH, or an exact Morse index.
It truncates the Fourier integral to [-R,R] and restricts the quadratic form to a
finite-dimensional C^2 compact-support basis. Its purpose is to:

* falsify overly strong positivity heuristics;
* estimate where negative directions begin to appear;
* inspect how the finite-basis negative index changes with support scale L;
* generate candidate vectors for later rigorous/interval certification.

Exact quadratic form used
-------------------------
For f supported in I_L=[-L/2,L/2], with paper Fourier transform

    fhat(r) = integral f(x) exp(i r x) dx,

the archimedean + pole sector is

    q_AP(f)
      = integral_R mu(r) |fhat(r)|^2 dr
        + 2 | integral f(x) cosh(x/2) dx |^2
        - 2 | integral f(x) sinh(x/2) dx |^2,

where

    mu(r) = [Re digamma(1/4 + i r/2) - log(pi)] / (2*pi).

Basis
-----
With t=2x/L in [-1,1], use

    phi_k(x) = (1-t^2)^3 P_k(t),   k=0,...,N-1,

inside I_L and zero outside. Because the factor (1-t^2)^3 has a third-order
zero at each endpoint, the zero extension is C^2, matching the regularity used
by the literature explicit formula.

Dependencies: numpy, scipy.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np
from scipy.linalg import eigh
from scipy.special import digamma, eval_legendre, roots_legendre


@dataclass
class SpectrumResult:
    L: float
    N: int
    R: float
    eigvals: np.ndarray

    @property
    def numerical_negative_count(self) -> int:
        # Diagnostic threshold only. This is not an interval-certified sign test.
        return int(np.count_nonzero(self.eigvals < -1e-6))


def mu(r: np.ndarray) -> np.ndarray:
    """Upstream Zeta23 normalization of the Gamma density mu."""
    z = 0.25 + 0.5j * r
    return (np.real(digamma(z)) - math.log(math.pi)) / (2.0 * math.pi)


def basis_matrix(x: np.ndarray, L: float, N: int) -> np.ndarray:
    """Return phi_k(x_j) as an (len(x),N) matrix."""
    t = 2.0 * x / L
    envelope = (1.0 - t * t) ** 3
    return np.column_stack(
        [envelope * eval_legendre(k, t) for k in range(N)]
    )


def form_matrices(
    L: float,
    N: int,
    *,
    nx: int = 240,
    nr: int = 1600,
    R: float = 100.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return (AP, Gamma, Pole, L2_Gram) matrices in the chosen basis."""
    if L <= 0:
        raise ValueError("L must be positive")
    if N < 1:
        raise ValueError("N must be at least 1")

    # Physical-space Gauss-Legendre quadrature on I_L.
    zx, wx = roots_legendre(nx)
    x = (L / 2.0) * zx
    dxw = (L / 2.0) * wx
    phi = basis_matrix(x, L, N)

    gram = phi.T @ (dxw[:, None] * phi)

    # Exact finite-rank pole formula, quadrature only for the moment integrals.
    c = phi.T @ (dxw * np.cosh(x / 2.0))
    s = phi.T @ (dxw * np.sinh(x / 2.0))
    pole = 2.0 * np.outer(c, c) - 2.0 * np.outer(s, s)

    # Fourier quadrature truncated to [-R,R].
    zr, wr = roots_legendre(nr)
    r = R * zr
    drw = R * wr

    # fhat_k(r) = int phi_k(x) exp(i r x) dx.
    fourier = np.exp(1j * np.outer(r, x)) @ (dxw[:, None] * phi)
    gamma = np.real(
        fourier.conj().T @ ((drw * mu(r))[:, None] * fourier)
    )

    ap = gamma + pole
    # Symmetrize away roundoff before the Hermitian generalized eigenproblem.
    ap = 0.5 * (ap + ap.T)
    gamma = 0.5 * (gamma + gamma.T)
    pole = 0.5 * (pole + pole.T)
    gram = 0.5 * (gram + gram.T)
    return ap, gamma, pole, gram


def spectrum(
    L: float,
    N: int,
    *,
    nx: int = 240,
    nr: int = 1600,
    R: float = 100.0,
) -> SpectrumResult:
    ap, _, _, gram = form_matrices(L, N, nx=nx, nr=nr, R=R)
    vals = eigh(ap, gram, eigvals_only=True, check_finite=True)
    return SpectrumResult(L=L, N=N, R=R, eigvals=vals)


def print_sweep(
    L_values: list[float],
    N_values: list[int],
    *,
    nx: int,
    nr: int,
    R: float,
) -> None:
    print("# finite-basis q_AP sweep -- NUMERICAL ONLY")
    print(f"# nx={nx} nr={nr} R={R}")
    print("# L          N   min_generalized_eigenvalue   neg_count   first_four")
    for L in L_values:
        for N in N_values:
            out = spectrum(L, N, nx=nx, nr=nr, R=R)
            first = " ".join(f"{v:+.9e}" for v in out.eigvals[:4])
            print(
                f"{L:10.6f} {N:3d} {out.eigvals[0]:+ .9e} "
                f"{out.numerical_negative_count:3d}   {first}"
            )


def print_R_stability(
    cases: list[tuple[float, int]],
    R_values: list[float],
    *,
    nx: int,
    nr: int,
) -> None:
    print("\n# R-truncation stability -- NUMERICAL ONLY")
    print(f"# nx={nx} nr={nr}")
    for L, N in cases:
        print(f"# case L={L:.12g}, N={N}")
        for R in R_values:
            out = spectrum(L, N, nx=nx, nr=nr, R=R)
            first = " ".join(f"{v:+.9e}" for v in out.eigvals[:3])
            print(f"R={R:7.2f}  {first}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--nx", type=int, default=240)
    parser.add_argument("--nr", type=int, default=1600)
    parser.add_argument("--R", type=float, default=100.0)
    args = parser.parse_args()

    L_values = [0.7, 0.8, 0.9, 1.0, math.log(4.0), 2.0, 3.0]
    N_values = [4, 6, 8, 10]
    print_sweep(L_values, N_values, nx=args.nx, nr=args.nr, R=args.R)

    print_R_stability(
        [(0.8, 10), (0.9, 10), (1.0, 10), (math.log(4.0), 10), (2.0, 10)],
        [50.0, 75.0, 100.0, 125.0, 150.0],
        nx=args.nx,
        nr=args.nr,
    )


if __name__ == "__main__":
    main()
