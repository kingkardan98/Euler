from sympy import nextprime
from sympy import primerange
from itertools import product

LIMIT = 10**9

def generate_admissible(limit):
    """
    Admissible numbers have prime factors that form a consecutive sequence
    starting from 2: e.g. {2}, {2,3}, {2,3,5}, {2,3,5,7}, ...
    
    So we enumerate all numbers of the form 2^a * 3^b * 5^c * ...
    where each prime up to the largest must appear at least once.
    
    Strategy: for each prefix of primes [2], [2,3], [2,3,5], ...,
    generate all products within limit where each prime appears >= 1 time.
    
    This is exponentially smaller than iterating all integers.
    """
    # Collect all primes we might need (primorial 2*3*5*7*11*13 > 10^9)
    primes = list(primerange(2, 60))  # 2*3*5*7*11*13*17 >> 10^9

    admissible = set()

    for num_primes in range(1, len(primes) + 1):
        p_set = primes[:num_primes]
        base = 1
        for p in p_set:
            base *= p  # minimum product (each prime to the 1st power)

        if base > limit:
            break  # Even the smallest product with these primes exceeds limit

        # Now enumerate all exponent combinations for this prime set.
        # For each prime p_i, exponent e_i >= 1, product <= limit.
        # We fix e_i >= 1 by dividing out the base and then allowing e_i >= 0
        # for the remaining headroom.
        remaining = limit // base  # headroom after each prime appears once

        # Build max exponents for the "extra" powers (beyond the mandatory 1)
        # extra_i >= 0, product of p_i^extra_i <= remaining
        def enumerate_extras(primes, remaining, current_product=1, idx=0):
            if idx == len(primes):
                yield current_product
                return
            p = primes[idx]
            extra = 1
            while current_product * extra <= remaining:
                yield from enumerate_extras(primes, remaining, current_product * extra, idx + 1)
                extra *= p

        for extra_product in enumerate_extras(p_set, remaining):
            admissible.add(base * extra_product)

    return sorted(admissible)


def pseudo_fortunate(num):
    """Find smallest prime p such that p - num >= 2."""
    candidate = nextprime(num)
    while candidate - num < 2:
        candidate = nextprime(candidate)
    return candidate - num


def main():
    print("Generating admissible numbers...")
    admissible = generate_admissible(LIMIT)
    print(f"Found {len(admissible)} admissible numbers under {LIMIT:,}")

    pseudo_sum = sum(set(pseudo_fortunate(n) for n in admissible))
    print(f"Sum of pseudo-fortunate numbers: {pseudo_sum}")


main()
