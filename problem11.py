# I need to check in just two "straight" directions and two "diagonal" directions:
# STRAIGHT - Right, down
# DIAGONAL - Right-to-left up-to-down, left-to-right up-to-down

def EastCheck(table, startingx, startingy, endx, endy):
    product = 0
    # For every row, I first go down one single row, then skip to the next row.
    for x in range(startingx, endx):
        for y in range(startingy + 3, endy):
            newProduct = table[x][y-3] * table[x][y-2] * table[x][y-1] * table[x][y]
            if newProduct > product:
                product = newProduct
    return product

def SouthCheck(table, startingx, startingy, endx, endy):
    product = 0
    # Same logic, going down and skipping columns
    for y in range(startingy, endy):
        for x in range(startingx + 3, endx):
            newProduct = table[x-3][y] * table[x-2][y] * table[x-1][y] * table[x][y]
            if newProduct > product:
                product = newProduct
    return product

def SECheck(table, startingx, startingy, endx, endy):
    # This logic is a bit trickier.
    # I need to go down one diagonal, reach a MAX value
    # and then skip diagonals. Do that until there are
    # less than four elements in that diagonal.
    product = 0
    x = startingx + 3
    y = startingy + 3
    while x < endx + 1  and y < endy + 1:
        newProduct = table[x-3][y-3] * table[x-2][y-2] * table[x-1][y-1] * table[x][y]
        if newProduct > product:
            product = newProduct
        x += 1
        y += 1
    return product

def SWCheck(table, startingx, startingy, endx, endy):
    # Same logic as before, different x direction.
    x = startingx - 3
    y = startingy + 3
    while x < endx + 1  and y < endy + 1:
        newProduct = table[x+3][y-3] * table[x+2][y-2] * table[x+1][y-1] * table[x][y]
        if newProduct > product:
            product = newProduct
        x += 1
        y += 1
    return product

def main():
    # Right check.
    table = [
        [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
        [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
        [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
        [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
        [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
        [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
        [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
        [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
        [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
        [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
        [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
        [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
        [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
        [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
        [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
        [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
        [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
        [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
        [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
        [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]
    ]

    products = [EastCheck(table,0,0,20,20), SouthCheck(table,0,0,20,20), 0, 0]
    for i in range(17):
        starting = [i, 0]
        offsetx = starting[0]
        product = SECheck(table, offsetx, 0, 20, 20 - offsetx)
        if product > products[2]:
            products[2] = product

    for j in range(17):
        starting = [0,j]
        offsety = starting[1]
        product = SECheck(table, 0, offsety, 20 - offsety, 20)
        if product > products[2]:
            products[2] = product

    for i in range(17):
        starting = [20 - i, 0]
        offsetx = 20 - i
        product = SWCheck(table, i, offsetx, 0, 20 - offsetx)
        if product > products[3]:
            products[3] = product

    for j in range(17):
        starting = [20, j]
        offsety = j
        product = SWCheck(table, 20, offsety, offsety, 20)
        if product > products[3]:
            products[3] = product

    print(max(products))

if __name__ == '__main__':
    main()