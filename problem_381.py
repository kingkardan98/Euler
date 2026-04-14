from recurring_functions.Eratosthenes import sieve_of_eratosthenes_yield
from tqdm import tqdm
from time import time

LIMIT = 10**8


def s(p):
    # Instead of applying the direct formula, I can apply Wilson's theorem
    if p == 2 or p == 3:
        return 0
    t1 = p - 1  # (p-1)! ≡ -1 ≡ p-1  (mod p)
    t2 = t1 * pow(p-1, -1, p) % p  # divide by (p-1)
    t3 = t2 * pow(p-2, -1, p) % p  # divide by (p-2)
    t4 = t3 * pow(p-3, -1, p) % p  # divide by (p-3)
    t5 = t4 * pow(p-4, -1, p) % p  # divide by (p-4)
    return (t1 + t2 + t3 + t4 + t5) % p


primes = sieve_of_eratosthenes_yield(LIMIT)

total = 0
start = time()
for prime in tqdm(primes, desc="Analyzing primes"):
    value = s(prime)
    total += value
end = time()
print(f"\nTotal: {total}\nTime: {end - start}")
