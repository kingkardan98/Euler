def minimize(roman):
    # RULES
    # IIIII -> V    OK
    # IIII -> IV    OK
    # VIIII -> IX   OK
    # VV -> X       OK
    # XXXXX -> L    OK
    # XXXX -> XL    OK
    # LXXXX -> XC   OK
    # LL -> C       OK
    # CCCCC -> D    OK
    # CCCC -> CD    OK
    # DCCCC -> CM
    # DD -> M       OK
    changed = True
    while changed:
        changed = False
        for i in range(len(roman)):
            if roman[i:i+5] == "IIIII":
                roman = minimize(roman[:i] + "V" + roman[i+5:])
                changed = True
                break
            elif roman[i:i+5] == "VIIII":
                roman = minimize(roman[:i] + "IX" + roman[i+5:] )
                changed = True
                break
            elif roman[i:i+4] == "IIII":
                roman = minimize(roman[:i] + "IV" + roman[i+4:] )
                changed = True
                break
            elif roman[i:i+2] == "VV":
                roman = minimize(roman[:i] + "X" + roman[i+2:] )
                changed = True
                break
            elif roman[i:i+5] == "XXXXX":
                roman = minimize(roman[:i] + "L" + roman[i+5:] )
                changed = True
                break
            elif roman[i:i+5] == "LXXXX":
                roman = minimize(roman[:i] + "XC" + roman[i+5:] )
                changed = True
                break
            elif roman[i:i+4] == "XXXX":
                roman = minimize(roman[:i] + "XL" + roman[i+4:] )
                changed = True
                break
            elif roman[i:i+2] == "LL":
                roman = minimize(roman[:i] + "C" + roman[i+2:] )
                changed = True
                break
            elif roman[i:i+5] == "CCCCC":
                roman = minimize(roman[:i] + "D" + roman[i+5:] )
                changed = True
                break
            elif roman[i:i+5] == "DCCCC":
                roman = minimize(roman[:i] + "CM" + roman[i+5:] )
                changed = True
                break
            elif roman[i:i+4] == "CCCC":
                roman = minimize(roman[:i] + "CD" + roman[i+4:] )
                changed = True
                break
            elif roman[i:i+2] == "DD":
                roman = minimize(roman[:i] + "M" + roman[i+2:] )
                changed = True
                break
    return roman

def main():
    with open("P89.txt", "r") as f:
        lines = f.readlines()
        running_total = 0
        for line in lines:
            line = line.strip()
            if line == "":
                continue
            newRoman = minimize(line)
            saved = len(line) - len(newRoman)
            running_total += saved
    print(running_total)

main()
