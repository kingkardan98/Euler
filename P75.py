from tqdm import tqdm
from collections import defaultdict
from math import gcd

def generate_pythagorean_triples(max_perimeter):
    """Generates all Pythagorean triples up to max_perimeter using Euclid's formula."""
    triples_count = defaultdict(int)

    for m in range(2, int((max_perimeter // 2) ** 0.5) + 1):
        for n in range(1, m):
            if (m - n) % 2 == 1 and gcd(m, n) == 1:  # m, n must be coprime and have opposite parity
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                perimeter = a + b + c

                # Scale up the primitive triple
                k = 1
                while k * perimeter <= max_perimeter:
                    triples_count[k * perimeter] += 1
                    k += 1

    return triples_count

def main():
    maxL = 1_500_000
    triples_count = generate_pythagorean_triples(maxL)
    
    # Count perimeters that have exactly one triple
    counter = sum(1 for count in triples_count.values() if count == 1)
    
    print(counter)

main()
