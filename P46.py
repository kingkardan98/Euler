# Find the smallest odd composite that defies Goldbach's conjecture.

# Get the sieve of Eratosthenes.

MAX_LIMIT = 10000

def sieveOfEratosthenes(n):
    prime_table = [True for i in range(n + 1)]
    prime_table[0] = prime_table[1] = False

    p = 2
    while (p * p <= n):
        if prime_table[p]:
            for i in range(p * p, n + 1, p):
                prime_table[i] = False
        p += 1

    primes = [i for i, is_prime in enumerate(prime_table) if is_prime]
    return primes

def goldbach(x, y):
    return x + 2 * (y ** 2)

def is_composite(n, primes):
    if n < 2:
        return False
    for prime in primes:
        if prime * prime > n:
            break
        if n % prime == 0:
            return True
    return False

def main():
    primes = sieveOfEratosthenes(MAX_LIMIT)
    
    # Increase the limit to ensure we find the smallest number correctly
    odd_goldbach_numbers = set(goldbach(x, y) for x in primes for y in range(1, MAX_LIMIT + 1) if goldbach(x, y) % 2 == 1)
    
    # Generate odd composite numbers up to a slightly higher limit
    limit = MAX_LIMIT * 2  # Increase limit to find all relevant odd composites
    odd_composite_numbers = [n for n in range(3, limit, 2) if is_composite(n, primes)]
    
    # Find the smallest odd composite number that is not in odd_goldbach_numbers
    for num in odd_composite_numbers:
        if num not in odd_goldbach_numbers:
            print(num)
            break

if __name__ == '__main__':
    main()
