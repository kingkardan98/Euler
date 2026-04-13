from math import floor

THETA = 1
TAU = 1


def b(n):
    if n == 1:
        return THETA
    return floor(b(n-1)) * (b(n-1) - floor(b(n-1) + 1))


def a(n):
    return floor(b(n))
