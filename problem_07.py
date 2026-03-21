def isPrime(number):
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True

def main():
    primes = [2,3]
    i = 1
    while len(primes) < 1000001:
        before = 6*i - 1
        after = 6*i + 1

        if isPrime(before):
            primes.append(before)
        
        if isPrime(after):
            primes.append(after)

        i += 1
    print(primes[-1])

if __name__ == '__main__':
    main()