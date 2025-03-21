import multiprocessing as mp
import math

# This program calculates an approximation of the exponential function ( e^{deg}
# ) using a parallelized approach. It divides the computation into chunks,
# processes them in parallel using multiple CPU cores, and then sums the
# results. The compute_chunk function calculates partial sums of the series
# expansion for ( e^{deg} ), and the main function orchestrates the parallel
# computation and aggregation of these partial results.

# * EXPECTED RESULT: 0.7

# NUMBER_OF_CPUS = mp.cpu_count()
# TOTAL_ITERATIONS = 10_000
NUMBER_OF_CPUS = 1
TOTAL_ITERATIONS = 1


def taylor_nth_term(f, a, n, x):
    """Computes the nth term of the Taylor series of f(x) at x = a."""
    derivative_n = f(a, n)  # Compute nth derivative at a
    term = (derivative_n / math.factorial(n)) * (x - a) ** n
    return term


# Example function: cos(x)
def cos_derivative(a, n):
    """Returns the nth derivative of cos(x) evaluated at x = a."""
    derivatives = [math.cos, math.sin, lambda x: -math.cos(x), lambda x: -math.sin(x)]
    return derivatives[n % 4](a)


# Compute the 4th term of the Taylor series for cos(x) at x = 0
n = 4
a = 0  # Maclaurin series
x = 0.5
nth_term = taylor_nth_term(cos_derivative, a, n, x)
print(f"The {n}th term of the Taylor series for cos(x) at x={x} is: {nth_term}")


def main(radians):
    return 1 + sum(result.get() for result in results)


# This line checks if the script is being run directly (not imported as a
# module). If true, the code block under this condition will execute.
if __name__ == "__main__":
    print("iterations?", TOTAL_ITERATIONS)
    radians = math.radians(180)  # 0.7853981633974483
    print("radians?", radians)
    # radians = 1
    print("main?", main(radians))
    # Output:
    # 1056.2538455391366
