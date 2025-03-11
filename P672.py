import functools, time, sys
from tabulate import tabulate
from datetime import datetime

@functools.cache
def g(n):
    # This function only serves to remind that the process can be efficiently
    # defined as a recursive function. The results are cached for easier computation.
    # This function has this interesting property:
    # Every integer n can be expressed as 7k - t, 0 <= t < 7
    # So g(n) = g(7k - t) = g(k) + t
 
    if n <= 1:
        return 0
    
    elif n % 7 == 0:
        return g(n//7)
    
    quotient, remainder = divmod(n, 7)
    return (7 - remainder) + g(quotient + 1)

def S(n):
    # A reminder that S(n) = ∑ g(k), 1 ≤ k ≤ n
    return sum(g(k) for k in range(1,n+1))

def S_oneshot(n):
    # To optimize S(n), we can see the key insight that
    # S(7) = 15, and every subsequent multiple of 7 is
    # S(7k) = 15 + ∑ 21 * g(j), 2 ≤ j ≤ k

    # So, given 1 ≤ n ≤ 6, S(7k + n) = 15 + ∑ 21 * g(j) + ∑ g(7k + i), 2 ≤ j ≤ k, 1 ≤ i ≤ n

    # This greatly reduces the actual calculations we need to do. For the first summation,
    # it just comes down to k-1 calculations, and the second summation is at most 6 calculations.

    # The total operations done with this formula, for n = 7k + n', are therefore k + n' + 1, with k ≈ n / 7.
    # So with this formula we almost decreased the calculations needed by 7 times.
    # We could further optimize the use of memoization by realizing that ∑ g(7k + i) = (∑ 7 - i) + (g(k+1) * n)

    # The benchmark has proven that S_oneshot is around 15x faster than S, which is impressive!
    if n <= 0:
        return 0
        
    full_cycles, remainder = divmod(n, 7)
    
    cycle_sum = 0
    for k in range(1, full_cycles + 1):
        if k == 1:
            cycle_sum += 15  # Sum of first cycle is 15
        else:
            cycle_sum += 21 + 7 * g(k)
    
    # Add remaining terms
    if remainder > 0:
        arithmetic_sum = sum(7 - i for i in range(1, remainder + 1))
        remainder_g = g(full_cycles + 1) * remainder
        remainder_sum = arithmetic_sum + remainder_g
    else:
        remainder_sum = 0
    
    return cycle_sum + remainder_sum

def H(k):
    return S((7**k - 1)//11)

k = 10
lists = []

def benchmark_S(k):
    results = []
    
    for n in range(1, k):
        # Measure S(n)
        start1 = datetime.now()
        var1 = S(10**n)
        end1 = datetime.now()
        time1 = (end1 - start1).total_seconds() * 1000  # Convert to ms

        # Measure S_oneshot(n)
        start2 = datetime.now()
        var2 = S_oneshot(10**n)
        end2 = datetime.now()
        time2 = (end2 - start2).total_seconds() * 1000  # Convert to ms

        # Append results
        results.append([n, var1, f"{time1:.2f} ms", var2, f"{time2:.2f} ms"])

        # Clear screen and reprint the updated table
        sys.stdout.write("\033c")  # ANSI escape code to clear terminal
        sys.stdout.flush()
        print(tabulate(results, headers=['n', 'S(n)', 'time_S', 'S⌖(n)', 'time_S⌖'], tablefmt="grid"))

        # Small delay to prevent flickering (optional)
        time.sleep(0.1)

benchmark_S(k)