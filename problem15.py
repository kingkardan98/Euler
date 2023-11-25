def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


def pathGen(n, m):
    # We can represent the set of moves with a string of R's and D's (Rights and Downs)
    # A complete path must contain n R's and m D's.
    # How many such strings exist? How can we create such a string recursively?
    # It is the case of extracting balls out of a sack without re-insertion.
    # The probability of extracting any sequence of n R's and m D's is
    # (n! m!)/((n+m)!). This comprehends all the balls, since extracting all the balls
    # equates to having completed a path. Since this value represents the probability,
    return ((factorial(n) * factorial(m))/factorial(n+m))**-1

print('{:.0f}'.format(pathGen(20,20)))