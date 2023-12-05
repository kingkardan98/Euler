# Every rational is either repeating or a decimal.
# I can check for remainders. If I find a repeating remainder, that is the period.
# If the remainder is zero, the number is a terminating decimal.

def checkPeriod(n):
    period = []
    result, remainder = divmod(1, n)
    period.append(result)
    remainders = [remainder]
    while True:
        result, remainder = divmod(remainder*10, n)
        if remainder == 0:
            return 0
        else:
            if remainder in remainders:
                return len(period)
            else:
                remainders.append(remainder)
                result, remainder = divmod(remainder*10, n)
                period.append(result)

maxPeriod = 0
maxValue = 0
for n in range(1, 1000):
    currentPeriod = checkPeriod(n)
    if currentPeriod > maxPeriod:
        maxPeriod = currentPeriod
        maxValue = n
print(maxValue)