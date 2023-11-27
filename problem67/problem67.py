# With this file extraction method, problem 67 is trivial.

data = []
file = open("0067_triangle.txt", "r")
for row in file:
    row = [int(el) for el in row.split()]
    data.append(row)

x = len(data) - 1

while x > 0:
    for y in range(x):
        # Every element gets summed with its children
        data[x-1][y] += max([data[x][y], data[x][y+1]])
    # We remove the row and go to the one above it
    data.pop(x)
    x -= 1

# This way, the sum is stored at the top
print(data[0][0])