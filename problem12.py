import math

def countDivisors(n):
    count = 0
    sqrt_n = int(math.sqrt(n))

    # Count divisors in pairs
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            # If divisors are the same, count only one
            if n // i == i:
                count += 1
            else:
                count += 2
    return count


def main():
    i = 0
    while True:
        i += 1
        if countDivisors(i) > 500:
            print(i)
            return
        i += 1

if __name__ == '__main__':
    main()