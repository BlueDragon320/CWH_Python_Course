# Write code for tic tac toe

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, mark):
    # rows, cols, diagonals
    for i in range(3):
        if all(cell == mark for cell in board[i]):
            return True
        if all(board[r][i] == mark for r in range(3)):
            return True
    if all(board[i][i] == mark for i in range(3)):
        return True
    if all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False

def board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_move(player, board):
    while True:
        try:
            move = input(f"Player {player} enter move (row col): ").split()
            if len(move) != 2:
                raise ValueError
            r, c = map(int, move)
            if r not in range(1, 4) or c not in range(1, 4):
                raise ValueError
            if board[r - 1][c - 1] != ' ':
                print("Cell already taken. Try again.")
                continue
            return r - 1, c - 1
        except ValueError:
            print("Invalid input. Enter two numbers 1-3 separated by space.")

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current = 'X'
    print("Tic Tac Toe")
    print_board(board)

    while True:
        r, c = get_move(current, board)
        board[r][c] = current
        print_board(board)

        if check_winner(board, current):
            print(f"Player {current} wins!")
            break
        if board_full(board):
            print("It's a draw!")
            break
        current = 'O' if current == 'X' else 'X'

if __name__ == "__main__":
    main()