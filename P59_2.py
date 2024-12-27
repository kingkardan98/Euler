# Now that we know that the text is keyed with "exp", it's just a matter of finding the sum
# of all ASCII characters.

from recurring_functions.Characters import xor, asciiToChar, charToAscii

def passKeyOverText(key, text, d):
    key_text = asciiToChar(key[0]) + asciiToChar(key[1]) + asciiToChar(key[2])
    xord_text = ''
    for i in range(len(text)):
        xord_text = xord_text + asciiToChar(xor(key[i % 3], text[i]))
    d.update({key_text : xord_text})
    return d

def main():
    # The key is exp -> 101, 120, 112
    key = [101, 120, 112]
    key_text = 'exp'
    textKeyDict = {}
    with open('./P59_aux.txt', 'r') as file:
        text = file.read()
        text = text.split(',')
        for i in range(len(text)):
            text[i] = int(text[i])

    textKeyDict = passKeyOverText(key, text, textKeyDict)
    sum = 0
    for e in textKeyDict[key_text]:
        sum += charToAscii(e)
    print(sum)
    
if __name__ == '__main__':
    main()