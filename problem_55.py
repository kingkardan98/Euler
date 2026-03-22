# Find all Lychrel numbers below 10000

MAX_ITERATIONS = 50
MAX_LIMIT = 10000

def is_palindrome(number):
    return str(number) == str(number)[::-1]

def is_lychrel(number):
    iterations = 0
    while iterations <= MAX_ITERATIONS:
        number = number + int(str(number)[::-1])
        iterations += 1
        if is_palindrome(number):
            return False

    return True

def main():
    lychrel_counter = 0
    for number in range(1, MAX_LIMIT + 1):
        if is_lychrel(number):
            lychrel_counter += 1
    print(lychrel_counter)

if __name__ == '__main__':
    main()