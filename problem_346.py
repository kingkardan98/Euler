import math
from tqdm import tqdm

MAXIMUM = 10**12


def calculate_repunit(base, n):
    return (base**n - 1) // (base - 1)


def generate_repunits():
    strong_repunits = set()

    # Since every integer >= 3 is a repunit for n=2,
    # any repunit with n >= 3 that is >= 3 is automatically strong.
    n = 3
    while True:
        max_base = math.ceil(MAXIMUM ** (1 / (n - 1)))
        if max_base <= 2:
            break
        for base in tqdm(range(2, max_base + 1), desc=f"n={n}"):
            repunit = calculate_repunit(base, n)
            if MAXIMUM >= repunit >= 3:
                strong_repunits.add(repunit)
        n += 1

    return strong_repunits


strong = generate_repunits()

# We need to add 1 at the end.
print(sum(strong) + 1)