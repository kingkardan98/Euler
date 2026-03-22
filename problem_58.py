from recurring_functions.Eratosthenes import sieve_of_eratosthenes
from recurring_functions.Spiral import get_diagonals

def main():
    dimension = 3
    while True:
        primes = sieve_of_eratosthenes(dimension ** 2)  # Get primes up to dimension^2
        
        # Extract the diagonals
        ldiag, rdiag = get_diagonals(dimension)
        diag_length = 2*dimension - 1
        
        # Count how many primes are in the diagonals
        prime_counter = sum(1 for num in ldiag if num in primes)
        prime_counter += sum(1 for num in rdiag if num in primes)

        perc = prime_counter / diag_length
        if dimension % 100 == 1:
            print(dimension - 1)
        
        if perc < 0.1:
            print("Dimensione finale: {}".format(dimension))
            return
        dimension += 2

if __name__ == '__main__':
    main()
