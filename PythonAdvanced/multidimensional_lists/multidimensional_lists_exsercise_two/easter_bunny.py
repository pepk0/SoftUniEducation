def check_valid(row: int, col: int, matrix: list) -> bool:
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])


def find_bunny(matrix: list) -> tuple:

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):

            if matrix[row][col] == "B":
                return row, col
    return -1, -1


field = [[el for el in input().split()]for _ in range(int(input()))]

directions = {
    "down": (1, 0),
    "up": (-1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

bunny_row, bunny_col = find_bunny(field)
most_eggs_collected = 0
best_move = None
best_path = []

for direction, move in directions.items():

    cur_eggs_collected = 0
    next_row, next_col = move
    curr_best_path = []
    cur_row, cur_col = bunny_row, bunny_col

    while True:

        if check_valid(cur_row + next_row, cur_col + next_col, field):
            if field[cur_row + next_row][cur_col + next_col] == "X":
                break
            else:
                cur_eggs_collected += int(field[cur_row +
                                            next_row][cur_col + next_col])
                curr_best_path.append([cur_row + next_row, cur_col + next_col])
                cur_row, cur_col = cur_row + next_row, cur_col + next_col
        else:
            break

    if cur_eggs_collected >= most_eggs_collected:
        best_move = direction
        best_path = curr_best_path
        most_eggs_collected = cur_eggs_collected

print(best_move, *best_path, most_eggs_collected, sep="\n")
