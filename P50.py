# Which prime below 10^6 can be written as the sum of the most consecutive primes?

# Easy as pie: generate the primes up to a million, add them up, and check if the result is a prime.

from recurring_functions.Eratosthenes import sieveOfEratosthenes

LIMIT = 10**6

def main():
    print("Generating primes...")
    primes = sieveOfEratosthenes(LIMIT)
    print("Done. Checking sublist sums...")
    
    # Create prefix sum array
    prefix_sum = [0] * (len(primes) + 1)
    for i in range(len(primes)):
        prefix_sum[i + 1] = prefix_sum[i] + primes[i]
    
    maximum_prime = 2
    maximum_combo = []
    prime_set = set(primes)  # Convert list to set for O(1) lookups
    
    for start in range(len(primes)):
        for end in range(start + 1, len(primes) + 1):
            sublist_sum = prefix_sum[end] - prefix_sum[start]
            if sublist_sum in prime_set and (end - start) > len(maximum_combo):
                maximum_prime = sublist_sum
                maximum_combo = primes[start:end]

    print("Done.")
    print(maximum_prime, maximum_combo)

if __name__ == '__main__':
    main()
