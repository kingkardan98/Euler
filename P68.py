# The magic 5-gon problem. Interesting!
# A magic n-gon is a ngon with "wings". Each line, from the wing to the last possible vertex in a straight line, must equal to the same total.
# In a magic 5-gon, there are only so many possibilities, so a good tactic would be to build the lists, and link together whatever points I need to.

# We can call them line1 through line5, and know that each time we update line-n[2], that's also line-n+1[1], if not set already.

# A visual representation of a 5-gon can be found in P68.png

# EDIT: extremely proud of this code! A 25% problem solved without any external help!
# EDIT 2: completely generalized the program, save for the filling logic. So close!
# Every second element is the last of the "previous" line, and every last element is the second of the "next" line.

# EDIT 3: Done! Completely generalized the program! And moved the function to the dedicated file for later use

from recurring_functions.MagicNgons import magicNgon

SIZE = 5

def main():
    possibleLengths = []
    strings = []
    magics = magicNgon(SIZE)
    for magic in magics:
        string = ''
        for line in magic:
            for i in range(len(line)):
                string = string + str(line[i])
        strings.append(string)
        if len(string) not in possibleLengths:
            possibleLengths.append(len(string))

    possibleLengths.sort()
    for length in possibleLengths:
        maxString = 0
        for string in strings:
            if len(string) == length:
                if int(string) > maxString:
                    maxString = int(string)
        print("The maximum {}-long string created from the set describing a magic {}-gon is {}".format(length, SIZE, maxString))

if __name__ == '__main__':
    main()