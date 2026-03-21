# I can reduce the field of search: if a number is evenly divisible by 20,
# it's also evenly divisible by all the divisors of 20.
# Doing this, I can WIDELY reduce my search power. I just need a set of divisors that cover
# all the numbers from 1 to 20.

# 20 = 1,2,4,5,10,20
# 19 = 19
# 18 = 3,6,9,18
# 17 = 17
# 16 = 8, 16
# 14 = 7, 14
# 13 = 13
# 11 = 11

# I've then reduced my search from 20 numbers to 10 already.
# I also know that if a number passes the 20 and 18 check,
# it would automatically pass the 12 and 15 check, so I further reduced to eight.
# This is now my final set of eight numbers.

def main():
    divisors = [20, 19, 18, 17, 16, 14, 13, 11]
    i = 2520
    isMagic = True
    while True:
        for div in divisors:
            if i % div != 0:
                isMagic = False
                break
        if isMagic:
            print(i)
            break
        else:
            isMagic = True
            i += 1

if __name__ == '__main__':
    main()