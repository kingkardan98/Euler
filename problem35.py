# Circular primes are ones such that all rotations of its digits are primes:
# 197 is prime, 971 is prime and 719 is prime.
# How many such numbers are below one million?

# C1: not all permutations, all ROTATIONS: 123, 231, 312. The "order" is mantained.

UPPER_LIMIT = 1000000

def sieveOfEratosthenes(n):
    # Table of all numbers up to a million
    prime_table = [True for i in range(UPPER_LIMIT + 1)]

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

def isCircular(p, primes):
    # Generate all rotations of the prime.
    prime_str = str(p)
    prime_len = len(prime_str)

    rotations = [prime_str]
    if prime_len == 1:
        pass
    else:
        # We just double the string and move along it to find all rotations.
        rotation_matrix = str(p) + str(p)
        start = 1
        finish = prime_len + 1
        rotation = rotation_matrix[start:finish]

        # And keep sliding until we hit the finish of the first string, which marks
        # the finish of rotations.
        while rotation != prime_str:
            rotations.append(rotation)
            start += 1
            finish += 1
            rotation = rotation_matrix[start:finish]
    
    # Now it's just a matter of checking if each rotation is prime.
    for number in rotations:
        if int(number) not in primes:
            return False
    return True

def main():
    # First step: generate all primes below one million. Easy enough, sieve of Erathostenes.
    primes = sieveOfEratosthenes(UPPER_LIMIT)

    # Second step: for each of the numbers in the list, check which are circular, and count them.
    circularCounter = 0
    for prime in primes:
        if isCircular(prime, primes):
            circularCounter += 1

    print(circularCounter)

if __name__ == '__main__':
    main()