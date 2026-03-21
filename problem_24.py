from itertools import permutations

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

perm = permutations(digits)

millionth = list(perm)[999999]

for digit in millionth:
    print(digit, end="")