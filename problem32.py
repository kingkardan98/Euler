# If a product is pandigital, it must be
# comprised of nine digits total.

def isPandigital(multiplicand, multiplier, result):
    strOperands = str(multiplicand) + str(multiplier) + str(result)

    if len(strOperands) > 9 or '0' in strOperands:
        return False
    
    strOperands = ''.join(sorted(strOperands, key=str.lower))
    if strOperands == '123456789':
        return True
    
    return False

products = []
multiplicand = 39
multiplier = 186


while multiplier <= 999:
    result = multiplicand * multiplier

    if isPandigital(multiplicand, multiplier, result) and (not result in products):
        products.append(result)

    multiplicand += 1

    if multiplicand == 999:
        multiplier += 1
        multiplicand = 1

print(sum(products))