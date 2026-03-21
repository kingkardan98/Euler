def pentagonal(n):
    return n * (3 * n - 1) // 2

def is_pentagonal(x):
    if x < 1:
        return False
    n = (1 + (1 + 24 * x) ** 0.5) / 6
    return n.is_integer()

def main():
    MAX = 10000
    pentagonals = [pentagonal(i) for i in range(1, MAX + 1)]
    pentagonal_set = set(pentagonals)
    min_distance = float('inf')
    result_pair = None

    for i in range(MAX):
        for j in range(i, MAX):
            pi = pentagonals[i]
            pj = pentagonals[j]
            if (pi + pj) in pentagonal_set and (pj - pi) in pentagonal_set:
                distance = pj - pi
                if distance < min_distance:
                    min_distance = distance
                    result_pair = (pi, pj)

    print(f"The pair of pentagonal numbers is: {result_pair} with a distance of {min_distance}")

if __name__ == "__main__":
    main()
