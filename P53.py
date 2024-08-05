LIMIT = 100
# LIMIT = 10000, pushed up here and... OverflowError

def generateFactorialTable(n):
    factorial_list = [1, 1] # 0! = 1, 1! = 1
    for i in range(2, n+1):
        factorial_list.append(i * factorial_list[i-1])
    return factorial_list

FACTORIAL_TABLE = generateFactorialTable(LIMIT)

def nOverR(n, r):
    if r == 0:
        return 1
    if r > n:
        return 0
    return factorial(n) / (factorial(r) * factorial(n-r))

def factorial(n, lookup_table=FACTORIAL_TABLE):
    return lookup_table[n]

def main():
    counter = 0
    for n in range(LIMIT + 1):
        for r in range(n+1):
            if nOverR(n, r) > 10**6:
                counter += 1
    print(counter)

if __name__ == '__main__':
    main()