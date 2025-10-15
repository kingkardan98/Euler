# Let's think about this critically: what are the values of T(n)?
# T(1) = 0 obviously
# What are the squares? The numbers I'm looking for can only be squares.

# Solution: 72673459417881349

import math, tqdm

DIGITS = 16

def squares(digits):
    for i in range(math.isqrt(10**digits)):
        yield i*i

def is2025(number):
    ns = str(number)
    splits = []

    for i in range(len(ns)):
        if ns[:i] == '' or ns[i:] == '':
            continue
        elif ns[:i][0] == '0' or ns[i:][0] == '0':
            continue
        splits.append((ns[:i], ns[i:]))

    for split in splits:
        concat = int(''.join(split))
        value = (int(split[0]) + int(split[1])) * (int(split[0]) + int(split[1]))
        if concat == value:
            return True
    return False

def main():
    gen = squares(DIGITS)
    candidates = []
    for _ in tqdm.tqdm(squares(16), desc='Processing', unit='num'):
        try:
            candidates.append(next(gen))
        except StopIteration:
            break

    print('Candidates have been generated. Checking property...')
    result = 0
    for c in tqdm.tqdm(candidates, desc='Processing', unit='num'):
        if is2025(c):
            result += c

    print(result)

main()