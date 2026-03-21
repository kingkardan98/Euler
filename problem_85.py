VALUE = 2000000

def countRectangles(length, height):
    """Count the number of rectangles in a rectangle grid"""
    return (((length) * (length+1)) / 2) * (((height) * (height+1)) / 2)

def main():
    # How do I restrict the range of numbers to check?
    # Of course binom(m+1, 2) * binom(n+1, 2) = binom(n+1, 2) * binom(m+1, 2)
    # which means I don't really need to check every couple possible: main(m, n) = main(n, m)
    # I then augment m and n accordingly, and check if the forumla turns up to be more than 2 * 10^6
    # If it is, I take the last value and current value, check which one is nearer to 2 million and save it.
    # I printed each change in delta, son when it stops it's a good first candidate to try.
    sum = 0
    delta = VALUE
    candidate_sum = 0
    candidate_m = 0
    candidate_n = 0
    m, n = 1, 1
    i = 0
    while m < VALUE:
        sum = countRectangles(m, n)
        newDelta = abs(VALUE - sum)
        if newDelta < delta:
            delta = newDelta
            candidate_sum = sum
            candidate_m = m
            candidate_n = n
            print("Steps done: {}".format(i))
            print("Candidates: {}, {}".format(m, n))
            print("Delta: {}".format(delta))
        n += 1
        if n >= m:
            n = 1
            m += 1
        
        i += 1

    return candidate_sum, candidate_m, candidate_n
        
print(main())