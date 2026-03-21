number = str(2**1000)

sum = 0
for digit in number:
    sum += int(digit)

print(sum)