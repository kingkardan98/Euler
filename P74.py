import math

def factorial_digit_sum(n):
    return sum(math.factorial(int(digit)) for digit in str(n))

def chain_length(start):
    seen = set()
    current = start
    while current not in seen:
        seen.add(current)
        current = factorial_digit_sum(current)
    return len(seen)

def count_sixty_term_chains(limit):
    count = 0
    for i in range(1, limit):
        if chain_length(i) == 60:
            count += 1
    return count

# Solve for numbers below one million
result = count_sixty_term_chains(10**6)
print("Number of chains with exactly 60 non-repeating terms:", result)
