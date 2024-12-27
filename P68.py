# The magic 5-gon problem. Interesting!
# A magic n-gon is a pentagon with "wings". Each line, from the wing to the last possible vertex in a straight line, must equal to the same total.
# In a magic 5-gon, there are only so many possibilities, so a good tactic would be to build the lists, and link together whatever points I need to.

# We can call them line1 through line5, and know that each time we update line-n[2], that's also line-n+1[1], if not set already.

# A visual representation of a 5-gon can be found in P68.png

# EDIT: extremely proud of this code! A 25% problem solved without any external help!

from itertools import permutations
from tqdm import tqdm

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

def magicPentagon():
    combs = permutations([x for x in range(1, 11)], 10)
    magics = []
    tracker = tqdm(total=3628800, desc="Checking magic 5-gons")
    for comb in combs:
        tracker.update(1)
        pentagon = [[0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0]]
        # Filling the pentagon manually, probably easier.
        pentagon[0][0] = comb[0]
        pentagon[0][1] = pentagon[4][2] = comb[1]
        pentagon[0][2] = pentagon[1][1] = comb[2]
        pentagon[1][0] = comb[3]
        pentagon[1][2] = pentagon[2][1] = comb[4]
        pentagon[2][0] = comb[5]
        pentagon[2][2] = pentagon[3][1] = comb[6]
        pentagon[3][0] = comb[7]
        pentagon[3][2] = pentagon[4][1] = comb[8]
        pentagon[4][0] = comb[9]

        # This way we have filled the pentagon, now we need to check if it's a valid magic 5-gon.
        if isMagic(pentagon):
            sortedPentagon = sortedMagic(pentagon)
            if sortedPentagon not in magics:
                magics.append(sortedPentagon)
    tracker.close()

    maxSixteen = 0
    for magic in magics:
        string = ''
        for line in magic:
            for i in range(len(line)):
                string = string + str(line[i])
                if len(string) == 16:
                    if int(string) > maxSixteen:
                        maxSixteen = int(string)
    print("The maximum 16-long string created from the set describing a magic 5-gon is {}".format(maxSixteen))

magicPentagon()