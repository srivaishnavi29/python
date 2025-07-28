def is_safe(row, col, n, board):
    for i in range(row):
        if board[i][col] == 'Q':
            return False
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
            return False
        if col + (row - i) < n and board[i][col + (row - i)] == 'Q':
            return False
    return True

def solve_n_queens_util(n, row, board, solutions):
    if row == n:
        solutions.append([''.join(r) for r in board])
        return

    for col in range(n):
        if is_safe(row, col, n, board):
            board[row][col] = 'Q'
            solve_n_queens_util(n, row + 1, board, solutions)
            board[row][col] = '.'

def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens_util(n, 0, board, solutions)
    return solutions


n = 4
results = solve_n_queens(n)
for i, solution in enumerate(results):
    print(f"Solution {i + 1}:")
    for row in solution:
        print(row)
    print()
