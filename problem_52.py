# Find the smallest number such that x, 2x, 3x, 4x, 5x and 6x are all permutations of each other.

import itertools

def main():
    i = 1
    while True:
        i_list = [*str(i)] # Makes a list of all the characters in a string
        i_split_perms = set(itertools.permutations(i_list))
        i_permutations = set()
        for perm in i_split_perms:
            i_permutations.add("".join(perm))
        isGood = True

        for j in range(2, 7):
            if str(i*j) not in i_permutations:
                isGood = False
        
        if isGood:
            print(i)
            return
        else:
            i += 1

if __name__ == '__main__':
    main()