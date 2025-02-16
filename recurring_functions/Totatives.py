from math import gcd

def phi(n):
    phi = int(n > 1 and n)
    for p in range(2, int(n ** .5) + 1):
        if not n % p:
            phi -= phi // p
            while not n % p:
                n //= p
    #if n is > 1 it means it is prime
    if n > 1: phi -= phi // n 
    return phi

def coprime_set(d):
    coprimes = set()
    for i in range(1,d):
        if gcd(i,d) == 1:
            coprimes.add(i)

    return coprimes