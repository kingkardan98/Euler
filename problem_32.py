# A number is n-pandigital if it uses the digits 1-n exactly once.
# Find the sum of all products such that the identity M1 x M2 = P
# is 9-pandigital.

# C1: the biggest 9-pandigital number is 987654321.
# This means we effectively check up to this number. This is the upper limit.

def isPandigital(product, factor1, factor2):
    id_str = str(product) + str(factor1) + str(factor2)

    if len(id_str) != 9:
        return False

    digits = set(id_str)
        
    return digits == set('123456789')


def main():
    pansum = set()

    for factor1 in range(1, 100):
        for factor2 in range(100, 10000 // factor1):
            product = factor1 * factor2
            if isPandigital(product=product, factor1=factor1, factor2=factor2):
                pansum.add(product)

    print(sum(pansum))

if __name__ == '__main__':
    main()
