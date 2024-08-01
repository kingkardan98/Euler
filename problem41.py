# What is the largest n-digit pandigital number that exists?

# C1: it can be at most 9 digits.
# It is a case of checking all the odd
# 9-digit pandigital numbers, and seeing
# which is the largest prime.

# C2: selecting the pandigitals in [10^9, 10^10) is the wrong approach.
# Way too long. How about permutations?

# C3: permutations was way more successful, good.
# Now we still use the sieve of Erathostenes to get the primes,
# for later ease of use of just looking in the list.

import itertools

def generatePermutations(lst):
    # The permutations get generated as a list of lists of the digits.
    permutations_as_lists = list(itertools.permutations(lst))

    # This new list will contain the actual integers.
    permutations = []

    for permutation in permutations_as_lists:
        # String where all the digits will be concatenated.
        perm_string = ''

        # The concatentation of all the actual digits.
        for element in permutation:
            perm_string += (str(element))

        # Append the integer, instead of the string, for later
        # ease of use.
        permutations.append(int(perm_string))
    
    return permutations

def sieveOfEratosthenes(n):
    # Table of all numbers up to n
    print("- Generating prime truth matrix table...")
    prime_table = [True for _ in range(n + 1)]
    print("- Done. Removing composite numbers...")

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

        # For aesthetic reasons.
        if p % 10000 == 0:
            print("-- Generated primes up to {}.\n".format(p))

    # Create the list of prime numbers
    for i in range(len(prime_table)):
        if prime_table[i]:
            primes.append(i)

    return primes

def main():
    digitList = [i for i in range(1, 10)]
    print("Generating pandigitals...")
    numList = generatePermutations(digitList)
    print("Done. Generating primes...")
    primes = sieveOfEratosthenes(10**10)
    print("Done. Finding greatest pandigital...")
    max = 0

    for number in numList:
        if number % 2 == 0:
            continue
        if number not in primes:
            continue
        if number < max:
            continue
        max = number

    print(max)

if __name__ == '__main__':
    main()