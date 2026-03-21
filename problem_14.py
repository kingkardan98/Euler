from itertools import count

def collatzer(num):
    if num == 1:
        return 1
    elif num % 2 == 0:
        return num//2
    return 3*num + 1

def main():
    maxNum = 0
    maxSteps = 0
    numbers = count(start=1)
    for i in numbers:
        if i == 10**6:
            break
        j = i
        steps = 0
        while i != 1:
            i = collatzer(i)
            steps += 1
        if steps > maxSteps:
            maxNum = j
            maxSteps = steps
    print(maxNum)

if __name__ == '__main__':
    main()