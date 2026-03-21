COLUMNS = 80
ROWS = 80

def getMatrixFromFile(file):
    matrix = []
    for line in file.readlines():
        row = [int(el) for el in line.strip().split(',')]
        matrix.append(row)
    return matrix

def main():
    with open("P82.txt", "r") as file:
        matrix = getMatrixFromFile(file)

    # dp[row][col] = minimal path sum starting at (row, col) to any rightmost cell
    dp = [[0]*COLUMNS for _ in range(ROWS)]

    # Initialize the last column of dp with the last column of the matrix
    for i in range(ROWS):
        dp[i][COLUMNS - 1] = matrix[i][COLUMNS - 1]

    # Fill the DP table from right to left
    for col in range(COLUMNS - 2, -1, -1):
        # Start by assuming we move directly right
        for row in range(ROWS):
            dp[row][col] = matrix[row][col] + dp[row][col + 1]

        # Now consider moving up
        for row in range(1, ROWS):
            dp[row][col] = min(dp[row][col], matrix[row][col] + dp[row - 1][col])

        # Now consider moving down
        for row in range(ROWS - 2, -1, -1):
            dp[row][col] = min(dp[row][col], matrix[row][col] + dp[row + 1][col])

    # The minimum path sum is the minimum value in the first column
    minSum = min(dp[row][0] for row in range(ROWS))
    print("Minimum Path Sum:", minSum)

if __name__ == "__main__":
    main()
