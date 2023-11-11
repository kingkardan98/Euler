import math, sys

def main():
    for c in range(1000):
        for b in range(1, c):
            for a in range(1, b):
                if a**2 + b**2 == c**2 and a + b + c == 1000:
                    print(a * b * c)
                    sys.exit()

if __name__ == '__main__':
    main()