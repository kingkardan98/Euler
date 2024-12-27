# Let's use this approach: instead of checking every single number, let's create the lists
# with numbers we already know are triangular, square...

# We order it, check if it's cyclic and wa-bam, we don't even need the polygonal check, it already passes.
# Only thing to check: the list must not contain duplicates.

# This way the total number of checks comes out to 140*100*81*70*63*58 = 2.9 * 10^11, which is ASTONISHINGLY less than 10^24 of the direct approach.
# 13 orders of magnitude!

# Another order of magnitude knocked down: the numbers must start from 1000.
# This brings the calculations to 96*69*56*48*43*40 = 3.062513664 × 10^10.
# This makes the difference from having the answer in 3 days to having it in 6 hours at most. Any other exploits?

# Yes: at the same index, every triangular number is smaller than a square,
# a square is smaller than a pentagonal and so on.
# We can check every index starting from the index previous to it. This optimizes the loop, but worst case scenario, it's exactly like before.

# We can remove all number that end with 00, 01, 02..., 09.
# Those are 10 numbers every 100.
# A sizeable dent: 88*53*47*44*40*30 = 1.15741824 × 10^10. 2 hours instead of 6, good!

# Numbers that appear in our list now have the following properties by design:
# - polygonal
# - bigger than 1000 (4 digits)
# - not ending with 00, 01, ..., 09 (un-cyclable)
# - sorted (design of the nested for loop, required by the problem)
# So it feels like all filters that could be applied have been. We must think outside of the box.

# I was assuming that the list was ordered because the n-th n-number is always smaller than the n-th n+1-number.
# But, for example, the 30th triangular number has 3 digits, the 30th octagonal is four-digits long.
# Since the set must be ordered, all n+1-numbers smaller than the minimum of n-numbers must be excluded.
# We've brought it into the lower order of magnitude: 88*52*46*42*38*27 = 9.070693632 × 10^9. This would take 1h30' on the Macintosh. Manageable!

# Let's give it to the gaming PC and see how it fares.

from recurring_functions.Polygonals import generatePolygonals
from tqdm import tqdm

LIMIT = 10000

def isSorted(lst):
    return lst == lst.sort()

def isCyclic(lst):
    # Checks directly with integers if the last two digits and the first two digits are the same
    for i in range(len(lst) - 1):
        current_end = lst[i] % 100  # Last two digits
        next_start = lst[i + 1] // 100  # First two digits
        if current_end != next_start:
            return False
    return True

def isDouble(lst):
    return len(lst) != len(set(lst))

def main():
    tri = list(generatePolygonals(3, LIMIT))
    squ = list(generatePolygonals(4, LIMIT))
    pen = list(generatePolygonals(5, LIMIT))
    hex = list(generatePolygonals(6, LIMIT))
    hep = list(generatePolygonals(7, LIMIT))
    oct = list(generatePolygonals(8, LIMIT))

    old_sets = [tri, squ, pen, hex, hep, oct]
    sets = []
    
    for i in range(len(old_sets)):
        s = [el for el in old_sets[i] if (el <= LIMIT) and (el >= 1000) and (el % 100 not in [1,2,3,4,5,6,7,8,9,0])]
        if i > 0:
            s = [el for el in old_sets[i] if (el <= LIMIT) and (el >= 1000) and (el % 100 not in [1,2,3,4,5,6,7,8,9,0]) and (el > min(sets[i-1]))]
        s.sort()
        sets.append(s)

    tracker = tqdm(total=88*52*46*42*38*27)

    for f in range(27):
        for e in range(f, 38):
            for d in range(e, 42):
                for c in range(d, 46):
                    for b in range(c, 52):
                        for a in range(b, 88):
                            tracker.update(1)
                            lst = [int(sets[5][f]), int(sets[4][e]), int(sets[3][d]), int(sets[2][c]), int(sets[1][b]), int(sets[0][a])]
                            if isDouble(lst) or (not isSorted(lst)) or (not isCyclic(lst)):
                                continue
                            break
                            

if __name__ == '__main__':
    main()