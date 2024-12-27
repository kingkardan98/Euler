import operator

def getDiagonals(dimension):
    # A spiral's diagonals, in the way that is created below, can be gathered by thinking of it like this:
    # B     C
    #    1
    # D     A
    # The left diagonal is B + A, the right one is D + C
    # Here are the formulas to get those diagonals
    ldiag = rdiag = []
    for n in range(dimension):
        a = 4*n**2 + 4*n + 1
        b = 4*n**2 + 1
        c = 4*n**2 - 2*n + 1
        d = 4*n**2 + 2*n + 1
        ldiag.append(b)
        ldiag.append(a)
        rdiag.append(c)
        rdiag.append(d)
    return ldiag, rdiag

def showSpiral(spiral):
    dimension = len(spiral)
    
    # Find the maximum number in the spiral (this is the largest number and will be used to determine the padding)
    max_number = dimension * dimension
    
    # Find the width of the largest number for consistent formatting
    width = len(str(max_number))
    
    for i in range(dimension):
        for j in range(dimension):
            # Format each number to be the same width
            print(f"{spiral[i][j]:{width}d}", end=" ")
        print()  # Move to the next line after printing a row

def fillSpiral(spiral, dimension, center, clockwise=False):
    number = 1  # The number with which to fill the cell
    steps_to_do = 1  # The number of steps to do before the next direction change
    steps_done = 0  # The number of steps done in this cycle
    step_binary_cycle = 0  # Used to alternate step size after every two cycles

    # Directions: clockwise or counter-clockwise
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] if clockwise else [(0, 1), (-1, 0), (0, -1), (1, 0)]
    current_direction = 0
    direction = directions[current_direction]  # Start with the first direction

    spiral[center][center] = number
    current_point = (center, center)

    while number < dimension ** 2:
        number += 1
        # Move to the next cell
        current_point = tuple(map(operator.add, current_point, direction))
        spiral[current_point[0]][current_point[1]] = number
        steps_done += 1

        if steps_done == steps_to_do:
            steps_done = 0
            current_direction = (current_direction + 1) % 4
            direction = directions[current_direction]
            if step_binary_cycle == 1:
                steps_to_do += 1
                step_binary_cycle = 0
            else:
                step_binary_cycle = 1

    return spiral

def createSpiral(dimension):
    # Trova il centro della spirale con la media aritmetica
    center =  (dimension + 1) // 2 - 1

    # Genera una spirale vuota
    spiral = [[0 for _ in range(dimension)] for _ in range(dimension)]
    
    # Riempie la spirale in senso antiorario
    spiral = fillSpiral(spiral, dimension, center)

    return spiral
