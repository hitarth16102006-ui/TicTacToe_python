import random

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


def show_mode_menu():
    print("\n" + "=" * 30)
    print("    Game Mode Selection")
    print("=" * 30)
    print("1. Human vs Human (2 Players)")
    print("2. Human vs AI (Easy)")
    print("3. Human vs AI (Hard)")
    print("=" * 30)

    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                return "2player", None
            elif choice == 2:
                return "ai", "easy"
            elif choice == 3:
                return "ai", "hard"
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")




def ai_easy_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)


def minimax(board, depth, is_maximizing, player, opponent):
    if check_winner(board, player):
        return 10 - depth
    if check_winner(board, opponent):
        return depth - 10
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = player
                    score = minimax(board, depth + 1, False, player, opponent)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = opponent
                    score = minimax(board, depth + 1, True, player, opponent)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score


def ai_hard_move(board, player):
    opponent = "X" if player == "O" else "O"
    best_score = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = player
                score = minimax(board, 0, False, player, opponent)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move


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

    game_mode, ai_difficulty = show_mode_menu()
    ai_player = "O" if game_mode == "ai" else None

    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        players = ["X", "O"]
        current = 0

        while True:
            print_board(board)
            player = players[current]

            if player == ai_player:
                if ai_difficulty == "easy":
                    row, col = ai_easy_move(board)
                    print(f"AI (Easy) chooses position {row * 3 + col + 1}")
                else:
                    row, col = ai_hard_move(board, player)
                    print(f"AI (Hard) chooses position {row * 3 + col + 1}")
            else:
                row, col = get_move(board, player)

            board[row][col] = player

            if check_winner(board, player):
                print_board(board)
                if player == ai_player:
                    print(f"🎉 AI wins!")
                else:
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