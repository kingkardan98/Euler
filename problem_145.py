# Easy

LIMITS = [(0, 10**n) for n in range(2, 8)]

from tqdm import tqdm

def reverse(i):
    return str(i)[::-1]

def generate_reversible_numbers(limit_d, limit_u):
    seen = set()
    reversible_numbers = []

    for i in range(limit_d, limit_u + 1):

        if i in seen:
            continue
        seen.add(i)

        reverse_i = reverse(i)
        int_reverse = int(reverse_i)
        if int_reverse in seen:
            continue
        if reverse_i[0] == '0':
            continue
        seen.add(int_reverse)

        rev_sum = i + int_reverse

        if any(int(digit) % 2 == 0 for digit in str(rev_sum)):
            continue

        reversible_numbers.append(i)
        reversible_numbers.append(int_reverse)

    return reversible_numbers

for limit in LIMITS:
    print(len(generate_reversible_numbers(*limit)))