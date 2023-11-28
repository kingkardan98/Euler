def alphaValue(name):
    score = 0
    for char in name.lower():
        # Since the Unicode of a is 97, we subtract 96
        score += ord(char) - 96
    return score

file = open('0022_names.txt', 'r')
nameDict = dict()

# Extracting all then
for text in file:
    nameList = text.split(',')

# Stripping the names of all the double quotes
tempNameList = []
for name in nameList:
    name = name.replace('"', '')
    tempNameList.append(name)

# Finalizing the list and sorting it alphabetically
nameList = tempNameList
nameList.sort()

# Calculating the score
totalScore = 0
for i in range(len(nameList)):
    totalScore += alphaValue(nameList[i]) * (i+1)
print(totalScore)