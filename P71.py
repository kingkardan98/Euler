from math import gcd

def find_fraction():
    target_n = 3
    target_d = 7
    limit = 1_000_000
    
    closest_n = 0
    closest_d = 1
    
    for d in range(1, limit + 1):
        n = (target_n * d - 1) // target_d  # Find the largest n such that n/d < 3/7
        if gcd(n, d) == 1:  # Ensure the fraction is reduced
            if n * closest_d > closest_n * d:  # Compare fractions
                closest_n, closest_d = n, d
    
    return closest_n

result = find_fraction()
print("The numerator of the fraction immediately to the left of 3/7 is:", result)
