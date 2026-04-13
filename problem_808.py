from recurring_functions.Eratosthenes import sieve_of_eratosthenes_yield
from math import isqrt
from tqdm import tqdm


# With a bit of trial and error, I found the exact value.
# With a rapid search of the last value of reversibles, this is the last prime number
# that's related to the sequence of reversibles.
PRIME_LIMIT = 31_100_101


def reverse(num):
    return int(str(num)[::-1])


def is_reversible(num, primes_set):
    rev = reverse(num)

    # Not palindrome
    if str(num) == str(num)[::-1]:
        return False

    root = isqrt(rev)

    return root in primes_set and root * root == rev


def main():
    print("Generating primes...")
    primes_list = list(sieve_of_eratosthenes_yield(PRIME_LIMIT))
    primes_set = set(primes_list)
    print("Done.")

    reversibles = set()
    pbar = tqdm(primes_list, desc="Primes checked")

    for prime in pbar:
        if len(reversibles) >= 50:
            break

        candidate = prime ** 2

        if is_reversible(candidate, primes_set):
            reversibles.add(candidate)
            reversibles.add(reverse(candidate))

    if len(reversibles) >= 50:
        print(sorted(list(reversibles))[-1])
        print(sum(reversibles))
    else:
        print(f"Only found {len(reversibles)} reversibles.")


main()
