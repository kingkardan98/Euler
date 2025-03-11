import decimal, math, datetime

def digitalSum(number, precision):
    decimal.getcontext().prec = precision + 10
    number = decimal.Decimal(number)
    sqrt_n = number.sqrt()
    
    sqrt_split = str(sqrt_n).split('.')
    sqrt_dec = sqrt_split[1][:precision - 1]
    digital_sum = sum(int(c) for c in sqrt_dec) + int(sqrt_split[0])
    return digital_sum

def main():
    start = datetime.datetime.now()
    noSquares = [_ for _ in range(1, 101) if math.isqrt(_)**2 != _]
    precision = 100
    totalSum = 0
    for number in noSquares:
        totalSum += digitalSum(number, precision)

    print(totalSum)
    time = datetime.datetime.now() - start
    print("{} ms".format(time.total_seconds() * 1000))

main()