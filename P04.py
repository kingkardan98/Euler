def isPalindrome(n):
    number = str(n)
    if number == number[::-1]:
        return True
    return False


def main():
    maxPalindrome = 999
    for i in range(1000):
        for j in range(1000):
            product = i * j
            if isPalindrome(product) and product > maxPalindrome:
                maxPalindrome = product
    print(maxPalindrome)

if __name__ == '__main__':
    main()