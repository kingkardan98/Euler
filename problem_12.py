from itertools import count

def countDivisors(number):
    count = 0
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            count += 1
            if i != number // i:
                count += 1
    return count

def main():
    series_sum = lambda n: n * (n + 1) // 2
    triangles = (series_sum(i) for i in count())
    print(triangles)
    for triangle in triangles:
        if countDivisors(triangle) > 500:
            print(triangle)
            break

if __name__ == '__main__':
    main()