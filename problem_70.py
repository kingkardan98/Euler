from recurring_functions.Totatives import phi
from itertools import permutations
from tqdm import tqdm

def is_permutation(n, m):
    return sorted(str(n)) == sorted(str(m))

def main():
    limit = 10**7
    perms = []
    ratios = []
    tracker = tqdm(total=limit)
    for i in range(1, limit):
        totative = phi(i)
        if is_permutation(totative, i):
            perms.append(i)
            ratios.append(i/totative)
        tracker.update(1)

    tracker.close()
    index_min = min(range(len(ratios)), key=ratios.__getitem__)
    print(perms[index_min])

main()