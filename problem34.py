# Find the sum of all numbers that are the sum of the factorial of their digits
# 145 = 1! + 4! + 5! = 1 + 24 + 120

# I got lucky with this assumption:
# UPPER_LIMIT = 10000000

# Plopped the sum in and it worked, but why?
# As 9! = 362880, numbers with many nines won't do obviously.
# Also, numbers with "small" digits (less than 5) but with a lot of digits
# won't do either, as UPPER_LIMIT => 8
# How to optimize this search?

# 9! x n is the most we can advance per one digit increase, 
# and 10^n - 1 is the biggest n-digit number. So

# 9! x 1 = 362880 > 9 = 10^1 - 1
# 9! x 2 = 725760 > 99 = 10^2 - 1
# ...
# 9! x 7 = 2540160 < 999999 = 10^7 - 1
# So the new upper limit is this!

UPPER_LIMIT = 2540160

import math

for i in range(3, 2540160):
    fact_sum = 0
    
    str_num = str(i)
    for digit in str_num:
        fact_sum += math.factorial(int(digit))

    if fact_sum == i:
        print(i)
    