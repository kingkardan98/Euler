# Is there an upper limit? Probably a cutoff diagonal.
# Let's think about some numbers.
# 
# 2 digits: 10^2 = 100, which already has 3 digits.
#           3^2 = 9, which only has 1 digit.
# This makes me think: there's like a beginning and end to this kind of pattern, like a closing scissor.
# Obviously, every number of ther form 10^n has n+1 digits, so that's a hard cutoff.

# Let's think about this scissor then:
# n^1 has 1 digit    -> n ∈ [1,9], 9 numbers
# n^2 has 2 digits   -> n ∈ [4,9], 6 numbers
# n^3 has 3 digits   -> n ∈ [5,9], 5 numbers
# n^4 has 4 digits   -> n ∈ [6,9], 4 numbers
# n^5 has 5 digits   -> n ∈ [7,9], 3 numbers
# n^6 has 6 digits   -> n ∈ [7,9], 3 numbers
# n^7 has 7 digits   -> n ∈ [8,9], 2 numbers
# n^8 has 8 digits   -> n ∈ [8,9], 2 numbers
# n^9 has 9 digits   -> n ∈ [8,9], 2 numbers
# n^10 has 10 digits -> n ∈ [8,9], 2 numbers
# n^11 has 11 digits -> n = 9, 1 number
# n^12 ... n^22 has 12 ... 21 digits -> n = 9, 10 numbers
# After that, we're done.

# Ok, let's do this programmatically then.

nth = 0
exponent = 1

while True:
    new_nth = nth
    for base in range(1, 10):
        power = base**exponent
        if len(str(power)) == exponent:
            new_nth += 1
    if new_nth == nth: # No new numbers, we're done.
        print(nth)
        break
    nth = new_nth
    exponent += 1