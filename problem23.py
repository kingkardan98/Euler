import math

def d(n):
    # We can easily reuse the function from P21
    divSum = 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            divSum += i
            if i != n // i:
                divSum += n // i
    return divSum + 1

def isAbundant(num):
    if d(num) > num:
        return True
    return False

# Let's generate all the abundant numbers below 28123
abundant = []
allNumbers = list(range(28124))

for i in allNumbers:
    if isAbundant(i):
        abundant.append(i)

# Let's get the range of all numbers and remove all the sums of two abundant numbers.
summation = 0
for n in abundant:
    for m in abundant[n:]:
        if n+m in allNumbers:
            print((n,m))
            allNumbers.remove(n+m)
            

print(summation)