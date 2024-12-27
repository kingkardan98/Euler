from recurring_functions.Eratosthenes import sieveOfEratosthenes

LIMIT = 10**10

primes = sieveOfEratosthenes(LIMIT)

with open("primes_database.txt", "a+") as file:
    file.write("{")
    for p in primes:
        file.write("{},".format(p), end="")
    file.write("}")