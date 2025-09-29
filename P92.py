SET89 = set()
loop89 = [89, 145, 42, 20, 4, 16, 37, 58]
for element in loop89:
    SET89.add(element)
SET1 = set()
SET1.add(1)
MAX = 10**7

def nextInChain(number: int) -> int:
    """Takes all digits of a number, squares each one of them and sums them up"""
    return sum([int(digit)**2 for digit in str(number)])

def isInSet(number: int, checkset: set):
    """Checks if a number is inside the checkset"""
    return number in checkset

def main():
    collapsing = []
    for i in range(1, MAX + 1):
        start = i
        currentChain = [start]
        n = start                     
        while True:
            if isInSet(n, SET1):
                for element in currentChain:
                    SET1.add(element)
                break
            elif isInSet(n, SET89):
                for element in currentChain:
                    SET89.add(element)
                collapsing.append(start)   
                break
            else:
                n = nextInChain(n)
                currentChain.append(n)
        if start % 10 == 0:
            percentage = start / MAX * 100
            print("%.2f" % percentage)
    print(len(collapsing))
            
main()