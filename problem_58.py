from recurring_functions.Eratosthenes import sieveOfEratosthenes
from recurring_functions.Spiral import getDiagonals

def main():
    dimension = 3
    while True:
        primes = sieveOfEratosthenes(dimension ** 2)  # Get primes up to dimension^2
        
        # Extract the diagonals
        ldiag, rdiag = getDiagonals(dimension)
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
