def is_palindrome(n):
    number = str(n)
    if number == number[::-1]:
        return True
    return False


def main():
    max_palindrome = 999
    for i in range(1000):
        for j in range(1000):
            product = i * j
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
    print(max_palindrome)

if __name__ == '__main__':
    main()