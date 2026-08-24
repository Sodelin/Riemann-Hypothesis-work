#!/usr/bin/env python3
"""Odd-sector finite-basis diagnostic for the localized Weil quadratic form.

STATUS: NUMERICAL DIAGNOSTIC ONLY.

This program does NOT prove RH, odd-sector positivity, or a spectral sign.
It is designed to falsify overly strong intermediate claims and locate near-null
vectors/prime thresholds for later interval certification.

Mathematical normalization
--------------------------
For a real odd test function f supported in [-a,a], the exact diagonal Weil form
in the normalization used by this repository is

  Q(f) = Gamma(f) + Pole(f) + Prime(f),

where

  Gamma(f) = integral mu(r) |fhat(r)|^2 dr,
  mu(r) = [Re digamma(1/4+i r/2)-log(pi)]/(2*pi),

  Pole(f) = -2 | integral f(x) sinh(x/2) dx |^2,

and

  Prime(f) = -2 sum_n Lambda(n)/sqrt(n)
                  Re integral f(x) f(x-log n) dx.

The positive cosh pole moment vanishes identically for odd f.
Only prime powers with log(n)<2a can contribute.

Basis
-----
Let t=x/a. We use the C^2 zero-extendable odd basis

  phi_j(x) = (1-t^2)^3 P_{2j+1}(t),  j=0,...,N-1,

on [-a,a], zero outside.

The Gamma Fourier integral is truncated to [-R,R], so even a numerically stable
sign is not a proof. A candidate negative or extremely small value must be
rechecked with interval arithmetic and a rigorous Fourier tail estimate.

Dependencies: numpy, scipy.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np
from scipy.linalg import eigh
from scipy.special import digamma, eval_legendre, roots_legendre


def von_mangoldt(n: int) -> float:
    """Return log(p) if n is a positive power of one prime p, else 0."""
    if n < 2:
        return 0.0
    for p in range(2, math.isqrt(n) + 1):
        if n % p == 0:
            m = n
            while m % p == 0:
                m //= p
            return math.log(p) if m == 1 else 0.0
    return math.log(n)  # n prime


def gamma_density(r: np.ndarray) -> np.ndarray:
    z = 0.25 + 0.5j * r
    return (np.real(digamma(z)) - math.log(math.pi)) / (2.0 * math.pi)


def odd_basis(x: np.ndarray, a: float, N: int) -> np.ndarray:
    t = x / a
    envelope = (1.0 - t * t) ** 3
    return np.column_stack(
        [envelope * eval_legendre(2 * j + 1, t) for j in range(N)]
    )


@dataclass
class Diagnostic:
    a: float
    N: int
    R: float
    active_prime_powers: list[int]
    eigenvalues: np.ndarray


def form_matrices(
    a: float,
    N: int,
    *,
    nx: int = 140,
    nr: int = 1200,
    R: float = 80.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, list[int]]:
    if a <= 0:
        raise ValueError("a must be positive")
    if N < 1:
        raise ValueError("N must be positive")

    # L2 Gram matrix and pole moment on [-a,a].
    zx, wx = roots_legendre(nx)
    x = a * zx
    dxw = a * wx
    phi = odd_basis(x, a, N)
    gram = phi.T @ (dxw[:, None] * phi)

    sinh_moment = phi.T @ (dxw * np.sinh(x / 2.0))
    pole = -2.0 * np.outer(sinh_moment, sinh_moment)

    # Gamma/digamma Fourier multiplier, truncated to [-R,R].
    zr, wr = roots_legendre(nr)
    r = R * zr
    drw = R * wr
    fourier = np.exp(1j * np.outer(r, x)) @ (dxw[:, None] * phi)
    gamma = np.real(
        fourier.conj().T
        @ ((drw * gamma_density(r))[:, None] * fourier)
    )

    # Exact finite prime-power sector at this support scale, with numerical
    # quadrature only for the correlation matrix entries.
    prime = np.zeros((N, N), dtype=float)
    active: list[int] = []
    max_n = int(math.floor(math.exp(2.0 * a) + 1e-12))

    for n in range(2, max_n + 1):
        lam = von_mangoldt(n)
        if lam == 0.0:
            continue
        shift = math.log(n)
        if shift >= 2.0 * a:
            continue

        # For int f(t) f(t-shift) dt, t lies in [-a+shift,a].
        z, w = roots_legendre(nx)
        lo, hi = -a + shift, a
        t = 0.5 * (hi + lo) + 0.5 * (hi - lo) * z
        ww = 0.5 * (hi - lo) * w
        left = odd_basis(t, a, N)
        right = odd_basis(t - shift, a, N)
        corr = left.T @ (ww[:, None] * right)
        corr = 0.5 * (corr + corr.T)

        prime += (-2.0 * lam / math.sqrt(n)) * corr
        active.append(n)

    full = gamma + pole + prime
    full = 0.5 * (full + full.T)
    gamma = 0.5 * (gamma + gamma.T)
    pole = 0.5 * (pole + pole.T)
    prime = 0.5 * (prime + prime.T)
    gram = 0.5 * (gram + gram.T)
    return full, gamma, pole, prime, gram, active


def spectrum(
    a: float,
    N: int,
    *,
    nx: int = 140,
    nr: int = 1200,
    R: float = 80.0,
) -> Diagnostic:
    full, _, _, _, gram, active = form_matrices(
        a, N, nx=nx, nr=nr, R=R
    )
    vals = eigh(full, gram, eigvals_only=True, check_finite=True)
    return Diagnostic(a=a, N=N, R=R, active_prime_powers=active, eigenvalues=vals)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=6)
    parser.add_argument("--nx", type=int, default=140)
    parser.add_argument("--nr", type=int, default=1200)
    parser.add_argument("--R", type=float, default=80.0)
    args = parser.parse_args()

    radii = [0.25, 0.30, 0.35, 0.40, 0.50, 0.60, 0.70, 0.80, 1.00]

    print("# odd localized Weil finite-basis sweep -- NUMERICAL ONLY")
    print(f"# N={args.N} nx={args.nx} nr={args.nr} R={args.R}")
    print("# a       prime-powers        first four generalized eigenvalues")

    for a in radii:
        out = spectrum(a, args.N, nx=args.nx, nr=args.nr, R=args.R)
        pp = ",".join(map(str, out.active_prime_powers)) or "-"
        ev = " ".join(f"{v:+.12e}" for v in out.eigenvalues[:4])
        print(f"{a:5.2f}    {pp:16s}    {ev}")

    print("\n# Fourier-cutoff stability -- NUMERICAL ONLY")
    for a in [0.60, 0.70, 0.80, 1.00]:
        print(f"# a={a}")
        for R, nr in [(60.0, 900), (80.0, 1200), (100.0, 1500), (120.0, 1800)]:
            out = spectrum(a, args.N, nx=args.nx, nr=nr, R=R)
            ev = " ".join(f"{v:+.12e}" for v in out.eigenvalues[:3])
            print(f"R={R:6.1f} nr={nr:4d}  {ev}")


if __name__ == "__main__":
    main()
