def fifthDigSum(n):
    digSum = 0
    for char in str(n):
        digSum += int(char)**5
    return digSum
sum = 0
for i in range(2, 10**6): 
    # Every digit can be at most
    # 9^5 = 59049, so every digit increment is at most this.
    # 10e6 ≃ 354294 
    # (This is a good limit, since the number will always be greater than the sum of its digits by a long shot)
    # Finding the exact limit is a pain in the ass I have no intention of confronting.
    digSum = fifthDigSum(i)
    if digSum == i:
        sum += i

print(sum)