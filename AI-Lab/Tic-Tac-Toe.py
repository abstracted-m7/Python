def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Checks if the specified player has won."""
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    """Checks if the board is full."""
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """Main function to play Tic Tac Toe."""
    # Initialize board
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Get the current player's move
        print(f"Player {players[current_player]}'s turn.")
        try:
            row, col = map(int, input("Enter row and column (0-2, space-separated): ").split())
            if board[row][col] != " ":
                print("Cell is already occupied. Try again.")
                continue
            board[row][col] = players[current_player]
        except (ValueError, IndexError):
            print("Invalid input. Enter row and column as two numbers between 0 and 2.")
            continue

        print_board(board)

        # Check for a winner
        if check_winner(board, players[current_player]):
            print(f"Player {players[current_player]} wins!")
            break

        # Check for a draw
        if is_full(board):
            print("The game is a draw!")
            break

        # Switch players
        current_player = 1 - current_player

if __name__ == "__main__":
    tic_tac_toe()