import math


def taylor_expansion(f, a, x, terms):
    """
    Computes the Taylor series expansion of a function f around x = a up to the given number of terms.

    Parameters:
    - f: Function that returns the nth derivative of f at a.
    - a: Point around which the series is expanded.
    - x: Value at which the series is evaluated.
    - terms: Number of terms to sum in the series.

    Returns:
    - Approximation of f(x) using Taylor series.
    """
    taylor_sum = 0
    for n in range(terms):
        derivative_n = f(a, n)  # Compute nth derivative at a
        term = (derivative_n / math.factorial(n)) * (x - a) ** n
        taylor_sum += term
    return taylor_sum


# Example function: cos(x)
def cos_derivative(a, n):
    """Returns the nth derivative of cos(x) evaluated at x = a."""
    derivatives = [math.cos, math.sin, lambda x: -math.cos(x), lambda x: -math.sin(x)]
    return derivatives[n % 4](a)


# Compute the Taylor series approximation of cos(x) at x = 0.5 using 6 terms
# x = 0.5  # 28.6479 degrees
x = 1  # 57.2958 degrees
# x = 10_000
a = 0  # Maclaurin series
terms = 6
approx_value = taylor_expansion(cos_derivative, a, x, terms)

print(f"Taylor series approximation of cos({x}) using {terms} terms: {approx_value}")
print(f"Actual cos({x}): {math.cos(x)}")
