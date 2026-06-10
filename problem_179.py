from sympy import divisor_count
from tqdm import tqdm

LIMIT = 10**7

counter = 0

for i in tqdm(range(2, LIMIT), desc="Integers"):
    if divisor_count(i-1) == divisor_count(i):
        counter += 1

print(counter)

