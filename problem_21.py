import math

def d(n):
    divSum = 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            divSum += i 
            if i != n // i:
                divSum += n // i
    return divSum + 1

divSums = []
for n in range(10001):
    divSums.append(d(n))

amicableSum = 0

for i in range(len(divSums)):
    for j in range(len(divSums)):
        if divSums[i] == j and divSums[j] == i and i < j:
            amicableSum += i + j

print(amicableSum)