def isIncreasing(numL):
    for i in range(1, len(numL)):
        if numL[i - 1] > numL[i]:
            return False
    return True

def isDecreasing(numL):
    for i in range(1, len(numL)):
        if numL[i - 1] < numL[i]:
            return False
    return True

def isBouncy(num):
    numL = [c for c in str(num)]
    if len(numL) < 3:
        return False
    
    if isIncreasing(numL) or isDecreasing(numL):
        return False
    return True

def main():
    ratio = 0
    bouncy = 0
    i = 0
    while True:
        if isBouncy(i):
            bouncy += 1
            ratio = bouncy / i
        if ratio == 0.99:
            break
        i += 1
    print(i)

main()