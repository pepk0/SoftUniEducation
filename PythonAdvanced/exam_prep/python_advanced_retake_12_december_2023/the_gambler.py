def in_matrix(row_: int, col_: int, matrix_size_: int) -> bool:
    return 0 <= row_ < matrix_size_ and 0 <= col_ < matrix_size_


matrix_size = int(input())

game_board = []
starting_amount = 100
gambler_row, gambler_col = 0, 0
jackpot = False
out_of_bonds = False

for row in range(matrix_size):
    matrix_row = [el for el in input()]
    if "G" in matrix_row:
        gambler_row, gambler_col = row, matrix_row.index("G")
    game_board.append(matrix_row)

game_board[gambler_row][gambler_col] = "-"

moves = {
    "down": (1, 0),
    "up": (-1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

command = input()

while command != "end":
    new_row, new_col = moves[command]

    gambler_row, gambler_col = gambler_row + new_row, gambler_col + new_col

    if in_matrix(gambler_row, gambler_col, matrix_size):
        if game_board[gambler_row][gambler_col] == "W":
            starting_amount += 100
        elif game_board[gambler_row][gambler_col] == "P":
            starting_amount -= 200
        elif game_board[gambler_row][gambler_col] == "J":
            starting_amount += 100000
            jackpot = True

        game_board[gambler_row][gambler_col] = "-"

    else:
        gambler_row, gambler_col = gambler_row - new_row, gambler_col - gambler_col
        out_of_bonds = True
        break

    if starting_amount <= 0:
        break

    if jackpot:
        break

    command = input()

game_board[gambler_row][gambler_col] = "G"

if jackpot:
    print(f"You win the Jackpot! \n"
          f"End of the game. Total amount: {starting_amount}$")
elif not jackpot and starting_amount > 0:
    print(f"End of the game. Total amount: {starting_amount}$")
elif out_of_bonds or starting_amount <= 0:
    print("Game over! You lost everything!")

if starting_amount > 0:
    [print(*row, sep="") for row in game_board]
