def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player

            if check_winner(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                game_over = True
            else:
                # Switch players
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That spot is already taken! Try again.")

        # Check for a tie
        if all(board[i][j] != ' ' for i in range(3) for j in range(3)) and not check_winner(board):
            print_board(board)
            print("It's a tie!")
            game_over = True

play_game()
