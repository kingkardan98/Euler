import math
from itertools import islice

LIMIT = 10000

def period(n):
    # This function finds the period of the continued fraction.
    m, d, a0 = 0, 1, int(math.sqrt(n))
    if a0 * a0 == n:  # Skip perfect squares
        return 0
    
    period = 0
    a = a0
    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        period += 1
        if a == 2 * a0:  # Period detected
            return period

def main():
    counter = 0
    for i in range(2, LIMIT + 1):
        if period(i) % 2 == 1:
            counter += 1
    print(counter)
    
if __name__ == '__main__':
    main()