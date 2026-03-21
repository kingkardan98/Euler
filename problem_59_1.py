from recurring_functions.Characters import xor, asciiToChar

def passKeyOverText(key, text, d):
    key_text = asciiToChar(key[0]) + asciiToChar(key[1]) + asciiToChar(key[2])
    xord_text = ''
    for i in range(len(text)):
        xord_text = xord_text + asciiToChar(xor(key[i % 3], text[i]))
    d.update({key_text : xord_text})
    with open('P59_out.txt', 'a+') as file:
        file.write("Chiave: {}\n".format(key_text))
        file.write(xord_text)
        file.write("\n\n\n")
    if 'the' in d[key_text] and 'and' in d[key_text]:
            print("Chiave sospetta: {}".format(key_text))
    return d

def updateKey(key):
    # Case 1: 122 x x -> 97 x+1 x
    if key[0] == 122 and key[1] < 122 and key[2] < 122:
        key[0] = 97
        key[1] += 1

    # Case 2: 122 122 x -> 97 97 x+1
    elif key[0] == 122 and key[1] == 122 and key[2] < 122:
        key[0] = 97
        key[1] = 97
        key[2] += 1

    # Case 3: 122 122 122 -> -1 -1 -1
    elif key[0] == 122 and key[1] == 122 and key[2] == 122:
        key[0] = -1
        key[1] = -1
        key[2] = -1

    # Case 4: x x x -> x+1 x x
    else:
        key[0] += 1

    return key

def main():
    key = [97, 97, 97]
    textKeyDict = {}
    with open('./P59_aux.txt', 'r') as file:
        text = file.read()
        text = text.split(',')
        for i in range(len(text)):
            text[i] = int(text[i])

    while key[2] < 122:
        textKeyDict = passKeyOverText(key, text, textKeyDict)

        key = updateKey(key)

        if key == [-1, -1, -1]:
            break

    
if __name__ == '__main__':
    main()

# Solution: the key is exp.