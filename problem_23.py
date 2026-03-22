import math

def get_divisors(num):
    if num==1:
        return 1
    n = math.ceil(math.sqrt(num))
    div_total = 1
    divisor = 2
    while divisor < n:
        if num%divisor == 0:
            div_total += divisor
            div_total += num // divisor
        divisor+=1
    if n**2==num:
        div_total+=n
    return div_total


def is_abundant(num):
    if get_divisors(num) > num:
        return True
    else:
        return False

abundant_nums = []
for x in range (0,28124):
    if is_abundant(x):
        abundant_nums.append(x)
del abundant_nums[0]

sums = [0]*28124
for x in range (0, len(abundant_nums)):
    for y in range (x, len(abundant_nums)):
            sum_of2_abundant_nums = abundant_nums[x] + abundant_nums[y]
            if sum_of2_abundant_nums<= 28123:
                if sums[sum_of2_abundant_nums] == 0:
                    sums[sum_of2_abundant_nums] = sum_of2_abundant_nums

total = 0
for x in range (1,len(sums)):
    if sums[x] == 0:
        total +=x

print('\n', total)