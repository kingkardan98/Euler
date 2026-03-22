from recurring_functions.Characters import xor, ascii_to_char

def pass_key_over_text(key, text, d):
    key_text = ascii_to_char(key[0]) + ascii_to_char(key[1]) + ascii_to_char(key[2])
    xord_text = ''
    for i in range(len(text)):
        xord_text = xord_text + ascii_to_char(xor(key[i % 3], text[i]))
    d.update({key_text : xord_text})
    with open('P59_out.txt', 'a+') as file:
        file.write("Chiave: {}\n".format(key_text))
        file.write(xord_text)
        file.write("\n\n\n")
    if 'the' in d[key_text] and 'and' in d[key_text]:
            print("Chiave sospetta: {}".format(key_text))
    return d

def update_key(key):
    # Case 1: 122 x x -> 97 x+1 x
    if key[0] == 122 and key[1] < 122 and key[2] < 122:
        key[0] = 97
        key[1] += 1

    # Case 2: 122 122 x -> 97 97 x+1
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
    text_key_dict = {}
    with open('./P59_aux.txt', 'r') as file:
        text = file.read()
        text = text.split(',')
        for i in range(len(text)):
            text[i] = int(text[i])

    while key[2] < 122:
        text_key_dict = pass_key_over_text(key, text, text_key_dict)

        key = update_key(key)

        if key == [-1, -1, -1]:
            break

    
if __name__ == '__main__':
    main()

# Solution: the key is exp.