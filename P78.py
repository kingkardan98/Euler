import functools

def generalizedPentagonal(k):
    k1 = k
    k2 = -k

    p1 = k1*(3*k1 - 1) // 2
    p2 = k2*(3*k2 - 1) // 2
    return [p1, p2]

@functools.cache
def partitions(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    
    total = 0
    k = 1
    while True:
        pentagonal1, pentagonal2 = generalizedPentagonal(k)
        if pentagonal1 > n and pentagonal2 > n:
            break

        sign = -1 if k % 2 == 0 else 1

        if pentagonal1 <= n:
            total += sign * partitions(n - pentagonal1)
        if pentagonal2 <= n:
            total += sign * partitions(n - pentagonal2)

        k += 1

    return total

n = 1

while True:
    if partitions(n) % 1_000_000 == 0:
        print(n)
        break
    elif n % 100 == 0:
        print(n)

    n += 1