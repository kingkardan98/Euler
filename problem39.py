# Say p is the perimeter of a right angle triangle, with side lengths a, b, c.
# If p = 120, there are exactly three triplets of numbers.

# For which number p <= 1000 is the number of solutions maximized?

# We are then trying to find the maximum of a function, f(x)
# f(x) counts the possible Pythagorean triplets that sum up to x.
# So it would be that f(120) = 3.

# If we implement this function, it's just as simple as letting it rip
# up to 1000, recording which x gives me the maximum and voila.

import math

def f(x):
    solutions = 0
    for c in range(1, math.ceil(x/2)):
        for b in range(1, c):
            for a in range(1, b):
                if a + b + c == x and a * a + b * b == c * c:
                    solutions += 1
    return solutions

max_solutions = 0
x_max = 0

for x in range(1, 1001):
    solutions = f(x)
    print("{}: {}".format(x, solutions))
    if solutions >= max_solutions:
        max_solutions = solutions
        x_max = x

print("Maximum: {}, {} solutions".format(x_max, max_solutions))

