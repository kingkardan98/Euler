import itertools

def prime_generator():
    primes = []
    for candidate in itertools.count(2):
        for prime in primes:
            if candidate % prime == 0:
                break
        else:
            yield candidate
            primes.append(candidate)

def isPrime(n):
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True