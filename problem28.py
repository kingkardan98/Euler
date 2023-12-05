dimension = 1001

spiral = [[0 for _ in range(dimension)] for _ in range(dimension)]

originX = originY = (dimension // 2)

def findNewDirection(direction):
    if direction == 'right':
        return 'down'
    elif direction == 'down':
        return 'left'
    elif direction == 'left':
        return 'up'
    elif direction == 'up':
        return 'right'

def step(x,y,direction):
    if direction == 'right':
        return x+1, y
    elif direction == 'down':
        return x, y+1
    elif direction == 'left':
        return x-1, y
    elif direction == 'up':
        return x, y-1

def write(x,y,value):
    spiral[y][x] = value

def loop(direction, value, x, y, steps):
    direction = findNewDirection(direction)
    try:
        for i in range(steps):
            x,y = step(x,y,direction)
            write(x,y,value)
            value += 1
        return direction, value, x, y
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
            if direction == None:
                break
            directionVariation += 1
        else:
            steps = steps + 1
            directionVariation = 1
            direction, value, x, y = loop(direction, value, x, y, steps)
            if direction == None:
                break
    except IndexError:
        print("Index error at {}, {} coordinates".format(x, y))
        break

# Sprial has been constructed correctly. Nicely done.
# Now to sum the diagonals.
sum = 0
for i in range(dimension):
    sum += spiral[i][i] + spiral[i][dimension - i - 1]

# Let's remove 1 because the center 1 is counted two times, as the only member of
# both diagonals.
print(sum - 1)