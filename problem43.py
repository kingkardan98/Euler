# Find the sum of all the 0 to 9-pandigital numbers that satisfy all the properties.

import itertools

def generate_permutations(lst):
    return list(itertools.permutations(lst))

def main():
    print("GENERATING PANDIGITALS...", end=" ")
    all_pandigitals = generate_permutations([str(i) for i in range(10)])
    print("DONE.\nC1: D2 D3 D4 % 2 == 0...", end=" ")

    # First property: D2 D3 D4 is even -> D4 is even
    all_pandigitals = [number for number in all_pandigitals if int(number[3]) % 2 == 0]
    print("DONE.\nC2: D3 D4 D5 % 3 == 0...", end=" ")

    # Second property: D3 D4 D5 is divisible by 3 -> D3 + D4 + D5 % 3 == 0
    all_pandigitals = [number for number in all_pandigitals if (int(number[2]) + int(number[3]) + int(number[4])) % 3 == 0]
    print("DONE.\nC3: D4 D5 D6 % 5 == 0...", end=" ")

    # Third property: D4 D5 D6 is divisible by 5 -> D6 % 5 == 0
    all_pandigitals = [number for number in all_pandigitals if int(number[5]) % 5 == 0]
    print("DONE.\nC4: D5 D6 D7 % 7 == 0...", end=" ")

    # Fourth property: D5 D6 D7 % 7 == 0 -> (D5 + D6*10 + D7*100) % 7 == 0
    all_pandigitals = [number for number in all_pandigitals if (int(number[4])*100 + int(number[5])*10 + int(number[6])) % 7 == 0]
    print("DONE.\nC5: D6 D7 D8 % 11 == 0...", end=" ")

    # Fifth property: D6 D7 D8 % 11 == 0 -> like above
    all_pandigitals = [number for number in all_pandigitals if (int(number[5])*100 + int(number[6])*10 + int(number[7])) % 11 == 0]
    print("DONE.\nC6: D7 D8 D9 % 13 == 0...", end=" ")

    # Sixth property: D7 D8 D9 % 13 == 0 -> like above
    all_pandigitals = [number for number in all_pandigitals if (int(number[6])*100 + int(number[7])*10 + int(number[8])) % 13 == 0]
    print("DONE.\nC7: D8 D9 D10 % 17 == 0...", end=" ")

    # Seventh property: D8 D9 D10 % 17 == 0 -> like above
    all_pandigitals = [number for number in all_pandigitals if (int(number[7])*100 + int(number[8])*10 + int(number[9])) % 17 == 0]
    print("DONE.\n\nAFTER THIS PROCESS THESE ARE THE REMAINING NUMBERS:")

    sum = 0
    for number in all_pandigitals:
        print(int("".join(number)), end=", ")
        sum += int("".join(number))

    print("\n\nTHEIR SUM IS", sum)

if __name__ == '__main__':
    main()