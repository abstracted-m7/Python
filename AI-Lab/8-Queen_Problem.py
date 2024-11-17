def solve_n_queens(n):
    def is_safe(row, col):
        return not (cols[col] or diag1[row - col + n - 1] or diag2[row + col])

    def place_queen(row):
        if row == n:  # All queens are placed successfully
            result.append(["".join(row_arr) for row_arr in board])
            return

        for col in range(n):
            if is_safe(row, col):
                # Place the queen
                board[row][col] = 'Q'
                cols[col] = diag1[row - col + n - 1] = diag2[row + col] = True

                place_queen(row + 1)  # Recurse for the next row

                # Remove the queen
                board[row][col] = '.'
                cols[col] = diag1[row - col + n - 1] = diag2[row + col] = False

    # Initialize data structures
    result = []
    board = [["."] * n for _ in range(n)]  # n x n chessboard
    cols = [False] * n  # Tracks columns
    diag1 = [False] * (2 * n - 1)  # Tracks top-left to bottom-right diagonals
    diag2 = [False] * (2 * n - 1)  # Tracks top-right to bottom-left diagonals

    place_queen(0)
    return result


# Example: Solve the 8-Queens problem
solutions = solve_n_queens(8)
for sol in solutions:
    for row in sol:
        print(row)
    print()
print(f"Number of solutions: {len(solutions)}")
