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


def factorial(num):
    p = 1
    for i in range(1, num + 1):
        p *= i
    return p


def talor_expansion(start, end, radians):
    result = 0
    for i in range(start, end, 4):  # even terms (+)
        result += (radians**i) / factorial(i)
    for j in range(start + 2, end, 4):  # odd terms (-)
        result -= (radians**j) / factorial(j)
    print("result?", result)
    return result


def main(radians):
    iterations_per_cpu = TOTAL_ITERATIONS // NUMBER_OF_CPUS
    pool = mp.Pool(processes=NUMBER_OF_CPUS)

    results = [
        pool.apply_async(talor_expansion, args=(i, i + iterations_per_cpu, radians))
        for i in range(0, TOTAL_ITERATIONS, iterations_per_cpu)
    ]
    pool.close()
    pool.join()

    return 1 + sum(result.get() for result in results)


# This line checks if the script is being run directly (not imported as a
# module). If true, the code block under this condition will execute.
if __name__ == "__main__":
    print("iterations?", TOTAL_ITERATIONS)
    radians = math.radians(45)  # 0.7853981633974483
    print("main?", main(radians))
    # Output:
    # 1056.2538455391366
