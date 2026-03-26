import math, ast

TEXT_FILENAME = 'problem_98_aux.txt'
LOOKUP_FILENAME = 'problem_98_lookup.txt'

def gather_text(filename):
    with open(filename, 'r') as f:
        text = f.readlines()[0].split(',')
        for i in range(len(text)):
            text[i] = text[i].replace('"', '')

    return text

def define_couples(candidate):
    if len(candidate) == 2:
        return [candidate]
    return [candidate[0], candidate[1]], [candidate[0], candidate[2]], [candidate[1], candidate[2]]

def anagram_engine(l, element_type="string"):
    anagrams = []
    seen = set()
    for element in l:
        if element in seen:
            continue

        seen.add(element)
        anagram_mini = [element]
        if element_type == "int":
            element_l = sorted(str(element))
        else:
            element_l = sorted(element)

        for challenger in l:
            if challenger == element:
                continue
            if challenger in seen:
                continue

            if element_type == "int":
                challenger_l = sorted(str(challenger))
            else:
                challenger_l = sorted(challenger)

            if element_l == challenger_l:
                seen.add(challenger)
                anagram_mini.append(challenger)

        if len(anagram_mini) > 1:
            anagrams.extend(define_couples(anagram_mini))

    return anagrams

def generate_squares(minn, maxx):
    # Generate all squares in the interval [minn, maxx]
    squares = []
    maximum = math.floor(math.sqrt(maxx))
    minimum = math.ceil(math.sqrt(minn))
    for x in range(minimum, maximum + 1):
        squares.append(x**2)
    return squares

def word_anagrams(text):
    anagrams = anagram_engine(text)
    return anagrams

def square_anagrams(l):
    anagramic_squares = anagram_engine(l, element_type="int")
    return anagramic_squares

def generate_lookup_tables(anagrams):
    lookup_tables = []
    max_length = max(len(anagram[0]) for anagram in anagrams)

    for length in range(max_length):
        minimum = 10 ** length
        maximum = 10**(length + 1) - 1
        lookup_table = generate_squares(minimum, maximum)
        lookup_table = square_anagrams(lookup_table)
        lookup_tables.append(lookup_table)

    return lookup_tables

def load_lookup_tables(filename):
    lookup_tables = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            lookup_tables.append(ast.literal_eval(line.strip()))
    return lookup_tables

def map_anagrams(couple, lookup_table):
    current_max = 0

    for square_anagram in lookup_table:

        # Check for unique digits before creating a mapping
        if (len(set(couple[0])) != len(set(str(square_anagram[0]))) or
                len(set(couple[1])) != len(set(str(square_anagram[1])))):
            continue
        mapping1 = str.maketrans(couple[0], str(square_anagram[0]))
        mapping2 = str.maketrans(couple[1], str(square_anagram[0]))
        if couple[1].translate(mapping1) == str(square_anagram[1]):
            if max(square_anagram[0], square_anagram[1]) > current_max:
                current_max = max(square_anagram[0], square_anagram[1])
        if couple[0].translate(mapping2) == str(square_anagram[1]):
            if max(square_anagram[0], square_anagram[1]) > current_max:
                current_max = max(square_anagram[0], square_anagram[1])
    return current_max


def main():
    text = gather_text(TEXT_FILENAME)
    anagram_words = word_anagrams(text)
    square_lookup_tables = load_lookup_tables(LOOKUP_FILENAME)

    # Saved lookup tables to TXT files for time consumption.
    # Didn't cheat, generated all fair and square.
    # I can just save 1'30'' each execution.
    """
    square_lookup_tables = generate_lookup_tables(anagram_words)
    with open('problem_98_lookup.txt', 'w') as f:
       for lookup_table in square_lookup_tables:
            f.write(str(lookup_table) + '\n')
    """

    # At this point, I need to map each couple onto a possible square anagram.
    # I'll take each couple and get its best mapping.
    max_square = 0
    for couple in anagram_words:
        length = len(couple[0])
        best_square = map_anagrams(couple, square_lookup_tables[length - 1])
        if best_square > max_square:
            max_square = best_square
    print(max_square)

if __name__ == '__main__':
    main()