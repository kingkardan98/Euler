# What is the largest n-digit pandigital number that exists?

# C1: it can be at most 9 digits.
# It is a case of checking all the odd
# 9-digit pandigital numbers, and seeing
# which is the largest prime.

# C1.1: 9-digit is a wrong assumption. Corrected later.

# C2: selecting the pandigitals in [10^9, 10^10) is the wrong approach.
# Way too long. How about permutations?

# C3: permutations was way more successful, good.
# Now we still use the sieve of Erathostenes to get the primes,
# for later ease of use of just looking in the list.

# C4: sieves take up way too much memory. Pivoting to primality checks
# and a yield function gave up memory.

import itertools
import math

def generatePermutations(lst):
    # Yield each permutation as a concatenated integer
    for permutation in itertools.permutations(lst):
        perm_string = ''.join(map(str, permutation))
        yield int(perm_string)

def isPrime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for div in range(3, int(math.sqrt(number)) + 1, 2):
        if number % div == 0:
            return False
    return True

def main():
    # 9-pandigital primes don't exists, since they're all divisible by 3.
    # Similarly, 8-pandigital primes don't exists, since they're also divisble by 3.
    # Best option: 7-pandigital
    digitList = [i for i in range(1, 8)]
    print("Generating pandigitals...")
    
    max_prime = 0
    counter = 0

    for number in generatePermutations(digitList):
        if counter % 1000 == 0 and counter != 0:
            print("- Checked {} numbers".format(counter))
        if isPrime(number) and number > max_prime:
            max_prime = number
        counter += 1

    print("Greatest pandigital prime:", max_prime)

if __name__ == "__main__":
    main()