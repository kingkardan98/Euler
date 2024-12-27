def xor(a, b):
    bin_a = str(bin(a))[2:] # Rimuove il prefisso 0b
    bin_b = str(bin(b))[2:]
    bin_result = ''

    max_len = max(len(bin_a), len(bin_b))
    bin_a = bin_a.zfill(max_len) # Makes the numbers the same length with zeros
    bin_b = bin_b.zfill(max_len)
    for i in range(max_len):
        if (bin_a[i] == '0' and bin_b[i] == '0') or (bin_a[i] == '1' and bin_b[i] == '1'):
            bin_result = bin_result + '0'
        else:
            bin_result = bin_result + '1'

    result = int(bin_result, 2)
    return result

def asciiToChar(n):
    return chr(n)

def charToAscii(c):
    return ord(c)