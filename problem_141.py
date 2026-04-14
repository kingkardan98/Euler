from tqdm import tqdm
import math

LIMIT = 1_000_000_000_000


def geometric_sequence(d, q, r):
    # We just have to check if any of the combinations form a geometric sequence
    # But r,q,d = d,q,r. If this was a geometric sequence, the ratio would just be the inverse.
    # So we just have three sequences to check, lovely, halved the problem.
    possibilities = [(d, q, r), (d, r, q), (q, d, r)]
    for perm in possibilities:
        try:
            result = perm[0] * perm[2] == perm[1] * perm[1]
        except ZeroDivisionError:
            continue
        if result:
            return True
    return False


def main():
    # We can drastically optimize the problem by just considering square numbers to begin with.
    candidates = (i**2 for i in range(1, math.ceil(math.sqrt(LIMIT))))
    candidates_list = list(candidates)
    square_progressive = set()

    # For each candidate, we can then yield divisors, and if the divisor
    # forms a geometric series with the quotient and remainder, nice.
    for candidate in tqdm(candidates_list):
        for divisor in range(1, int(candidate**0.5) + 1):
            quotient, remainder = divmod(candidate, divisor)
            if geometric_sequence(divisor, quotient, remainder):
                square_progressive.add(candidate)
    print(sum(square_progressive))


main()