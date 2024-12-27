# I try to implement a solution with the blog of
# Martin Ueding, which explains the code a lot.

from recurring_functions.Eratosthenes import sieveOfEratosthenes
from recurring_functions.MillerRabin import isPrime
from math import log10, floor

LIMIT = 10000

def comb(a, b):
    len_a = floor(log10(a))+1
    len_b = floor(log10(b))+1
    if isPrime(int(a*(10**len_b)+b)) and isPrime(int(b*(10**len_a)+a)):
        return True
    return False

def main():
    primes = sieveOfEratosthenes(LIMIT)
    # a is first number
    for a in primes:
        # b is second number
        for b in primes:
            # check if b is less than a
            if b < a:
                continue
            # check if a and b satisfy the condition
            if comb(a, b):
                # c is the third number
                for c in primes:
                    # check if c is less than b
                    if c < b:
                        continue
                    # check if a,c and b, c satisfy the condition
                    if comb(a, c) and comb(b, c):
                        # d is the fourth number
                        for d in primes:
                            # check if d is less than c
                            if d < c:
                                continue
                            # check if (a,d), (b,d) and (c,d) satisfy the condition
                            if comb(a, d) and comb(b, d) and comb(c, d):
                                # e is the fifth prime
                                for e in primes:
                                    # check if e is less than d
                                    if e < d:
                                        continue
                                    # check if (a, e), (b, e), (c, e) and (d, e) satisfy condition
                                    if comb(a, e) and comb(b, e) and comb(c, e) and comb(d, e):
                                        print(a+b+c+d+e)
                                        return
                                    
if __name__ == '__main__':
    main()