# Now that we know that the text is keyed with "exp", it's just a matter of finding the sum
# of all ASCII characters.

from recurring_functions.Characters import xor, ascii_to_char, char_to_ascii

def passKeyOverText(key, text, d):
    key_text = ascii_to_char(key[0]) + ascii_to_char(key[1]) + ascii_to_char(key[2])
    xord_text = ''
    for i in range(len(text)):
        xord_text = xord_text + ascii_to_char(xor(key[i % 3], text[i]))
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
        sum += char_to_ascii(e)
    print(sum)
    
if __name__ == '__main__':
    main()