def main():
    S = 0
    square_sum = 0
    for i in range(101):
        S += i
        square_sum += i ** 2
    sum_squared = S ** 2
    print(sum_squared - square_sum)

if __name__ == '__main__':
    main()