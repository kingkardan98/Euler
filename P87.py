# How many numbers below fifty million can be expressed as x^2 + y^3 + z^4, where x,y,z are all primes?
# The best approach is to iterate over the primes instead of over the numbers.
# Since we must stay below 50 million, we can put a hard limit on x, y and z (even if it is unoptimized)

from recurring_functions.Eratosthenes import sieveOfEratosthenes
from math import pow, ceil


MAX_VALUE = 5 * 10**7

MAX_X = int(MAX_VALUE**(1/2))
MAX_Y = int(MAX_VALUE**(1/3))
MAX_Z = int(MAX_VALUE**(1/4))

counter = set()
i = 0
print(MAX_X)

# I take all the primes up to MAX_X, since it's the biggest of the bunch
print("Calculating primes...")
primes_x = sorted(list(sieveOfEratosthenes(MAX_X)))
primes_y = sorted(list(sieveOfEratosthenes(MAX_Y)))
primes_z = sorted(list(sieveOfEratosthenes(MAX_Z)))
print("Primes calculated.")

for x in primes_x:
    for y in primes_y:
        for z in primes_z:
            s = x**2 + y**3 + z**4
            if s < MAX_VALUE:
                counter.add(s)
    i += 1
    if i%100 == 0:
        print("x controllati: {}".format(i))
print(len(counter))