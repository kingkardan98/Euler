number = str(2**1000)

S = 0
for digit in number:
    S += int(digit)

print(S)