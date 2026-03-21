import heapq

COLUMNS = 80
ROWS = 80

def getMatrixFromFile(file):
    matrix = []
    for line in file.readlines():
        row = [int(el) for el in line.strip().split(',')]
        matrix.append(row)
    return matrix

def dijkstra(matrix):
    dist = [[float('inf')] * COLUMNS for _ in range(ROWS)]
    visited = [[False] * COLUMNS for _ in range(ROWS)]
    dist[0][0] = matrix[0][0]

    # Min-heap of (cost, row, col)
    heap = [(matrix[0][0], 0, 0)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    while heap:
        cost, row, col = heapq.heappop(heap)

        if visited[row][col]:
            continue
        visited[row][col] = True

        if (row, col) == (ROWS - 1, COLUMNS - 1):
            return cost  # Reached destination

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < ROWS and 0 <= c < COLUMNS and not visited[r][c]:
                new_cost = cost + matrix[r][c]
                if new_cost < dist[r][c]:
                    dist[r][c] = new_cost
                    heapq.heappush(heap, (new_cost, r, c))

    return dist[ROWS - 1][COLUMNS - 1]  # fallback (should always reach earlier)

def main():
    with open("P82.txt", "r") as file:
        matrix = getMatrixFromFile(file)

    minSum = dijkstra(matrix)
    print("Minimum Path Sum (start to end, 4 directions):", minSum)

if __name__ == "__main__":
    main()
