# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

def isPalindrome(number):
    # Just comparing the string to its counterpart read backwards
    return str(number) == str(number)[::-1]

UPPER_LIMIT = 1000000

base10Palindromes = []
bothBasesPalindromes = []

for i in range(UPPER_LIMIT + 1):
    # First, find all palindromes in base 10, just to narrow the search.

    if isPalindrome(i):
        base10Palindromes.append(i)
    
# Now, for each 10-palindrome, we convert it, and check if that is also a palindrome.
for number in base10Palindromes:
    if isPalindrome(bin(number).replace('0b', '')):
        bothBasesPalindromes.append(number)

print(sum(bothBasesPalindromes))
