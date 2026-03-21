# Curious fraction: 49/98 = 4/8
# This is mathematically correct, but an inexperienced mathematician 
# would go about it simplifying the 9s instead of the correct route.

# If the fraction contains two multiples of ten it's immediately discarded.
# There are exactly four of this fractions, less than one and with two digits factors.

# Write the denominator of the product of this four fractions in its lowest terms.

def isCommonDigit(num, den):
    # The function returns -1 as an "error" code (no common digits, or trivial example).

    # Trivial example: both numbers are multiples of 10.
    if num % 10 == 0 and den % 10 == 0:
        return -1
    

    num_str = str(num)
    den_str = str(den)

    # Find the first common digit.
    for i in range(2):
        for j in range(2):
            if num_str[i] == den_str[j]:
                return num_str[i]
    return -1

def makeFraction(num, den):
    # Simply returns the fraction in string form.
    return str(num) + '/' + str(den)

def main():
    # "Dumb" for loops, without looking at the fact that the numerator, in some cases, might be bigger.
    for num in range(10, 100):
        for den in range(11, 100):
            # Find the common digit
            common_digit = isCommonDigit(num, den)

            # If no common digit, skip to the next iteration
            if common_digit == -1 or common_digit == 0:
                continue

            # Make the fraction strings
            orig_fraction = makeFraction(num, den)

            # Remove the common digit (inexperienced simplification)
            new_num = int(str(num).replace(common_digit, '', 1))
            new_den = int(str(den).replace(common_digit, '', 1))

            # Ensure the denominator is valid and make "simplified" fraction
            if new_den == 0:
                new_fraction = "2/1" # Purposefully out of bounds value
            else:
                new_fraction = makeFraction(new_num, new_den)

            # Check if fractions have the same value, and if they are less than 1
            if (eval(orig_fraction) == eval(new_fraction) and eval(orig_fraction) < 1):
                print(orig_fraction)

            # Now to a simple calculator calculation!
            # It comes out to 1/100 !

if __name__ == '__main__':
    main()