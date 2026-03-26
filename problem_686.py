# I'm going to try and be smart about this: let's find out the first values of p(123, n) and let's see what I get out of it.

# print(2**12710)
# Ok, so I can get up to p(123, 45). I'll generate the sequence up to that point, then check OEIS.
# After that, I'll check if the sequence has a formula, and implement that formula into Python.
# I'll have my result super quick.

# OEIS was of no help, damn.

import math
from tqdm import tqdm

def p(l, n, base=2):
    length = len(l)
    counter = 0
    i = 0
    pbar = tqdm(total=n, desc="Progress")
    while True:
        i += 1
        log_frac = math.modf(i * math.log10(base))[0]
        if str(10 ** log_frac)[:length + 1].replace('.', '') == l:
            counter += 1
            pbar.update(1)
            if counter == n:
                return i


print(p("123", 678910))