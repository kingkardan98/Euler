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

from problem_35 import sieve_of_eratosthenes

UPPER_LIMIT = 10**6

def find_truncatables(primes):
    # Simply create a list of all truncatables.
    truncatables = []
    for prime in primes:
        # 2, 3, 5, 7 are not considered truncatable
        if prime in [2, 3, 5, 7]:
            continue
        if is_truncatable(prime, primes):
            truncatables.append(prime)
    
    return truncatables

def is_truncatable(prime, primes):
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
    primes = sieve_of_eratosthenes(UPPER_LIMIT)
    print(sum(find_truncatables(primes)))

if __name__ == '__main__':
    main()
