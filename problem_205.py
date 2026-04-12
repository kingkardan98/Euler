import random
from tqdm import tqdm


# === SIMULATION ===
# This isn't the method of choice. This is extremely slow and inefficient.
# I kept it to know what I aim to do.

GAMES = 100_000_000


def average_die_throw(sides, dies):
    # Extremely elegant formula I found on omnicalculator.com
    return (sides + 1) // 2 * dies


def throw(sides, dies):
    total = 0
    for _ in range(dies):
        total += random.randint(1, sides)
    return total


def simulation():
    pyramid_wins = 0
    for _ in tqdm(range(GAMES), desc="Simulating game"):
        pyramid_total = throw(4, 9)
        cubic_total = throw(6, 6)
        if pyramid_total > cubic_total:
            pyramid_wins += 1
    print(pyramid_wins / GAMES)


# === PROBABILITIES ===

# We can build a dictionary of how many ways I can make a sum with my dies.

def totals_map(sides, dies):
    distribution = {i: 0 for i in range(dies, sides*dies + 1)}
    current_dies = [1] * dies
    while True:
        distribution[sum(current_dies)] += 1
        if all([t == sides for t in current_dies]):
            break

        # This next logic works like an odometer.
        i = 0
        current_dies[i] += 1
        while current_dies[i] > sides:
            current_dies[i] = 1
            i += 1
            current_dies[i] += 1
    return distribution


def main():
    pyramid_ways = totals_map(4, 9)
    cubic_ways = totals_map(6, 6)
    pyramid_wins = 0
    total_counter = sum(v for v in pyramid_ways.values()) * sum(c for c in cubic_ways.values())
    for p, pp in pyramid_ways.items():
        for c, cc in cubic_ways.items():
            if p > c:
                pyramid_wins += pp*cc
    print(pyramid_wins / total_counter)


main()