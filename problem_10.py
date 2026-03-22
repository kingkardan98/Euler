import math

def trial_division(number):
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True

def prime_gen(upper):
    primes = [2]
    n = 3
    while n < upper:
        if trial_division(n):
            primes.append(n)
        n += 2
    return primes

def main():
    primes = prime_gen(2000000)
    print(sum(primes))

if __name__ == '__main__':
    main()