def out_of_bonds(row_: int, col_: int, matrix_: list) -> bool:
    return 0 <= row_ < len(matrix_) and 0 <= col_ < len(matrix_[0])


matrix_size, _ = [int(i) for i in input().split()]

boy_row, boy_col = 0, 0
neighborhood = []

for row in range(matrix_size):
    matrix_row = [el for el in input()]
    if "B" in matrix_row:
        boy_row, boy_col = row, matrix_row.index("B")
    neighborhood.append(matrix_row)

cur_row, cur_col = boy_row, boy_col

moves = {
    "down": (1, 0),
    "up": (-1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

neighborhood[cur_row][cur_col] = "-"

while True:
    new_row, new_col = moves[input()]

    if out_of_bonds(cur_row + new_row, cur_col + new_col, neighborhood):

        cur_row, cur_col = cur_row + new_row, cur_col + new_col

        if neighborhood[cur_row][cur_col] == "*":
            cur_row, cur_col = cur_row - new_row, cur_col - new_col
        elif neighborhood[cur_row][cur_col] == "P":
            print("Pizza is collected. 10 minutes for delivery.")
            neighborhood[cur_row][cur_col] = "R"
        elif neighborhood[cur_row][cur_col] == "A":
            neighborhood[cur_row][cur_col] = "P"
            print("Pizza is delivered on time! Next order...")
            break
        else:
            neighborhood[cur_row][cur_col] = "."
    else:
        neighborhood[boy_row][boy_col] = " "
        print("The delivery is late. Order is canceled.")
        break

    neighborhood[boy_row][boy_col] = "B"

[print(*row, sep="") for row in neighborhood]
