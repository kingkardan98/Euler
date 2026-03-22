SET89 = set()
loop89 = [89, 145, 42, 20, 4, 16, 37, 58]
for element in loop89:
    SET89.add(element)
SET1 = set()
SET1.add(1)
MAX = 10**7

def next_in_chain(number: int) -> int:
    """Takes all digits of a number, squares each one of them and sums them up"""
    return sum([int(digit)**2 for digit in str(number)])

def is_in_set(number: int, checkset: set):
    """Checks if a number is inside the checkset"""
    return number in checkset

def main():
    collapsing = []
    for i in range(1, MAX + 1):
        start = i
        current_chain = [start]
        n = start                     
        while True:
            if is_in_set(n, SET1):
                for node in current_chain:
                    SET1.add(node)
                break
            elif is_in_set(n, SET89):
                for node in current_chain:
                    SET89.add(node)
                collapsing.append(start)   
                break
            else:
                n = next_in_chain(n)
                current_chain.append(n)
        if start % 10 == 0:
            percentage = start / MAX * 100
            print("%.2f" % percentage)
    print(len(collapsing))
            
main()