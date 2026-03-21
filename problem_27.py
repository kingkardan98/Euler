import math

maxa = 0
maxb = 0
maxn = 0

def isPrime(n):
    if n < 0:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        quadratic = lambda n: n**2 + a*n + b
        n = 0
        while isPrime(quadratic(n)):
            n += 1
        if n > maxn:
            maxa = a
            maxb = b
            maxn = n

print(maxa*maxb, maxa, maxb)