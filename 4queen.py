from collections import deque

def is_valid(board, row, col):
    # Check if placing a queen at the given position is valid

    # Check vertically
    for i in range(row):
        if board[i] == col:
            return False

    # Check diagonals
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True

def solve_nqueens():
    queue = deque()
    queue.append([])  # Start with an empty board
    solutions = []

    while queue:
        board = queue.popleft()

        # If the board has 4 queens, it is a valid solution
        if len(board) == 4:
            solutions.append(board)
            continue

        # Find the next row to place a queen
        row = len(board)

        # Try placing a queen in each column of the current row
        for col in range(8):
            if is_valid(board, row, col):
                new_board = board + [col]
                queue.append(new_board)

    return solutions

# Solve the 4-Queens problem
solutions = solve_nqueens()

# Print the solutions with assigned numbers
for index, solution in enumerate(solutions):
    board = [['.'] * 8 for _ in range(8)]
    for row, col in enumerate(solution):
        board[row][col] = 'Q'

    print(f"Solution {index+1}:")
    for row in board:
        print(' '.join(row))
    print()
