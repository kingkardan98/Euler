import math

def d(n):
    divSum = 0
    if n == 1:
        return 1
    if n == 2:
        return 3
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divSum += i 
            divSum += (n//i)
    return divSum - n

divSums = []
amicable = []
for n1 in range(10001):
    divSums.append(d(n1))
    print(d(n1))

amicable = list(set(amicable))

print(sum(amicable))