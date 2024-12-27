from math import sqrt

def generatePolygonals(size, limit):
    if size == 3:
        return {n*(n+1)/2 for n in range(1, limit)}
    elif size == 4:
        return {n**2 for n in range(1, limit)}
    elif size == 5:
        return {n*(3*n - 1)/2 for n in range(1, limit)}
    elif size == 6:
        return {n*(2*n - 1) for n in range(1, limit)}
    elif size == 7:
        return {n*(5*n - 3)/2 for n in range(1, limit)}
    elif size == 8:
        return {n*(3*n - 2) for n in range(1, limit)} 

def isTriangular(n):
    # We invert the triangular
    factor = -(1/2) + sqrt(1/4 + 2*n)
    return factor == int(factor)

def isSquare(n):
    factor = sqrt(n)
    return factor == int(factor)

def isPentagonal(n):
    factor = (-(1/2) + sqrt(1/4 + 6*n))/3
    return factor == int(factor)

def isHexagonal(n):
    factor = (1 + sqrt(1 + 8*n))/4
    return factor == int(factor)

def isHeptagonal(n):
    factor = (3/2 + sqrt(9/4 + 10*n)) / 5
    return factor == int(factor)

def isOctagonal(n):
    factor = (1 + sqrt(1 + 3*n)) / 3
    return factor == int(factor)