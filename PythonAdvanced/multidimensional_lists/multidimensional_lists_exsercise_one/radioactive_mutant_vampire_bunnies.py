def bunny_expansion(matrix_: list, cur_row: int, cur_col: int) -> bool:
    expansions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    player_hit = False
    for new_row, new_col in expansions:
        if 0 <= cur_row + new_row < len(matrix_) and \
                0 <= cur_col + new_col < len(matrix_[0]):

            if matrix_[cur_row + new_row][cur_col + new_col] == "P":
                player_hit = True

            matrix_[cur_row + new_row][cur_col + new_col] = "B"

    return player_hit


def in_matrix(row_: int, col_: int, matrix_: list) -> bool:
    return 0 <= row_ < len(matrix_) and 0 <= col_ < len(matrix_[0])


rows, cols = [int(i) for i in input().split()]
player_row, player_col = 0, 0
lair = []

for index_row in range(rows):
    matrix_row = [el for el in input()]
    if "P" in matrix_row:
        player_row, player_col = index_row, matrix_row.index("P")
    lair.append(matrix_row)

moves = [el for el in input()]

player_moves = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

player_hit = False
player_won = False
bunny_hit = False

for move in moves:

    next_row, next_col = player_moves[move]

    if in_matrix(player_row + next_row, player_col + next_col, lair):
        lair[player_row][player_col] = "."
        player_row, player_col = next_row + player_row, next_col + player_col

        if lair[player_row][player_col] == "B":
            player_hit = True
        else:
            lair[player_row][player_col] = "P"

    else:
        lair[player_row][player_col] = "."
        player_won = True

    bunnies = []
    for row in range(rows):
        for col in range(cols):

            if lair[row][col] == "B":
                bunnies.append((row, col))

    for bunny_row, bunny_col in bunnies:
        bunny_hit = bunny_expansion(lair, bunny_row, bunny_col)

    if player_hit or player_won or bunny_hit:
        break

for row in lair:
    print(*row, sep="")

print("dead:" if player_hit or bunny_hit else "won:", player_row, player_col)
