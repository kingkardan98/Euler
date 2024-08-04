import math

goldenRatio = (1 + math.sqrt(5))/2
conjugateRatio = (1 - math.sqrt(5))/2
fibList = [1,1]
    
def fibonacci(index):
    return fibList[index-1] + fibList[index-2]

n = 2
while True:
    fibValue = fibonacci(n)
    if len(str(fibValue)) < 1000:
        n = n + 1
        fibList.append(fibValue)
    else:
        print(n)
        break