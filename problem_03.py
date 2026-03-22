def is_prime(n):
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True

def main():
    number = 600851475143
    prime_factors = []
    i = 2
    while number > 1:
        if number % i == 0 and is_prime(i):
            if not i in prime_factors:
                prime_factors.append(i)
            number = number / i
            i = 2
        else:
            i += 1
    print(max(prime_factors))

if __name__ == '__main__':
    main()