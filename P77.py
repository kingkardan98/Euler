import functools
from recurring_functions.Primes import prime_generator, isPrime

def primes_up_to(n):
    for prime in prime_generator():
        if prime > n:
            break
        yield prime

@functools.cache
def partitions_primes(number, top):
    if number == 0:
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    
    result = sum(
        partitions_primes(
            number - x, min(number - x, x)) 
            for x in primes_up_to(top)
        )
    
    if number <= top and isPrime(number):
        result += 1
    return result

totalCount = 0
i = 0
while totalCount < 5000:
    i += 1
    totalCount = partitions_primes(i, i)
    print(i, totalCount)