from sympy.ntheory import factorint
from tqdm import tqdm

LIMIT = 10**8

def is_semiprime(num):
    factors = factorint(num)
    if len(factors) > 2:
        return False
    if sum(val for _, val in factors.items()) != 2:
        return False
    return True

def main():
    semiprimes = []
    for num in tqdm(range(LIMIT), desc="Integers"):
        if is_semiprime(num):
            semiprimes.append(num)
    print(len(semiprimes))

main()
