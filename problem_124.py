from sympy.ntheory import factorint

LIMIT = 100_000
TARGET = 10_000

def rad(n):
    factors = factorint(n)
    prod = 1
    for prime in factors:
        prod *= prime
    return prod

def list_builder():
    result = []
    for n in range(1, LIMIT + 1):
        result.append({n: rad(n)})

    return result

def main():
    rad_list = list_builder()
    sort_list = sorted(rad_list, key=lambda d: next(iter(d.values())))
    print(sort_list[TARGET - 1])

main()
