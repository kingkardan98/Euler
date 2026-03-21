from sympy import continued_fraction_convergents

# Manually constructing the continued fraction for e up to 100 terms
def construct_continued_fraction_e(limit):
    sequence = [2]  # First term of the continued fraction of e
    k = 1
    while len(sequence) < limit:
        sequence += [1, 2 * k, 1]  # Pattern: [1, 2k, 1]
        k += 1
    return sequence[:limit]

# Compute the 100th convergent of e
def calculate_100th_convergent_sum():
    # Generate the continued fraction sequence for e up to 100 terms
    e_cf = construct_continued_fraction_e(100)
    
    # Compute convergents using sympy
    convergents = list(continued_fraction_convergents(e_cf))
    
    # Extract the numerator of the 100th convergent
    numerator = convergents[-1].p  # The numerator of the 100th convergent
    
    # Sum the digits of the numerator
    print(sum(int(c) for c in str(numerator)))

# Compute and return the result
calculate_100th_convergent_sum()
