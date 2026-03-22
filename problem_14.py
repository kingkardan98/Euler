from itertools import count

def collatzer(num):
    if num == 1:
        return 1
    elif num % 2 == 0:
        return num//2
    return 3*num + 1

def main():
    max_num = 0
    max_steps = 0
    numbers = count(start=1)
    for i in numbers:
        if i == 10**6:
            break
        j = i
        steps = 0
        while i != 1:
            i = collatzer(i)
            steps += 1
        if steps > max_steps:
            max_num = j
            max_steps = steps
    print(max_num)

if __name__ == '__main__':
    main()