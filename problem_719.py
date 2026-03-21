import itertools, math
import tqdm

MAX_NUMBER = 10**12

# INTUITION 1: we just need to check the squares. Up to 10^12, that means only 0.000001% of all the numbers. Not bad.
# INTUITION 2: numbers in the form 10^x are guaranteed to work. However, it's such a small percentage it's not ideal to check.
# INTUITION 3: I simply need to exclude all 1-digit numbers, since they don't fit the bill for the problem. I was off by 1.
# The solutions is 128088830547982
               

def isSNumber(number):
    number_list = [c for c in str(number)]
    root = math.isqrt(number)
    
    # If the square root isn't an integer, skip immediately
    if root * root != number:
        return False

    for combo in itertools.product(["", "+"], repeat=len(number_list) - 1):
        expr = "".join(a + b for a, b in zip(number_list, combo + ("",)))
        parts = expr.split("+")
        total = sum(int(p) for p in parts)
        if total == root:
            return True
    return False

def T(lst):
    total = 0
    for i in tqdm.tqdm(lst, desc="Processing", unit="num"):
        total += i * isSNumber(i)
    return total

def main():
    squares = []
    number = 10
    while True:
        square = number*number
        if square > MAX_NUMBER:
            break
        squares.append(square)
        number += 1
    print(T(squares))

main()