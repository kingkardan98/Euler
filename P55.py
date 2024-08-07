# Find all Lychrel numbers below 10000

MAX_ITERATIONS = 50
MAX_LIMIT = 10000

def isPalindrome(number):
    return str(number) == str(number)[::-1]

def isLychrel(number):
    iterations = 0
    while iterations <= MAX_ITERATIONS:
        number = number + int(str(number)[::-1])
        iterations += 1
        if isPalindrome(number):
            return False

    return True

def main():
    lychrelCounter = 0
    for number in range(1, MAX_LIMIT + 1):
        if isLychrel(number):
            lychrelCounter += 1
    print(lychrelCounter)

if __name__ == '__main__':
    main()