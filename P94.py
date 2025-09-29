from math import isqrt

MAX_PERIMETER = 10**9

# Let's reason about almost-equilateral triangles.
# An almost equilateral triangle is valid if it respects two rules:
# 1) the sides are of the type (a, a, a+1) or (a, a, a-1)
# 2) the sides respect the triangle rule (a <= b + c, b <= a + c, c <= a + b)
# First thing first, an easy implementation of the triangle inequality

def triangleInequality(a, b, c):
    return (a < b + c) and (b < a + c) and (c < a + b)

# The problem asks for the sum of all perimeters of all almost-equilateral triangles, 
# with maximum perimeter 1 billion, that have integer area. What to do?

def isCompliant(a, b, c):
    """Returns True if the almost-equilateral triangle has integer area and perimeter less or equal than 1 billion"""
    if not triangleInequality(a, b, c):
        return False
    perimeter = a + b + c
    if perimeter > MAX_PERIMETER:
        return False
    partial = (perimeter*(perimeter-2*a)*(perimeter-2*b)*(perimeter-2*c))
    if partial <= 0 or partial % 16 != 0 or isqrt(partial//16)**2 == partial//16:
        return False
    return True

# At this point, what we need to do is check every possible almost-equilateral triangle
# Make a generator for that
def triangleGenerator():
    a = 1
    while True:
        # Return both possible almost-equilaterals: we'll call the first over an the second under
        yield ((a, a, a+1), (a, a, a-1))
        a += 1

def main():
    gen = triangleGenerator()
    sumPerimeter = 0
    while True:
        trOver, trUnder = next(gen)
        a = trOver[0]
        if a % 1000 == 0:
            print("Misura lato controllato: {}".format(a))
        if (not isCompliant(*trOver)) and (not isCompliant(*trUnder)):
            continue
        if isCompliant(*trOver):
            sumPerimeter += sum(trOver)
        if isCompliant(*trUnder):
            sumPerimeter += sum(trUnder)
        if a > MAX_PERIMETER:
            break
    print(sumPerimeter)

main()