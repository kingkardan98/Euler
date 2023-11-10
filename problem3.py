def is_prime(n):
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True

def main():
    number = 600851475143
    primeFactors = []
    i = 2
    while number > 1:
        if number % i == 0 and is_prime(i):
            if not i in primeFactors:
                primeFactors.append(i)
            number = number / i
            i = 2
        else:
            i += 1
    print(max(primeFactors))

if __name__ == '__main__':
    main()