def print_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)
    print("\n")


def check_winner(board, player):
   
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))


def get_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            row, col = divmod(move - 1, 3)
            if board[row][col] != " ":
                print("That cell is already taken. Try again.")
                continue
            return row, col
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


def play_game():
    print("=" * 30)
    print("    Welcome to Tic Tac Toe!")
    print("=" * 30)
    print("\nBoard positions:")
    print(" 1 | 2 | 3 ")
    print("-" * 9)
    print(" 4 | 5 | 6 ")
    print("-" * 9)
    print(" 7 | 8 | 9 \n")

    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        players = ["X", "O"]
        current = 0

        while True:
            print_board(board)
            player = players[current]
            row, col = get_move(board, player)
            board[row][col] = player

            if check_winner(board, player):
                print_board(board)
                print(f"🎉 Player {player} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            current = 1 - current

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    play_game()