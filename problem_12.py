from itertools import count

def count_divisors(number):
    counter = 0
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            counter += 1
            if i != number // i:
                counter += 1
    return counter

def main():
    series_sum = lambda n: n * (n + 1) // 2
    triangles = (series_sum(i) for i in count())
    print(triangles)
    for triangle in triangles:
        if count_divisors(triangle) > 500:
            print(triangle)
            break

if __name__ == '__main__':
    main()