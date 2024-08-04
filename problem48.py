# Find the last ten digits of Sum(n=1 to 1000) n^n

def main():
    sum = 0
    for n in range(1, 1001):
        sum += n**n

    # Preparing to print string
    sum_str = str(sum)
    length = len(sum_str)
    print(sum_str[length - 10:])

if __name__ == "__main__":
    main()