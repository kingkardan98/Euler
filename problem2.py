def fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    sum = 0
    i = 0
    greatest = 1
    while greatest < 4000000:
        term = fibonacci(i)
        if term % 2 == 0:
            sum += term
        greatest = term
        i += 1
    print(sum)

if __name__ == '__main__':
    main()