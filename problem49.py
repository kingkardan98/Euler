# Find the one other sequence like 1487, 4817, 8147. This sequence has three properties:
# P1) All its components are in ascending order
# P2) All its components are prime numbers
# P3) All its components are permutations of each other
# 
# Game plan:
# - Generate all 4-digit prime numbers (easily done with sieve of Eratosthenes)
# - Define a step, start from the first 4-digit prime number and add it to this prime (ensuring P1 from here on)
# - - If the landing prime is a permutation of the first and 4 digits, add the step again
# - - - If the landing prime is a permutation of the second and 4 digits, we're done, return the triplet
# - - Else, go to the next ptime
# - Increase step (the maximum possible increase is around 10k, so not that big)

from recurring_functions.Eratosthenes import sieveOfEratosthenes
import itertools

LIMIT = 10000

def isPermutation(new, original):
    original_char_list = [e for e in str(original)]
    new_str = str(new)

    permutations = []
    for tup in list(itertools.permutations(original_char_list)):
        permutations.append(''.join(tup))

    if new_str in permutations:
        return True
    return False

def checkTriplets(primes, step):
    for prime in primes:
        second_prime = prime + step
        # I named them second_prime and third_prime, but no one assures me they're primes in the start.
        if isPermutation(second_prime, prime) and second_prime in primes:
            third_prime = second_prime + step
            if isPermutation(third_prime, second_prime) and third_prime in primes:
                print("One triplet is: {}, {}, {}, with step {}".format(prime, second_prime, third_prime, step))
        

def main():
    # Here we have all 4-digit primes.
    primes = [prime for prime in sieveOfEratosthenes(LIMIT) if prime > 1000 and prime < 10000]

    step = 1
    while step <= 9999:
        checkTriplets(primes, step)
        step += 1

    return

if __name__ == '__main__':
    main()
