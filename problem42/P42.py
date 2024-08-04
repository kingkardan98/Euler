# Count how many triangle words are in the text file.
# A triangle word is a word such that the sum of the values
# of all the letters in the word add up to a triangular number.

# A triangular number is a number that arises from the sequence
# t_n = n*(n+1)/2

# C1: This sequence can also be described as
# s_n = s_(n-1) + n, which is recursively way better and compact

# Definition of triangular numbers. Really easy.
def triangular(n):
    if n == 1:
        return 1
    return triangular(n-1) + n

# This function reads and parses the file
def read(file):
    with open(file, 'r') as f:
        text = f.read()

    word_list = [word.strip('"').upper() for word in text.split(',')]
    return word_list

# Simple function that calculates the value of a word.
def wordValue(word):
    value = 0
    for char in word:
        # 64 is the value of capital A. Since all words are capitalized in the file
        # (but I also capitalized them in the list)  this "normalizes" the values.
        value += ord(char) - 64
    return value

# Easiest way to check is to generate triangular numbers.
# Start from 1, and work your way up to number.
# If the landing triangle number is not equal to number,
# number is not triangular.
def isTriangular(number):
    # If the word is 'A', it's good.
    if number == 1:
        return True
    
    i = 1
    triang = 1
    
    while triang < number:
        i += 1
        triang = triangular(i)
    
    if triang == number:
        return True
    return False

def main():
    count_triangulars = 0

    word_list = read('0042_words.txt')

    for word in word_list:
        word_value = wordValue(word)
        if isTriangular(word_value):
            count_triangulars += 1
    
    print(count_triangulars)

if __name__ == '__main__':
    main()