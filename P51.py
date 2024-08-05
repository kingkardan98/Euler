'''
Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) 
with the same digit, is part of an eight prime value family.

Example: 1st digit of *3 -> 13, 23, 43, 53, 73, 83 are six primes
Example: 3rd and 4th digit of 56**3 -> 56003, 56113, 56333, 56443, 56663, 56773, 56993 are seven primes.
Find such a set of length 8.
'''

from recurring_functions.Eratosthenes import sieveOfEratosthenes
import itertools

LIMIT = 1000000

def searchSet(prime, primes):
    prime_str = str(prime)
    length = len(prime_str)

    binary_mask_list = list(itertools.product((True, False), repeat=length))

    binary_mask_list = [binary_mask for binary_mask in binary_mask_list if 
                        binary_mask != tuple(True for _ in range(length)) and 
                        binary_mask != tuple(False for _ in range(length))]
    
    for binary_mask in binary_mask_list:
        number_matrix = ''
        for i in range(length):
            number_matrix += prime_str[i] if not binary_mask[i] else '*'

        
        # At this point, we have a generated matrix. Now it's just a matter of changing all the asterisks
        # into a digit.
        matrix_values = []
        for i in range(10):
            matrix_values.append(int(number_matrix.replace('*', str(i))))
        
        # At this point, it's just a matter of looking how many are primes.
        prime_counter = 0
        for value in matrix_values:
            if value in primes:
                prime_counter += 1

        if prime_counter == 8:
            return matrix_values
    
    return None

def main():
    primes = set(sieveOfEratosthenes(LIMIT)) 
    for prime in primes:
        family = searchSet(prime, primes)
        if family is not None:
            for element in family:
                if element in primes:
                    print(sorted(family))
                    return

if __name__ == '__main__':
    main()
