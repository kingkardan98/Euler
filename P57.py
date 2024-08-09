from fractions import Fraction
import math

def evaluate_continued_fraction(continued_fraction):
    # continued_fraction is a list of integers [a0, a1, a2, ..., an]
    n = len(continued_fraction)
    
    if n == 0:
        raise ValueError("The continued fraction list should not be empty")
    
    # Initialize numerator and denominator
    numerator = 1
    denominator = continued_fraction[-1]
    
    for i in range(n-2, -1, -1):
        numerator, denominator = denominator, continued_fraction[i] * denominator + numerator
    
    # The fraction is denominator/numerator due to the way we iterated
    return denominator, numerator

counter = 0
for i in range(1, 1001):
    terms = [1]
    terms.extend([2 for _ in range(1, i)])

    den, num = evaluate_continued_fraction(terms)

    if len(str(den)) > len(str(num)):
        counter += 1

print(counter)