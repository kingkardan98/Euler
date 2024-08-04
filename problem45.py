# Find the first numbers that are triangular, pentagonal and hexagonal at the same time.

# T(n) = n*(n+1)/2 => n = sqrt(2x + 1/4) - 1/2
# P(n') = n'*(3n'-1)/2 => n' = (sqrt(2*x + 1/12) + 1/(2*sqrt(3)))/sqrt(3)
# H(n'') = n"*(2n" - 1) => n" = (sqrt(x + 1/8) + 1/(2*sqrt(2))) / sqrt(2)

# Now it's just a matter of producing triangular numbers, starting from n = 285, and checking if
# for any of those numbers I get an integer solutions to the other two equations.

from math import sqrt

def T(n):
    return n*(n+1) // 2

def isPentagonal(x):
    # Standard check to see if a number is pentagonal.
    formula = (1 + sqrt(1 + 24*x))/6
    return formula.is_integer()

def isHexagonal(x):
    # Standard check to see if a number is hexagonal.
    formula = (1 + sqrt(1 + 8*x))/4
    return formula.is_integer()

def main():
    # Starting at n = 286 since we're looking for the next
    # triangular number with that property.
    n = 286
    while True:
        triang = T(n)
        if isPentagonal(triang) and isHexagonal(triang):
            print(triang)
            return
        n += 1
    
if __name__ == '__main__':
    main()