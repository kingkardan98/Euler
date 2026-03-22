# Find an arbitrary digit of Champernowne's constant.

# Simple: generate a string that's just the decimal part
# and check the length of it

def champernowne(n):
    number_to_concatenate = 1
    ch_constant = ''
    while len(ch_constant) < n:
        ch_constant = ch_constant + str(number_to_concatenate)
        number_to_concatenate += 1
    return int(ch_constant[n-1])

result = 1

for n in range(1,7):
    result *= champernowne(10**n)

print(result)