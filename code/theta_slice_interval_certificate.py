#!/usr/bin/env python3
"""Directed-rounding interval certificate for the theta-slice obstruction.

This script uses only Python's standard library.  It proves that the Toeplitz
quadratic form in dossier section 9.7 is negative.  No floating-point
transcendental functions are used: exponentials are enclosed by positive
Taylor sums with an explicit geometric remainder, and every Decimal operation
is rounded outward.
"""

from decimal import Decimal as D
from decimal import ROUND_CEILING, ROUND_FLOOR, localcontext
from math import comb

PRECISION = 80
TAYLOR_ORDER = 80

# A rigorous decimal bracket using 50 known digits of pi.
PI = (
    D("3.14159265358979323846264338327950288419716939937510"),
    D("3.14159265358979323846264338327950288419716939937511"),
)


def directed(operation, rounding):
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = rounding
        return +operation()


def down(operation):
    return directed(operation, ROUND_FLOOR)


def up(operation):
    return directed(operation, ROUND_CEILING)


def interval_add(left, right):
    return (
        down(lambda: left[0] + right[0]),
        up(lambda: left[1] + right[1]),
    )


def interval_multiply_positive(left, right):
    assert left[0] >= 0 and right[0] >= 0
    return (
        down(lambda: left[0] * right[0]),
        up(lambda: left[1] * right[1]),
    )


def interval_inverse_positive(value):
    assert value[0] > 0
    return (
        down(lambda: D(1) / value[1]),
        up(lambda: D(1) / value[0]),
    )


def interval_power_positive(value, exponent):
    result = (D(1), D(1))
    base = value
    while exponent:
        if exponent & 1:
            result = interval_multiply_positive(result, base)
        exponent //= 2
        if exponent:
            base = interval_multiply_positive(base, base)
    return result


def exp_positive_scalar(value):
    """Outward enclosure of exp(value) for a nonnegative exact Decimal."""
    assert value >= 0
    if value == 0:
        return D(1), D(1)

    scale = max(1, int(value.to_integral_value(rounding=ROUND_CEILING)))
    q_lower = down(lambda: value / D(scale))
    q_upper = up(lambda: value / D(scale))

    # The truncated positive series is a lower bound.
    term = D(1)
    lower = D(1)
    for k in range(1, TAYLOR_ORDER + 1):
        term = down(lambda term=term, k=k: term * q_lower / D(k))
        lower = down(lambda lower=lower, term=term: lower + term)

    # Add an explicit geometric majorant for the omitted positive tail.
    term = D(1)
    upper = D(1)
    for k in range(1, TAYLOR_ORDER + 1):
        term = up(lambda term=term, k=k: term * q_upper / D(k))
        upper = up(lambda upper=upper, term=term: upper + term)
    next_term = up(
        lambda: term * q_upper / D(TAYLOR_ORDER + 1)
    )
    denominator = down(
        lambda: D(1) - q_upper / D(TAYLOR_ORDER + 2)
    )
    upper = up(lambda: upper + next_term / denominator)

    return interval_power_positive((lower, upper), scale)


def exp_positive(value):
    """Outward enclosure of exp(x) for x in a nonnegative interval."""
    return (
        exp_positive_scalar(value[0])[0],
        exp_positive_scalar(value[1])[1],
    )


def exp_negative(value):
    """Outward enclosure of exp(-x) for x in a positive interval."""
    return interval_inverse_positive(exp_positive(value))


def a_bounds(r):
    """Enclose a(exp(r)), where a(x)=2 sum_{n>=1} exp(-pi*n^2*x)."""
    exp_r = exp_positive((r, r))
    first_five = (D(0), D(0))

    for n in range(1, 6):
        exponent = interval_multiply_positive(PI, exp_r)
        exponent = (
            down(lambda exponent=exponent, n=n: exponent[0] * D(n * n)),
            up(lambda exponent=exponent, n=n: exponent[1] * D(n * n)),
        )
        first_five = interval_add(first_five, exp_negative(exponent))

    # For n>=6, n^2 >= 36+13(n-6), and exp(r)>=1.  Therefore
    # 2*sum exp(-pi*n^2*exp(r)) <= 2*exp(-36*pi)/(1-exp(-13*pi)).
    ratio_upper = exp_negative(
        (down(lambda: D(13) * PI[0]), up(lambda: D(13) * PI[1]))
    )[1]
    leading_upper = exp_negative(
        (down(lambda: D(36) * PI[0]), up(lambda: D(36) * PI[1]))
    )[1]
    tail_upper = up(
        lambda: D(2) * leading_upper / (D(1) - ratio_upper)
    )

    return (
        down(lambda: D(2) * first_five[0]),
        up(lambda: D(2) * first_five[1] + tail_upper),
    )


def kernel_bounds(r):
    """Enclose G(r)=a(exp(r))*a(exp(-r)) for r>=0.

    Jacobi inversion gives
      a(exp(-r)) = exp(r/2)*(1+a(exp(r))) - 1,
    so only the rapidly convergent theta series at exp(r)>=1 is needed.
    """
    a_value = a_bounds(r)
    half_exp = exp_positive(
        (down(lambda: r / D(2)), up(lambda: r / D(2)))
    )
    second_factor = interval_multiply_positive(
        half_exp,
        (down(lambda: D(1) + a_value[0]), up(lambda: D(1) + a_value[1])),
    )
    second_factor = (
        down(lambda: second_factor[0] - D(1)),
        up(lambda: second_factor[1] - D(1)),
    )
    assert second_factor[0] > 0
    return interval_multiply_positive(a_value, second_factor)


def main():
    # Points r_j=0.15*j and c_j=(-1)^j*binom(10,j).
    coefficients = [(-1) ** j * comb(10, j) for j in range(11)]
    lag_weights = [
        sum(
            coefficients[j] * coefficients[j + lag]
            for j in range(11 - lag)
        )
        * (1 if lag == 0 else 2)
        for lag in range(11)
    ]
    kernel_intervals = [
        kernel_bounds(D(3 * lag) / D(20)) for lag in range(11)
    ]

    lower = D(0)
    upper = D(0)
    for weight, value in zip(lag_weights, kernel_intervals):
        if weight >= 0:
            lower = down(lambda lower=lower, weight=weight, value=value:
                         lower + D(weight) * value[0])
            upper = up(lambda upper=upper, weight=weight, value=value:
                       upper + D(weight) * value[1])
        else:
            lower = down(lambda lower=lower, weight=weight, value=value:
                         lower + D(weight) * value[1])
            upper = up(lambda upper=upper, weight=weight, value=value:
                       upper + D(weight) * value[0])

    print("lag weights:", lag_weights)
    print("quadratic-form lower bound:", lower)
    print("quadratic-form upper bound:", upper)
    print("interval width:", upper - lower)
    assert upper < 0, "certificate failed: the upper endpoint is not negative"
    print("CERTIFIED: upper endpoint < 0, so G is not positive definite.")


if __name__ == "__main__":
    main()
