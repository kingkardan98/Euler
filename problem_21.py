import math

def d(num):
    div_sum = 0
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            div_sum += i
            if i != num // i:
                div_sum += num // i
    return div_sum + 1

divSums = []
for n in range(10001):
    divSums.append(d(n))

amicableSum = 0

for i in range(len(divSums)):
    for j in range(len(divSums)):
        if divSums[i] == j and divSums[j] == i and i < j:
            amicableSum += i + j

print(amicableSum)