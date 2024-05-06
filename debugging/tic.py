def print_board(board):
    """Print the current state of the tic-tac-toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Check if there's a winner in the current state of the board."""
    # Check rows for a win
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a win
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """Main function to run the tic-tac-toe game."""
    board = [[" "]*3 for _ in range(3)]  # Initialize the board
    player = "X"  # Start with player X
    while not check_winner(board):  # Continue until there's a winner
        print_board(board)  # Print the current board
        try:
            # Get user input for row and column
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if row not in range(3) or col not in range(3):
                raise ValueError
            if board[row][col] == " ":
                board[row][col] = player  # Update the board with player's move
                player = "O" if player == "X" else "X"  # Switch player for the next turn
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")

    print_board(board)  # Print final board after the game ends
    print("Player " + player + " wins!")  # Announce the winner

tic_tac_toe()  # Start the game

