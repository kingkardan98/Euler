# ////////////////////////////////////////////////////////
# Product-sum numbers
# Project Euler Problem 88
# Python version of Stephan Brumme's C++ solution

LIMIT = 12000

# minK[k] = minimal product-sum number for set size k
minK = [float('inf')] * (LIMIT + 1)

def valid(n, k):
    """Check if n is a smaller minimal product-sum number for k terms."""
    if k > LIMIT:
        return False
    if n < minK[k]:
        minK[k] = n
        return True
    return False

def get_min_k(n, product, summ, depth=1, min_factor=2):
    """
    Recursively find all factor combinations of n
    n: original number
    product: remaining product
    summ: remaining sum
    depth: number of terms so far
    min_factor: smallest factor to try (avoid duplicates)
    """
    if product == 1:
        # add remaining 1s to match sum
        return 1 if valid(n, depth + summ - 1) else 0

    result = 0
    if depth > 1:
        if product == summ:
            return 1 if valid(n, depth) else 0
        if valid(n, depth + summ - product):
            result += 1

    # try all factors >= min_factor
    i = min_factor
    while i * i <= product:
        if product % i == 0:
            result += get_min_k(n, product // i, summ - i, depth + 1, i)
        i += 1

    return result

def main():
    n = 4
    sum_result = 0
    todo = LIMIT - 1  # 2..LIMIT

    while todo > 0:
        found = get_min_k(n, n, n)
        if found > 0:
            todo -= found
            sum_result += n
        n += 1

    print(sum_result)

if __name__ == "__main__":
    main()
