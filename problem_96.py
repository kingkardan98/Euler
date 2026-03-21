"""Utilities for processing Project Euler problem 96 boards."""

from tqdm import tqdm
import time

def solve(board):
    """Solve a sudoku board."""
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True
            board[row][col] = 0
    return False

def valid(board, num, pos):
    """Check if a number is valid."""
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for j in range(len(board)):
        if board[j][pos[1]] == num and pos[0] != j:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def print_board(board):
    """Print the board in a nice way."""
    for i in range(len(board)):
        if i % 3 == 0:
            print(" ———————————————————————————")

        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" │ ", end="")
            if j == 8:
                print(str(board[i][j]) + " │ ")
            else:
                print(str(board[i][j]) + " ", end="")
    print(" ———————————————————————————")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j
    return None

def gather_boards(file_path):
    """Read a text file and return all boards."""
    boards = []
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.readlines()

    for i in range(len(text)):
        if "Grid" in text[i]:
            sudoku = []
            for j in range(1, 10):
                line_str = [int(c) for c in text[i + j].strip("\n")]
                sudoku.append(line_str)
            boards.append(sudoku)
    return boards

def main():
    boards = gather_boards("problem_96.txt")
    sum_total = 0

    pbar = tqdm(boards, desc="Boards processed")
    start = time.time()

    for board in boards:
        solve(board)
        sum_total += board[0][0] * 100 + board[0][1] * 10 + board[0][2]
        pbar.update(1)
    print("Sum:", sum_total)
    print("Time taken: ", time.time() - start)

if __name__ == "__main__":
    main()