# Find the sum of the only eleven prime numbers that are truncatable
# left to right and right to left.

# Truncatable left to right: 3797 -> 797 -> 97 -> 7, all primes
# Truncatable right to left: 3797 -> 379 -> 37 -> 3, all primes

# C1: if a prime number contains an even digit, it is immediately disqualified.
# I'll reuse the sieve of Eratosthenes from P35 to generate primes.

# C2: To find an upper limit: is there such a point where a prime MUST have an even digit
# in its decimal notation?
# The problem suggests that there are only 11 such numbers. How about fine tuning the upper
# limit until we find them all?

# Got it! Eleventh prime is 739397.
UPPER_LIMIT = 10**6

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

def findTruncatables(primes):
    # Simply create a list of all truncatables.
    truncatables = []
    for prime in primes:
        # 2, 3, 5, 7 are not considered truncatable
        if prime in [2, 3, 5, 7]:
            continue
        if isTruncatable(prime, primes):
            truncatables.append(prime)
    
    return truncatables

def isTruncatable(prime, primes):
    prime_str = str(prime)
    length = len(prime_str)
    
    # Left to right truncations
    l_r_truncations = [prime]

    while True:
        prime_str = prime_str[:length-1]
        length = len(prime_str)
        if prime_str == '':
            break
        l_r_truncations.append(int(prime_str))

    # Reset variables
    prime_str = str(prime)

    # Right to left truncations
    r_l_truncations = [prime]

    while True:
        prime_str = prime_str[1:]
        if prime_str == '':
            break
        r_l_truncations.append(int(prime_str))

    # Now it's just a matter of checking if all the truncations are prime
    for prime in l_r_truncations:
        if prime not in primes:
            return False
        
    for prime in r_l_truncations:
        if prime not in primes:
            return False
        
    return True

def main():
    primes = sieveOfEratosthenes(UPPER_LIMIT)
    print(sum(findTruncatables(primes)))

if __name__ == '__main__':
    main()
