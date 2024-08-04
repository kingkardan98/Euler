def sieveOfEratosthenes(n):
    # Table of all numbers up to a million
    prime_table = [True for i in range(n + 1)]

    # 0 and 1 are not primes.
    prime_table[0] = False
    prime_table[1] = False

    # The list of the actual numbers. Will fill later.
    primes = []

    # Prime factor to clear with
    p = 2

    # It is sufficient to search up to the last prime such that p^2 < UPPER_LIMIT,
    # since for every n, if p is the smallest prime divisor of n, it is true that
    # n = p * r >= p * p = p^2. So:

    while (p * p <= n):
        # If primes[p] is True, then it's prime
        if prime_table[p]:
            # Delete all multiples, starting from p^2, since all
            # smaller numbers have already been taken care of.
            # The step is p, so we're virtually multiplying.
            for i in range(p * p, n + 1, p):
                prime_table[i] = False
        p += 1

    # Create the list of prime numbers
    for i in range(len(prime_table)):
        if prime_table[i]:
            primes.append(i)

    return primes
