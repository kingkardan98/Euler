# A unique square that is 1_2_3_4_5_6_7_8_9_0, I'm asked to find the square root of this possible number.
# This is the case of iterating over 9 digits x1 to x9.
# I'll try and fill each digit with a number, then increment.
# Check if that number is a square, then done.

# This is an extremely slow approach. Let's start by making some constraints: 
# the number must be between 1020304050607080900 and 192939495969798990.
# This restricts the search field to [1010101010, 1389026623]
# Square each number in this field. When we find something that hits we're good.

# We went from 10^9 iterations to 4 x 10^8. which is already half an order of magnitude and a lot of simpler calculations.

import re
from tqdm import tqdm

MIN = 1_010_101_010
MAX = 1_389_026_623

def isValidSquare(sq):
    return bool(re.fullmatch(r'1\d2\d3\d4\d5\d6\d7\d8\d9\d0', str(sq)))

def main():
    pbar = tqdm(range(MAX, MIN, -1), desc="Iterations")
    for i in range(MIN, MAX + 1): # Inverted loop because solution is right at the end
        if isValidSquare(str(i*i)):
            return i
        pbar.update(1)
        
print(1389019170*1389019170)