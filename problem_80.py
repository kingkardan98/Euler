import decimal, math, datetime

def digital_sum(number, precision):
    decimal.getcontext().prec = precision + 10
    number = decimal.Decimal(number)
    sqrt_n = number.sqrt()
    
    sqrt_split = str(sqrt_n).split('.')
    sqrt_dec = sqrt_split[1][:precision - 1]
    digitalsum = sum(int(c) for c in sqrt_dec) + int(sqrt_split[0])
    return digitalsum

def main():
    start = datetime.datetime.now()
    no_squares = [_ for _ in range(1, 101) if math.isqrt(_)**2 != _]
    precision = 100
    total_sum = 0
    for number in no_squares:
        total_sum += digital_sum(number, precision)

    print(total_sum)
    time = datetime.datetime.now() - start
    print("{} ms".format(time.total_seconds() * 1000))

main()