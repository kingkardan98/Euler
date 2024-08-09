from recurring_functions.Eratosthenes import sieveOfEratosthenes

def findNewDirection(direction):
    if direction == 'right':
        return 'down'
    elif direction == 'down':
        return 'left'
    elif direction == 'left':
        return 'up'
    elif direction == 'up':
        return 'right'

def step(x, y, direction):
    if direction == 'right':
        return x + 1, y
    elif direction == 'down':
        return x, y + 1
    elif direction == 'left':
        return x - 1, y
    elif direction == 'up':
        return x, y - 1

def write(x, y, value, spiral):
    spiral[y][x] = value

def loop(direction, value, x, y, steps, spiral):
    for i in range(steps):
        x, y = step(x, y, direction)
        if not (0 <= x < len(spiral) and 0 <= y < len(spiral)):
            return None, None, None, None
        write(x, y, value, spiral)
        value += 1
    direction = findNewDirection(direction)
    return direction, value, x, y

def checkPrimeRate(spiral, dimension, primes):
    allNumbers = dimension ** 2
    primeCounter = 0
    for i in range(dimension):
        if spiral[i][i] in primes:
            primeCounter += 1
        if spiral[i][dimension - 1 - i] in primes:
            primeCounter += 1
    
    if primeCounter / (2 * dimension - 1) < 0.1:
        return True
    return False

def main():
    dimension = 3  # Starting with the smallest odd dimension that can form a valid spiral
    while True:
        spiral = [[0 for _ in range(dimension)] for _ in range(dimension)]
        primes = sieveOfEratosthenes(dimension**2)

        origin = dimension // 2
        value = 1
        x = origin
        y = origin
        direction = 'right'
        steps = 1

        write(x, y, value, spiral)
        value += 1

        while value <= dimension**2:
            direction, value, x, y = loop(direction, value, x, y, steps, spiral)
            if direction is None:
                break
            direction, value, x, y = loop(direction, value, x, y, steps, spiral)
            if direction is None:
                break
            steps += 1

        if checkPrimeRate(spiral, dimension, primes):
            print("Dimension {}: stop.".format(dimension))
            return

        dimension += 2

if __name__ == '__main__':
    main()
