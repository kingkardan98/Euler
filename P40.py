# Find an arbitrary digit of Champernowne's constant.

# Simple: generate a string that's just the decimal part
# and check the length of it

def champernowne(n):
    numberToConcatenate = 1
    chConstant = ''
    while len(chConstant) < n:
        chConstant = chConstant + str(numberToConcatenate)
        numberToConcatenate += 1
    return int(chConstant[n-1])

result = 1

for n in range(1,7):
    result *= champernowne(10**n)

print(result)