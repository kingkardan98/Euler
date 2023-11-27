# We extract the data from the text file.
file = open("C:\\Users\\Banco6\\Desktop\\Euler\\problem18\\problem18.txt", "r")
data = []
for line in file:
    row = line.split()
    for i in range(len(row)):
        row[i] = int(row[i])
    data.append(row)

finalRow = len(data)
currentRow = 1
sum = data[0][0]
lastRow = data[0]
lastTerm = data[0][0]
lastIndex = lastRow.index(lastTerm)

while currentRow < finalRow:
    newTerm = max([data[currentRow][lastIndex], data[currentRow][lastIndex + 1]])
    lastTerm = newTerm
    lastRow = data[currentRow]
    lastIndex = lastRow.index(lastTerm)
    sum += newTerm
    currentRow += 1

print(sum)