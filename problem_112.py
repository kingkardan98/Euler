def is_increasing(num_l):
    for i in range(1, len(num_l)):
        if num_l[i - 1] > num_l[i]:
            return False
    return True

def is_decreasing(num_l):
    for i in range(1, len(num_l)):
        if num_l[i - 1] < num_l[i]:
            return False
    return True

def is_bouncy(num):
    num_l = [c for c in str(num)]
    if len(num_l) < 3:
        return False
    
    if is_increasing(num_l) or is_decreasing(num_l):
        return False
    return True

def main():
    ratio = 0
    bouncy = 0
    i = 0
    while True:
        if is_bouncy(i):
            bouncy += 1
            ratio = bouncy / i
        if ratio == 0.99:
            break
        i += 1
    print(i)

main()