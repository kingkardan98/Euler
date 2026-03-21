# ================
# |    IDEA 1    |
# ================

# RULE 1: 6 = 9 for the roll-over rule
# RULE 2: I can have the same digit in both sets

# INSIGHT 1: the set of second digits is just {1, 4, 5, 6, 9}, 
#            and since 6 = 9 => {1, 4, 5, 6}
# INSIGHT 2: 0, 2, 3 and 8 only appear in the first digit.
# INSIGHT 3: 5 only appears in the second digit
# INSIGHT 4: 7 appears nowhere.
# INSIGHT 5: a set that contains 6 / 9 has a "real" length of 7 digits, since they can be flipped over.

# These insights tell me that D1 = {0, 2, 3, 8, x, y} and D2 = {5, a, b, c, d, e}
# At this point I only need to change over 8 digits in two sets.
# x and y are to be chosen from the set {1, 4, 6}
# a, b, c, d, e are to be chosen from the set {1, 4, 6}. Since two of the digits are "redundant", I'll just choose them randomly from what I have left
# Then #({0, 2, 3, 8, x, y}, x, y in {1, 4, 6}) = 3
# And #({5, a, b, c, d, e}) = #({1, 4, 5, 6, d, e}, d, e in {0, 1, ..., 9}) = 36

# So 36 * 3 = 108. But Euler Project says it's wrong.
# Is there any way to brute-force it dumbly?

# If we check "dumbly", there are binom(10, 6) * binom(10, 6) possibilities = 44100. Not even that many.
# I might want to create all the possible cubes, and check if I can create the squares.
# If I can, just count up the configuration.

from itertools import combinations, combinations_with_replacement, product

SQUARE_DIGITS = [(0,1),(0,4),(0,9),(1,6),(2,5),(3,6),(4,9),(6,4),(8,1)]

def expanded_digits(cube):
    s = set(cube)
    if 6 in s or 9 in s:
        s.add(6); s.add(9)
    return s

def is_valid_pair(cubeA, cubeB):
    a_digits = expanded_digits(cubeA)
    b_digits = expanded_digits(cubeB)
    for d1, d2 in SQUARE_DIGITS:
        if not ((d1 in a_digits and d2 in b_digits) or (d1 in b_digits and d2 in a_digits)):
            return False
    return True

all_cubes = list(combinations(range(10), 6))

def yield_valid_pairs():
    for a, b in combinations_with_replacement(all_cubes, 2):
        if is_valid_pair(a, b):
            yield (a, b)

# Example usage:
valid_pairs = list(yield_valid_pairs())
print("Number of unordered valid pairs:", len(valid_pairs))

