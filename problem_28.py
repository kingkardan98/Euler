dimension = 1001

spiral = [[0 for _ in range(dimension)] for _ in range(dimension)]

originX = originY = (dimension // 2)

def find_new_direction(direct):
    if direct == 'right':
        return 'down'
    elif direct == 'down':
        return 'left'
    elif direct == 'left':
        return 'up'
    elif direct == 'up':
        return 'right'
    return None

def step(dir_x, dir_y, direct):
    if direct == 'right':
        return dir_x + 1, dir_y
    elif direct == 'down':
        return dir_x, dir_y + 1
    elif direct == 'left':
        return dir_x - 1, dir_y
    elif direct == 'up':
        return dir_x, dir_y - 1
    return None

def write(x_val, y_val, val):
    spiral[y_val][x_val] = val

def loop(direct, val, dir_x, dir_y, step_count):
    direct = find_new_direction(direct)
    try:
        for j in range(step_count):
            dir_x,dir_y = step(dir_x, dir_y, direct)
            write(dir_x, dir_y, val)
            val += 1
        return direct, val, dir_x, dir_y
    except IndexError:
            return None, None, None, None


# We now spiralize. I have to move counter-clockwise.
# I think I figured it out: we need some auxiliary variables.
# I've set the starting point, directionVariation and the direction 
# in a way that sets off the loop correctly.

value = 1
x = originX
y = originY + 1
direction = 'left'
steps = 1
directionVariation = -1

# Here's the thing:

# If directionVariation < 2:
#      find new direction
#      for steps:
#          step
#          write
#          value++
# Else:
#      steps++
#      find new direction
#      for steps:
#          step
#          write
#          value++

while value < dimension**2:
    try:
        if directionVariation < 2:
            direction, value, x, y = loop(direction, value, x, y, steps)
            if direction is None:
                break
            directionVariation += 1
        else:
            steps = steps + 1
            directionVariation = 1
            direction, value, x, y = loop(direction, value, x, y, steps)
            if direction is None:
                break
    except IndexError:
        print("Index error at {}, {} coordinates".format(x, y))
        break

# Spiral has been constructed correctly. Nicely done.
# Now to sum the diagonals.
S = 0
for i in range(dimension):
    S += spiral[i][i] + spiral[i][dimension - i - 1]

# Let's remove 1 because the center 1 is counted two times, as the only member of
# both diagonals.
print(S - 1)