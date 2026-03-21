# Find the first four consecutive numbers that have four distinct prime factors.

def factor_set(number):
    factors = set()
    divisor = 2
    while number > 1:
        if number % divisor == 0:
            factors.add(divisor)
            number = number // divisor
            divisor = 2
        else:
            divisor += 1
    return factors

def main():
    i = 1
    while True:
        if len(factor_set(i)) == 4 and len(factor_set(i+1)) == 4 and len(factor_set(i+2)) == 4 and len(factor_set(i+3)) == 4:
            print(i, i+1, i+2, i+3)
            return
        i += 1

if __name__ == '__main__':
    main()