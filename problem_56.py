# Find the number in the form a^b such that the sum of its digits is maximized, for a,b < 100.

maximum_sum_digit = 0
number = 0

for a in range(100):
    for b in range(100):
        power = a**b
        digit_sum = 0
        for char in str(power):
            digit_sum += int(char)
        if digit_sum > maximum_sum_digit:
            maximum_sum_digit = digit_sum
            number = power

print(maximum_sum_digit)