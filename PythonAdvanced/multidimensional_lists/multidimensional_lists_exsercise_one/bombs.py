def valid_coordinates(row_: int, col_: int, matrix_: list) -> bool:
    return 0 <= row_ < len(matrix_) and 0 <= col_ < len(matrix_[0])


def detonate_bombs(matrix_: list, cur_row: int, cur_col: int) -> None:
    positions_to_detonate = (
        lambda x, y: (x - 1, y),
        lambda x, y: (x + 1, y),
        lambda x, y: (x, y - 1),
        lambda x, y: (x, y + 1),
        lambda x, y: (x - 1, y - 1),
        lambda x, y: (x + 1, y + 1),
        lambda x, y: (x - 1, y + 1),
        lambda x, y: (x + 1, y - 1),
    )

    bomb = matrix_[cur_row][cur_col]
    matrix_[cur_row][cur_col] -= bomb

    for position in positions_to_detonate:
        new_row, new_col = position(cur_row, cur_col)

        if valid_coordinates(new_row, new_col, matrix_) and \
                matrix_[new_row][new_col] > 0:

            matrix_[new_row][new_col] -= bomb


matrix = [[int(i) for i in input().split()] for _ in range(int(input()))]
coordinates_of_bombs = [tuple(int(x) for x in i.split(","))
                        for i in input().split()]

for bomb_row, bomb_col in coordinates_of_bombs:
    if matrix[bomb_row][bomb_col] <= 0:
        continue
    detonate_bombs(matrix, bomb_row, bomb_col)

alive_cells = [num for row in range(len(matrix))
               for num in matrix[row] if num > 0]

print(f"Alive cells: {len(alive_cells)}", f"Sum: {sum(alive_cells)}", sep="\n")

for row in matrix:
    print(*row, sep=" ")
