from itertools import permutations
from tqdm import tqdm
from math import factorial

def fillNgon(ngon, perm):
    size = len(ngon)
    # Fill the first line, just to have a starting point
    ngon[0][0] = perm[0]
    ngon[0][1] = ngon[size - 1][2] = perm[1]
    ngon[0][2] = ngon[1][1] = perm[2]

    # Then fill the others
    for j in range(1, size-1):
        ngon[j][0] = perm[2*j + 1]
        ngon[j][2] = ngon[j+1][1] = perm[2*j + 2]

    # And then, the last number.
    ngon[size-1][0] = perm[-1]
    return ngon

def isMagic(ngon):
    sums = []
    for line in ngon:
        sums.append(sum(line))
    if len(set(sums)) == 1: # If it's magic all sums are equal
        return True
    return False

def sortedMagic(ngon):
    # We just need to find the index with the minimum external, and then it's designed to go around clockwise.
    sortedNgon = []
    min_ext = len(ngon) * 2 + 1
    index = -1
    for i in range(len(ngon)):
        if ngon[i][0] < min_ext:
            min_ext = ngon[i][0]
            index = i
    
    # At this point, we have the first line, and then we just have to go around.
    for j in range(index, len(ngon) + index):
        sortedNgon.append(ngon[j % len(ngon)])

    return sortedNgon

def magicNgon(size):
    perms = permutations([x for x in range(1, size*2 + 1)], size*2)
    magics = []
    tracker = tqdm(total=factorial(size*2), desc="Checking magic {}-gons".format(size))
    for perm in perms:
        tracker.update(1)
        ngon = [[0,0,0] for _ in range(size)]
        # Filling the ngon manually, probably easier.
        ngon = fillNgon(ngon, perm)

        # This way we have filled the ngon, now we need to check if it's a valid magic 5-gon.
        if isMagic(ngon):
            sortedngon = sortedMagic(ngon)
            if sortedngon not in magics:
                magics.append(sortedngon)
    tracker.close()
    return magics