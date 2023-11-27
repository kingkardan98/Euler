def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

number = str(factorial(100))
digSum = 0
for digit in number:
    digSum += int(digit)

print(digSum)