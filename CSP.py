def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False
    # Check diagonals
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(board, row, n):
    if row == n:
        return True
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            if solve_n_queens(board, row + 1, n):
                return True
            board[row] = -1  # Backtrack
    return False

def n_queens_csp(n):
    board = [-1] * n
    if solve_n_queens(board, 0, n):
        return board
    return None

def print_board(solution, n):
    if solution:
        print("Solution found:")
        for row in range(n):
            line = ""
            for col in range(n):
                line += "Q " if solution[row] == col else ". "
            print(line)
    else:
        print("No solution exists")

if __name__ == "__main__":
    n = 4
    print(f"{n}-Queens Problem:")
    solution = n_queens_csp(n)
    print_board(solution, n)
    n = 8
    print(f"\n{n}-Queens Problem:")
    solution = n_queens_csp(n)
    if solution:
        print(f"Solution: {solution}")
    else:
        print("No solution found")