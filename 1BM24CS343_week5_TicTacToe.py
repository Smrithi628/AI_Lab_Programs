
board = [" "] * 9
def display():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("---------")

def check_winner():
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None

player = "X"
while True:
    display()
    pos = int(input("Player " + player + ", enter position (1-9): "))
    if pos < 1 or pos > 9 or board[pos-1] != " ":
        print("Invalid position! Try again.")
        continue
    board[pos-1] = player
    if check_winner():
        display()
        print("Player", player, "wins!")
        break
    if " " not in board:
        display()
        print("It's a draw!")
        break
    player = "O" if player == "X" else "X"
