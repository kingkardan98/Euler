def main():
    sum = 0
    squareSum = 0
    for i in range(101):
        sum += i
        squareSum += i ** 2
    sumSquared = sum ** 2
    print(sumSquared - squareSum)

if __name__ == '__main__':
    main()